"""The store's pie history as one static page: a chart per (platform,
artifact, workload, program, mode), pie commits on the x axis, each cell's
primary metric on the y axis, FLOP/s in the tooltip."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from pie_evals.schema import CellStatus

from . import flops
from .store import Store

PIE_COMMIT_URL = "https://github.com/pie-project/pie/commit/"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>pie-evals history</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<style>
  body { font: 14px/1.4 -apple-system, system-ui, sans-serif; margin: 0 auto; max-width: 1200px; padding: 16px; color: #1f2328; }
  h1 { font-size: 20px; } h2 { font-size: 16px; margin-top: 32px; border-bottom: 1px solid #d0d7de; padding-bottom: 4px; }
  .filters { display: flex; gap: 12px; flex-wrap: wrap; margin: 12px 0; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 16px; }
  .card { border: 1px solid #d0d7de; border-radius: 6px; padding: 8px; }
  .card h3 { font-size: 13px; margin: 0 0 4px; font-weight: 600; }
  .muted { color: #656d76; font-size: 12px; }
</style>
</head>
<body>
<h1>pie-evals history</h1>
<p class="muted">pie alone, on every platform, over pie commits. Generated __GENERATED__. Click a point to open the commit.</p>
<div class="filters">
  <label>platform <select id="platform"></select></label>
  <label>model <select id="artifact"></select></label>
</div>
<div id="out"></div>
<script>
const DATA = __DATA__;
const COMMIT = "__COMMIT_URL__";
const sel = (id, values) => { const s = document.getElementById(id); s.innerHTML = ["(all)", ...values].map(v => `<option>${v}</option>`).join(""); s.onchange = draw; };
sel("platform", [...new Set(DATA.map(d => d.platform))].sort());
sel("artifact", [...new Set(DATA.map(d => d.artifact))].sort());
const charts = [];
function draw() {
  charts.splice(0).forEach(c => c.destroy());
  const p = document.getElementById("platform").value, a = document.getElementById("artifact").value;
  const out = document.getElementById("out"); out.innerHTML = "";
  const byPlat = {};
  DATA.filter(d => (p === "(all)" || d.platform === p) && (a === "(all)" || d.artifact === a))
      .forEach(d => (byPlat[d.platform] ||= []).push(d));
  for (const plat of Object.keys(byPlat).sort()) {
    const h = document.createElement("h2"); h.textContent = `${plat} · ${byPlat[plat][0].accelerator}`; out.appendChild(h);
    const grid = document.createElement("div"); grid.className = "grid"; out.appendChild(grid);
    for (const s of byPlat[plat]) {
      const card = document.createElement("div"); card.className = "card";
      card.innerHTML = `<h3>${s.artifact} · ${s.workload}${s.program === "text-completion-bench" ? "" : " · " + s.program} · ${s.mode}</h3><div class="muted">${s.metric}</div><canvas></canvas>`;
      grid.appendChild(card);
      charts.push(new Chart(card.querySelector("canvas"), {
        type: "line",
        data: { labels: s.points.map(x => x.commit.slice(0, 8)), datasets: [{ data: s.points.map(x => x.value), borderColor: "#0969da", pointRadius: 3, tension: 0 }] },
        options: {
          plugins: { legend: { display: false }, tooltip: { callbacks: {
            title: i => `${s.points[i[0].dataIndex].commit.slice(0, 10)} · ${s.points[i[0].dataIndex].date}`,
            afterLabel: i => { const x = s.points[i.dataIndex]; return [x.prefill_tflops != null ? `prefill ${x.prefill_tflops.toFixed(2)} TFLOP/s` : null, x.decode_tflops != null ? `decode ${x.decode_tflops.toFixed(2)} TFLOP/s` : null, x.tier].filter(Boolean); } } } },
          scales: { y: { beginAtZero: false } },
          onClick: (e, el) => { if (el.length) window.open(COMMIT + s.points[el[0].index].commit, "_blank"); },
        },
      }));
    }
  }
}
draw();
</script>
</body>
</html>
"""


def series(store: Store) -> list[dict]:
    t = store.table()
    if t.num_rows == 0:
        return []
    cols = ["engine", "status", "platform", "accelerator", "artifact", "workload", "program", "mode", "tier", "primary_metric",
            "primary_value", "prefill_tok_s", "decode_tok_s", "output_tok_s", "pie_commit", "started_at", "record_json"]
    rows = [r for r in t.select(cols).to_pylist()
            if r["engine"] == "pie" and r["status"] == str(CellStatus.PASS) and r["primary_value"] is not None and r["pie_commit"]]
    rows.sort(key=lambda r: r["started_at"])
    grouped: dict[tuple, list[dict]] = defaultdict(list)
    for r in rows:
        grouped[(r["platform"], r["artifact"], r["workload"], r["program"], r["mode"], r["primary_metric"])].append(r)
    out = []
    for (plat, art, wl, prog, mode, metric), rs in sorted(grouped.items()):
        cell = json.loads(rs[-1]["record_json"])["cell"]
        config = flops.model_config(cell["artifact"]["base_model"]) if cell["artifact"]["kind"] == "full" else None
        by_commit: dict[str, dict] = {}
        for r in rs:
            tf = flops.tflops(r, cell["workload"]["params"], config)
            by_commit[r["pie_commit"]] = {"commit": r["pie_commit"], "value": r["primary_value"], "tier": r["tier"],
                                          "date": r["started_at"].strftime("%Y-%m-%d"), **tf}
        out.append({"platform": plat, "accelerator": rs[-1]["accelerator"], "artifact": art, "workload": wl, "program": prog,
                    "mode": mode, "metric": metric.replace("_tok_s", " tok/s").replace("_", " "), "points": list(by_commit.values())})
    return out


def render(store: Store, out: Path) -> int:
    from datetime import datetime, timezone

    data = series(store)
    out.mkdir(parents=True, exist_ok=True)
    html = (PAGE.replace("__DATA__", json.dumps(data))
                .replace("__COMMIT_URL__", PIE_COMMIT_URL)
                .replace("__GENERATED__", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")))
    (out / "index.html").write_text(html)
    return len(data)
