from pathlib import Path

from pie_evals.orchestrate import runpod
from pie_evals.orchestrate.matrix import Matrix

ROOT = Path(__file__).resolve().parents[1]


def test_startup_script_has_three_kill_layers_and_caches_on_volume():
    s = runpod.startup_script(["self-hosted", "linux", "l40s-x1"], repo="o/r", runner_token="T", image_version="v1", kill_minutes=90)
    assert "sleep $(( 90 * 60 ))" in s and "runpodctl remove pod" in s  # self-destruct
    assert "--ephemeral" in s and "--labels \"self-hosted,linux,l40s-x1,img-v1\"" in s
    assert "HF_HUB_CACHE=/workspace/hf" in s and "PIE_EVALS_CACHE=/workspace/pie-evals-cache" in s and "PIE_ROOT=/workspace/pie" in s
    assert "actions-runner-linux-x64" in s  # installs the runner on a stock image


def test_create_pod_pins_volume_datacenter(monkeypatch):
    m = Matrix.load(ROOT / "matrix")
    calls = []

    def fake_gql(query, variables=None, api_key=None):
        calls.append((query, variables))
        if "networkVolumes" in query:
            return {"myself": {"networkVolumes": [{"id": "vol1", "name": "n", "size": 500, "dataCenterId": "EU-RO-1"}]}}
        return {"podFindAndDeployOnDemand": {"id": "pod123", "name": "x"}}

    monkeypatch.setattr(runpod, "_gql", fake_gql)
    h = runpod.create_pod(m.platforms["l40s-x1"], image="img", repo="o/r", runner_token="T", image_version="v", kill_minutes=90,
                          network_volume_id="vol1", allowed_cuda_versions=["13.0"], api_key="k")
    assert h.id == "pod123" and h.data_center == "EU-RO-1"
    inp = calls[-1][1]["input"]
    assert inp["dataCenterId"] == "EU-RO-1" and inp["networkVolumeId"] == "vol1" and inp["volumeMountPath"] == "/workspace"
    assert inp["gpuTypeId"] == "NVIDIA L40S" and inp["gpuCount"] == 1 and inp["allowedCudaVersions"] == ["13.0"]
    assert any(e["key"] == "PIE_EVALS_KILL_MINUTES" and e["value"] == "90" for e in inp["env"])


def test_reap_uses_name_timestamp(monkeypatch):
    import time
    now = int(time.time())
    monkeypatch.setattr(runpod, "list_pods", lambda api_key=None: [
        {"id": "old", "name": f"pie-evals-l40s-x1-{now - 3 * 3600}"},
        {"id": "new", "name": f"pie-evals-l40s-x1-{now - 60}"},
        {"id": "other", "name": "someone-elses-pod"},
    ])
    killed = runpod.reap(2 * 3600, api_key="k", dry_run=True)
    assert killed == ["old"]
