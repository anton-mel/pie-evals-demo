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


def ensure_python_headers(py: Path, log=print) -> bool:
    """triton (and torch.compile) build a small C extension at runtime against
    the interpreter's headers; a system python without ``python3-dev`` has none
    and every vLLM/SGLang engine core then dies with ``Python.h: No such file``
    (nightly 35895697621 lost all 66 vLLM cells to it). Install the headers
    for the interpreter's own minor version when they are missing."""
    try:
        out = subprocess.run(
            [str(py), "-c", "import sys, sysconfig; print(sysconfig.get_paths()['include']); print(sys.version_info[0], sys.version_info[1])"],
            capture_output=True, text=True, check=True, timeout=60,
        ).stdout.split()
        include, major, minor = Path(out[0]), out[1], out[2]
    except (OSError, subprocess.SubprocessError, IndexError) as e:
        log(f"baseline: cannot query the include dir of {py}: {e}")
        return False
    if (include / "Python.h").exists():
        return True
    pkg = f"python{major}.{minor}-dev"
    log(f"baseline: {include}/Python.h is missing; installing {pkg}")
    apt = ["apt-get"] if os.geteuid() == 0 else ["sudo", "-n", "apt-get"]
    env = dict(os.environ, DEBIAN_FRONTEND="noninteractive")
    try:
        subprocess.run(apt + ["update", "-qq"], env=env, check=False, timeout=600, capture_output=True)
        subprocess.run(apt + ["install", "-y", "-qq", pkg], env=env, check=True, timeout=900, capture_output=True)
    except (OSError, subprocess.SubprocessError) as e:
        log(f"baseline: {pkg} install failed ({e}); engines that JIT C extensions will crash")
        return False
    ok = (include / "Python.h").exists()
    log(f"baseline: {pkg} installed; Python.h present: {ok}")
    return ok


def cuda_toolkit_version(py: Path | None = None) -> tuple[str, str] | None:
    """(major, minor) of the CUDA this image was built for: torch's, when a
    baseline interpreter is given, else /usr/local/cuda/version.json."""
    if py is not None:
        try:
            cuda = subprocess.run([str(py), "-c", "import torch; print(torch.version.cuda)"], capture_output=True, text=True, check=True, timeout=300).stdout.strip()
            major, minor = cuda.split(".")[:2]
            return major, minor
        except (OSError, subprocess.SubprocessError, ValueError):
            pass
    try:
        import json

        v = json.loads(Path("/usr/local/cuda/version.json").read_text())["cuda"]["version"]
        major, minor = v.split(".")[:2]
        return major, minor
    except (OSError, KeyError, ValueError):
        return None


def ensure_cuda_devkit(py: Path | None = None, log=print) -> bool:
    """The runner image is ``nvidia/cuda:*-runtime``: no nvcc, no CUDA headers,
    no ``libcudadevrt.a``. vLLM/SGLang JIT kernels with nvcc (gemma's
    head_dim-512 prefill, ``sgl_kernel_jit``; nightly 35918372228), and pie's
    NVRTC path needs ``libcudadevrt.a`` for cooperative launches
    (``attention.mla_latents`` on the GLM mini, nightly 35935510089). Install
    the toolkit packages for the image's CUDA from the NVIDIA apt repo it
    already carries; once per pod (container disk)."""
    nvcc = Path("/usr/local/cuda/bin/nvcc")
    header = Path("/usr/local/cuda/include/cuda_runtime.h")
    devrt = Path("/usr/local/cuda/lib64/libcudadevrt.a")
    if nvcc.exists() and header.exists() and devrt.exists():
        return True
    ver = cuda_toolkit_version(py)
    if ver is None:
        log("baseline: cannot tell the image's CUDA version; not installing the toolkit")
        return False
    major, minor = ver
    pkgs = [p for p, missing in ((f"cuda-nvcc-{major}-{minor}", not nvcc.exists()), (f"cuda-cudart-dev-{major}-{minor}", not (header.exists() and devrt.exists()))) if missing]
    log(f"baseline: {nvcc.name}/{header.name}/{devrt.name} missing; installing {' '.join(pkgs)}")
    apt = ["apt-get"] if os.geteuid() == 0 else ["sudo", "-n", "apt-get"]
    env = dict(os.environ, DEBIAN_FRONTEND="noninteractive")
    try:
        subprocess.run(apt + ["update", "-qq"], env=env, check=False, timeout=600, capture_output=True)
        subprocess.run(apt + ["install", "-y", "-qq", "--no-install-recommends", *pkgs], env=env, check=True, timeout=1200, capture_output=True)
    except (OSError, subprocess.SubprocessError) as e:
        log(f"baseline: CUDA toolkit install failed ({e}); engines that JIT CUDA kernels will crash")
        return False
    ok = nvcc.exists() and header.exists() and devrt.exists()
    log(f"baseline: nvcc {nvcc.exists()}, cuda_runtime.h {header.exists()}, libcudadevrt.a {devrt.exists()}")
    return ok


