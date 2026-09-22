"""Build pie once per (commit, features) and cache the artifacts on the
shared volume, so a fan-out of N pods builds 0 times, not N.

Artifacts per build: the ``pie`` CLI binary, the embedded-engine wheel
(``pie_server-*.whl``, maturin) with its ``_engine`` .so, and the
``text-completion-bench`` guest (wasm). ``restore`` puts them where the bench
scripts look; ``build`` produces them in a pod-local checkout so concurrent
pods never touch the same work tree or cargo target dir.

pie compiles its CUDA kernels with NVRTC at runtime (cudarc ``nvrtc``), so a
CUDA build is GPU-generation independent and one cache entry serves every
NVIDIA platform.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def cache_key(commit: str, features: list[str]) -> str:
    return f"{commit[:12]}-{'+'.join(features) or 'none'}"


def cache_dir(commit: str, features: list[str], root: Path | None = None) -> Path:
    root = root or Path(os.environ.get("PIE_EVALS_CACHE", Path.home() / ".cache/pie-evals"))
    return root / "builds" / cache_key(commit, features)


def is_cached(commit: str, features: list[str], root: Path | None = None) -> bool:
    d = cache_dir(commit, features, root)
    return (d / "pie").exists() and (d / "text_completion_bench.wasm").exists() and any(d.glob("pie_server-*.whl"))


def ensure_checkout(pie_root: Path, commit: str, mirror: Path | None = None, upstream: str = "git@github.com:pie-project/pie.git") -> None:
    """A pod-local checkout at ``pie_root`` pinned to ``commit``. If a bare
    mirror exists on the volume it is the clone source (fast, no network);
    the mirror itself is only ever fetched, never checked out, so N pods can
    share it."""
    if not (pie_root / ".git").exists():
        src = str(mirror) if mirror and mirror.exists() else upstream
        subprocess.run(["git", "clone", "--quiet", src, str(pie_root)], check=True)
        if mirror and mirror.exists():
            subprocess.run(["git", "-C", str(pie_root), "remote", "set-url", "origin", upstream], check=False)
    head = subprocess.run(["git", "-C", str(pie_root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if not head.startswith(commit) and not commit.startswith(head):
        r = subprocess.run(["git", "-C", str(pie_root), "checkout", "--quiet", commit], capture_output=True, text=True)
        if r.returncode != 0:
            subprocess.run(["git", "-C", str(pie_root), "fetch", "--quiet", "origin"], check=True)
            subprocess.run(["git", "-C", str(pie_root), "checkout", "--quiet", commit], check=True)


def update_mirror(mirror: Path, upstream: str = "git@github.com:pie-project/pie.git") -> None:
    if not mirror.exists():
        subprocess.run(["git", "clone", "--quiet", "--mirror", upstream, str(mirror)], check=True)
    else:
        subprocess.run(["git", "-C", str(mirror), "fetch", "--quiet", "--prune"], check=False)


def build(pie_root: Path, commit: str, features: list[str], *, cache_root: Path | None = None, target_dir: Path | None = None, python: str = "python3", timeout_s: int = 3600, log=print) -> Path:
    """Build the three artifacts and store them under the cache dir."""
    out = cache_dir(commit, features, cache_root)
    out.mkdir(parents=True, exist_ok=True)
    env = {**os.environ}
    if target_dir:
        env["CARGO_TARGET_DIR"] = str(target_dir)  # pod-local: never a shared cargo target
    feats = ",".join(features)
    log(f"build: pie {commit[:12]} features={feats} target={env.get('CARGO_TARGET_DIR', 'in-tree')}")
    subprocess.run(["cargo", "build", "--release", "-p", "pie", "--bin", "pie", "--features", feats], cwd=pie_root, env=env, check=True, timeout=timeout_s)
    tdir = Path(env.get("CARGO_TARGET_DIR", pie_root / "target"))
    shutil.copy2(tdir / "release" / "pie", out / "pie")
    # embedded engine wheel (the python bench path on CUDA)
    if "cuda" in features:
        log("build: embedded engine wheel (maturin)")
        subprocess.run([python, "-m", "pip", "install", "-q", "--break-system-packages", "maturin"], check=False)
        subprocess.run([python, "-m", "maturin", "build", "--release", "-o", str(out), "--features", feats], cwd=pie_root / "sdk/server/python", env=env, check=True, timeout=timeout_s)
    # guest program: built in-tree (bench_inferlet_paths looks under tests/inferlets/target)
    log("build: text-completion-bench (wasm32-wasip2)")
    genv = {k: v for k, v in env.items() if k != "CARGO_TARGET_DIR"}
    subprocess.run(["cargo", "build", "--release", "--target", "wasm32-wasip2", "-p", "text-completion-bench"], cwd=pie_root / "tests/inferlets", env=genv, check=True, timeout=timeout_s)
    shutil.copy2(pie_root / "tests/inferlets/target/wasm32-wasip2/release/text_completion_bench.wasm", out / "text_completion_bench.wasm")
    (out / "COMMIT").write_text(commit + "\n")
    log(f"build: cached at {out}")
    return out


def restore(pie_root: Path, commit: str, features: list[str], *, cache_root: Path | None = None, python: str = "python3", log=print) -> bool:
    """Put cached artifacts where the bench scripts look. Returns False on a cache miss."""
    d = cache_dir(commit, features, cache_root)
    if not is_cached(commit, features, cache_root):
        return False
    binary = pie_root / "target/release/pie"
    binary.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(d / "pie", binary)
    wasm = pie_root / "tests/inferlets/target/wasm32-wasip2/release/text_completion_bench.wasm"
    wasm.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(d / "text_completion_bench.wasm", wasm)
    whl = sorted(d.glob("pie_server-*.whl"))
    if whl:
        subprocess.run([python, "-m", "pip", "install", "-q", "--break-system-packages", "--force-reinstall", "--no-deps", str(whl[-1])], check=True)
        # pie_bench.py puts sdk/server/python/python first on sys.path, which shadows the
        # installed package; the compiled module must sit in the source dir (maturin develop layout)
        so = subprocess.run([python, "-c", "import pie._engine as e; print(e.__file__)"], capture_output=True, text=True).stdout.strip()
        if so:
            shutil.copy2(so, pie_root / "sdk/server/python/python/pie" / Path(so).name)
    log(f"restore: {d} -> {pie_root}")
    return True


def ensure(pie_root: Path, commit: str, features: list[str], *, cache_root: Path | None = None, target_dir: Path | None = None, python: str = "python3", log=print) -> None:
    if restore(pie_root, commit, features, cache_root=cache_root, python=python, log=log):
        return
    build(pie_root, commit, features, cache_root=cache_root, target_dir=target_dir, python=python, log=log)
    restore(pie_root, commit, features, cache_root=cache_root, python=python, log=log)
