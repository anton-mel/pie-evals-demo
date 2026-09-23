from pathlib import Path

import pytest

from pie_evals.orchestrate.jobs import make_jobs, process_key, shard_groups, cell_minutes
from pie_evals.orchestrate.matrix import Matrix
from pie_evals.orchestrate.store import Store
from pie_evals.schema import Tier

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def matrix():
    return Matrix.load(ROOT / "matrix")


def test_shards_respect_budget_and_keep_groups_whole(matrix):
    cells = [c for c in matrix.runnable(Tier.NIGHTLY) if c.platform.id == "l40s-x1"]
    shards = shard_groups(cells, matrix.job_budget_minutes)
    assert sum(len(s) for s in shards) == len(cells)
    for sh in shards:
        assert sum(cell_minutes(c) for c in sh) <= matrix.job_budget_minutes
    # a process group is either entirely inside one shard, or (only if it was itself over budget) split
    placement = {}
    for i, sh in enumerate(shards):
        for c in sh:
            placement.setdefault(process_key(c), set()).add(i)
    groups = {}
    for c in cells:
        groups.setdefault(process_key(c), []).append(c)
    for k, idxs in placement.items():
        if len(idxs) > 1:
            assert sum(cell_minutes(c) for c in groups[k]) > matrix.job_budget_minutes, f"group {k} split without need"


def test_jobs_carry_time_policy(matrix, tmp_path):
    jobs = make_jobs(matrix, Tier.NIGHTLY, pie_commit="abc", store=Store(tmp_path), platforms=["l40s-x1"])
    assert len(jobs) > 1
    ids = [j.job_id for j in jobs]
    assert len(ids) == len(set(ids))
    for j in jobs:
        assert j.budget_s == matrix.job_budget_minutes * 60
        assert j.kill_s == int(matrix.job_budget_minutes * matrix.kill_factor * 60)
        assert j.per_cell_timeout_s <= j.kill_s
        assert j.est_minutes <= matrix.job_budget_minutes


def test_every_tier_within_job_caps(matrix):
    cells = matrix.expand()
    for t in Tier:
        assert matrix.check_budget(t, cells) == [], matrix.check_budget(t, cells)


def test_multi_gpu_platforms_only_run_tp_gt1(matrix):
    for c in matrix.expand():
        if c.platform.count >= 2 and c.mode.tp == 1:
            assert c.tiers == [], f"{c.platform.id} tp1 must not be scheduled"


def test_available_platforms_keeps_runpod_and_online_resident(matrix, monkeypatch):
    import json

    from pie_evals.orchestrate import jobs as J

    runners = {"runners": [{"status": "online", "labels": [{"name": "self-hosted"}, {"name": "macos"}, {"name": "m1-max-32g"}]},
                           {"status": "offline", "labels": [{"name": "m4-pro-48g"}]}]}
    monkeypatch.setattr(J.subprocess, "run", lambda *a, **k: type("R", (), {"stdout": json.dumps(runners)})())
    ok, skipped = J.available_platforms(matrix, "o/r")
    assert "l40s-x1" in ok and "m1-max-32g" in ok
    assert "m4-pro-48g" in skipped and "m2-max" in skipped
