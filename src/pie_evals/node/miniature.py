"""Miniature checkpoints: real shapes of big architectures, cheap.

Wraps pie's ``scripts/bench/shrink_checkpoint.py`` (HTTP range requests against the
HF shards; keeps whole width dimensions, selects source layers, keeps the
first N routed experts, optionally aliases the block ``--repeat`` times). The
result is a genuine checkpoint of the same architecture that loads unmodified
in pie and vLLM.

The output is placed *inside the HF cache* as
``models--<org>--<name>/snapshots/<recipe.tag>`` so pie's
``resolve_local_model`` (and vLLM's cache lookup) see it as an ordinary
snapshot; the snapshot name doubles as the checkpoint revision for
provenance.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from pie_evals.schema import ArtifactKind, ArtifactSpec, MiniatureRecipe

SHRINK_SCRIPT = "scripts/bench/shrink_checkpoint.py"


def repo_cache_dirname(repo_id: str) -> str:
    """``org/name`` -> ``models--org--name`` (huggingface_hub's layout)."""
    return "models--" + repo_id.replace("/", "--")


def miniature_snapshot_dir(artifact: ArtifactSpec, hf_cache: Path) -> Path:
    if artifact.miniature is None:
        raise ValueError(f"artifact {artifact.id} has no miniature recipe")
    return Path(hf_cache) / repo_cache_dirname(artifact.base_model) / "snapshots" / artifact.miniature.tag


def miniature_argv(
    artifact: ArtifactSpec, pie_root: Path, out_dir: Path, python: str, cache_dir: Path | None = None
) -> list[str]:
    """The exact ``shrink_checkpoint.py`` invocation for a recipe (pure)."""
    r = artifact.miniature
    if r is None:
        raise ValueError(f"artifact {artifact.id} has no miniature recipe")
    argv = [
        python, str(Path(pie_root) / SHRINK_SCRIPT),
        "--repo", artifact.base_model,
        "--revision", artifact.revision or "main",
        "--out", str(out_dir),
        "--layers", r.layers,
        "--repeat", str(r.repeat),
        # the script's convention: 0 = keep all experts
        "--experts", str(r.experts if r.experts is not None else 0),
    ]
    if r.text_only:
        argv.append("--text-only")
    if cache_dir is not None:
        argv += ["--cache", str(cache_dir)]
    return argv


def ensure_miniature(
    artifact: ArtifactSpec, pie_root: Path, hf_cache: Path, python: str, timeout_s: int = 3600
) -> Path:
    """Return the miniature snapshot dir, building it with the recipe if it is
    not there yet (``config.json`` present = built)."""
    if artifact.kind != ArtifactKind.MINIATURE:
        raise ValueError(f"artifact {artifact.id} is not a miniature")
    out = miniature_snapshot_dir(artifact, hf_cache)
    if (out / "config.json").exists():
        return out
    # Build into a private temp dir and rename into place: the HF cache can be
    # a network volume shared by concurrent pods, and two of them building the
    # same miniature into the same directory destroyed each other's files.
    # The raw-tensor cache is pod-local for the same reason (and it is only a
    # download cache).
    import os
    import shutil
    import tempfile

    # raw-tensor spans can be tens of GB (a pod's container disk is 40-80 GB and filled
    # up): keep them on the shared cache under a directory unique to this process, and
    # drop them once the snapshot is in place
    base = Path(os.environ.get("PIE_EVALS_SHRINK_CACHE") or (Path(os.environ["PIE_EVALS_CACHE"]) / "shrink" if os.environ.get("PIE_EVALS_CACHE") else tempfile.gettempdir()))
    cache_dir = base / f"{os.uname().nodename}-{os.getpid()}" / repo_cache_dirname(artifact.base_model)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.parent / f".tmp-{out.name}-{os.getpid()}"
    shutil.rmtree(tmp, ignore_errors=True)
    argv = miniature_argv(artifact, pie_root, tmp, python, cache_dir=cache_dir)
    proc = subprocess.run(argv, capture_output=True, text=True, timeout=timeout_s, check=False)
    if proc.returncode != 0 or not (tmp / "config.json").exists():
        shutil.rmtree(tmp, ignore_errors=True)
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-20:]
        raise RuntimeError(
            f"shrink_checkpoint failed for {artifact.id} (exit {proc.returncode}):\n" + "\n".join(tail)
        )
    (tmp / ".miniature.json").write_text(
        json.dumps({"artifact": artifact.id, "recipe": artifact.miniature.model_dump(), "argv": argv}, indent=2)
    )
    if (out / "config.json").exists():  # someone else finished first
        shutil.rmtree(tmp, ignore_errors=True)
        shutil.rmtree(cache_dir, ignore_errors=True)
        return out
    os.replace(tmp, out)
    shutil.rmtree(cache_dir, ignore_errors=True)
    return out


# ---- layer planning (pure) --------------------------------------------------------


def pattern_period(layer_types: list[str]) -> int:
    """Smallest ``p`` with ``layer_types[i] == layer_types[i + p]`` for every
    ``i`` (``len(layer_types)`` if the sequence does not repeat)."""
    n = len(layer_types)
    if n == 0:
        return 1
    for p in range(1, n):
        if all(layer_types[i] == layer_types[i + p] for i in range(n - p)):
            return p
    return n


def _ranges(idx: list[int]) -> str:
    """``[0,1,2,3,7]`` -> ``"0-3,7"`` (the script's ``--layers`` grammar)."""
    if not idx:
        return ""
    idx = sorted(set(idx))
    parts: list[str] = []
    start = prev = idx[0]
    for i in idx[1:]:
        if i == prev + 1:
            prev = i
            continue
        parts.append(f"{start}-{prev}" if prev > start else f"{start}")
        start = prev = i
    parts.append(f"{start}-{prev}" if prev > start else f"{start}")
    return ",".join(parts)


def plan_layers(layer_types: list[str], periods: int, always_last: bool = True) -> str:
    """``--layers`` selection keeping ``periods`` whole periods of the
    per-layer type pattern from the front, plus the final source layer when
    ``always_last`` (families special-case it: last-layer norms, MTP hooks,
    the full-attention closer in sliding stacks).

    >>> plan_layers(["sliding", "sliding", "full"] * 4, 2)
    '0-5,11'
    """
    n = len(layer_types)
    if n == 0:
        raise ValueError("no layers")
    if periods < 1:
        raise ValueError("periods must be >= 1")
    p = pattern_period(layer_types)
    keep = list(range(min(n, p * periods)))
    if always_last and (n - 1) not in keep:
        keep.append(n - 1)
    return _ranges(keep)


def num_layers_of(snapshot_dir: str | Path) -> int | None:
    cfg_path = Path(snapshot_dir) / "config.json"
    if not cfg_path.exists():
        return None
    try:
        cfg = json.loads(cfg_path.read_text())
    except (OSError, ValueError):
        return None
    n = cfg.get("num_hidden_layers")
    if n is None and isinstance(cfg.get("text_config"), dict):
        n = cfg["text_config"].get("num_hidden_layers")
    return int(n) if n is not None else None


def recipe_from_snapshot(snapshot_dir: str | Path) -> MiniatureRecipe | None:
    p = Path(snapshot_dir) / ".miniature.json"
    if not p.exists():
        return None
    return MiniatureRecipe.model_validate(json.loads(p.read_text())["recipe"])
