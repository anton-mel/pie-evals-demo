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
        {"cell_key": "pie|l40s-x1|a|ss-128-64|text-completion-bench|tp1", "pie_commit": "aaaa", "status": "pass"},
        {"cell_key": "pie|l40s-x1|a|c8|text-completion-bench|tp1", "pie_commit": "aaaa", "status": "crash"},
        {"cell_key": "pie|l40s-x1|a|c64|text-completion-bench|tp1", "pie_commit": "bbbb", "status": "pass"},
        {"cell_key": "vllm|l40s-x1|a|c8|text-completion-bench|tp1", "pie_commit": None, "status": "pass"},
    ]
    cols = {name: [row.get(name) for row in rows] for name in ARROW_SCHEMA.names}
    pq.write_table(pa.table(cols, schema=ARROW_SCHEMA), out)
    done = recorded_cell_keys(st, Tier("nightly"), "aaaa")
    # every recorded outcome at this commit counts, a crash included; other commits and baselines do not
    assert done == {rows[0]["cell_key"], rows[1]["cell_key"]}
    assert recorded_cell_keys(st, Tier("smoke"), "aaaa") == set()
