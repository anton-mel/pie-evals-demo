"""Reference implementations of the same weights, behind lazy imports.

* :class:`HFReference` — ``transformers`` on CUDA/CPU. The reference for
  HF-safetensors checkpoints (bf16, fp8, mxfp4 via transformers' dequant).
* :class:`MlxReference` — ``mlx_lm`` on Apple silicon. The reference for
  ``mlx-community`` conversions, mirroring how pie's own
  ``scripts/gemma4_parity_ref.py`` reads them (``mlx_lm.load`` +
  ``make_prompt_cache``, greedy argmax step by step, float32 logits).

Nothing here is imported at package import time; ``torch``/``mlx`` are
resolved inside the constructors, so a node without them can still run the
perf side and the pure parity arithmetic.

Reference outputs are expensive and deterministic, so :class:`ReferenceCache`
stores them as ``.npz`` keyed by ``(checkpoint revision, prompt hash,
max_new_tokens)`` — computed once per checkpoint, reused across engines and
runs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Protocol

import numpy as np


class Reference(Protocol):
    name: str

    def greedy(self, prompt_ids: list[int], max_new_tokens: int) -> list[int]: ...

    def teacher_forced_logits(self, ids: list[int]) -> np.ndarray: ...


def reference_for(platform_os: str, source_format: str) -> str:
    """Which reference implementation to read a checkpoint against.

    ``"mlx"`` for MLX checkpoints on macOS (mlx_lm is the implementation the
    conversion was made for); ``"hf"`` everywhere else.
    """
    if str(platform_os).lower() in ("macos", "darwin", "mac") and str(source_format) == "mlx":
        return "mlx"
    return "hf"


# ---- HF transformers -----------------------------------------------------------


class HFReference:
    name = "hf"

    def __init__(self, snapshot_dir: str | Path, dtype: str = "bfloat16", device: str = "cuda"):
        import torch  # lazy
        from transformers import AutoModelForCausalLM  # lazy

        self.torch = torch
        self.snapshot_dir = Path(snapshot_dir)
        self.device = device
        self.dtype = getattr(torch, dtype) if isinstance(dtype, str) else dtype
        self.model = AutoModelForCausalLM.from_pretrained(
            str(self.snapshot_dir), torch_dtype=self.dtype, device_map=None, trust_remote_code=True
        )
        self.model.to(device)
        self.model.eval()

    @property
    def vocab_size(self) -> int:
        return int(self.model.get_output_embeddings().weight.shape[0])

    def greedy(self, prompt_ids: list[int], max_new_tokens: int) -> list[int]:
        """Greedy continuation (new tokens only), no EOS early stop so the
        length is deterministic and comparable to the engine's ``--max-tokens``."""
        torch = self.torch
        ids = torch.tensor([list(prompt_ids)], dtype=torch.long, device=self.device)
        with torch.no_grad():
            out = self.model.generate(
                ids,
                max_new_tokens=max_new_tokens,
                min_new_tokens=max_new_tokens,
                do_sample=False,
                num_beams=1,
                pad_token_id=self.model.config.pad_token_id or self.model.config.eos_token_id,
            )
        return [int(t) for t in out[0, ids.shape[1]:].tolist()]

    def teacher_forced_logits(self, ids: list[int]) -> np.ndarray:
        """``[len(ids), vocab]`` float32 logits; row ``i`` is the distribution
        over the token *after* ``ids[i]``."""
        torch = self.torch
        x = torch.tensor([list(ids)], dtype=torch.long, device=self.device)
        with torch.no_grad():
            logits = self.model(input_ids=x, use_cache=False).logits[0]
        return logits.float().cpu().numpy().astype(np.float32)


# ---- mlx_lm ---------------------------------------------------------------------


