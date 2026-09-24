from pathlib import Path

from pie_evals.node.cli import mask_gpus
from pie_evals.orchestrate.jobs import make_jobs, plan_pods
from pie_evals.orchestrate.matrix import Matrix
from pie_evals.schema import Tier

ROOT = Path(__file__).resolve().parents[1]


def test_one_pod_hosts_the_x1_and_x2_of_its_gpu():
    m = Matrix.load(ROOT / "matrix")
    js = make_jobs(m, Tier.NIGHTLY, pie_commit="c" * 40, platforms=["l40s-x1", "l40s-x2", "rtx4090-x1"], engines=["pie"])
    pods = {p["pod"]: p for p in plan_pods(m, js)}
    assert set(pods) == {"l40s-x2", "rtx4090-x1"}
    l40s = pods["l40s-x2"]
    assert {"l40s-x1", "l40s-x2"} <= set(l40s["labels"])
    assert set(l40s["jobs"]) == {j.job_id for j in js if j.platform_id.startswith("l40s")}
    # the kill timer covers the whole queue, never less than one job's
    assert l40s["kill_minutes"] >= max(m.kill_minutes, int(l40s["est_minutes"] * m.kill_factor))
    assert len(js) > len(pods)
    # no x2 stock: the x1's own pod is tried next (it seats only the x1 shards)
    assert l40s["fallback"] == ["l40s-x2", "l40s-x1"] and pods["rtx4090-x1"]["fallback"] == ["rtx4090-x1"]


def test_resident_runners_need_no_pod():
    m = Matrix.load(ROOT / "matrix")
    js = make_jobs(m, Tier.NIGHTLY, pie_commit="c" * 40, platforms=["m5-max-48g"], engines=["pie"])
    assert js and plan_pods(m, js) == []


def test_mask_gpus_keeps_the_platform_count(monkeypatch):
    m = Matrix.load(ROOT / "matrix")
    js = make_jobs(m, Tier.NIGHTLY, pie_commit="c" * 40, platforms=["l40s-x1"], engines=["pie"])
    import subprocess

    class R:
        stdout = "GPU 0: NVIDIA L40S (UUID: a)\nGPU 1: NVIDIA L40S (UUID: b)\n"

    monkeypatch.setattr(subprocess, "run", lambda *a, **k: R())
    monkeypatch.setattr("shutil.which", lambda _: "/usr/bin/nvidia-smi")
    env: dict = {}
    assert mask_gpus(js[0], env) == "0" and env["CUDA_VISIBLE_DEVICES"] == "0"
    env = {"CUDA_VISIBLE_DEVICES": "1"}
    assert mask_gpus(js[0], env) is None and env["CUDA_VISIBLE_DEVICES"] == "1"


def test_run_label_isolates_a_runs_pods(tmp_path):
    import json
    import subprocess
    import sys

    out = tmp_path / "jobs"
    subprocess.run([sys.executable, "-m", "pie_evals.orchestrate.cli", "jobs", "--tier", "nightly", "--pie-commit", "c" * 40, "--platform", "l40s-x1", "--engine", "pie", "--artifact", "qwen3.5-0.8b-bf16", "--run-label", "run-42", "--out", str(out)], check=True, cwd=ROOT, capture_output=True)
    shards = json.loads((out / "gh-matrix.json").read_text())["include"]
    pods = json.loads((out / "pods.json").read_text())["include"]
    assert shards and all("run-42" in s["labels"] for s in shards)
    assert pods and all("run-42" in p["labels"] for p in pods)