ensure_nvcc = ensure_cuda_devkit  # the old name


def ensure_flashinfer_aot(py: Path, marker: Path, log=print) -> bool:
    """vLLM's FlashInfer backend JIT-compiles its attention kernels with nvcc,
    and the runner image ships only the CUDA runtime (nightly 35908055874 lost
    every gemma/qwen vLLM cell to ``/usr/local/cuda/bin/nvcc: not found``).
    FlashInfer publishes the compiled kernels as ``flashinfer-cubin`` and
    ``flashinfer-jit-cache`` wheels per CUDA version; install the pair that
    matches the venv's flashinfer and torch, once per venv."""
    if marker.exists():
        return True
    try:
        out = subprocess.run(
            [str(py), "-c", "import flashinfer, torch; print(flashinfer.__version__); print(torch.version.cuda)"],
            capture_output=True, text=True, check=True, timeout=300,
        ).stdout.split()
        fi, cuda = out[0], out[1]
    except (OSError, subprocess.SubprocessError, IndexError) as e:
        log(f"baseline: no flashinfer/torch to match an AOT cache to ({e})")
        return False
    cu = "cu" + cuda.replace(".", "")[:3]
    # the cubins are CUDA-agnostic and live at the index root; the JIT cache
    # (the compiled attention kernels) is per CUDA version
    plan = [
        (f"flashinfer-jit-cache=={fi}", f"https://flashinfer.ai/whl/{cu}/"),
        (f"flashinfer-cubin=={fi}", "https://flashinfer.ai/whl/"),
    ]
    ok = True
    for spec, index in plan:
        log(f"baseline: installing {spec} from {index}")
        try:
            if shutil.which("uv"):
                subprocess.run(["uv", "pip", "install", "--quiet", "--python", str(py), "--extra-index-url", index, spec], check=True, timeout=1800)
            else:
                subprocess.run([str(py), "-m", "pip", "install", "-q", "--extra-index-url", index, spec], check=True, timeout=1800)
        except (OSError, subprocess.SubprocessError) as e:
            log(f"baseline: {spec} install failed ({e}); FlashInfer may JIT and need nvcc")
            ok = False
    if ok:
        marker.write_text(fi + "\n")
    return ok


def ensure_baseline(engine: str, version: str, root: Path | None = None, *, timeout_s: int = 3600, log=print) -> Path:
    """Install the baseline into its venv if needed; return its python."""
    if engine not in SPECS:
        raise ValueError(f"no installer for baseline {engine}")
    d = venv_dir(engine, version, root)
    py = d / "bin" / "python"
    if (d / ".ok").exists():
        ensure_python_headers(py, log=log)
        if engine in ("vllm", "sglang"):
            ensure_nvcc(py, log=log)
            ensure_flashinfer_aot(py, d / ".flashinfer-aot", log=log)
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
    ensure_python_headers(py, log=log)
    if engine in ("vllm", "sglang"):
        ensure_nvcc(py, log=log)
        ensure_flashinfer_aot(py, d / ".flashinfer-aot", log=log)
    (d / ".ok").write_text(version + "\n")
    return py
