from pathlib import Path

from pie_evals.node import reclaim
from pie_evals.orchestrate.jobs import make_jobs
from pie_evals.orchestrate.matrix import Matrix
from pie_evals.schema import Tier

ROOT = Path(__file__).resolve().parents[1]


def test_reclaim_keeps_this_jobs_imports_and_builds(tmp_path: Path, monkeypatch):
    m = Matrix.load(ROOT / "matrix")
    job = make_jobs(m, Tier.NIGHTLY, pie_commit="c" * 40, platforms=["l40s-x1"], engines=["pie"], cells=[c for c in m.expand() if c.artifact.id == "qwen3.5-0.8b-bf16"])[0]
    root = tmp_path / "cache"
    for d in ("artifacts/qwen3.5-0.8b-bf16-cccccccc", "artifacts/qwen3.5-0.8b-bf16-01234567", "artifacts/gemma-4-e4b-bf16-cccccccc", "artifacts/.tmp-x", "builds/cccccccccccc-cuda", "builds/012345678901-cuda", "shrink"):
        (root / d).mkdir(parents=True)
        (root / d / "f").write_bytes(b"x" * 10)
    monkeypatch.setenv("PIE_EVALS_CACHE", str(root))
    # plenty of room: nothing touched
    monkeypatch.setattr(reclaim, "free_gib", lambda p: 500.0)
    assert reclaim.reclaim(job, tmp_path / "hf", log=lambda *_: None) == 0.0
    assert (root / "artifacts/gemma-4-e4b-bf16-cccccccc").exists()
    # short on disk: everything this job does not need goes, its own import and build stay
    monkeypatch.setattr(reclaim, "free_gib", lambda p: 10.0)
    monkeypatch.setattr(reclaim, "_drop_hf_repos", lambda *a, **k: None)
    reclaim.reclaim(job, tmp_path / "hf", log=lambda *_: None)
    assert (root / "artifacts/qwen3.5-0.8b-bf16-cccccccc").exists()
    assert (root / "builds/cccccccccccc-cuda").exists()
    for gone in ("artifacts/qwen3.5-0.8b-bf16-01234567", "artifacts/gemma-4-e4b-bf16-cccccccc", "artifacts/.tmp-x", "builds/012345678901-cuda", "shrink"):
        assert not (root / gone).exists(), gone
