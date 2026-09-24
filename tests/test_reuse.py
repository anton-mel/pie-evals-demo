import time

from pie_evals.orchestrate import runpod


def _runner(pod: str, labels: list[str], busy: bool, status: str = "online") -> dict:
    return {"name": f"runpod-{pod}", "status": status, "busy": busy, "labels": [{"name": x} for x in ["self-hosted", "Linux", "X64", *labels]]}


def test_a_live_pod_with_every_label_is_reused():
    runners = [
        _runner("aaa", ["l40s-x1"], True),
        _runner("bbb", ["l40s-x1", "l40s-x2"], True),
        _runner("ccc", ["l40s-x1", "l40s-x2"], False, status="offline"),
        {"name": "Anton's Mac", "status": "online", "busy": False, "labels": [{"name": "m5-max-48g"}]},
    ]
    assert runpod.reusable_pod(["self-hosted", "linux", "l40s-x2", "l40s-x1"], runners) == ("bbb", ["l40s-x1", "l40s-x2"])
    assert runpod.reusable_pod(["self-hosted", "linux", "l40s-x1"], runners)[0] == "aaa"
    assert runpod.reusable_pod(["self-hosted", "linux", "a100-pcie-x1"], runners) is None
    assert runpod.busy_pods(runners) == {"aaa", "bbb"}


def test_reap_spares_a_busy_pod_until_the_hard_cap(monkeypatch):
    now = int(time.time())
    monkeypatch.setattr(runpod, "list_pods", lambda api_key=None: [
        {"id": "busy", "name": f"pie-evals-l40s-x2-{now - 5 * 3600}"},
        {"id": "ancient", "name": f"pie-evals-l40s-x2-{now - 31 * 3600}"},
        {"id": "idle", "name": f"pie-evals-l40s-x1-{now - 3 * 3600}"},
        {"id": "young", "name": f"pie-evals-l40s-x1-{now - 60}"},
    ])
    killed = runpod.reap(int(2.5 * 3600), api_key="k", dry_run=True, keep={"busy", "ancient"}, hard_max_age_s=30 * 3600)
    assert killed == ["ancient", "idle"]
