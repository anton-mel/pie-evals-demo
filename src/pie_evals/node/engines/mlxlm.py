"""mlx-lm adapter: drives ``benches/mlx_bench.py`` (macOS only).

mlx_bench.py spawns ``python -m mlx_lm server`` itself (``--spawn``, the
default) with the interpreter given by ``--python``. Two things the script is
explicit about and this adapter honours:

* mlx-lm's server has no ``ignore_eos``; the script refuses ``--ignore-eos``
  and asks for ``--no-ignore-eos`` on BOTH engines. The common args carry
  ``--ignore-eos`` for every other engine, so it is rewritten here and the
  parity check (``check_input_parity``) is what tells whether the pie cell
  compared against this one stopped at the same token counts.
* ``--dump-all-token-ids`` is not parsed by mlx_bench.py (no
  ``add_output_dump_args``); it is dropped from the argv.
"""

from __future__ import annotations

import os
import socket
import subprocess
from pathlib import Path

from pie_evals.schema import EngineName, ErrorClass, WorkloadSpec

from .base import Engine, EngineLaunchError, register
from .shape import hf_snapshot_dir


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


@register
class MlxlmEngine(Engine):
    name = EngineName.MLXLM
    script = "benches/mlx_bench.py"

    def default_python(self) -> str:
        return os.environ.get("MLX_PY") or "/tmp/pievenv/bin/python"

    def model_arg(self) -> str:
        """Snapshot directory of the MLX checkpoint (mlx-lm and the tokenizer
        both read it from disk; an HF id would make mlx-lm try the network)."""
        snap = hf_snapshot_dir(self.artifact.base_model, self.artifact.revision)
        if snap is None:
            raise EngineLaunchError(
                ErrorClass.LOAD_FAIL,
                f"no local snapshot for {self.artifact.base_model!r}; download it before benchmarking",
            )
        return str(snap)

    def engine_args(self, workload: WorkloadSpec) -> list[str]:
        r = self.recipe
        args: list[str] = []
        if self.server_url:
            args += ["--no-spawn", "--url", self.server_url]
        else:
            args += ["--python", self.python, "--port", str(int(r.get("port") or self._port()))]
            if r.get("server_module"):
                args += ["--server-module", str(r["server_module"])]
            extra = r.get("server_extra") or []
            if isinstance(extra, str):
                extra = extra.split()
            if extra:
                args += ["--server-extra", " ".join(str(x) for x in extra)]
            # prompt cache: 0 keeps it out of the measurement (the script's
            # default); the prefix_shared recipe turns it on.
            args += ["--prompt-cache-size", str(int(r.get("prompt_cache_size", 0)))]
            args += ["--prompt-concurrency", str(int(r.get("prompt_concurrency", 8)))]
            args += ["--startup-timeout", str(r.get("startup_timeout", 300))]
        # --decode-concurrency is derived by the script from --concurrency;
        # nothing to emit.
        if r.get("connect_retries") is not None:
            args += ["--connect-retries", str(int(r["connect_retries"]))]
        if r.get("request_timeout"):
            args += ["--request-timeout", str(r["request_timeout"])]
        return args

    def _port(self) -> int:
        if not hasattr(self, "_chosen_port"):
            self._chosen_port = _free_port()
        return self._chosen_port

    def build_argv(self, workload: WorkloadSpec, common_args: list[str], json_out: Path) -> list[str]:
        argv = super().build_argv(workload, common_args, json_out)
        out: list[str] = []
        for a in argv:
            if a == "--ignore-eos":
                # see module docstring: mlx-lm cannot pin output length.
                out.append("--no-ignore-eos")
            elif a == "--dump-all-token-ids":
                # TODO(pie/benches): mlx_bench.py has no output-dump flags.
                continue
            else:
                out.append(a)
        return out

    def version(self) -> str:
        try:
            out = subprocess.run(
                [self.python, "-c", "import mlx_lm; print(mlx_lm.__version__)"],
                capture_output=True, text=True, timeout=120, check=False,
            )
            v = out.stdout.strip().splitlines()
            return v[-1] if out.returncode == 0 and v else "unknown"
        except Exception:
            return "unknown"

    def leftover_process_names(self) -> list[str]:
        # the server is `python -m mlx_lm server`; its process name is the
        # interpreter's, which cannot be swept by name.
        return []