class MlxReference:
    name = "mlxlm"

    def __init__(self, snapshot_dir: str | Path, dtype: str = "bfloat16", device: str = "gpu"):
        import mlx.core as mx  # lazy
        from mlx_lm import load  # lazy
        from mlx_lm.models.cache import make_prompt_cache  # lazy

        self.mx = mx
        self._make_prompt_cache = make_prompt_cache
        self.snapshot_dir = Path(snapshot_dir)
        mx.set_default_device(mx.gpu if device == "gpu" else mx.cpu)
        self.model, self.tokenizer = load(str(self.snapshot_dir))
        self.dtype = dtype  # the checkpoint decides; kept for the record

    def greedy(self, prompt_ids: list[int], max_new_tokens: int) -> list[int]:
        mx = self.mx
        cache = self._make_prompt_cache(self.model)
        out = self.model(mx.array([list(prompt_ids)]), cache=cache)[0, -1].astype(mx.float32)
        mx.eval(out)
        gen: list[int] = []
        for _ in range(max_new_tokens):
            nxt = int(mx.argmax(out).item())
            gen.append(nxt)
            out = self.model(mx.array([[nxt]]), cache=cache)[0, -1].astype(mx.float32)
            mx.eval(out)
        return gen

    def teacher_forced_logits(self, ids: list[int]) -> np.ndarray:
        mx = self.mx
        tf = self.model(mx.array([list(ids)]))[0].astype(mx.float32)
        mx.eval(tf)
        return np.asarray(tf).astype(np.float32)


def load_reference(kind: str, snapshot_dir: str | Path, **kw: Any) -> HFReference | MlxReference:
    if kind == "mlx":
        return MlxReference(snapshot_dir, **kw)
    if kind == "hf":
        return HFReference(snapshot_dir, **kw)
    raise ValueError(f"unknown reference kind {kind!r}")


# ---- cache ----------------------------------------------------------------------


def prompt_hash(ids: list[int]) -> str:
    return hashlib.sha256(json.dumps([int(i) for i in ids]).encode()).hexdigest()[:16]


class ReferenceCache:
    """``<cache_dir>/<revision>/<kind>-<prompt_hash>-n<max_new_tokens>.npz``.

    ``revision`` is the checkpoint commit (or miniature recipe tag), which is
    what makes a cached reference valid: same weights, same prompt, same
    length -> same greedy tokens / teacher-forced logits, whichever reference
    process produced them.
    """

    def __init__(self, cache_dir: str | Path):
        self.cache_dir = Path(cache_dir)

    def _path(self, revision: str, kind: str, ids: list[int], n: int) -> Path:
        rev = str(revision).replace("/", "_")
        return self.cache_dir / rev / f"{kind}-{prompt_hash(ids)}-n{n}.npz"

    def get(self, revision: str, kind: str, ids: list[int], n: int) -> np.ndarray | None:
        p = self._path(revision, kind, ids, n)
        if not p.exists():
            return None
        with np.load(p) as z:
            if "ids" in z and z["ids"].tolist() != [int(i) for i in ids]:
                return None  # hash collision or hand-edited file
            return z["value"]

    def put(self, revision: str, kind: str, ids: list[int], n: int, value: np.ndarray) -> Path:
        p = self._path(revision, kind, ids, n)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(".tmp.npz")
        np.savez(tmp, ids=np.asarray(ids, dtype=np.int64), value=np.asarray(value))
        tmp.replace(p)
        return p

    def greedy(self, ref: Reference, revision: str, prompt_ids: list[int], max_new_tokens: int) -> list[int]:
        hit = self.get(revision, "greedy", prompt_ids, max_new_tokens)
        if hit is not None:
            return [int(t) for t in hit.tolist()]
        out = ref.greedy(prompt_ids, max_new_tokens)
        self.put(revision, "greedy", prompt_ids, max_new_tokens, np.asarray(out, dtype=np.int64))
        return out

    def teacher_forced_logits(self, ref: Reference, revision: str, ids: list[int]) -> np.ndarray:
        hit = self.get(revision, "tf", ids, len(ids))
        if hit is not None:
            return hit
        out = ref.teacher_forced_logits(ids)
        self.put(revision, "tf", ids, len(ids), out.astype(np.float32))
        return out
