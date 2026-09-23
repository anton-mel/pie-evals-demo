"""llama.cpp adapter: drives ``scripts/bench/llamacpp_bench.py``.

The script spawns ``llama-server`` itself (``--server-bin`` + ``--gguf-model``)
and already forces ``--flash-attn on``, ``--parallel <concurrency>`` and a
per-slot ``--ctx-size``; other server flags travel in ``--server-extra`` as one
space-separated string.

``--model`` is the TOKENIZER source (the script renders the chat template with
``transformers.AutoTokenizer`` and counts prompt tokens with it); the GGUF file
goes to ``--gguf-model``. A bare ``.gguf`` path is not something AutoTokenizer
can load, so ``model_arg`` points at the checkpoint's tokenizer instead.
"""

from __future__ import annotations

import os
import re
import socket
import subprocess
import sys
from pathlib import Path

from pie_evals.schema import EngineName, ErrorClass, WorkloadSpec

from .base import Engine, EngineLaunchError, register
from .shape import hf_snapshot_dir, hf_snapshot_file

_TOKENIZER_FILES = ("tokenizer.json", "tokenizer_config.json", "tokenizer.model")


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


@register
class LlamacppEngine(Engine):
    name = EngineName.LLAMACPP
    script = "scripts/bench/llamacpp_bench.py"

    def default_python(self) -> str:
        # The script only needs `transformers` for the tokenizer; any
        # interpreter that has it will do.
        return os.environ.get("LLAMACPP_PY") or sys.executable

    # ---- inputs ------------------------------------------------------------
    def server_bin(self) -> str:
        return str(self.recipe.get("server_bin") or os.environ.get("LLAMA_SERVER_BIN") or "llama-server")

    def gguf_path(self) -> Path:
        a = self.artifact
        if not a.gguf_file:
            raise EngineLaunchError(ErrorClass.LOAD_FAIL, f"artifact {a.id}: gguf_file not set (the arm must be named)")
        p = Path(a.gguf_file).expanduser()
        if p.is_absolute() and p.is_file():
            return p
        found = hf_snapshot_file(a.base_model, a.gguf_file, a.revision)
        if found is None:
            raise EngineLaunchError(
                ErrorClass.LOAD_FAIL,
                f"{a.gguf_file} not found in cache for {a.base_model}: resolve_local_model would fail; download it before benchmarking",
            )
        return found

    def model_arg(self) -> str:
        """Tokenizer source for ``--model``: recipe ``tokenizer_model``, else the
        GGUF repo's own snapshot when it ships a tokenizer, else the base
        checkpoint the GGUF was converted from (``<repo>`` minus ``-GGUF``)."""
        if self.recipe.get("tokenizer_model"):
            return str(self.recipe["tokenizer_model"])
        snap = hf_snapshot_dir(self.artifact.base_model, self.artifact.revision)
        if snap is not None and any((snap / f).is_file() for f in _TOKENIZER_FILES):
            return str(snap)
        return re.sub(r"[-_]GGUF$", "", self.artifact.base_model, flags=re.IGNORECASE)

    # ---- argv --------------------------------------------------------------
    def engine_args(self, workload: WorkloadSpec) -> list[str]:
        r = self.recipe
        args: list[str] = []
        if self.server_url:
            # attach to a server started elsewhere (no --server-bin -> the
            # script only health-checks --url)
            args += ["--url", self.server_url]
        else:
            args += ["--server-bin", self.server_bin(), "--gguf-model", str(self.gguf_path())]
            args += ["--port", str(int(r.get("port") or self._port()))]
            # -ngl: `all` offloads every layer (the script's default too).
            args += ["--gpu-layers", str(r.get("gpu_layers", "all"))]
            extra = r.get("server_extra") or []
            if isinstance(extra, str):
                extra = extra.split()
            extra = [str(x) for x in extra]
            if self.mode.tp > 1 and not any(x == "--split-mode" for x in extra):
                # llama.cpp has no TP proper; row split is its closest shape.
                extra += ["--split-mode", str(r.get("split_mode", "row"))]
            if extra:
                args += ["--server-extra", " ".join(extra)]
        # Slots (`--parallel`) = --concurrency and `-fa on` are set by the
        # script itself; nothing to emit for them.
        # TODO(pie/benches): the script sends cache_prompt=false per request,
        # so `--cache-reuse` in server_extra cannot take effect on the prefix
        # shape until a --cache-prompt flag exists.
        if r.get("request_timeout"):
            args += ["--request-timeout", str(r["request_timeout"])]
        return args

    def _port(self) -> int:
        if not hasattr(self, "_chosen_port"):
            self._chosen_port = _free_port()
        return self._chosen_port

    def build_argv(self, workload: WorkloadSpec, common_args: list[str], json_out: Path) -> list[str]:
        argv = super().build_argv(workload, common_args, json_out)
        # TODO(pie/benches): llamacpp_bench.py does not call
        # add_output_dump_args, so --dump-all-token-ids (which the base argv
        # always asks for) is refused by its argparse. Dropped here; the run
        # then carries no token ids for the parity gate.
        return [a for a in argv if a != "--dump-all-token-ids"]

    # ---- provenance --------------------------------------------------------
    def version(self) -> str:
        try:
            out = subprocess.run([self.server_bin(), "--version"], capture_output=True, text=True, timeout=30, check=False)
        except Exception:
            return "unknown"
        text = (out.stdout or "") + "\n" + (out.stderr or "")
        m = re.search(r"version:\s*(\S+(?:\s*\([^)]*\))?)", text)
        if m:
            return m.group(1).strip()
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        return lines[0][:80] if lines else "unknown"

    def leftover_process_names(self) -> list[str]:
        return ["llama-server"]
