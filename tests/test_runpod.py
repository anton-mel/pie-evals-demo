from pathlib import Path

from pie_evals.orchestrate import runpod
from pie_evals.orchestrate.matrix import Matrix

ROOT = Path(__file__).resolve().parents[1]


def test_startup_script_matches_runner_image_layout():
    s = runpod.startup_script(["self-hosted", "linux", "l40s-x1"], repo="pie-project/pie-evals", kill_minutes=90)
    # three-layer kill: self-destruct timer, then terminate after the single job
    assert "sleep $(( 90 * 60 ))" in s and s.count("terminate") >= 3 and "DELETE" in s
    # one ephemeral job, labels carry the platform
    assert "--ephemeral" in s and "--labels \"self-hosted,linux,l40s-x1,img-latest\"" in s
    assert "/opt/actions-runner" in s  # the image's runner, not a fresh download
    # env layout of the image's runner.sh, plus what pie-evals adds
    for k in ("RUSTUP_HOME=$V/.rustup", "CARGO_HOME=$V/.cargo", "PIE_HOME=$V/.pie", "HF_HOME=$V/.hf", "HF_HUB_CACHE=$V/.hf/hub", "PIE_EVALS_CACHE=$V/pie-evals-cache"):
        assert k in s, k
    # shared-volume safety: work tree and cargo target are pod-local
    assert "CARGO_TARGET_DIR=/tmp/target" in s and "PIE_ROOT=/tmp/pie" in s and "PIE_MIRROR=$V/pie.git" in s
    # token minted in-pod from the PAT, as the image does
    assert "actions/runners/registration-token" in s and "GH_RUNNER_PAT" in s


def test_create_pod_rest_body(monkeypatch):
    m = Matrix.load(ROOT / "matrix")
    calls = []

    def fake_req(method, path, body=None, api_key=None, params=None):
        calls.append((method, path, body))
        if path.startswith("/networkvolumes/"):
            return {"id": "vol1", "dataCenterId": "EU-RO-1", "size": 500}
        if path == "/pods" and method == "POST":
            return {"id": "pod123"}
        return {}

    monkeypatch.setattr(runpod, "_req", fake_req)
    h = runpod.create_pod(m.platforms["l40s-x2"], repo="o/r", runner_pat="PAT", kill_minutes=90, network_volume_id="vol1", allowed_cuda_versions=["13.0"], api_key="k")
    assert h.id == "pod123" and h.data_center == "EU-RO-1"
    method, path, body = calls[-1]
    assert (method, path) == ("POST", "/pods")
    assert body["gpuTypeIds"] == ["NVIDIA L40S"] and body["gpuCount"] == 2
    assert body["networkVolumeId"] == "vol1" and body["volumeMountPath"] == "/workspace" and body["dataCenterIds"] == ["EU-RO-1"]
    assert body["imageName"] == runpod.DEFAULT_IMAGE and body["allowedCudaVersions"] == ["13.0"]
    assert body["env"]["GH_RUNNER_PAT"] == "PAT" and body["env"]["PIE_EVALS_PLATFORM"] == "l40s-x2"
    assert body["dockerStartCmd"][:2] == ["bash", "-lc"] and "--ephemeral" in body["dockerStartCmd"][2]


def test_create_pod_unpins_a_data_center_the_rest_schema_rejects(monkeypatch):
    m = Matrix.load(ROOT / "matrix")
    posts = []

    def fake_req(method, path, body=None, api_key=None, params=None):
        if path == "/pods" and method == "POST":
            posts.append(dict(body))
            if body.get("dataCenterIds"):
                raise RuntimeError('runpod POST /pods: 400 [{"problems":["At /pods/properties/dataCenterIds/items/enum: value must be one of ..."]}]')
            return {"id": "pod123"}
        return {}

    monkeypatch.setattr(runpod, "_req", fake_req)
    monkeypatch.setattr(runpod, "choose_placement", lambda *a, **k: runpod.Placement(data_center="US-MO-2", volume_id=None, stock="Low", note="stock"))
    h = runpod.create_pod(m.platforms["pro6000-x1"], repo="o/r", runner_pat="PAT", kill_minutes=90, volumes={"EUR-IS-1": "v1"}, api_key="k", log=lambda *_: None)
    assert h.id == "pod123" and h.data_center is None
    assert posts[0]["dataCenterIds"] == ["US-MO-2"] and "dataCenterIds" not in posts[1]


def test_reap_uses_name_timestamp(monkeypatch):
    import time

    now = int(time.time())
    monkeypatch.setattr(runpod, "list_pods", lambda api_key=None: [
        {"id": "old", "name": f"pie-evals-l40s-x1-{now - 3 * 3600}"},
        {"id": "new", "name": f"pie-evals-l40s-x1-{now - 60}"},
        {"id": "other", "name": "someone-elses-pod"},
    ])
    assert runpod.reap(2 * 3600, api_key="k", dry_run=True) == ["old"]


def test_placement_prefers_volume_dc_with_stock(monkeypatch):
    table = {("NVIDIA L40S", "EUR-IS-1"): "None", ("NVIDIA L40S", "US-TX-3"): "Low", ("NVIDIA GeForce RTX 4090", "EUR-IS-1"): "Medium"}
    monkeypatch.setattr(runpod, "stock", lambda g, dc, n=1, api_key=None: table.get((g, dc), "None"))
    monkeypatch.setattr(runpod, "data_centers", lambda api_key=None: [{"id": "EU-FR-1", "storageSupport": True}])
    vols = {"EUR-IS-1": "v1", "US-TX-3": "v2"}
    pl = runpod.choose_placement("NVIDIA GeForce RTX 4090", 1, volumes=vols, preferred=["EUR-IS-1"])
    assert (pl.data_center, pl.volume_id) == ("EUR-IS-1", "v1")
    pl = runpod.choose_placement("NVIDIA L40S", 1, volumes=vols, preferred=["EUR-IS-1"])
    assert (pl.data_center, pl.volume_id) == ("US-TX-3", "v2")  # second volume DC, has stock
    pl = runpod.choose_placement("NVIDIA H100 PCIe", 1, volumes=vols, preferred=["EUR-IS-1"])
    assert pl.data_center is None and pl.volume_id is None  # nowhere: unpinned


def test_matrix_loads_runpod_layout():
    m = Matrix.load(ROOT / "matrix")
    assert m.runpod["volumes"]["EUR-IS-1"] == "6v0l13yth9"
