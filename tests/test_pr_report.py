from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from pie_evals.node import build as pb
from pie_evals.orchestrate import dashboard, flops
from pie_evals.orchestrate import pr_report as prr
from pie_evals.orchestrate.matrix import Matrix
from pie_evals.orchestrate.store import Store
from pie_evals.schema import CellStatus, PerfMetrics, Provenance, Record, Tier

ROOT = Path(__file__).resolve().parents[1]

QWEN35_08B = {
    "hidden_size": 1024, "num_hidden_layers": 24, "num_attention_heads": 8, "num_key_value_heads": 2, "head_dim": 256,
    "intermediate_size": 3584, "vocab_size": 248320, "attn_output_gate": True,
    "layer_types": (["linear_attention"] * 3 + ["full_attention"]) * 6,
    "linear_num_key_heads": 16, "linear_num_value_heads": 16, "linear_key_head_dim": 128, "linear_value_head_dim": 128,
    "linear_conv_kernel_dim": 4,
}


@pytest.fixture(scope="module")
def matrix():
    return Matrix.load(ROOT / "matrix")


def _cell(matrix, platform, workload):
    return next(c for c in matrix.runnable(Tier.TARGETED)
                if c.platform.id == platform and c.workload.id == workload)


def _rec(cell, value, when, *, commit, status=CellStatus.PASS, run="r"):
    prov = Provenance(harness_commit="h", pie_commit=commit, engine_version=commit, checkpoint_revision="rev", hardware_fingerprint={"gpu_cores": "40"})
    return Record(run_id=run, job_id="j", tier=Tier.TARGETED, cell_id=cell.cell_id, cell_key=cell.cell_key, cell=cell, status=status,
                  perf=PerfMetrics(primary="decode_tok_s", decode_tok_s=value, prefill_tok_s=value * 30, rounds=[value], cov=0.002),
                  provenance=prov, started_at=when, duration_s=30.0)


def _node_out(tmp_path, records):
    d = tmp_path / "out"
    d.mkdir()
    (d / "records.jsonl").write_text("\n".join(r.model_dump_json() for r in records) + "\n")
    return d


def test_targeted_is_small_and_pie_only(matrix):
    cells = matrix.runnable(Tier.TARGETED)
    assert cells and all(c.engine.value == "pie" and c.mode.tp == 1 for c in cells)
    assert {c.workload.id for c in cells} == {"control-aa", "ss-128-64", "lc-1k-128", "lc-2k-128", "c8", "c32"}
    assert not matrix.check_budget(Tier.TARGETED)


def test_metal_build_is_cached_without_a_wheel(tmp_path):
    d = pb.cache_dir("a" * 40, ["metal"], tmp_path)
    (d / "wasm").mkdir(parents=True)
    (d / "pie").write_text("")
    (d / "wasm" / "x.wasm").write_text("")
    assert pb.is_cached("a" * 40, ["metal"], tmp_path)
    assert not pb.is_cached("a" * 40, ["cuda"], tmp_path)


def test_flops_scale_with_the_rate():
    one = flops.tflops({"decode_tok_s": 100.0, "prefill_tok_s": 1000.0}, {"prefill": 128, "decode": 64}, QWEN35_08B)
    two = flops.tflops({"decode_tok_s": 200.0, "prefill_tok_s": 2000.0}, {"prefill": 128, "decode": 64}, QWEN35_08B)
    assert two["decode_tflops"] == pytest.approx(2 * one["decode_tflops"])
    assert two["prefill_tflops"] == pytest.approx(2 * one["prefill_tflops"])
    per_token = flops.decode_flops_per_token(QWEN35_08B, 160)
    assert 1.4e9 < per_token < 1.8e9
    batched = flops.tflops({"output_tok_s": 1000.0, "prefill_tok_s": 5.0}, {"prefill": 128, "decode": 128, "concurrency": 8}, QWEN35_08B)
    assert batched["prefill_tflops"] is None and batched["decode_tflops"] > 0
    assert flops.tflops({"decode_tok_s": 1.0}, {"prefill": 1}, None) == {"prefill_tflops": None, "decode_tflops": None}


def test_pr_report_flags_a_drop_against_main(tmp_path, matrix, monkeypatch):
    monkeypatch.setattr(flops, "model_config", lambda repo: QWEN35_08B)
    cell = _cell(matrix, "m5-max-48g", "ss-128-64")
    st = Store(tmp_path / "store")
    t0 = datetime(2026, 9, 1, tzinfo=timezone.utc)
    for i, v in enumerate([500, 502, 501, 503]):
        st.write_run([_rec(cell, v, t0 + timedelta(days=i), commit=f"main{i}", run=f"r{i}")], tier=Tier.TARGETED, run_id=f"r{i}")
    out = _node_out(tmp_path, [_rec(cell, 450, t0 + timedelta(days=9), commit="pr")])
    rows = prr.node_rows([out])
    body, verdict = prr.build(rows, prr.main_history(st, exclude_commit="pr"), pie_commit="pr" * 20, mode="targeted",
                              expected=["m5-max-48g", "m1-max-32g"])
    assert verdict["regressions"] == 1 and verdict["missing"] == ["m1-max-32g"]
    assert body.startswith(prr.MARKER) and "🔴" in body and "Slower than main" in body


def test_pr_report_keeps_a_noisy_value_out_of_the_verdict(tmp_path, matrix, monkeypatch):
    monkeypatch.setattr(flops, "model_config", lambda repo: None)
    cell = _cell(matrix, "m5-max-48g", "c8")
    out = _node_out(tmp_path, [_rec(cell, 900, datetime.now(timezone.utc), commit="pr", status=CellStatus.NOISY)])
    body, verdict = prr.build(prr.node_rows([out]), {}, pie_commit="pr" * 20, mode="targeted")
    assert verdict["noisy"] == 1 and verdict["regressions"] == 0 and "⚠️ noisy" in body


def test_dashboard_has_one_series_per_cell(tmp_path, matrix, monkeypatch):
    monkeypatch.setattr(flops, "model_config", lambda repo: QWEN35_08B)
    st = Store(tmp_path / "store")
    t0 = datetime(2026, 9, 1, tzinfo=timezone.utc)
    for i, wl in enumerate(["ss-128-64", "lc-2k-128"]):
        cell = _cell(matrix, "m5-max-48g", wl)
        for j in range(2):
            st.write_run([_rec(cell, 400 + j, t0 + timedelta(days=j), commit=f"c{j}", run=f"r{i}{j}")], tier=Tier.TARGETED, run_id=f"r{i}{j}")
    assert dashboard.render(st, tmp_path / "site") == 2
    html = (tmp_path / "site" / "index.html").read_text()
    assert "lc-2k-128" in html and "decode_tflops" in html
