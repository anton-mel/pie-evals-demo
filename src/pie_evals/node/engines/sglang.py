"""SGLang adapter: drives ``scripts/bench/sglang_bench.py``.

The one flag that must never be left to the engine's default is
``--sglang-cuda-graph-max-bs``: SGLang derives its graph ceiling from a
hardware-tier heuristic and a decode batch beyond it silently runs eager
(4,642 vs 14,042 tok/s on the same cell). It is always set to the shape's
concurrency, the way vLLM captures up to ``max_num_seqs``.
"""

from __future__ import annotations

import os
import subprocess

from pie_evals.schema import EngineName, WorkloadSpec

from .base import Engine, register
from .shape import max_model_len_for, workload_concurrency


@register
class SglangEngine(Engine):
    name = EngineName.SGLANG
    script = "scripts/bench/sglang_bench.py"
    #: the runner image has no nvcc: DeepGEMM's JIT (gemma / gpt-oss on
    #: Blackwell, nightly 35921789513) would abort every cell; the FlashInfer
    #: kernels come precompiled (baselines.ensure_flashinfer_aot).
    env_defaults = {"SGL_ENABLE_JIT_DEEPGEMM": "0", "SGLANG_ENABLE_JIT_DEEPGEMM": "0"}  # 0.5.20 reads the second, warns on the first

    def default_env(self) -> dict[str, str]:
        # sgl_kernel_jit builds land on the volume instead of the pod's
        # container disk, so a kernel compiles once per (version, arch)
        from pie_evals.node.baselines import cache_root

        return {"SGLANG_JIT_CACHE_DIR": str(cache_root() / "jit" / "sglang")}

    def default_python(self) -> str:
        if os.environ.get("SGLANG_PY"):
            return os.environ["SGLANG_PY"]
        from pie_evals.node.baselines import baseline_python

        pin = self.recipe.get("pin")
        py = baseline_python("sglang", pin) if pin else None
        return str(py) if py else "/root/.venv/sglang/bin/python"

    def model_arg(self) -> str:
        # The runner resolves the checkpoint (a miniature lives under a snapshot
        # dir with no refs/main, so an HF id would not find it) and passes the
        # path through the recipe; a bare HF id is the fallback.
        return str(self.recipe.get("snapshot_dir") or self.artifact.base_model)

    def engine_args(self, workload: WorkloadSpec) -> list[str]:
        r = self.recipe
        args: list[str] = ["--tp-size", str(max(1, int(self.mode.tp)))]
        gmu = r.get("gpu_mem_util", 0.90)
        if gmu is not None:
            args += ["--gpu-mem-util", str(gmu)]  # -> mem_fraction_static
        args += ["--max-model-len", str(max_model_len_for(workload))]  # -> context_length

        graph_bs = r.get("cuda_graph_max_bs")
        if graph_bs is None:
            graph_bs = workload_concurrency(workload)
        args += ["--sglang-cuda-graph-max-bs", str(int(graph_bs))]

        if r.get("report_timing", True):
            args += ["--report-timing"]
        if r.get("attention_backend"):
            args += ["--sglang-attention-backend", str(r["attention_backend"])]
        if r.get("sampling_backend"):
            args += ["--sglang-sampling-backend", str(r["sampling_backend"])]
        if r.get("page_size"):
            args += ["--sglang-page-size", str(int(r["page_size"]))]
        if r.get("max_total_tokens"):
            args += ["--sglang-max-total-tokens", str(int(r["max_total_tokens"]))]
        if r.get("disable_cuda_graph"):
            args.append("--sglang-disable-cuda-graph")
        if r.get("disable_piecewise_cuda_graph"):
            args.append("--sglang-disable-piecewise-cuda-graph")

        hybrid_swa = r.get("disable_hybrid_swa_memory")
        if hybrid_swa is None:
            # Sliding-window families (Gemma): SGLang's hybrid sizer derives a
            # budget from the SWA layers and then refuses to start because the
            # full-attention layers cannot hold it (common.py's flag help).
            # One uniform pool is what vLLM does, so it is the comparable
            # policy as well as the one that runs.
            hybrid_swa = self.artifact.family.startswith("gemma")
        if hybrid_swa:
            args.append("--sglang-disable-hybrid-swa-memory")

        # TODO(pie/benches): sglang_bench.py hard-codes disable_radix_cache=True
        # and has no flag to enable it, so the prefix_shared shape cannot hand
        # SGLang its prefix cache (recipe knob `radix_cache` is recorded only).
        # TODO(pie/benches): no --sglang-enable-torch-compile flag (recipe knob
        # `torch_compile` is recorded only).

        if r.get("cpu_affinity"):
            args += ["--cpu-affinity", str(r["cpu_affinity"])]
        if r.get("request_timeout"):
            args += ["--request-timeout", str(r["request_timeout"])]
        return args

    def version(self) -> str:
        try:
            out = subprocess.run(
                [self.python, "-c", "import sglang; print(sglang.__version__)"],
                capture_output=True, text=True, timeout=120, check=False,
            )
            v = out.stdout.strip().splitlines()
            return v[-1] if out.returncode == 0 and v else "unknown"
        except Exception:
            return "unknown"

    def leftover_process_names(self) -> list[str]:
        return ["sglang::scheduler", "sglang::detokenizer", "sglang::scheduler_TP0"]
