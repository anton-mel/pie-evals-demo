from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from pie_evals.orchestrate.jobs import recorded_cell_keys
from pie_evals.orchestrate.store import Store
from pie_evals.schema.cell import Tier
from pie_evals.schema.record import ARROW_SCHEMA


def test_recorded_cell_keys_are_per_commit_and_tier(tmp_path: Path):
    st = Store(tmp_path)
    out = st.records_dir / "nightly" / "2026-09" / "run1.parquet"
    out.parent.mkdir(parents=True)
    rows = [
        {"cell_key": "pie|l40s-x1|a|ss-128-64|text-completion-bench|tp1", "pie_commit": "aaaa", "status": "pass", "engine": "pie"},
        {"cell_key": "pie|l40s-x1|a|c8|text-completion-bench|tp1", "pie_commit": "aaaa", "status": "crash", "engine": "pie"},
        {"cell_key": "pie|l40s-x1|a|c64|text-completion-bench|tp1", "pie_commit": "bbbb", "status": "pass", "engine": "pie"},
        {"cell_key": "vllm|l40s-x1|a|c8|text-completion-bench|tp1", "pie_commit": None, "status": "pass", "engine": "vllm", "engine_version": "0.30.0"},
        {"cell_key": "vllm|l40s-x1|a|c64|text-completion-bench|tp1", "pie_commit": None, "status": "pass", "engine": "vllm", "engine_version": "0.29.0"},
        {"cell_key": "pie|l40s-x1|a|c32|text-completion-bench|tp1", "pie_commit": "aaaa", "status": "not_run", "engine": "pie"},
    ]
    cols = {name: [row.get(name) for row in rows] for name in ARROW_SCHEMA.names}
    pq.write_table(pa.table(cols, schema=ARROW_SCHEMA), out)
    done = recorded_cell_keys(st, Tier("nightly"), "aaaa", {"vllm": "0.30.0"})
    # every pie outcome at this commit counts, a crash included — not a cell the budget never reached, not another
    # commit; a baseline counts at its pinned version whatever the pie commit
    assert done == {rows[0]["cell_key"], rows[1]["cell_key"], rows[3]["cell_key"]}
    assert recorded_cell_keys(st, Tier("smoke"), "aaaa") == set()
