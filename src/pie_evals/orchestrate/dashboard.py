from __future__ import annotations

import json
import subprocess
from collections import defaultdict
from pathlib import Path

from pie_evals.schema import CellStatus, Tier

from . import flops
from .matrix import Matrix
from .store import Store

METRICS = [
    ("Prefill", "128-token prompt", "ss-128-64", "prefill_tok_s", "prefill_tflops"),
    ("Prefill", "1k-token prompt", "lc-1k-128", "prefill_tok_s", "prefill_tflops"),
    ("Prefill", "2k-token prompt", "lc-2k-128", "prefill_tok_s", "prefill_tflops"),
    ("Decode", "1 request", "ss-128-64", "decode_tok_s", "decode_tflops"),
    ("Decode", "8 requests at once", "c8", "output_tok_s", "decode_tflops"),
    ("Decode", "32 requests at once", "c32", "output_tok_s", "decode_tflops"),
]
DEFAULT_MODEL = "qwen3.5-0.8b-bf16"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pie Stats</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<style>
  * { box-sizing: border-box; }
  body { font: 15px/1.5 -apple-system, system-ui, sans-serif; margin: 0; color: #1f2328; background: #f6f8fa; }
  header { background: #fff; border-bottom: 1px solid #d8dee4; }
  .bar { max-width: 1000px; margin: 0 auto; padding: 12px 16px; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
  .brand { font-weight: 700; font-size: 17px; }
  nav { display: flex; gap: 8px; flex-wrap: wrap; }
  nav button, .pill, .signout, .signin, select, button.act {
    box-sizing: border-box; height: 32px; display: inline-flex; align-items: center; gap: 6px;
    border: 1px solid #d0d7de; border-radius: 999px; padding: 0 14px; background: #fff; color: #424a53;
    font: inherit; font-size: 14px; line-height: 1; cursor: pointer; }
  nav button:hover, .pill:hover, .signout:hover, select:hover { background: #f6f8fa; }
  nav button.on { background: #1f2328; border-color: #1f2328; color: #fff; }
  .grow { flex: 1; }
  main { max-width: 1000px; margin: 0 auto; padding: 20px 16px 48px; }
  .controls { max-width: 1000px; margin: 0 auto; padding: 16px 16px 0; display: flex; gap: 16px; flex-wrap: wrap; align-items: center; color: #424a53; font-size: 14px; }
  .controls[hidden] { display: none; }
  .controls select { margin-left: 6px; }
  .card { background: #fff; border: 1px solid #d8dee4; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
  h2 { font-size: 16px; margin: 0 0 12px; }
  .muted { color: #656d76; font-size: 13px; }
  .big { font-size: 26px; font-weight: 600; }
  .up { color: #1a7f37; } .down { color: #cf222e; }
  .row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  @media (max-width: 800px) { .tiles { grid-template-columns: 1fr 1fr; } }
  @media (max-width: 520px) { .tiles { grid-template-columns: 1fr; } }
  .tile { background: #fff; border: 1px solid #d8dee4; border-radius: 8px; padding: 10px 12px; min-width: 0; }
  .tile .name { font-weight: 600; font-size: 14px; }
  .tile .now { font-size: 13px; color: #424a53; margin: 2px 0 6px; }
  .chart { position: relative; height: 120px; }
  .phase { font-size: 13px; font-weight: 600; color: #656d76; text-transform: uppercase; letter-spacing: .04em; margin: 0 0 8px; }
  .tiles + .phase { margin-top: 20px; }
  @media (max-width: 700px) { .row { grid-template-columns: 1fr; } }
  table { border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }
  th, td { text-align: left; padding: 8px 10px; border-bottom: 1px solid #eaeef2; vertical-align: top; }
  th { font-size: 13px; color: #424a53; font-weight: 600; }
  td.num, th.num { text-align: right; }
  table.compact { table-layout: fixed; font-size: 13px; }
  table.compact th, table.compact td { padding: 3px 8px; line-height: 1.4; }
  td.clip { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px; }
  .idle { background: #1a7f37; } .busy { background: #bf8700; } .offline { background: #cf222e; }
  .tag { display: inline-block; background: #eaeef2; border-radius: 10px; padding: 0 8px; margin: 0 4px 4px 0; font-size: 13px; }
  .avatar { width: 22px; height: 22px; border-radius: 50%; vertical-align: middle; margin-right: 6px; }
  select { appearance: none; -webkit-appearance: none; padding-right: 30px;
    background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23656d76'/%3E%3C/svg%3E") no-repeat right 12px center; }
  input { font: inherit; font-size: 14px; height: 32px; box-sizing: border-box; padding: 0 14px; border: 1px solid #d0d7de; border-radius: 999px; }
  input[type=checkbox] { height: auto; }
  button.act { background: #1f2328; border-color: #1f2328; color: #fff; font-weight: 600; }
  button.act:hover { background: #32383f; }
  label.check { display: block; padding: 4px 0; }
  code { background: #eaeef2; border-radius: 4px; padding: 1px 5px; font-size: 13px; }
  a { color: #0969da; text-decoration: none; }
  .signin { background: #1f2328; border-color: #1f2328; color: #fff; font-weight: 600; }
  .signin:hover { background: #32383f; }
  .signin svg { fill: currentColor; }
  #who { display: flex; align-items: center; gap: 8px; }
  .pill { padding: 0 12px 0 4px; color: #1f2328; }
  .pill .avatar { margin: 0; }
  .signout:hover, .pill:hover { background: #f6f8fa; }
  .modal { position: fixed; inset: 0; background: rgba(31, 35, 40, .45); display: flex; align-items: flex-start; justify-content: center; padding: 8vh 16px; z-index: 10; }
  .modal[hidden] { display: none; }
  .sheet { position: relative; background: #fff; border-radius: 10px; width: min(640px, 100%); max-height: 84vh; overflow: auto; box-shadow: 0 8px 24px rgba(0,0,0,.2); }
  .sheet .card { border: 0; margin: 0; }
  .subtabs { display: flex; gap: 8px; margin: -4px 32px 16px 0; }
  .picklist { max-height: 220px; overflow: auto; border: 1px solid #eaeef2; border-radius: 6px; padding: 4px 8px; margin-bottom: 12px; }
  label.clip { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .tag.new { background: #fff8c5; }
  pre.cmd { background: #f6f8fa; border: 1px solid #d8dee4; border-radius: 6px; padding: 10px; white-space: pre-wrap; word-break: break-all; font-size: 12px; }
  .x { position: absolute; top: 8px; right: 10px; border: 0; background: none; font-size: 22px; line-height: 1; cursor: pointer; color: #656d76; }
</style>
</head>
<body>
<header><div class="bar">
  <span class="brand">Pie Stats</span>
  <nav id="tabs"></nav>
  <span class="grow"></span>
  <span id="who"></span>
</div></header>
<div class="controls" id="controls">
  <label>model <select id="model"></select></label>
  <label>show <select id="unit"><option value="v">tok/s</option><option value="tflops">TFLOP/s</option></select></label>
</div>
<main id="main"></main>
<div id="modal" class="modal" hidden><div class="sheet"><button class="x" id="close" aria-label="close">×</button><div id="sheet"></div></div></div>
<script>
const DATA = __DATA__;
const TABS = ["Overview", "Pushes", "Macs", "People"];
const COLORS = ["#0969da", "#bf8700", "#8250df"];
const modelName = id => (DATA.models.find(m => m.id === id) || { name: id }).name;
const macName = id => (DATA.pool.find(m => m.id === id) || { name: id }).name;
let tab = "Overview", charts = [], me = null;
const token = () => { try { return localStorage.getItem("pie-evals-token"); } catch { return null; } };

const modelSel = document.getElementById("model");
modelSel.innerHTML = DATA.models.filter(m => m.has_results).map(m => `<option value="${m.id}">${m.name}</option>`).join("");
modelSel.value = DATA.default_model; modelSel.onchange = draw;
const unitSel = document.getElementById("unit"); unitSel.onchange = draw;
const unitName = () => unitSel.value === "v" ? "tok/s" : "TFLOP/s";

function series(mac, metric) {
  const byCommit = (DATA.results[mac]?.models[modelSel.value] || {})[metric] || {};
  return DATA.commits.filter(c => byCommit[c.sha]).map(c => ({ sha: c.sha, ...byCommit[c.sha] }));
}
const macs = () => Object.keys(DATA.results).filter(m => DATA.results[m].models[modelSel.value]);

function overview() {
  const list = macs(), key = unitSel.value;
  if (!list.length) { document.getElementById("main").innerHTML = `<div class="card muted">No results for this model yet.</div>`; return; }
  const fmt = v => key === "v" ? Math.round(v).toLocaleString() : v.toFixed(2);
  let html = "";
  for (const phase of ["Prefill", "Decode"]) {
    html += `<div class="phase">${phase}</div><div class="tiles">`;
    DATA.metrics.forEach((m, i) => {
      if (m.phase !== phase) return;
      const now = list.map((mac, k) => {
        const s = series(mac, i).filter(p => p[key] != null), last = s[s.length - 1];
        return last ? `<span style="color:${COLORS[k % COLORS.length]}">${fmt(last[key])}</span>` : "";
      }).filter(Boolean).join(" · ");
      html += `<div class="tile"><div class="name">${m.name}</div><div class="now">${now || "–"} ${now ? unitName() : ""}</div>` +
              `<div class="chart"><canvas data-metric="${i}"></canvas></div></div>`;
    });
    html += `</div>`;
  }
  document.getElementById("main").innerHTML = html;
  document.querySelectorAll("canvas").forEach(cv => {
    const i = +cv.dataset.metric;
    const labels = DATA.commits.map(c => c.sha).filter(sha => list.some(mac => series(mac, i).some(p => p.sha === sha && p[key] != null)));
    charts.push(new Chart(cv, { type: "line",
      data: { labels: labels.map(s => s.slice(0, 7)), datasets: list.map((mac, k) => {
        const by = Object.fromEntries(series(mac, i).map(p => [p.sha, p[key]]));
        return { label: DATA.results[mac].name, data: labels.map(l => by[l] ?? null), borderColor: COLORS[k % COLORS.length],
                 backgroundColor: COLORS[k % COLORS.length], pointRadius: 2, borderWidth: 2, spanGaps: true };
      }) },
      options: { responsive: true, maintainAspectRatio: false,
                 plugins: { legend: { display: list.length > 1, position: "bottom", labels: { boxWidth: 8, font: { size: 11 } } } },
                 scales: { x: { ticks: { font: { size: 10 }, maxRotation: 0, autoSkip: true } }, y: { ticks: { font: { size: 10 } } } },
                 onClick: (e, el) => { if (el.length) window.open(`https://github.com/${DATA.pie_repo}/commit/` + labels[el[0].index]); } } }));
  });
}

function pushes() {
  let html = `<div class="card"><h2>Recent pushes</h2><table class="compact"><colgroup><col><col style="width:140px"><col style="width:96px"></colgroup>` +
             `<tr><th>commit</th><th>author</th><th>date</th></tr>`;
  [...DATA.commits].reverse().forEach(c => {
    html += `<tr><td class="clip" title="${c.message.replace(/"/g, "&quot;")}"><a href="https://github.com/${DATA.pie_repo}/commit/${c.sha}" target="_blank">${c.sha.slice(0, 7)}</a> ${c.message}</td>` +
            `<td class="clip">${c.author}</td><td>${c.date}</td></tr>`;
  });
  document.getElementById("main").innerHTML = html + `</table></div>`;
}

function pool() {
  let html = `<div class="card"><h2>Connected Macs</h2><table><tr><th>Mac</th><th>memory</th><th>status</th><th>last run</th></tr>`;
  for (const m of DATA.pool) html += `<tr><td>${m.name} <span class="muted">${m.id}</span></td><td>${m.memory_gib ? m.memory_gib + " GB" : ""}</td><td><span class="dot ${m.status}"></span>${m.status}</td><td>${m.last}</td></tr>`;
  if (!DATA.pool.length) html += `<tr><td colspan="4" class="muted">No Mac is connected.</td></tr>`;
  document.getElementById("main").innerHTML = html + `</table></div>`;
}

function people() {
  let html = `<div class="card"><h2>People</h2><table><tr><th>who</th><th>models</th><th>Macs</th></tr>`;
  for (const p of DATA.people) {
    html += `<tr><td><img class="avatar" src="https://github.com/${p.login}.png?size=44">${p.login}</td>` +
      `<td>${p.models.map(m => `<span class="tag">${modelName(m)}</span>`).join("") || `<span class="muted">default</span>`}</td>` +
      `<td>${p.macs.map(m => `<span class="tag">${macName(m)}</span>`).join("") || `<span class="muted">every connected Mac</span>`}</td></tr>`;
  }
  if (!DATA.people.length) html += `<tr><td colspan="3" class="muted">Nobody has a setup yet: everyone gets ${modelName(DATA.default_model)} on every connected Mac.</td></tr>`;
  document.getElementById("main").innerHTML = html + `</table></div>`;
}

async function gh(path, opts = {}) {
  const r = await fetch(`https://api.github.com/${path}`, { ...opts, headers: { Authorization: `Bearer ${token()}`, Accept: "application/vnd.github+json", ...(opts.headers || {}) } });
  if (!r.ok && r.status !== 404) throw new Error(`${r.status} ${await r.text()}`);
  return r.status === 404 ? null : r.json();
}
function openSheet() { document.getElementById("modal").hidden = false; setup(); }
function closeSheet() { document.getElementById("modal").hidden = true; }
document.getElementById("close").onclick = closeSheet;
document.getElementById("modal").onclick = e => { if (e.target.id === "modal") closeSheet(); };
document.addEventListener("keydown", e => { if (e.key === "Escape") closeSheet(); });
let section = "My commits";
const pickList = (name, items, checked) => items.map(x => `<label class="check"><input type="checkbox" name="${name}" value="${x.id}" ${checked.includes(x.id) ? "checked" : ""}> ${x.name}${x.hint ? ` <span class="muted">${x.hint}</span>` : ""}</label>`).join("");
const picked = name => [...document.querySelectorAll(`#sheet input[name=${name}]:checked`)].map(x => x.value);
const macItems = () => DATA.pool.map(m => ({ id: m.id, name: m.name, hint: m.id }));
function macChoice(cur) {
  return `<label class="check"><input type="checkbox" name="all" ${cur.length ? "" : "checked"}> every connected Mac</label>${pickList("mac", macItems(), cur)}`;
}
async function setup() {
  const main = document.getElementById("sheet");
  if (!me) {
    main.innerHTML = `<div class="card"><h2>Sign in with GitHub</h2><p class="muted">Paste a fine-grained GitHub token for <b>${DATA.repo}</b> with <b>Contents</b> and <b>Actions</b> read & write. It stays in this browser.</p>` +
      `<input id="tok" type="password" placeholder="github_pat_…" size="40"> <button class="act" id="go">Sign in</button> <span id="err" class="down"></span></div>`;
    document.getElementById("go").onclick = async () => {
      try { localStorage.setItem("pie-evals-token", document.getElementById("tok").value.trim()); } catch {}
      await signIn(); if (me) setup(); else document.getElementById("err").textContent = "That token did not work.";
    };
    return;
  }
  const sections = ["My commits", "Run now", "Add a Mac"];
  main.innerHTML = `<div class="card"><nav class="subtabs">${sections.map(x => `<button class="${x === section ? "on" : ""}">${x}</button>`).join("")}</nav><div id="body"></div></div>`;
  main.querySelectorAll(".subtabs button").forEach(b => b.onclick = () => { section = b.textContent; setup(); });
  const body = document.getElementById("body");
  if (section === "My commits") return myCommits(body);
  if (section === "Run now") return runNow(body);
  return addMac(body);
}
async function myCommits(body) {
  const file = await gh(`repos/${DATA.repo}/contents/users/${me.login}.json`);
  const cur = file ? JSON.parse(atob(file.content)) : { models: [DATA.default_model], macs: [], enabled: true };
  body.innerHTML = `<p class="muted">What runs when a commit by <b>${me.login}</b> lands on pie main.</p>` +
    `<label class="check"><input type="checkbox" name="enabled" ${cur.enabled === false ? "" : "checked"}> benchmark my commits</label>` +
    `<div class="row"><div><h2>Models</h2>${pickList("model", DATA.models, cur.models || [])}</div><div><h2>Macs</h2>${macChoice(cur.macs || [])}</div></div>` +
    `<button class="act" id="save">Save</button> <span id="msg" class="muted"></span>`;
  document.getElementById("save").onclick = async () => {
    const data = { models: picked("model"), macs: picked("all").length ? [] : picked("mac"), enabled: picked("enabled").length > 0 };
    const msg = document.getElementById("msg"); msg.textContent = "Saving…";
    try {
      const now = await gh(`repos/${DATA.repo}/contents/users/${me.login}.json`);
      await gh(`repos/${DATA.repo}/contents/users/${me.login}.json`, { method: "PUT", body: JSON.stringify({
        message: `users: ${me.login} ${data.enabled ? "runs " + (data.models.join(", ") || "the default") : "skips benchmarks"}`,
        content: btoa(JSON.stringify(data, null, 2) + "\\n"), ...(now ? { sha: now.sha } : {}) }) });
      msg.textContent = data.enabled ? "Saved. Your next push to main runs this." : "Saved. Your pushes are not benchmarked.";
    } catch (e) { msg.textContent = "Could not save: " + e.message; }
  };
}
async function runNow(body) {
  body.innerHTML = `<p class="muted">Loading recent pie commits…</p>`;
  let recent = [];
  try { recent = await gh(`repos/${DATA.pie_repo}/commits?sha=main&per_page=30`) || []; } catch (e) { body.innerHTML = `<p class="down">${e.message}</p>`; return; }
  const measured = new Set(DATA.commits.map(c => c.sha));
  body.innerHTML = `<p class="muted">Benchmark chosen pie commits now: catch up on ones that were skipped, or add models and Macs to ones already measured.</p>` +
    `<h2>Commits</h2><div class="picklist">${recent.map(c => `<label class="check clip"><input type="checkbox" name="commit" value="${c.sha}"> ` +
      `<code>${c.sha.slice(0, 7)}</code> ${c.commit.message.split("\\n")[0]} ${measured.has(c.sha) ? `<span class="tag">measured</span>` : `<span class="tag new">not measured</span>`}</label>`).join("")}</div>` +
    `<div class="row"><div><h2>Models</h2>${pickList("model", DATA.models, [DATA.default_model])}</div><div><h2>Macs</h2>${macChoice([])}</div></div>` +
    `<button class="act" id="run">Run</button> <span id="msg" class="muted"></span>`;
  document.getElementById("run").onclick = async () => {
    const commits = picked("commit"), models = picked("model"), macs = picked("all").length ? [] : picked("mac");
    const msg = document.getElementById("msg");
    if (!commits.length || !models.length) { msg.textContent = "Pick at least one commit and one model."; return; }
    msg.textContent = "Starting…";
    try {
      for (const sha of commits) {
        await gh(`repos/${DATA.repo}/actions/workflows/pie-eval.yml/dispatches`, { method: "POST",
          body: JSON.stringify({ ref: "main", inputs: { pie_commit: sha, models: models.join(","), macs: macs.join(",") } }) });
      }
      msg.innerHTML = `Started ${commits.length} run${commits.length > 1 ? "s" : ""}. <a href="https://github.com/${DATA.repo}/actions/workflows/pie-eval.yml" target="_blank">Follow them</a>`;
    } catch (e) { msg.textContent = "Could not start: " + e.message; }
  };
}
function addMac(body) {
  const cmd = `PLATFORM_ID=<id> ./infra/mac/setup-runner.sh "$(gh api -X POST repos/${DATA.repo}/actions/runners/registration-token -q .token)"`;
  body.innerHTML = `<p class="muted">Connect a Mac so it can take benchmark runs. On that Mac, in a checkout of <b>${DATA.repo}</b>, run:</p>` +
    `<pre class="cmd">${cmd.replace(/</g, "&lt;")}</pre><button class="act" id="copy">Copy</button> <span id="msg" class="muted"></span>` +
    `<p class="muted"><code>&lt;id&gt;</code> is the Mac's entry in <code>matrix/platforms.yaml</code>, for example <code>m5-max-48g</code>. ` +
    `Creating the registration token needs admin on ${DATA.repo}; without it, ask an admin for a token. The Mac shows up under Macs once it is connected.</p>`;
  document.getElementById("copy").onclick = async () => {
    try { await navigator.clipboard.writeText(cmd); document.getElementById("msg").textContent = "Copied."; } catch { document.getElementById("msg").textContent = "Select and copy the command."; }
  };
}
async function signIn() {
  me = null;
  if (token()) { try { me = await gh("user"); } catch { me = null; } }
  renderWho();
}
function renderWho() {
  document.getElementById("who").innerHTML = me
    ? `<a href="#" id="me" class="pill"><img class="avatar" src="${me.avatar_url}">${me.login}</a><a href="#" id="out" class="signout">Sign out</a>`
    : `<a href="#" id="in" class="signin"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>Sign in with GitHub</a>`;
  const o = document.getElementById("out"), i = document.getElementById("in"), m = document.getElementById("me");
  if (o) o.onclick = e => { e.preventDefault(); try { localStorage.removeItem("pie-evals-token"); } catch {} me = null; renderWho(); closeSheet(); };
  if (i) i.onclick = e => { e.preventDefault(); openSheet(); };
  if (m) m.onclick = e => { e.preventDefault(); openSheet(); };
}

function draw() {
  charts.forEach(c => c.destroy()); charts = [];
  document.getElementById("tabs").innerHTML = TABS.map(t => `<button class="${t === tab ? "on" : ""}">${t}</button>`).join("");
  document.querySelectorAll("#tabs button").forEach(b => b.onclick = () => { tab = b.textContent; draw(); });
  document.getElementById("controls").hidden = tab !== "Overview";
  ({ "Overview": overview, "Pushes": pushes, "Macs": pool, "People": people })[tab]();
}
signIn().then(draw);
</script>
</body>
</html>
"""


def _gh(path: str) -> dict | list | None:
    try:
        out = subprocess.run(["gh", "api", path], capture_output=True, text=True, check=True).stdout
        return json.loads(out)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def runners(repo: str) -> list[dict] | None:
    got = _gh(f"repos/{repo}/actions/runners?per_page=100")
    return got.get("runners", []) if isinstance(got, dict) else None


def _pool(live: list[dict] | None, matrix: Matrix, last: dict[str, str]) -> list[dict]:
    pool = []
    for r in live or []:
        labels = [lab["name"] for lab in r.get("labels", [])]
        if "macOS" not in labels and "macos" not in labels:
            continue
        pid = next((lab for lab in labels if lab in matrix.platforms), None)
        spec = matrix.platforms.get(pid) if pid else None
        pool.append({
            "name": spec.accelerator if spec else r["name"],
            "id": pid or "",
            "memory_gib": int(spec.memory_gib) if spec else None,
            "status": "busy" if r["status"] == "online" and r.get("busy") else "idle" if r["status"] == "online" else "offline",
            "last": last.get(pid, ""),
        })
    return sorted(pool, key=lambda m: m["name"])


def mac_models(matrix: Matrix) -> list[dict]:
    seen: dict[str, dict] = {}
    for c in matrix.expand():
        if (c.platform.os == "macos" and c.engine.value == "pie" and c.program.id == "text-completion-bench"
                and c.mode.tp == 1 and c.declared_unsupported_reason is None and c.artifact.kind.value == "full"):
            seen[c.artifact.id] = {"id": c.artifact.id, "name": f"{c.artifact.base_model} · {c.artifact.scheme}"}
    return sorted(seen.values(), key=lambda m: m["name"])


def people(users_dir: Path) -> list[dict]:
    out = []
    for f in sorted(users_dir.glob("*.json")) if users_dir.is_dir() else []:
        try:
            d = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        out.append({"login": f.stem, "models": list(d.get("models") or []), "macs": list(d.get("macs") or [])})
    return out


def build(store: Store, matrix: Matrix, live: list[dict] | None, *, repo: str, pie_repo: str,
          users_dir: Path = Path("users"), lookup_commits: bool = True) -> dict:
    t = store.table(Tier.TARGETED)
    rows = [r for r in t.to_pylist() if r["status"] == str(CellStatus.PASS) and r["pie_commit"]] if t.num_rows else []
    rows.sort(key=lambda r: r["started_at"])

    results: dict[str, dict] = {}
    order: list[str] = []
    last: dict[str, str] = {}
    have: set[str] = set()
    for r in rows:
        if r["pie_commit"] not in order:
            order.append(r["pie_commit"])
        last[r["platform"]] = f"{r['started_at']:%Y-%m-%d} · {r['pie_commit'][:7]}"
        mac = results.setdefault(r["platform"], {"name": r["accelerator"], "models": defaultdict(lambda: defaultdict(dict))})
        cell = json.loads(r["record_json"])["cell"]
        tf = None
        for i, (_, _, wl, field, tf_field) in enumerate(METRICS):
            if wl == r["workload"] and r.get(field) is not None:
                if tf is None:
                    tf = flops.tflops(r, cell["workload"]["params"], flops.model_config(cell["artifact"]["base_model"]))
                mac["models"][r["artifact"]][i][r["pie_commit"]] = {"v": r[field], "tflops": tf[tf_field]}
                have.add(r["artifact"])

    commits = []
    for sha in order:
        info = _gh(f"repos/{pie_repo}/commits/{sha}") if lookup_commits else None
        commit = (info or {}).get("commit", {})
        commits.append({
            "sha": sha,
            "message": (commit.get("message") or "").splitlines()[0][:90] if commit else "",
            "author": ((info or {}).get("author") or {}).get("login") or (commit.get("author") or {}).get("name", ""),
            "date": (commit.get("committer") or {}).get("date", ""),
        })
    commits.sort(key=lambda c: c["date"] or "~")
    for c in commits:
        c["date"] = c["date"][:10]

    models = mac_models(matrix)
    for m in models:
        m["has_results"] = m["id"] in have
    return {
        "repo": repo, "pie_repo": pie_repo, "default_model": DEFAULT_MODEL,
        "metrics": [{"phase": p, "name": n} for p, n, *_ in METRICS],
        "commits": commits, "results": results, "models": models,
        "pool": _pool(live, matrix, last), "people": people(users_dir),
    }


def render(store: Store, matrix: Matrix, out: Path, live: list[dict] | None = None, *, repo: str = "pie-project/pie-evals",
           pie_repo: str = "pie-project/pie", users_dir: Path = Path("users"), lookup_commits: bool = True) -> int:
    data = build(store, matrix, live, repo=repo, pie_repo=pie_repo, users_dir=users_dir, lookup_commits=lookup_commits)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(PAGE.replace("__DATA__", json.dumps(data)))
    return len(data["commits"])
