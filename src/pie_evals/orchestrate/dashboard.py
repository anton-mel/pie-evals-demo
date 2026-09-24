"""The store's pie history as one static page: an overview matrix (platform x
model, latest vs previous pie commit) plus a chart per (platform, artifact,
workload, program, mode) with pie commits on the x axis. Toggle switches every
chart and the matrix between tok/s and TFLOP/s so the two never disagree."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from pie_evals.schema import CellStatus

from . import flops
from .store import Store

PIE_COMMIT_URL = "https://github.com/pie-project/pie/commit/"

# Plain-language label + display group for a workload shape, derived from
# matrix/workloads.yaml's own kind/params so the dashboard never invents
# meanings the config doesn't state. Group order matches that file's section
# comments (self-check, single stream, concurrency sweep, ...).
GROUP_ORDER = ["Self-check", "Single stream", "Concurrency sweep", "Long context",
               "Prefix sharing", "Length mix", "KV oversubscription", "Replay", "Other"]


def _toks(n: int) -> str:
    return f"{n / 1024:g}K" if n >= 1024 else str(n)


def _workload_label(w: dict) -> tuple[str, str]:
    kind, p = w.get("kind"), w.get("params", {})
    if kind == "control_aa":
        return f"Self-check · {p['prefill']}→{p['decode']} tok", "Self-check"
    if kind == "single_stream":
        return f"Single stream · {_toks(p['prefill'])}→{p['decode']} tok", "Single stream"
    if kind == "concurrency":
        base = f"Concurrency {p['concurrency']} · {_toks(p['prefill'])}→{p['decode']} tok"
        return (base + " · KV oversub", "KV oversubscription") if p.get("kv_oversubscribe") else (base, "Concurrency sweep")
    if kind == "long_context":
        return f"Long context {_toks(p['prefill'])} → {p['decode']} tok", "Long context"
    if kind == "prefix_shared":
        return f"Shared prefix {_toks(p['shared_prefix'])} × {p['variants']} variants", "Prefix sharing"
    if kind == "mixed_length":
        return f"Mixed lengths · {p['num_requests']} req", "Length mix"
    if kind == "replay":
        return f"Replay: {p.get('trace', w['id'])}", "Replay"
    return w["id"], "Other"



PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>pie-evals history</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<style>
  :root {
    color-scheme: light;
    --surface-1: #fcfcfb;
    --surface-2: #f9f9f7;
    --text-primary: #0b0b0b;
    --text-secondary: #52514e;
    --text-muted: #898781;
    --gridline: #e1e0d9;
    --baseline: #c3c2b7;
    --border: rgba(11,11,11,0.10);
    --series-1: #2a78d6;
    --good: #0ca30c;
    --warning: #fab219;
    --critical: #d03b3b;
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) {
      color-scheme: dark;
      --surface-1: #1a1a19;
      --surface-2: #0d0d0d;
      --text-primary: #ffffff;
      --text-secondary: #c3c2b7;
      --text-muted: #898781;
      --gridline: #2c2c2a;
      --baseline: #383835;
      --border: rgba(255,255,255,0.10);
      --series-1: #3987e5;
      --good: #0ca30c;
      --warning: #fab219;
      --critical: #e66767;
    }
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --surface-1: #1a1a19;
    --surface-2: #0d0d0d;
    --text-primary: #ffffff;
    --text-secondary: #c3c2b7;
    --text-muted: #898781;
    --gridline: #2c2c2a;
    --baseline: #383835;
    --border: rgba(255,255,255,0.10);
    --series-1: #3987e5;
    --good: #0ca30c;
    --warning: #fab219;
    --critical: #e66767;
  }
  * { box-sizing: border-box; }
  body {
    font: 14px/1.4 -apple-system, system-ui, "Segoe UI", sans-serif;
    margin: 0; padding: 0 16px 48px;
    background: var(--surface-2); color: var(--text-primary);
  }
  .wrap { max-width: 1200px; margin: 0 auto; }
  header { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; padding: 20px 0 4px; flex-wrap: wrap; }
  h1 { font-size: 20px; margin: 0; }
  h2 { font-size: 15px; margin: 0 0 10px; }
  .muted { color: var(--text-secondary); font-size: 12px; }
  .theme-btn {
    border: 1px solid var(--border); background: var(--surface-1); color: var(--text-secondary);
    border-radius: 6px; padding: 5px 10px; font-size: 12px; cursor: pointer;
  }
  .toolbar {
    display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
    margin: 12px 0 24px; padding: 10px 12px; background: var(--surface-1);
    border: 1px solid var(--border); border-radius: 8px;
  }
  .toolbar label { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-secondary); }
  .toolbar select {
    font: inherit; font-size: 12px; padding: 4px 6px; border-radius: 5px;
    border: 1px solid var(--border); background: var(--surface-2); color: var(--text-primary);
  }
  .segmented { display: inline-flex; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }
  .segmented button {
    font: inherit; font-size: 12px; padding: 5px 10px; border: 0; cursor: pointer;
    background: var(--surface-2); color: var(--text-secondary);
  }
  .segmented button + button { border-left: 1px solid var(--border); }
  .segmented button[aria-pressed="true"] { background: var(--series-1); color: #fff; }

  section { margin-top: 28px; }
  table.matrix { border-collapse: collapse; width: 100%; font-size: 12px; }
  table.matrix caption { caption-side: bottom; text-align: left; padding-top: 8px; color: var(--text-muted); font-size: 11px; }
  table.matrix th, table.matrix td { border: 1px solid var(--gridline); padding: 6px 8px; text-align: right; white-space: nowrap; }
  table.matrix thead th { text-align: center; color: var(--text-secondary); font-weight: 600; background: var(--surface-1); position: sticky; top: 0; }
  table.matrix tbody th { text-align: left; color: var(--text-primary); font-weight: 600; background: var(--surface-1); position: sticky; left: 0; }
  table.matrix tbody th .accel { display: block; font-weight: 400; color: var(--text-muted); font-size: 10.5px; }
  table.matrix td { font-variant-numeric: tabular-nums; cursor: pointer; }
  table.matrix td:hover { outline: 2px solid var(--series-1); outline-offset: -2px; }
  table.matrix td.empty { color: var(--text-muted); cursor: default; text-align: center; }
  table.matrix td.empty:hover { outline: none; }
  .delta { display: block; font-size: 11px; }
  .delta.good { color: var(--good); }
  .delta.critical { color: var(--critical); }
  .delta.flat { color: var(--text-muted); }

  .detail-head { border-bottom: 1px solid var(--gridline); padding-bottom: 6px; margin-bottom: 4px; }
  .detail-head h2 { margin-bottom: 2px; }
  .program-block + .program-block { margin-top: 28px; }
  .program-block > .program-title { font-size: 12px; font-weight: 600; color: var(--text-secondary); margin: 18px 0 8px; }
  .group-block + .group-block { margin-top: 18px; }
  .group-block > .group-title {
    font-size: 11px; font-weight: 600; letter-spacing: .03em; text-transform: uppercase;
    color: var(--text-muted); margin: 0 0 8px;
  }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 14px; }
  .card { border: 1px solid var(--border); background: var(--surface-1); border-radius: 8px; padding: 10px; }
  .card h3 { font-size: 12.5px; margin: 0 0 2px; font-weight: 600; }
  .card .unit { font-size: 11px; color: var(--text-muted); margin-bottom: 4px; }
  .card canvas { max-height: 160px; }
  .empty-state { color: var(--text-secondary); padding: 32px 20px; text-align: center; background: var(--surface-1); border: 1px dashed var(--border); border-radius: 8px; }
</style>
</head>
<body>
<div class="wrap">
<header>
  <div>
    <h1>pie-evals history</h1>
    <p class="muted">pie alone, on every platform, over pie commits &mdash; commit vs. improvement. Generated __GENERATED__.</p>
  </div>
  <button class="theme-btn" id="theme-toggle" type="button">theme</button>
</header>

<div class="toolbar">
  <label>platform <select id="platform"></select></label>
  <label>model <select id="artifact"></select></label>
  <label>unit
    <span class="segmented" id="unit" role="group">
      <button type="button" data-unit="tok" aria-pressed="true">tok/s</button>
      <button type="button" data-unit="tflops" aria-pressed="false">TFLOP/s</button>
    </span>
  </label>
</div>

<section id="overview">
  <h2>Overview &mdash; latest vs. previous commit</h2>
  <div id="matrix-out"></div>
</section>

<section id="detail">
  <div id="charts-out"></div>
</section>
</div>

<script>
const DATA = __DATA__;
const GROUP_ORDER = __GROUP_ORDER__;
const COMMIT = "__COMMIT_URL__";

// -- theme: OS default, overridable, remembered per viewer only --
const root = document.documentElement;
const themeBtn = document.getElementById("theme-toggle");
function applyTheme(t) {
  if (t) { root.setAttribute("data-theme", t); } else { root.removeAttribute("data-theme"); }
  themeBtn.textContent = t === "dark" ? "dark" : t === "light" ? "light" : "auto";
}
try { applyTheme(localStorage.getItem("pie-evals-theme") || ""); } catch (e) { applyTheme(""); }
themeBtn.onclick = () => {
  const cur = root.getAttribute("data-theme") || "";
  const next = cur === "" ? "dark" : cur === "dark" ? "light" : "";
  applyTheme(next);
  try { localStorage.setItem("pie-evals-theme", next); } catch (e) {}
};

const fmt = (v, unit) => v == null ? "n/a" : unit === "tflops" ? v.toFixed(2) : Math.round(v).toLocaleString();
const seriesColor = () => getComputedStyle(root).getPropertyValue("--series-1").trim();

let unit = "tok";
const unitButtons = document.querySelectorAll("#unit button");
unitButtons.forEach(b => b.onclick = () => {
  unit = b.dataset.unit;
  unitButtons.forEach(x => x.setAttribute("aria-pressed", String(x === b)));
  draw();
});

const platformSel = document.getElementById("platform");
const artifactSel = document.getElementById("artifact");
const sel = (el, values) => { el.innerHTML = ["(all)", ...values].map(v => `<option>${v}</option>`).join(""); el.onchange = draw; };
sel(platformSel, [...new Set(DATA.map(d => d.platform))].sort());
sel(artifactSel, [...new Set(DATA.map(d => d.artifact))].sort());

function pointValue(p) { return unit === "tflops" ? p.decode_tflops : p.value; }

// one representative series per (platform, artifact): the one with the most
// recorded commits, so the overview reflects the workload run most often.
function representatives() {
  const byCombo = new Map();
  for (const s of DATA) {
    const key = s.platform + "\\u0000" + s.artifact;
    const cur = byCombo.get(key);
    if (!cur || s.points.length > cur.points.length) byCombo.set(key, s);
  }
  return byCombo;
}

function accelOf(platform) {
  const s = DATA.find(d => d.platform === platform);
  return s ? s.accelerator : "";
}

function drawMatrix() {
  const platforms = [...new Set(DATA.map(d => d.platform))].sort();
  const artifacts = [...new Set(DATA.map(d => d.artifact))].sort();
  const reps = representatives();
  const out = document.getElementById("matrix-out");
  const table = document.createElement("table");
  table.className = "matrix";
  const thead = `<thead><tr><th>platform</th>${artifacts.map(a => `<th>${a}</th>`).join("")}</tr></thead>`;
  const rows = platforms.map(p => {
    const cells = artifacts.map(a => {
      const s = reps.get(p + "\\u0000" + a);
      if (!s) return `<td class="empty">&mdash;</td>`;
      const pts = s.points;
      const last = pts[pts.length - 1], prev = pts.length > 1 ? pts[pts.length - 2] : null;
      const lv = pointValue(last), pv = prev ? pointValue(prev) : null;
      if (lv == null) return `<td class="empty" data-platform="${p}" data-artifact="${a}">n/a</td>`;
      let deltaHtml = "";
      if (pv != null && pv !== 0) {
        const pct = (lv - pv) / pv * 100;
        const cls = pct > 2 ? "good" : pct < -2 ? "critical" : "flat";
        const arrow = pct > 2 ? "\\u25b2" : pct < -2 ? "\\u25bc" : "\\u2192";
        deltaHtml = `<span class="delta ${cls}">${arrow} ${pct >= 0 ? "+" : ""}${pct.toFixed(1)}%</span>`;
      }
      return `<td data-platform="${p}" data-artifact="${a}">${fmt(lv, unit)}${deltaHtml}</td>`;
    }).join("");
    return `<tr><th>${p}<span class="accel">${accelOf(p)}</span></th>${cells}</tr>`;
  }).join("");
  table.innerHTML = thead + `<tbody>${rows}</tbody>` +
    `<caption>Each cell is the platform/model pair's most-run workload. Click a cell to see every workload, mode and metric for that pair below. &#9650;/&#9660; mark a change past &plusmn;2% since the previous recorded commit.</caption>`;
  out.innerHTML = "";
  out.appendChild(table);
  table.querySelectorAll("td[data-platform]").forEach(td => td.onclick = () => {
    platformSel.value = td.dataset.platform;
    artifactSel.value = td.dataset.artifact;
    draw();
    document.getElementById("detail")?.scrollIntoView({ behavior: "smooth", block: "start" });
  });
}

const charts = [];
function drawCharts() {
  charts.splice(0).forEach(c => c.destroy());
  const p = platformSel.value, a = artifactSel.value;
  const out = document.getElementById("charts-out");
  out.innerHTML = "";
  if (p === "(all)" || a === "(all)") {
    out.innerHTML = '<p class="empty-state">Pick a platform and a model above \\u2014 or click a cell in the overview \\u2014 to see its full history: every workload, mode and metric.</p>';
    return;
  }
  const matching = DATA.filter(d => d.platform === p && d.artifact === a);
  if (matching.length === 0) { out.innerHTML = '<p class="empty-state">No runs for this platform / model yet.</p>'; return; }

  const head = document.createElement("div"); head.className = "detail-head";
  head.innerHTML = `<h2>${p} \\u00b7 ${accelOf(p)} \\u00b7 ${a}</h2>`;
  out.appendChild(head);

  const byProgram = {};
  matching.forEach(d => (byProgram[d.program] ||= []).push(d));
  const programs = Object.keys(byProgram).sort();
  for (const prog of programs) {
    const progBlock = document.createElement("div"); progBlock.className = "program-block";
    if (programs.length > 1) {
      const pt = document.createElement("div"); pt.className = "program-title"; pt.textContent = prog; progBlock.appendChild(pt);
    }
    const byGroup = {};
    byProgram[prog].forEach(d => (byGroup[d.workload_group] ||= []).push(d));
    for (const group of GROUP_ORDER.filter(g => byGroup[g])) {
      const series = byGroup[group].filter(s => s.points.some(pt => pointValue(pt) != null))
                                    .sort((x, y) => x.workload_label.localeCompare(y.workload_label) || x.mode.localeCompare(y.mode));
      if (series.length === 0) continue;
      const groupBlock = document.createElement("div"); groupBlock.className = "group-block";
      const gt = document.createElement("div"); gt.className = "group-title"; gt.textContent = group; groupBlock.appendChild(gt);
      const grid = document.createElement("div"); grid.className = "grid"; groupBlock.appendChild(grid);
      progBlock.appendChild(groupBlock);
      for (const s of series) {
        const pts = s.points.filter(pt => pointValue(pt) != null);
        const card = document.createElement("div"); card.className = "card";
        const modeTag = /^tp\\d+$/.test(s.mode) ? s.mode.toUpperCase() : s.mode;
        const unitLabel = unit === "tflops" ? "decode TFLOP/s" : s.metric;
        card.innerHTML = `<h3>${s.workload_label}</h3><div class="unit">${modeTag} \\u00b7 ${unitLabel}</div><canvas></canvas>`;
        grid.appendChild(card);
        charts.push(new Chart(card.querySelector("canvas"), {
          type: "line",
          data: { labels: pts.map(x => x.commit.slice(0, 8)), datasets: [{
            data: pts.map(x => pointValue(x)), borderColor: seriesColor(), borderWidth: 2,
            pointRadius: 4, pointBackgroundColor: seriesColor(), tension: 0,
          }] },
          options: {
            plugins: {
              legend: { display: false },
              tooltip: { callbacks: {
                title: i => `${pts[i[0].dataIndex].commit.slice(0, 10)} \\u00b7 ${pts[i[0].dataIndex].date}`,
                afterLabel: i => { const x = pts[i.dataIndex]; return [
                  x.prefill_tflops != null ? `prefill ${x.prefill_tflops.toFixed(2)} TFLOP/s` : null,
                  x.decode_tflops != null ? `decode ${x.decode_tflops.toFixed(2)} TFLOP/s` : null,
                  x.tier,
                ].filter(Boolean); } } },
            },
            scales: {
              x: { grid: { color: getComputedStyle(root).getPropertyValue("--gridline") }, ticks: { color: getComputedStyle(root).getPropertyValue("--text-muted") } },
              y: { beginAtZero: false, grid: { color: getComputedStyle(root).getPropertyValue("--gridline") }, ticks: { color: getComputedStyle(root).getPropertyValue("--text-muted") } },
            },
            onClick: (e, el) => { if (el.length) window.open(COMMIT + pts[el[0].index].commit, "_blank"); },
          },
        }));
      }
    }
    out.appendChild(progBlock);
  }
}

function draw() { drawMatrix(); drawCharts(); }
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
        label, group = _workload_label(cell["workload"])
        by_commit: dict[str, dict] = {}
        for r in rs:
            tf = flops.tflops(r, cell["workload"]["params"], config)
            by_commit[r["pie_commit"]] = {"commit": r["pie_commit"], "value": r["primary_value"], "tier": r["tier"],
                                          "date": r["started_at"].strftime("%Y-%m-%d"), **tf}
        out.append({"platform": plat, "accelerator": rs[-1]["accelerator"], "artifact": art, "workload": wl, "program": prog,
                    "mode": mode, "metric": metric.replace("_tok_s", " tok/s").replace("_", " "),
                    "workload_label": label, "workload_group": group, "points": list(by_commit.values())})
    return out


def render(store: Store, out: Path) -> int:
    from datetime import datetime, timezone

    data = series(store)
    out.mkdir(parents=True, exist_ok=True)
    html = (PAGE.replace("__DATA__", json.dumps(data))
                .replace("__GROUP_ORDER__", json.dumps(GROUP_ORDER))
                .replace("__COMMIT_URL__", PIE_COMMIT_URL)
                .replace("__GENERATED__", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")))
    (out / "index.html").write_text(html)
    return len(data)
