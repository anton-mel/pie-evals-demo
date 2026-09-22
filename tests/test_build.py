
from pie_evals.node import build as pb


def test_cache_key_and_miss(tmp_path):
    assert pb.cache_key("fa26669562dc7829c0f89c212529bc7f606a5e5c", ["cuda"]) == "fa26669562dc-cuda"
    assert not pb.is_cached("fa26669562dc", ["cuda"], tmp_path)


def test_restore_places_artifacts(tmp_path, monkeypatch):
    d = pb.cache_dir("abc123def456", ["cuda"], tmp_path)
    d.mkdir(parents=True)
    (d / "pie").write_bytes(b"bin")
    (d / "text_completion_bench.wasm").write_bytes(b"wasm")
    (d / "pie_server-0.5.0-cp312-none-any.whl").write_bytes(b"whl")
    pie_root = tmp_path / "pie"
    (pie_root / "sdk/server/python/python/pie").mkdir(parents=True)
    ran = []
    monkeypatch.setattr(pb.subprocess, "run", lambda *a, **k: ran.append(a[0]) or type("R", (), {"stdout": "", "returncode": 0})())
    assert pb.restore(pie_root, "abc123def456", ["cuda"], cache_root=tmp_path, log=lambda *_: None)
    assert (pie_root / "target/release/pie").read_bytes() == b"bin"
    assert (pie_root / "tests/inferlets/target/wasm32-wasip2/release/text_completion_bench.wasm").exists()
    assert any("pip" in a for a in ran)  # wheel installed
