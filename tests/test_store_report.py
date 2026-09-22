from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from pie_evals.orchestrate import report as rp
from pie_evals.orchestrate.jobs import make_jobs
from pie_evals.orchestrate.matrix import Matrix
from pie_evals.orchestrate.store import Store
from pie_evals.schema import CellStatus, PerfMetrics, Provenance, Record, Tier

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def matrix():
    return Matrix.load(ROOT / "matrix")


def _rec(cell, value, when, status=CellStatus.PASS, engine_version="abc123", run="r"):
    prov = Provenance(harness_commit="h", pie_commit="abc123", engine_version=engine_version, checkpoint_revision="rev", hardware_fingerprint={"gpu": "x"})
    return Record(run_id=run, job_id="j", tier=Tier.SMOKE, cell_id=cell.cell_id, cell_key=cell.cell_key, cell=cell.model_copy(update={"engine_version": engine_version}),
                  status=status, perf=PerfMetrics(primary="decode_tok_s", decode_tok_s=value, rounds=[value], cov=0.002, prompt_tokens=100, output_tokens=64),
                  provenance=prov, started_at=when, duration_s=30.0)


def test_store_roundtrip_and_history(tmp_path, matrix):
    cells = matrix.runnable(Tier.SMOKE)
    cell = next(c for c in cells if c.workload.id == "ss-128-64" and c.artifact.id == "qwen3-0.6b-bf16" and c.platform.id == "l40s-x1" and c.program.id == "text-completion-bench")
    st = Store(tmp_path / "store")
    t0 = datetime(2026, 9, 1, tzinfo=timezone.utc)
    for i, v in enumerate([430, 432, 431, 433]):
        st.write_run([_rec(cell, v, t0 + timedelta(days=i), run=f"r{i}")], tier=Tier.SMOKE, run_id=f"r{i}", when=t0 + timedelta(days=i))
    hist = st.history()
    assert hist[cell.cell_id] == [430, 432, 431, 433]
    assert st.latest_by_cell()[cell.cell_id]["primary_value"] == 433


def test_store_refuses_missing_provenance(tmp_path, matrix):
    cell = matrix.runnable(Tier.SMOKE)[0]
    r = _rec(cell, 1.0, datetime.now(timezone.utc))
    r.provenance.checkpoint_revision = None
    with pytest.raises(ValueError):
        Store(tmp_path).write_run([r], tier=Tier.SMOKE, run_id="x")


def test_regression_is_noise_aware(tmp_path, matrix):
    cells = matrix.runnable(Tier.SMOKE)
    cell = next(c for c in cells if c.workload.id == "ss-128-64" and c.artifact.id == "qwen3-0.6b-bf16" and c.platform.id == "l40s-x1" and c.program.id == "text-completion-bench")
    st = Store(tmp_path / "store")
    t0 = datetime(2026, 9, 1, tzinfo=timezone.utc)
    vals = [430, 432, 431, 433, 430, 400]  # last one is a ~7% drop against <0.5% spread
    for i, v in enumerate(vals):
        st.write_run([_rec(cell, v, t0 + timedelta(days=i), run=f"r{i}")], tier=Tier.SMOKE, run_id=f"r{i}", when=t0 + timedelta(days=i))
    regs = rp.regressions(matrix, st, Tier.SMOKE)
    assert len(regs) == 1 and regs[0]["kind"] == "regression" and regs[0]["delta_rel"] < -0.05
    md = rp.regressions_markdown(regs)
    assert "regression" in md


def test_coverage_report_lists_not_run(tmp_path, matrix):
    st = Store(tmp_path / "store")
    views = rp.coverage(matrix, st, Tier.SMOKE)
    statuses = {v.status for v in views}
    assert "not_run" in statuses and "declared_unsupported" in statuses
    md = rp.coverage_markdown(views, Tier.SMOKE)
    assert "## Gaps" in md and "not_run" in md


def test_baseline_ratio_requires_input_parity(tmp_path, matrix):
    cells = matrix.runnable(Tier.NIGHTLY)
    pie = next(c for c in cells if str(c.engine) == "pie" and c.workload.id == "c32" and c.artifact.id == "qwen3-0.6b-bf16" and c.platform.id == "l40s-x1" and c.program.id == "text-completion-bench")
    vllm = next(c for c in cells if str(c.engine) == "vllm" and c.workload.id == "c32" and c.artifact.id == "qwen3-0.6b-bf16" and c.platform.id == "l40s-x1" and c.program.id == "text-completion-bench")
    st = Store(tmp_path / "store")
    now = datetime.now(timezone.utc)
    rp_ = _rec(pie, 9399, now)
    rv = _rec(vllm, 9056, now, engine_version="0.26.1")
    rv.provenance.pie_commit = None
    rv.provenance.engine_config_recipe = "competitive"
    st.write_run([rp_, rv], tier=Tier.NIGHTLY, run_id="n1", when=now)
    ratios = rp.baseline_ratios(matrix, st, Tier.NIGHTLY)
    assert len(ratios) == 1 and ratios[0]["pie_leads"] and ratios[0]["input_ok"]
    assert abs(ratios[0]["baseline_over_pie"] - 9056 / 9399) < 1e-6


def test_jobs_group_one_model_per_process(matrix, tmp_path):
    jobs = make_jobs(matrix, Tier.SMOKE, pie_commit="abc123", store=Store(tmp_path), platforms=["l40s-x1"])
    assert 1 <= len(jobs) <= matrix.suites["smoke"].max_jobs_per_platform
    for j in jobs:
        assert j.platform_id == "l40s-x1" and j.pie_build_features == ["cuda"]
        groups = j.cells_by_process()
        assert all(len({c.artifact.artifact_key for c in g}) == 1 for g in groups.values())
        assert j.model_dump_json()  # serialisable
