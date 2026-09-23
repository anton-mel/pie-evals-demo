"""Baseline engines on the node.

The runner image ships pie's toolchain only; vLLM and SGLang are installed
once per pinned version into a venv on the shared cache (the volume) and
reused by every pod after that. llama.cpp needs nvcc for a CUDA build and
the image has only the CUDA runtime, so it is not installed here (Linux
llama.cpp cells are declared unsupported in matrix/support.yaml).
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

SPECS = {
    "vllm": lambda v: [f"vllm=={v}"],
    "sglang": lambda v: [f"sglang[all]=={v}"],
}


def cache_root(root: Path | None = None) -> Path:
    return root or Path(os.environ.get("PIE_EVALS_CACHE", Path.home() / ".cache/pie-evals"))


def venv_dir(engine: str, version: str, root: Path | None = None) -> Path:
    return cache_root(root) / f"venv-{engine}-{version}"


def baseline_python(engine: str, version: str, root: Path | None = None) -> Path | None:
    """The interpreter for a baseline pin if it is installed, else None."""
    d = venv_dir(engine, version, root)
    return d / "bin" / "python" if (d / ".ok").exists() else None


def ensure_baseline(engine: str, version: str, root: Path | None = None, *, timeout_s: int = 3600, log=print) -> Path:
    """Install the baseline into its venv if needed; return its python."""
    if engine not in SPECS:
        raise ValueError(f"no installer for baseline {engine}")
    d = venv_dir(engine, version, root)
    py = d / "bin" / "python"
    if (d / ".ok").exists():
        return py
    if d.exists():
        shutil.rmtree(d, ignore_errors=True)  # a half-finished install
    log(f"baseline: installing {engine}=={version} into {d} (once per volume)")
    if shutil.which("uv"):
        subprocess.run(["uv", "venv", "--quiet", "--python", "3.12", str(d)], check=True)
        subprocess.run(["uv", "pip", "install", "--quiet", "--python", str(py), *SPECS[engine](version)], check=True, timeout=timeout_s)
    else:
        subprocess.run(["python3", "-m", "venv", str(d)], check=True)
        subprocess.run([str(py), "-m", "pip", "install", "-q", *SPECS[engine](version)], check=True, timeout=timeout_s)
    (d / ".ok").write_text(version + "\n")
    return py
