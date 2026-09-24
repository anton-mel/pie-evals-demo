from __future__ import annotations

import json
import subprocess
from collections import defaultdict
from datetime import datetime, timedelta, timezone
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
<title>benchmarks</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2067.89%2067.89'%3E%3Cpath%20d='M52.96,11.53l-43.52,6.4c-3.85.57-5.64,5.08-3.22,8.13l27.3,34.49c2.41,3.05,7.22,2.34,8.65-1.27l16.21-40.89c1.43-3.61-1.58-7.42-5.43-6.86Z'%20fill='none'%20stroke='%23000'%20stroke-miterlimit='10'%20stroke-width='8'/%3E%3C/svg%3E">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<style>
  * { box-sizing: border-box; }
  body { font: 15px/1.5 -apple-system, system-ui, sans-serif; margin: 0; color: #1f2328; background: #f6f8fa; }
  header { background: #fff; border-bottom: 1px solid #d8dee4; }
  .bar { max-width: 1000px; margin: 0 auto; padding: 12px 16px; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
  .brand { font-weight: 700; font-size: 17px; display: inline-flex; align-items: center; gap: 3px; }
  .logo { width: 22px; height: 22px; }
  nav { display: flex; gap: 8px; flex-wrap: wrap; }
  nav button, .pill, .signin, select, button.act {
    box-sizing: border-box; height: 32px; display: inline-flex; align-items: center; gap: 6px;
    border: 1px solid #d0d7de; border-radius: 999px; padding: 0 14px; background: #fff; color: #424a53;
    font: inherit; font-size: 14px; line-height: 1; cursor: pointer; }
  nav button:hover, .pill:hover, select:hover { background: #f6f8fa; }
  nav button.on { background: #1f2328; border-color: #1f2328; color: #fff; }
  .grow { flex: 1; }
  main { max-width: 1000px; margin: 0 auto; padding: 20px 16px 48px; }
  .controls { max-width: 1000px; margin: 0 auto; padding: 16px 16px 0; display: flex; gap: 16px; flex-wrap: wrap; align-items: center; color: #424a53; font-size: 14px; }
  .controls[hidden] { display: none; }
  .controls select { margin-left: 6px; }
  .card { background: #fff; border: 1px solid #d8dee4; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
  h2 { font-size: 16px; margin: 0 0 12px; }
  .muted { color: #656d76; font-size: 13px; }
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
  table.compact { font-size: 13px; }
  table.fixed { table-layout: fixed; }
  table.compact .avatar { width: 18px; height: 18px; }
  table.compact .tag { margin: 0 4px 0 0; }
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
  .modal { position: fixed; inset: 0; background: rgba(31, 35, 40, .45); display: flex; align-items: flex-start; justify-content: center; padding: 8vh 16px; z-index: 10; }
  .modal[hidden] { display: none; }
  .sheet { position: relative; background: #fff; border-radius: 10px; width: min(640px, 100%); max-height: 84vh; overflow: auto; box-shadow: 0 8px 24px rgba(0,0,0,.2); }
  .sheet .card { border: 0; margin: 0; }
  .tag.new { background: #fff8c5; }
  pre.cmd { background: #f6f8fa; border: 1px solid #d8dee4; border-radius: 6px; padding: 10px; white-space: pre-wrap; word-break: break-all; font-size: 12px; }
  .x { position: absolute; top: 8px; right: 10px; border: 0; background: none; font-size: 22px; line-height: 1; cursor: pointer; color: #656d76; }
  tr.push { cursor: pointer; } tr.push:hover { background: #f6f8fa; }
  .toolbar { display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin: 0 0 12px; }
  .auto { font-size: 14px; color: #424a53; display: inline-flex; align-items: center; gap: 6px; flex-wrap: wrap; }
  .auto .tag, .pill.small, .filter select { box-sizing: border-box; height: 28px; display: inline-flex; align-items: center; margin: 0;
    font-size: 13px; line-height: 1; border: 1px solid #d0d7de; border-radius: 999px; background-color: #fff; color: #1f2328; }
  .auto .tag { padding: 0 12px; }
  .auto .tag.off { background: #fff8c5; border-color: #eac54f; }
  .on-word { color: #656d76; }
  h2.group { font-size: 15px; font-weight: 600; color: #1f2328; margin: 0 0 8px 2px; }
  h2.group .muted { font-weight: 400; margin-left: 4px; }
  .card + h2.group { margin-top: 24px; }
  .kicker { font-size: 12px; font-weight: 700; letter-spacing: .04em; color: #656d76; margin-right: 4px; }
  .pill.small { padding: 0 12px; gap: 6px; margin-left: 4px; }
  .filter select { padding: 0 30px 0 12px; }
  .filter { font-size: 14px; color: #424a53; display: inline-flex; align-items: center; gap: 6px; }
  .pager { display: flex; justify-content: center; align-items: center; gap: 6px; padding: 14px 0 0; flex-wrap: wrap; }
  .pager .pill { padding: 0 12px; min-width: 32px; justify-content: center; }
  .pager .pill.on { background: #1f2328; border-color: #1f2328; color: #fff; }
  .pager .pill:disabled { opacity: .4; cursor: default; }
  .pager .gap { color: #656d76; padding: 0 2px; }
  tr.person { cursor: pointer; } tr.person:hover { background: #f6f8fa; }
  button.link { border: 0; background: none; color: #0969da; font: inherit; cursor: pointer; padding: 0 0 0 6px; }
  #who { position: relative; }
  .menu { position: absolute; right: 0; top: 40px; background: #fff; border: 1px solid #d0d7de; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,.12); padding: 6px; z-index: 20; min-width: 160px; display: flex; flex-direction: column; }
  .menu button { border: 0; background: none; font: inherit; font-size: 14px; text-align: left; padding: 8px 12px; border-radius: 8px; cursor: pointer; color: #1f2328; }
  .menu button:hover { background: #f6f8fa; }
  .gridwrap { overflow-x: auto; margin: 12px 0; }
  table.grid td, table.grid th { padding: 5px 8px; font-size: 13px; }
  table.grid .c { text-align: center; }
  .ok { color: #1a7f37; font-weight: 700; }
  .label { font-size: 13px; font-weight: 600; color: #424a53; margin: 8px 0 4px; }
</style>
</head>
<body>
<header><div class="bar">
  <span class="brand"><svg class="logo" viewBox="0 0 67.89 67.89" aria-hidden="true"><path d="M52.96,11.53l-43.52,6.4c-3.85.57-5.64,5.08-3.22,8.13l27.3,34.49c2.41,3.05,7.22,2.34,8.65-1.27l16.21-40.89c1.43-3.61-1.58-7.42-5.43-6.86Z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="8"/></svg>pie</span>
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
const TABS = ["Overview", "Pushes", "Machines", "People"];
const COLORS = ["#0969da", "#bf8700", "#8250df", "#1a7f37", "#cf222e"];
const NL = String.fromCharCode(10);
const esc = x => String(x ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
const modelName = id => (DATA.models.find(m => m.id === id) || { name: id }).name;
const RUNNABLE = [...new Map(DATA.pool.filter(m => m.os === "macos").map(m => [m.id, m])).values()];
const macName = id => (DATA.pool.find(m => m.id === id) || DATA.results[id] || { name: id }).name;
let tab = "Overview", charts = [], me = null, mine = null, author = "", page = 0;
const PER_PAGE = 20;
const token = () => { try { return localStorage.getItem("pie-evals-token"); } catch { return null; } };

const modelSel = document.getElementById("model");
modelSel.innerHTML = DATA.models.filter(m => m.has_results).map(m => `<option value="${m.id}">${esc(m.name)}</option>`).join("");
modelSel.value = DATA.default_model; modelSel.onchange = draw;
const unitSel = document.getElementById("unit"); unitSel.onchange = draw;
const unitName = () => unitSel.value === "v" ? "tok/s" : "TFLOP/s";

function series(mac, metric) {
  const byCommit = (DATA.results[mac]?.models[modelSel.value] || {})[metric] || {};
  return DATA.commits.filter(c => byCommit[c.sha]).map(c => ({ sha: c.sha, ...byCommit[c.sha] }));
}
const macs = () => Object.keys(DATA.results).filter(m => DATA.results[m].models[modelSel.value]);
function ran(sha) {
  const out = new Set();
  for (const [mac, r] of Object.entries(DATA.results))
    for (const [model, metrics] of Object.entries(r.models))
      if (Object.values(metrics).some(byCommit => byCommit[sha])) out.add(`${mac}|${model}`);
  return out;
}

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
                 onClick: (e, el) => { if (el.length) openCommit(labels[el[0].index]); } } }));
  });
}

function summary() {
  const tag = x => `<span class="tag">${esc(x)}</span>`;
  if (!mine || mine.enabled !== true) return `<span class="tag off">nothing, switched off</span>`;
  const models = (mine?.models || []).length ? mine.models.map(modelName) : [modelName(DATA.default_model)];
  const where = (mine?.macs || []).length ? mine.macs.map(macName) : ["every connected machine"];
  return `${models.map(tag).join("")}<span class="on-word">on</span>${where.map(tag).join("")}`;
}
const when = d => d ? new Date(d) : null;
const fmtDate = d => { const t = when(d); return t && !isNaN(t) ? `${t.getFullYear()}-${String(t.getMonth() + 1).padStart(2, "0")}-${String(t.getDate()).padStart(2, "0")}` : ""; };
const fmtTime = d => { const t = when(d); return t && !isNaN(t) && d.length > 10 ? `${String(t.getHours()).padStart(2, "0")}:${String(t.getMinutes()).padStart(2, "0")}` : ""; };
const ALL = [...DATA.commits, ...DATA.history].sort((a, b) => (b.date || "").localeCompare(a.date || ""));
const allCommits = () => ALL;
function pushes() {
  const head = me
    ? `<div class="auto"><span class="kicker">CI/CD</span><span>Your pushes run</span>${summary()}<button class="pill small" id="edit">` +
      `<svg width="12" height="12" viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Z"/></svg>Change</button></div>`
    : `<div class="auto muted"><a href="#" id="sig">Sign in</a> to choose what runs on your pushes and to add runs to any commit.</div>`;
  const commits = allCommits(), authors = [...new Set(commits.map(c => c.author).filter(Boolean))].sort((a, b) => a.localeCompare(b));
  if (author && !authors.includes(author)) authors.push(author);
  const filter = `<label class="filter">author <select id="author"><option value="">everyone</option>` +
    authors.map(a => `<option value="${esc(a)}" ${a === author ? "selected" : ""}>${esc(a)}</option>`).join("") + `</select></label>`;
  let html = `<div class="toolbar">${head}${filter}</div><div class="card"><table class="compact fixed"><colgroup><col><col style="width:140px"><col style="width:96px"><col style="width:60px"><col style="width:120px"></colgroup>` +
             `<tr><th>commit</th><th>author</th><th>date</th><th>time</th><th>benchmarks</th></tr>`;
  const matching = commits.filter(c => !author || c.author === author);
  const pages = Math.max(1, Math.ceil(matching.length / PER_PAGE));
  page = Math.min(page, pages - 1);
  const shown = matching.slice(page * PER_PAGE, (page + 1) * PER_PAGE);
  if (!shown.length) html += `<tr><td colspan="5" class="muted">No pushes by ${esc(author)} yet.</td></tr>`;
  for (const c of shown) {
    const n = ran(c.sha).size;
    html += `<tr class="push" data-sha="${c.sha}"><td class="clip" title="${esc(c.message)}"><code>${c.sha.slice(0, 7)}</code> ${esc(c.message)}</td>` +
            `<td class="clip">${esc(c.author)}</td><td>${fmtDate(c.date)}</td><td class="muted">${fmtTime(c.date)}</td>` +
            `<td>${n ? `<span class="tag">${n} run${n > 1 ? "s" : ""}</span>` : `<span class="tag new">N/A</span>`}</td></tr>`;
  }
  document.getElementById("main").innerHTML = html + `</table>${pager(pages)}</div>`;
  document.querySelectorAll("tr.push").forEach(tr => tr.onclick = () => openCommit(tr.dataset.sha));
  document.getElementById("author").onchange = e => { author = e.target.value; page = 0; draw(); };
  document.querySelectorAll(".pager button[data-page]").forEach(b => b.onclick = () => { page = +b.dataset.page; draw(); window.scrollTo(0, 0); });
  const e = document.getElementById("edit"), s = document.getElementById("sig");
  if (e) e.onclick = editMine;
  if (s) s.onclick = ev => { ev.preventDefault(); openSignIn(); };
}
function pager(pages) {
  if (pages < 2) return "";
  const want = [...new Set([0, pages - 1, page - 1, page, page + 1].filter(i => i >= 0 && i < pages))].sort((a, b) => a - b);
  let out = "", prev = -1;
  for (const i of want) {
    if (i - prev > 1) out += `<span class="gap">…</span>`;
    out += `<button class="pill ${i === page ? "on" : ""}" data-page="${i}">${i + 1}</button>`;
    prev = i;
  }
  return `<div class="pager"><button class="pill" data-page="${Math.max(0, page - 1)}" ${page === 0 ? "disabled" : ""}>‹ Prev</button>${out}` +
         `<button class="pill" data-page="${Math.min(pages - 1, page + 1)}" ${page === pages - 1 ? "disabled" : ""}>Next ›</button></div>`;
}

function openCommit(sha) {
  const c = allCommits().find(x => x.sha === sha) || { sha, message: "", author: "", date: "" };
  const done = ran(sha), cols = [...new Set([...RUNNABLE.map(m => m.id), ...Object.keys(DATA.results)])];
  let grid = `<table class="grid"><tr><th>model</th>${cols.map(m => `<th class="c">${esc(macName(m))}</th>`).join("")}</tr>`;
  for (const m of DATA.models) {
    grid += `<tr><td>${esc(m.name)}</td>` + cols.map(mac => done.has(`${mac}|${m.id}`)
      ? `<td class="c"><span class="ok" title="measured">✓</span></td>`
      : me && RUNNABLE.some(p => p.id === mac) ? `<td class="c"><input type="checkbox" data-mac="${mac}" data-model="${m.id}"></td>` : `<td class="c muted">–</td>`).join("") + `</tr>`;
  }
  grid += `</table>`;
  sheet(`<h2><a href="https://github.com/${DATA.pie_repo}/commit/${sha}" target="_blank"><code>${sha.slice(0, 7)}</code></a> ${esc(c.message)}</h2>` +
    `<div class="muted">${esc(c.author)} · ${fmtDate(c.date)} ${fmtTime(c.date)} · ✓ already measured</div><div class="gridwrap">${grid}</div>` +
    (me ? `<button class="act" id="run">Run selected</button> <span id="msg" class="muted"></span>`
        : `<div class="muted"><a href="#" id="sig2">Sign in</a> to add runs to this commit.</div>`));
  const s2 = document.getElementById("sig2");
  if (s2) s2.onclick = ev => { ev.preventDefault(); openSignIn(); };
  const run = document.getElementById("run");
  if (run) run.onclick = async () => {
    const byMac = {};
    document.querySelectorAll("#sheet input[data-mac]:checked").forEach(x => (byMac[x.dataset.mac] ||= []).push(x.dataset.model));
    const msg = document.getElementById("msg");
    if (!Object.keys(byMac).length) { msg.textContent = "Tick what to add."; return; }
    msg.textContent = "Starting…";
    try {
      for (const [mac, models] of Object.entries(byMac))
        await gh(`repos/${DATA.repo}/actions/workflows/pie-eval.yml/dispatches`, { method: "POST",
          body: JSON.stringify({ ref: "main", inputs: { pie_commit: sha, models: models.join(","), macs: mac } }) });
      msg.innerHTML = `Started. <a href="https://github.com/${DATA.repo}/actions/workflows/pie-eval.yml" target="_blank">Follow</a>`;
    } catch (e) { msg.textContent = "Could not start: " + e.message; }
  };
}

async function editMine() {
  const cur = mine || { models: [DATA.default_model], macs: [], enabled: false };
  const pick = (name, items, checked) => items.map(x => `<label class="check"><input type="checkbox" name="${name}" value="${x.id}" ${checked.includes(x.id) ? "checked" : ""}> ${esc(x.name)}</label>`).join("");
  sheet(`<h2>What runs on your pushes</h2><p class="muted">Every commit you land on pie main runs this.</p>` +
    `<label class="check"><input type="checkbox" name="enabled" ${cur.enabled === true ? "checked" : ""}> benchmark my pushes</label>` +
    `<div class="row"><div><div class="label">Models</div>${pick("model", DATA.models, cur.models || [])}</div>` +
    `<div><div class="label">Machines</div><label class="check"><input type="checkbox" name="all" ${(cur.macs || []).length ? "" : "checked"}> every connected machine</label>` +
    `${pick("mac", RUNNABLE, cur.macs || [])}</div></div><button class="act" id="save">Save</button> <span id="msg" class="muted"></span>`);
  const picked = n => [...document.querySelectorAll(`#sheet input[name=${n}]:checked`)].map(x => x.value);
  document.getElementById("save").onclick = async () => {
    const data = { ...(mine || {}), models: picked("model"), macs: picked("all").length ? [] : picked("mac"), enabled: picked("enabled").length > 0 };
    const msg = document.getElementById("msg"); msg.textContent = "Saving…";
    try {
      const path = `repos/${DATA.repo}/contents/users/${me.login}.json`, now = await gh(path);
      await gh(path, { method: "PUT", body: JSON.stringify({
        message: `users: ${me.login} ${data.enabled ? "runs " + (data.models.join(", ") || "the default") : "skips benchmarks"}`,
        content: btoa(JSON.stringify(data, null, 2) + NL), ...(now ? { sha: now.sha } : {}) }) });
      mine = data; closeSheet(); draw();
    } catch (e) { msg.textContent = "Could not save: " + e.message; }
  };
}

function pool() {
  let html = "";
  for (const kind of [...new Set(["self-hosted", ...DATA.pool.map(m => m.kind)])]) {
    const list = DATA.pool.filter(m => m.kind === kind);
    const title = kind === "self-hosted" ? "Self-hosted" : kind;
    html += `<h2 class="group">${esc(title)} <span class="muted">${list.length}</span></h2><div class="card"><table class="compact"><tr><th>machine</th><th>memory</th><th>status</th><th>last run</th></tr>`;
    for (const m of list) html += `<tr><td>${esc(m.name)} <span class="muted">${m.id}</span></td>` +
      `<td>${m.memory_gib ? m.memory_gib + " GB" : ""}</td><td><span class="dot ${m.status}"></span>${m.status}</td><td>${m.last}</td></tr>`;
    if (!list.length) html += `<tr><td colspan="4" class="muted">None connected.</td></tr>`;
    html += `</table></div>`;
  }
  document.getElementById("main").innerHTML = html;
}
function people() {
  const ago = d => { if (!d) return "–"; const h = (Date.now() - new Date(d)) / 36e5; return h < 1 ? "just now" : h < 24 ? `${Math.round(h)}h ago` : `${Math.round(h / 24)}d ago`; };
  const time = m => !m ? "–" : m >= 60 ? `${(m / 60).toFixed(1)} h` : `${Math.round(m)} min`;
  let html = `<div class="card"><table class="compact"><tr><th>who</th><th>access</th><th class="num">today</th><th class="num">last 30 days</th><th class="num">total</th><th class="num">last active</th></tr>`;
  for (const p of DATA.people) {
    html += `<tr class="person" data-login="${esc(p.login)}"><td><img class="avatar" src="https://github.com/${p.login}.png?size=44">${esc(p.login)}</td>` +
      `<td class="muted">${esc(p.role || "–")}</td><td class="num">${time(p.today)}</td><td class="num">${time(p.month)}</td><td class="num">${time(p.total)}</td>` +
      `<td class="num muted">${ago(p.last)}</td></tr>`;
  }
  if (!DATA.people.length) html += `<tr><td colspan="6" class="muted">Nobody has signed in yet.</td></tr>`;
  document.getElementById("main").innerHTML = html + `</table><div class="muted" style="margin-top:8px">Everyone who has signed in, and the machine time their benchmarks used.</div></div>`;
  document.querySelectorAll("tr.person").forEach(tr => tr.onclick = () => { author = tr.dataset.login; tab = "Pushes"; draw(); });
}

async function gh(path, opts = {}) {
  const r = await fetch(`https://api.github.com/${path}`, { ...opts, headers: { Authorization: `Bearer ${token()}`, Accept: "application/vnd.github+json", ...(opts.headers || {}) } });
  if (!r.ok && r.status !== 404) throw new Error(`${r.status} ${await r.text()}`);
  if (r.status === 404 || r.status === 204) return null;
  return r.json();
}
function sheet(html) { document.getElementById("sheet").innerHTML = `<div class="card">${html}</div>`; document.getElementById("modal").hidden = false; }
function closeSheet() { document.getElementById("modal").hidden = true; }
document.getElementById("close").onclick = closeSheet;
document.getElementById("modal").onclick = e => { if (e.target.id === "modal") closeSheet(); };
document.addEventListener("keydown", e => { if (e.key === "Escape") { closeSheet(); closeMenu(); } });

function openSignIn() {
  sheet(`<h2>Sign in with GitHub</h2><p class="muted">Paste a fine-grained GitHub token for <b>${DATA.repo}</b> with <b>Contents</b> and <b>Actions</b> read & write. It stays in this browser.</p>` +
    `<input id="tok" type="password" placeholder="github_pat_…" size="40"> <button class="act" id="go">Sign in</button> <span id="err" class="down"></span>`);
  document.getElementById("go").onclick = async () => {
    try { localStorage.setItem("pie-evals-token", document.getElementById("tok").value.trim()); } catch {}
    await signIn();
    if (me) { closeSheet(); draw(); } else document.getElementById("err").textContent = "That token did not work.";
  };
}
function addMac() {
  const cmd = `PLATFORM_ID=<id> ./infra/mac/setup-runner.sh "$(gh api -X POST repos/${DATA.repo}/actions/runners/registration-token -q .token)"`;
  sheet(`<h2>Add a Mac</h2><p class="muted">On the Mac, in a checkout of <b>${DATA.repo}</b>, run:</p><pre class="cmd">${esc(cmd)}</pre>` +
    `<button class="act" id="copy">Copy</button> <span id="msg" class="muted"></span>` +
    `<p class="muted"><code>&lt;id&gt;</code> is the Mac's entry in <code>matrix/platforms.yaml</code>, for example <code>m5-max-48g</code>. The token needs admin on ${DATA.repo}.</p>`);
  document.getElementById("copy").onclick = async () => {
    try { await navigator.clipboard.writeText(cmd); document.getElementById("msg").textContent = "Copied."; } catch { document.getElementById("msg").textContent = "Select and copy the command."; }
  };
}

function closeMenu() { document.querySelector(".menu")?.remove(); }
document.addEventListener("click", e => { if (!e.target.closest("#who")) closeMenu(); });
async function signIn() {
  me = null; mine = null;
  if (token()) {
    try { me = await gh("user"); } catch { me = null; }
    if (me) {
      try {
        const path = `repos/${DATA.repo}/contents/users/${me.login}.json`, f = await gh(path);
        if (f) mine = JSON.parse(atob(f.content));
        else {
          mine = { models: [DATA.default_model], macs: [], enabled: false, joined: new Date().toISOString().slice(0, 10) };
          await gh(path, { method: "PUT", body: JSON.stringify({ message: `users: ${me.login} joined`, content: btoa(JSON.stringify(mine, null, 2) + NL) }) });
        }
      } catch { mine = null; }
    }
  }
  renderWho();
}
function renderWho() {
  const who = document.getElementById("who");
  who.innerHTML = me
    ? `<button class="pill" id="me"><img class="avatar" src="${me.avatar_url}">${esc(me.login)}</button>`
    : `<button class="signin" id="in"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>Sign in with GitHub</button>`;
  const i = document.getElementById("in"), m = document.getElementById("me");
  if (i) i.onclick = openSignIn;
  if (m) m.onclick = () => {
    if (document.querySelector(".menu")) return closeMenu();
    who.insertAdjacentHTML("beforeend", `<div class="menu"><button id="add">Add a Mac</button><button id="out">Sign out</button></div>`);
    document.getElementById("add").onclick = () => { closeMenu(); addMac(); };
    document.getElementById("out").onclick = () => { closeMenu(); try { localStorage.removeItem("pie-evals-token"); } catch {} me = null; mine = null; renderWho(); draw(); };
  };
}

function draw() {
  charts.forEach(c => c.destroy()); charts = [];
  document.getElementById("tabs").innerHTML = TABS.map(t => `<button class="${t === tab ? "on" : ""}">${t}</button>`).join("");
  document.querySelectorAll("#tabs button").forEach(b => b.onclick = () => { tab = b.textContent; draw(); });
  document.getElementById("controls").hidden = tab !== "Overview";
  ({ "Overview": overview, "Pushes": pushes, "Machines": pool, "People": people })[tab]();
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


def history(pie_repo: str) -> list[dict]:
    try:
        out = subprocess.run(["gh", "api", "--paginate", "--slurp", f"repos/{pie_repo}/commits?sha=main&per_page=100"],
                             capture_output=True, text=True, check=True).stdout
        pages = json.loads(out)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return []
    return [{"sha": c["sha"], "message": (c["commit"]["message"] or "").splitlines()[0][:120] if c["commit"]["message"] else "",
             "author": (c.get("author") or {}).get("login") or c["commit"]["author"]["name"],
             "date": c["commit"]["committer"]["date"]} for page in pages for c in page]


def runners(repo: str) -> list[dict] | None:
    got = _gh(f"repos/{repo}/actions/runners?per_page=100")
    return got.get("runners", []) if isinstance(got, dict) else None


def _pool(live: list[dict] | None, matrix: Matrix, last: dict[str, str]) -> list[dict]:
    pool = []
    for r in live or []:
        labels = [lab["name"] for lab in r.get("labels", [])]
        pid = next((lab for lab in labels if lab in matrix.platforms), None)
        if not pid:
            continue
        spec = matrix.platforms[pid]
        pool.append({
            "name": spec.accelerator,
            "id": pid,
            "kind": "RunPod" if spec.runpod_gpu_type else "self-hosted",
            "os": spec.os,
            "memory_gib": int(spec.memory_gib),
            "status": "busy" if r["status"] == "online" and r.get("busy") else "idle" if r["status"] == "online" else "offline",
            "last": last.get(pid, ""),
        })
    return sorted(pool, key=lambda m: (m["kind"] != "self-hosted", m["name"]))


def mac_models(matrix: Matrix) -> list[dict]:
    seen: dict[str, dict] = {}
    for c in matrix.expand():
        if (c.platform.os == "macos" and c.engine.value == "pie" and c.program.id == "text-completion-bench"
                and c.mode.tp == 1 and c.declared_unsupported_reason is None and c.artifact.kind.value == "full"):
            seen[c.artifact.id] = {"id": c.artifact.id, "name": c.artifact.base_model, "scheme": str(c.artifact.scheme)}
    names = [m["name"] for m in seen.values()]
    for m in seen.values():
        scheme = m.pop("scheme")
        if names.count(m["name"]) > 1:
            m["name"] = f"{m['name']} ({scheme})"
    return sorted(seen.values(), key=lambda m: m["name"])


def _paginate(path: str) -> list:
    try:
        out = subprocess.run(["gh", "api", "--paginate", "--slurp", path], capture_output=True, text=True, check=True).stdout
        return json.loads(out)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return []


def _when(ts: str | None) -> datetime | None:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None


def usage(repo: str, authors: dict[str, str], *, now: datetime | None = None) -> dict[str, dict]:
    now = now or datetime.now(timezone.utc)
    today, month = now.replace(hour=0, minute=0, second=0, microsecond=0), now - timedelta(days=30)
    pages = _paginate(f"repos/{repo}/actions/workflows/pie-eval.yml/runs?per_page=100")
    out: dict[str, dict] = {}
    for run in (r for page in pages for r in page.get("workflow_runs", [])):
        sha = (run.get("display_title") or "").split()[-1] if run.get("display_title") else ""
        who = (run.get("triggering_actor") or {}).get("login") if run.get("event") == "workflow_dispatch" else authors.get(sha)
        if not who:
            continue
        u = out.setdefault(who, {"today": 0.0, "month": 0.0, "total": 0.0, "last": ""})
        u["last"] = max(u["last"], run.get("created_at") or "")
        start, end = _when(run.get("run_started_at")), _when(run.get("updated_at"))
        if not (start and end and run.get("status") == "completed"):
            continue
        minutes = max(0.0, (end - start).total_seconds() / 60)
        u["total"] += minutes
        if start >= month:
            u["month"] += minutes
        if start >= today:
            u["today"] += minutes
    return out


def people(repo: str, authors: dict[str, str], users_dir: Path) -> list[dict]:
    members = {f.stem for f in users_dir.glob("*.json")} if users_dir.is_dir() else set()
    if not members:
        return []
    roles = {c["login"]: c.get("role_name", "") for page in _paginate(f"repos/{repo}/collaborators?affiliation=all&per_page=100") for c in page}
    used = usage(repo, authors)
    none = {"today": 0.0, "month": 0.0, "total": 0.0, "last": ""}
    rows = [{"login": who, "role": roles.get(who, ""), **used.get(who, none)} for who in members]
    return sorted(rows, key=lambda p: (-p["month"], -p["total"], p["login"].lower()))


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

    known = {c["sha"]: c for c in (history(pie_repo) if lookup_commits else [])}
    commits = []
    for sha in order:
        if sha in known:
            commits.append(dict(known[sha]))
            continue
        info = _gh(f"repos/{pie_repo}/commits/{sha}") if lookup_commits else None
        commit = (info or {}).get("commit", {})
        commits.append({
            "sha": sha,
            "message": (commit.get("message") or "").splitlines()[0][:90] if commit else "",
            "author": ((info or {}).get("author") or {}).get("login") or (commit.get("author") or {}).get("name", ""),
            "date": (commit.get("committer") or {}).get("date", ""),
        })
    commits.sort(key=lambda c: c["date"] or "~")
    measured = {c["sha"] for c in commits}
    all_commits = [c for c in known.values() if c["sha"] not in measured]

    models = mac_models(matrix)
    for m in models:
        m["has_results"] = m["id"] in have
    return {
        "repo": repo, "pie_repo": pie_repo, "default_model": DEFAULT_MODEL,
        "metrics": [{"phase": p, "name": n} for p, n, *_ in METRICS],
        "commits": commits, "history": all_commits, "results": results, "models": models,
        "pool": _pool(live, matrix, last),
        "people": people(repo, {c["sha"]: c["author"] for c in [*known.values(), *commits]}, users_dir) if lookup_commits else [],
    }


def render(store: Store, matrix: Matrix, out: Path, live: list[dict] | None = None, *, repo: str = "pie-project/pie-evals",
           pie_repo: str = "pie-project/pie", users_dir: Path = Path("users"), lookup_commits: bool = True) -> int:
    data = build(store, matrix, live, repo=repo, pie_repo=pie_repo, users_dir=users_dir, lookup_commits=lookup_commits)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(PAGE.replace("__DATA__", json.dumps(data)))
    return len(data["commits"])
