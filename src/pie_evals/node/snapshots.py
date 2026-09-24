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
    marker = artifact.gguf_file or "config.json"  # a GGUF repo carries no config.json
    if artifact.revision and (base / artifact.revision / marker).exists():
        return base / artifact.revision
    snaps = sorted(d for d in base.glob("*") if (d / marker).exists()) if base.exists() else []
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
        return _with_gguf_config(artifact, have, log)
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
    return _with_gguf_config(artifact, Path(path), log)


def _with_gguf_config(artifact: ArtifactSpec, path: Path, log=print) -> Path:
    """pie reads a snapshot's encoding from config.json ("a snapshot must carry
    the config.json its encoding is read from"); a GGUF repo ships none, so the
    base model's is copied in — also into a snapshot fetched before this existed."""
    if artifact.gguf_config_from and not (path / "config.json").exists():
        from huggingface_hub import hf_hub_download

        log(f"download: config.json of {artifact.gguf_config_from} -> {path}")
        src = hf_hub_download(artifact.gguf_config_from, "config.json", token=os.environ.get("HF_TOKEN") or None)
        (path / "config.json").write_bytes(Path(src).read_bytes())
    return path
