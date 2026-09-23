
from pie_evals.node import build as pb


def test_cache_key_and_miss(tmp_path):
    assert pb.cache_key("fa26669562dc7829c0f89c212529bc7f606a5e5c", ["cuda"]) == "fa26669562dc-cuda"
    assert not pb.is_cached("fa26669562dc", ["cuda"], tmp_path)


def test_restore_places_artifacts(tmp_path, monkeypatch):
    d = pb.cache_dir("abc123def456", ["cuda"], tmp_path)
    d.mkdir(parents=True)
    (d / "pie").write_bytes(b"bin")
    (d / "wasm").mkdir()
    (d / "wasm" / "text_completion_bench.wasm").write_bytes(b"wasm")
    (d / "pie_server-0.5.0-cp312-none-any.whl").write_bytes(b"whl")
    pie_root = tmp_path / "pie"
    (pie_root / "python/server/python/pie").mkdir(parents=True)
    installed = []
    monkeypatch.setattr(pb, "bench_python", lambda cache_root=None, log=print: tmp_path / "venv/bin/python")
    monkeypatch.setattr(pb, "_pip_install", lambda py, args: installed.append(args))
    monkeypatch.setattr(pb.subprocess, "run", lambda *a, **k: type("R", (), {"stdout": "", "returncode": 0})())
    assert pb.restore(pie_root, "abc123def456", ["cuda"], cache_root=tmp_path, set_env=False, log=lambda *_: None)
    assert (pie_root / "target/release/pie").read_bytes() == b"bin"
    assert (pie_root / "examples/target/wasm32-wasip2/release/text_completion_bench.wasm").exists()
    assert installed and installed[0][-1].endswith(".whl")  # wheel installed into the bench venv
    assert installed[0][0] == "--force-reinstall"
