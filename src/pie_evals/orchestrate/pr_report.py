"""One pie commit's results against pie ``main``'s history, as a PR comment.

The commit's records come straight from the node outputs of its run (a PR's
results are never written to the store); the history is the store's PASS
records of the same cells from the tiers that run pie alone with the same
repetition policy (targeted and smoke).
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from pie_evals.node.metrics.stats import median, regression_verdict
from pie_evals.schema import CellStatus, Record, Tier

from . import flops
from .store import Store

MARKER = "<!-- pie-evals -->"
HISTORY_TIERS = (Tier.TARGETED, Tier.SMOKE)


def node_rows(node_outs: list[Path]) -> list[dict[str, Any]]:
    rows = []
    for d in node_outs:
        f = Path(d) / "records.jsonl"
        if f.exists():
            for line in f.read_text().splitlines():
                if line.strip():
                    rec = Record.model_validate_json(line)
                    rows.append({**rec.to_row(), "params": rec.cell.workload.params, "base_model": rec.cell.artifact.base_model})
    return rows


def main_history(store: Store, *, exclude_commit: str | None, limit: int = 10) -> dict[str, list[float]]:
    rows = []
    for tier in HISTORY_TIERS:
        t = store.table(tier)
        if t.num_rows:
            rows += t.select(["cell_id", "status", "primary_value", "started_at", "pie_commit"]).to_pylist()
    rows = [r for r in rows if r["status"] == str(CellStatus.PASS) and r["primary_value"] is not None
            and r["pie_commit"] != exclude_commit]
    rows.sort(key=lambda r: r["started_at"])
    hist: dict[str, list[float]] = defaultdict(list)
    for r in rows:
        hist[r["cell_id"]].append(float(r["primary_value"]))
    return {k: v[-limit:] for k, v in hist.items()}


def _fmt(v: float | None, spec: str = ",.0f") -> str:
    return format(v, spec) if v is not None else "–"


def build(rows: list[dict[str, Any]], history: dict[str, list[float]], *, pie_commit: str, mode: str,
          run_url: str | None = None, dashboard: str | None = None, expected: list[str] | None = None) -> tuple[str, dict[str, Any]]:
    by_platform: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        by_platform[r["platform"]].append(r)

    regressed, improved, broken, unsteady = [], [], [], []
    sections = []
    for plat in sorted(by_platform):
        prs = sorted(by_platform[plat], key=lambda r: r["workload"])
        head = prs[0]
        fp = json.loads(head.get("hardware_fingerprint_json") or "{}")
        title = f"#### {head['accelerator']} (`{plat}`)"
        if fp.get("gpu_cores"):
            title += f" · {fp['gpu_cores']} GPU cores"
        lines = [title, "", "| workload | metric | this commit | main | change | prefill TFLOP/s | decode TFLOP/s |",
                 "|---|---|---:|---:|---:|---:|---:|"]
        for r in prs:
            name = f"{r['workload']}" + (f" · {r['program']}" if r["program"] != "text-completion-bench" else "")
            noisy = r["status"] == str(CellStatus.NOISY) and r["primary_value"] is not None
            if not noisy and (r["status"] != str(CellStatus.PASS) or r["primary_value"] is None):
                why = r.get("error_class") or r["status"]
                broken.append(f"{plat} {r['workload']} ({why})")
                lines.append(f"| {name} | – | ❌ {why} | | | | |")
                continue
            if noisy:
                unsteady.append(f"{plat} {r['workload']}")
            value = float(r["primary_value"])
            h = history.get(r["cell_id"], [])
            base = median(h) if h else None
            change = "⚠️ noisy" if noisy else ""
            if base:
                v = regression_verdict(value, h) if len(h) >= 3 and not noisy else None
                pct = 100 * (value / base - 1)
                mark = ""
                if v and v.regressed:
                    mark = " 🔴"
                    regressed.append(f"{plat} {r['workload']} ({pct:+.1f}%)")
                elif v and v.improved:
                    mark = " 🟢"
                    improved.append(f"{plat} {r['workload']} ({pct:+.1f}%)")
                change = f"{pct:+.1f}%{mark}" + (" ⚠️ noisy" if noisy else "")
            tf = flops.tflops(r, r["params"], flops.model_config(r["base_model"]))
            metric = r["primary_metric"].replace("_tok_s", " tok/s").replace("_", " ")
            lines.append(f"| {name} | {metric} | {_fmt(value)} | {_fmt(base)} | {change} | "
                         f"{_fmt(tf['prefill_tflops'], '.2f')} | {_fmt(tf['decode_tflops'], '.2f')} |")
        sections.append("\n".join(lines))

    missing = sorted(set(expected or []) - set(by_platform))
    summary = [MARKER, f"### pie-evals · {mode} · `{pie_commit[:10]}`", ""]
    if missing:
        summary.append(f"**No result from:** {', '.join(missing)}")
    if regressed:
        summary.append(f"**Slower than main:** {', '.join(regressed)}")
    if improved:
        summary.append(f"**Faster than main:** {', '.join(improved)}")
    if broken:
        summary.append(f"**Did not run:** {', '.join(broken)}")
    if unsteady:
        summary.append(f"**Too noisy to judge:** {', '.join(unsteady)}")
    if not (missing or regressed or improved or broken or unsteady):
        summary.append("Every workload is within its usual noise of `main`.")
    summary.append("")
    summary.append("Change is against the median of the last `main` runs of the same cell; 🔴/🟢 only when outside "
                   "that cell's own noise band (needs 3+ runs).")
    links = [f"[run]({run_url})" if run_url else "", f"[history]({dashboard})" if dashboard else ""]
    if any(links):
        summary.append(" · ".join(x for x in links if x))
    body = "\n\n".join([summary[0] + "\n" + summary[1], *[x for x in summary[3:] if x], *sections]) + "\n"
    verdict = {"regressions": len(regressed), "improvements": len(improved), "broken": len(broken), "noisy": len(unsteady), "missing": missing}
    return body, verdict
