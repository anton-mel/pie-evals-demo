"""Checkpoints on the node.

pie's ``resolve_local_model`` refuses to touch the network, so pie-evals
fetches checkpoints itself: full artifacts through ``huggingface_hub``
(``HF_TOKEN`` honoured for gated repos), miniatures through pie's
``shrink_checkpoint.py`` (see ``miniature.py``). ``prepare`` does this for
every artifact of a tier before the bench fan-out so that N bench pods find
everything on the shared volume.
"""

from __future__ import annotations

import os
from pathlib import Path

from pie_evals.schema import ArtifactKind, ArtifactSpec

WEIGHT_PATTERNS = ["*.json", "*.safetensors", "*.txt", "*.model", "*.tiktoken", "tokenizer*", "*.py"]


def hf_cache_dir() -> Path:
    return Path(os.environ.get("HF_HUB_CACHE") or (Path(os.environ["HF_HOME"]) / "hub" if os.environ.get("HF_HOME") else Path.home() / ".cache/huggingface/hub"))


def snapshot_dir_if_present(artifact: ArtifactSpec, hf_cache: Path) -> Path | None:
    org, _, name = artifact.base_model.partition("/")
    base = hf_cache / f"models--{org}--{name}" / "snapshots"
    if artifact.revision and (base / artifact.revision / "config.json").exists():
        return base / artifact.revision
    snaps = sorted(d for d in base.glob("*") if (d / "config.json").exists()) if base.exists() else []
    return snaps[-1] if snaps else None


class SnapshotMissing(FileNotFoundError):
    pass


def ensure_snapshot(artifact: ArtifactSpec, hf_cache: Path, *, pie_root: Path | None = None, python: str = "python3", download: bool = True, log=print) -> Path:
    """Return the artifact's snapshot dir. Miniatures are built if absent
    (atomically, see miniature.py). Full checkpoints are downloaded only when
    ``download`` is set — the bench node runs with it off, because fetching
    belongs to the ``prepare`` stage that runs once before the fan-out."""
    if artifact.kind == ArtifactKind.MINIATURE:
        from .miniature import ensure_miniature

        assert pie_root is not None
        return ensure_miniature(artifact, pie_root, hf_cache, python=python)
    have = snapshot_dir_if_present(artifact, hf_cache)
    if have:
        return have
    if not download:
        raise SnapshotMissing(f"checkpoint {artifact.base_model} not in HF cache {hf_cache} (run `pie-evals-node prepare`, or `run --download`; pie's resolve_local_model refuses network)")
    from huggingface_hub import snapshot_download

    log(f"download: {artifact.base_model}@{artifact.revision or 'main'} -> {hf_cache}")
    kw = {"revision": artifact.revision} if artifact.revision else {}
    if artifact.gguf_file:
        kw["allow_patterns"] = ["*.json", artifact.gguf_file]
    else:
        kw["allow_patterns"] = WEIGHT_PATTERNS
    path = snapshot_download(artifact.base_model, cache_dir=str(hf_cache), token=os.environ.get("HF_TOKEN") or None, **kw)  # an empty secret must not become "Bearer "
    return Path(path)
