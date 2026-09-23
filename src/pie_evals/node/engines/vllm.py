"""vLLM adapter: drives ``scripts/bench/vllm_bench.py``.

vllm_bench.py boots the ``LLM`` (or ``AsyncLLM`` under ``--report-timing``)
in-process, so there is no persistent-server path; each run loads the model.
Every flag emitted here is parsed by vllm_bench.py or scripts/bench/common.py.
"""

from __future__ import annotations

import json
import os
import subprocess
from typing import Any

from pie_evals.schema import EngineName, WorkloadSpec

from .base import Engine, register
from .shape import is_prefix_workload, max_model_len_for

_VLLM_KV_DTYPES = {"bf16": "auto", "fp16": "auto", "auto": "auto", "fp8": "fp8", "fp8_e4m3": "fp8_e4m3", "fp8_e5m2": "fp8_e5m2"}


@register
class VllmEngine(Engine):
    name = EngineName.VLLM
    script = "scripts/bench/vllm_bench.py"

    def default_python(self) -> str:
        return os.environ.get("VLLM_PY") or "/root/.venv/vllm/bin/python"

    def model_arg(self) -> str:
        # vLLM resolves HF ids itself (offline cache under HF_HUB_CACHE); a
        # local snapshot path is taken as-is.
        return self.artifact.base_model

    def engine_args(self, workload: WorkloadSpec) -> list[str]:
        r = self.recipe
        args: list[str] = ["--tp-size", str(max(1, int(self.mode.tp)))]
        gmu = r.get("gpu_mem_util", 0.90)
        if gmu is not None:
            args += ["--gpu-mem-util", str(gmu)]
        args += ["--max-model-len", str(max_model_len_for(workload))]

        # max_num_seqs: vllm_bench.py derives it from --concurrency (1 in
        # latency mode) and there is no --max-num-seqs flag; nothing to emit.
        # TODO(pie/benches): none needed unless admission should differ from
        # the client's offered concurrency.

        if r.get("report_timing", True):
            args += ["--report-timing"]
        if r.get("attention_backend"):
            args += ["--attention-backend", str(r["attention_backend"])]
        if r.get("moe_backend"):
            args += ["--moe-backend", str(r["moe_backend"])]

        prefix = r.get("prefix_caching")
        if prefix is None:
            prefix = is_prefix_workload(workload)
        args.append("--prefix-caching" if prefix else "--no-prefix-caching")

        if r.get("chunked_prefill") is False:
            args.append("--no-chunked-prefill")
        if r.get("max_num_batched_tokens"):
            args += ["--max-num-batched-tokens", str(int(r["max_num_batched_tokens"]))]
        if r.get("num_gpu_blocks_override"):
            args += ["--num-gpu-blocks-override", str(int(r["num_gpu_blocks_override"]))]
        if r.get("block_size"):
            args += ["--block-size", str(int(r["block_size"]))]
        if r.get("enforce_eager"):
            args.append("--enforce-eager")

        kv = r.get("kv_cache_dtype") or _VLLM_KV_DTYPES.get(str(self.artifact.kv_dtype), str(self.artifact.kv_dtype))
        if kv and kv != "auto":
            args += ["--kv-cache-dtype", str(kv)]

        # speculative modes: the comparable vLLM feature per pie mode.
        spec = self.mode.spec_dec
        if r.get("speculative_config"):
            cfg = r["speculative_config"]
            args += ["--speculative-config", cfg if isinstance(cfg, str) else json.dumps(cfg)]
        elif spec == "ngram":
            args += ["--spec-method", "ngram", "--spec-tokens", str(int(r.get("spec_tokens", 4)))]
        elif spec == "mtp" and r.get("mtp_assistant_model"):
            args += ["--mtp-assistant-model", str(r["mtp_assistant_model"]), "--mtp-method", str(r.get("mtp_method", "gemma4_mtp"))]
            args += ["--mtp-num-drafts", str(int(r.get("mtp_num_drafts", 3)))]
            if r.get("mtp_draft_tp_size"):
                args += ["--mtp-draft-tp-size", str(int(r["mtp_draft_tp_size"]))]
        # eagle / dflash2 / dspark need a drafter checkpoint the recipe must
        # name via `speculative_config`; without it the cell runs without
        # speculation and the program's baseline_equivalents decide whether
        # that is a comparison at all.

        if r.get("cpu_affinity"):
            args += ["--cpu-affinity", str(r["cpu_affinity"])]
        if r.get("request_timeout"):
            args += ["--request-timeout", str(r["request_timeout"])]
        # TODO(pie/benches): no flag for torch.compile / cudagraph capture
        # sizes (vLLM compilation_config); vLLM's defaults apply.
        return args

    def version(self) -> str:
        try:
            out = subprocess.run(
                [self.python, "-c", "import vllm; print(vllm.__version__)"],
                capture_output=True, text=True, timeout=120, check=False,
            )
            v = out.stdout.strip().splitlines()
            return v[-1] if out.returncode == 0 and v else "unknown"
        except Exception:
            return "unknown"

    def counters_from_summary(self, summary: dict[str, Any]) -> dict[str, float]:
        cfg = summary.get("config") or {}
        out: dict[str, float] = {}
        for label, key in (
            ("spec_acceptance_rate", "vllm spec acceptance rate"),
            ("spec_mean_acceptance_length", "vllm spec mean acceptance length"),
            ("spec_drafts", "vllm spec drafts"),
        ):
            v = cfg.get(key)
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                out[label] = float(v)
        return out

    def leftover_process_names(self) -> list[str]:
        return ["VLLM::EngineCore", "EngineCore"]
