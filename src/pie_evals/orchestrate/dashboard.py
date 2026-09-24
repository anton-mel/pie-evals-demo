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
<title>pie evals</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<style>
  * { box-sizing: border-box; }
  body { font: 15px/1.5 -apple-system, system-ui, sans-serif; margin: 0; color: #1f2328; background: #f6f8fa; }
  header { background: #fff; border-bottom: 1px solid #d8dee4; }
  .bar { max-width: 1000px; margin: 0 auto; padding: 12px 16px; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
  .brand { font-weight: 700; font-size: 17px; }
  nav { display: flex; gap: 4px; flex-wrap: wrap; }
  nav button { font: inherit; border: 0; background: none; padding: 6px 12px; border-radius: 6px; cursor: pointer; color: #424a53; }
  nav button.on { background: #eaeef2; color: #1f2328; font-weight: 600; }
  .grow { flex: 1; }
  main { max-width: 1000px; margin: 0 auto; padding: 20px 16px 48px; }
  .card { background: #fff; border: 1px solid #d8dee4; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
  h2 { font-size: 16px; margin: 0 0 12px; }
  .muted { color: #656d76; font-size: 13px; }
  .big { font-size: 26px; font-weight: 600; }
  .up { color: #1a7f37; } .down { color: #cf222e; }
  .row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .charts { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 12px; }
  .chart { position: relative; height: 200px; min-width: 0; }
  @media (max-width: 700px) { .charts { grid-template-columns: 1fr; } }
  @media (max-width: 700px) { .row { grid-template-columns: 1fr; } }
  table { border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }
  th, td { text-align: left; padding: 8px 10px; border-bottom: 1px solid #eaeef2; vertical-align: top; }
  th { font-size: 13px; color: #424a53; font-weight: 600; }
  td.num, th.num { text-align: right; }
  tr.push { cursor: pointer; } tr.push:hover { background: #f6f8fa; }
  .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px; }
  .idle { background: #1a7f37; } .busy { background: #bf8700; } .offline { background: #cf222e; }
  .tag { display: inline-block; background: #eaeef2; border-radius: 10px; padding: 0 8px; margin: 0 4px 4px 0; font-size: 13px; }
  .avatar { width: 22px; height: 22px; border-radius: 50%; vertical-align: middle; margin-right: 6px; }
  select, input, button.act { font: inherit; padding: 6px 10px; border: 1px solid #d0d7de; border-radius: 6px; background: #fff; }
  button.act { background: #1f883d; color: #fff; border-color: #1a7f37; cursor: pointer; }
  label.check { display: block; padding: 4px 0; }
  code { background: #eaeef2; border-radius: 4px; padding: 1px 5px; font-size: 13px; }
  a { color: #0969da; text-decoration: none; }
</style>
</head>
<body>
<header><div class="bar">
  <span class="brand">pie evals</span>
  <nav id="tabs"></nav>
  <span class="grow"></span>
  <select id="unit"><option value="v">tok/s</option><option value="tflops">TFLOP/s</option></select>
  <select id="model"></select>
  <span id="who"></span>
</div></header>
<main id="main"></main>
<script>
const DATA = __DATA__;
const TABS = ["Overview", "Pushes", "Macs", "People", "My setup"];
const COLORS = ["#0969da", "#bf8700", "#8250df"];
const pct = (a, b) => (a / b - 1) * 100;
const signed = v => `<span class="${v > 0.5 ? "up" : v < -0.5 ? "down" : ""}">${v > 0 ? "+" : ""}${v.toFixed(1)}%</span>`;
const mean = xs => xs.reduce((a, b) => a + b, 0) / xs.length;
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
function phaseChange(mac, phase, from, to) {
  const xs = DATA.metrics.map((m, i) => [m, i]).filter(([m]) => m.phase === phase).map(([, i]) => {
    const s = series(mac, i), a = s.find(p => p.sha === from), b = s.find(p => p.sha === to);
    return a && b ? pct(b.v, a.v) : null;
  }).filter(v => v != null);
  return xs.length ? mean(xs) : null;
}
const macs = () => Object.keys(DATA.results).filter(m => DATA.results[m].models[modelSel.value]);

function overview() {
  let html = "";
  for (const mac of macs()) {
    const shas = DATA.commits.filter(c => DATA.metrics.some((_, i) => series(mac, i).some(p => p.sha === c.sha))).map(c => c.sha);
    html += `<div class="card"><h2>${DATA.results[mac].name}</h2><div class="muted">${shas.length} pushes · ${unitName()} per push</div>` +
      `<div class="charts"><div class="chart"><canvas data-mac="${mac}" data-phase="Prefill"></canvas></div>` +
      `<div class="chart"><canvas data-mac="${mac}" data-phase="Decode"></canvas></div></div></div>`;
  }
  document.getElementById("main").innerHTML = html || `<div class="card muted">No results for this model yet.</div>`;
  const key = unitSel.value;
  document.querySelectorAll("canvas").forEach(cv => {
    const rows = DATA.metrics.map((m, i) => [m, i]).filter(([m]) => m.phase === cv.dataset.phase);
    const labels = DATA.commits.map(c => c.sha).filter(sha => rows.some(([, i]) => series(cv.dataset.mac, i).some(p => p.sha === sha)));
    charts.push(new Chart(cv, { type: "line",
      data: { labels: labels.map(s => s.slice(0, 7)), datasets: rows.map(([m, i], k) => {
        const by = Object.fromEntries(series(cv.dataset.mac, i).map(p => [p.sha, p[key]]));
        return { label: m.name, data: labels.map(l => by[l] ?? null), borderColor: COLORS[k], backgroundColor: COLORS[k], pointRadius: 3, spanGaps: true };
      }) },
      options: { responsive: true, maintainAspectRatio: false,
                 plugins: { title: { display: true, text: `${cv.dataset.phase} · ${unitName()}` }, legend: { position: "bottom", labels: { boxWidth: 10 } } },
                 scales: { y: { beginAtZero: false } } } }));
  });
}

function pushes() {
  const list = macs();
  let html = `<div class="card"><h2>Pushes to main</h2><table><tr><th>commit</th><th>author</th>` +
    list.map(m => `<th class="num">${DATA.results[m].name}<br><span class="muted">prefill · decode</span></th>`).join("") + `</tr>`;
  [...DATA.commits].reverse().forEach(c => {
    const i = DATA.commits.indexOf(c), prev = DATA.commits[i - 1];
    const cells = list.map(m => {
      if (!prev) return `<td class="num muted">first</td>`;
      const p = phaseChange(m, "Prefill", prev.sha, c.sha), d = phaseChange(m, "Decode", prev.sha, c.sha);
      return `<td class="num">${p == null ? "–" : signed(p)} · ${d == null ? "–" : signed(d)}</td>`;
    }).join("");
    html += `<tr class="push" data-sha="${c.sha}"><td><a href="https://github.com/${DATA.pie_repo}/commit/${c.sha}" target="_blank">${c.sha.slice(0, 7)}</a> ${c.message}<div class="muted">${c.date}</div></td><td>${c.author}</td>${cells}</tr>` +
            `<tr class="detail" data-for="${c.sha}" hidden><td colspan="${2 + list.length}">${detail(c.sha, list)}</td></tr>`;
  });
  document.getElementById("main").innerHTML = html + `</table><div class="muted" style="margin-top:8px">Average change against the previous push. Click a push for every test.</div></div>`;
  document.querySelectorAll("tr.push").forEach(tr => tr.onclick = e => {
    if (e.target.tagName === "A") return;
    const d = document.querySelector(`tr.detail[data-for="${tr.dataset.sha}"]`); d.hidden = !d.hidden;
  });
}
function detail(sha, list) {
  let html = `<table><tr><th>test</th>` + list.map(m => `<th class="num">${DATA.results[m].name}</th>`).join("") + `</tr>`;
  DATA.metrics.forEach((m, i) => {
    html += `<tr><td>${m.phase} · ${m.name}</td>` + list.map(mac => {
      const s = series(mac, i), k = s.findIndex(p => p.sha === sha);
      if (k < 0) return `<td class="num muted">–</td>`;
      const p = s[k], ch = k > 0 ? " " + signed(pct(p.v, s[k - 1].v)) : "";
      return `<td class="num">${Math.round(p.v).toLocaleString()} tok/s${p.tflops != null ? ` · ${p.tflops.toFixed(2)} TFLOP/s` : ""}${ch}</td>`;
    }).join("") + `</tr>`;
  });
  return html + `</table>`;
}

function pool() {
  let html = `<div class="card"><h2>Connected Macs</h2><table><tr><th>Mac</th><th>memory</th><th>status</th><th>last run</th></tr>`;
  for (const m of DATA.pool) html += `<tr><td>${m.name} <span class="muted">${m.id}</span></td><td>${m.memory_gib ? m.memory_gib + " GB" : ""}</td><td><span class="dot ${m.status}"></span>${m.status}</td><td>${m.last}</td></tr>`;
  if (!DATA.pool.length) html += `<tr><td colspan="4" class="muted">No Mac is connected.</td></tr>`;
  document.getElementById("main").innerHTML = html + `</table><div class="muted" style="margin-top:8px">A Mac joins with <code>infra/mac/setup-runner.sh</code>.</div></div>`;
}

function people() {
  let html = `<div class="card"><h2>People</h2><table><tr><th>who</th><th>models</th><th>Macs</th><th>last measured push</th></tr>`;
  for (const p of DATA.people) {
    const last = [...DATA.commits].reverse().find(c => c.author === p.login);
    html += `<tr><td><img class="avatar" src="https://github.com/${p.login}.png?size=44">${p.login}</td>` +
      `<td>${p.models.map(m => `<span class="tag">${modelName(m)}</span>`).join("") || `<span class="muted">default</span>`}</td>` +
      `<td>${p.macs.map(m => `<span class="tag">${macName(m)}</span>`).join("") || `<span class="muted">every connected Mac</span>`}</td>` +
      `<td>${last ? `<a href="https://github.com/${DATA.pie_repo}/commit/${last.sha}" target="_blank">${last.sha.slice(0, 7)}</a> ${last.date}` : `<span class="muted">none yet</span>`}</td></tr>`;
  }
  if (!DATA.people.length) html += `<tr><td colspan="4" class="muted">Nobody has a setup yet: everyone gets ${modelName(DATA.default_model)} on every connected Mac.</td></tr>`;
  document.getElementById("main").innerHTML = html + `</table><div class="muted" style="margin-top:8px">` +
    `Anyone who can write to <b>${DATA.repo}</b> can set their own. For one commit only, add a line to its message: ` +
    `<code>Evals: models=${DATA.default_model} macs=${DATA.pool[0]?.id || "m5-max-48g"}</code></div></div>`;
}

async function gh(path, opts = {}) {
  const r = await fetch(`https://api.github.com/${path}`, { ...opts, headers: { Authorization: `Bearer ${token()}`, Accept: "application/vnd.github+json", ...(opts.headers || {}) } });
  if (!r.ok && r.status !== 404) throw new Error(`${r.status} ${await r.text()}`);
  return r.status === 404 ? null : r.json();
}
async function setup() {
  const main = document.getElementById("main");
  if (!me) {
    main.innerHTML = `<div class="card"><h2>Sign in</h2><p class="muted">Paste a GitHub token that can write to <b>${DATA.repo}</b> (fine-grained: Contents read & write). It stays in this browser.</p>` +
      `<input id="tok" type="password" placeholder="github_pat_…" size="40"> <button class="act" id="go">Sign in</button> <span id="err" class="down"></span></div>`;
    document.getElementById("go").onclick = async () => {
      try { localStorage.setItem("pie-evals-token", document.getElementById("tok").value.trim()); } catch {}
      await signIn(); if (me) setup(); else document.getElementById("err").textContent = "That token did not work.";
    };
    return;
  }
  const file = await gh(`repos/${DATA.repo}/contents/users/${me.login}.json`);
  const cur = file ? JSON.parse(atob(file.content)) : { models: [DATA.default_model], macs: [] };
  main.innerHTML = `<div class="card"><h2>What runs on my pushes</h2><p class="muted">When a commit by <b>${me.login}</b> lands on pie main, these models run on these Macs.</p>` +
    `<div class="row"><div><h2>Models</h2>${DATA.models.map(m => `<label class="check"><input type="checkbox" name="model" value="${m.id}" ${cur.models.includes(m.id) ? "checked" : ""}> ${m.name}</label>`).join("")}</div>` +
    `<div><h2>Macs</h2><label class="check"><input type="checkbox" name="all" ${cur.macs.length ? "" : "checked"}> every connected Mac</label>` +
    DATA.pool.map(m => `<label class="check"><input type="checkbox" name="mac" value="${m.id}" ${cur.macs.includes(m.id) ? "checked" : ""}> ${m.name} <span class="muted">${m.id}</span></label>`).join("") +
    `</div></div><button class="act" id="save">Save</button> <span id="msg" class="muted"></span></div>`;
  document.getElementById("save").onclick = async () => {
    const pick = n => [...document.querySelectorAll(`input[name=${n}]:checked`)].map(x => x.value);
    const body = { models: pick("model"), macs: document.querySelector("input[name=all]").checked ? [] : pick("mac") };
    const msg = document.getElementById("msg"); msg.textContent = "Saving…";
    try {
      const now = await gh(`repos/${DATA.repo}/contents/users/${me.login}.json`);
      await gh(`repos/${DATA.repo}/contents/users/${me.login}.json`, { method: "PUT", body: JSON.stringify({
        message: `users: ${me.login} runs ${body.models.join(", ") || "the default"}`,
        content: btoa(JSON.stringify(body, null, 2) + "\\n"), ...(now ? { sha: now.sha } : {}) }) });
      msg.textContent = "Saved. Your next push to main runs this.";
    } catch (e) { msg.textContent = "Could not save: " + e.message; }
  };
}
async function signIn() {
  me = null;
  if (token()) { try { me = await gh("user"); } catch { me = null; } }
  renderWho();
}
function renderWho() {
  document.getElementById("who").innerHTML = me
    ? `<img class="avatar" src="${me.avatar_url}">${me.login} <a href="#" id="out">sign out</a>`
    : `<a href="#" id="in">sign in</a>`;
  const o = document.getElementById("out"), i = document.getElementById("in");
  if (o) o.onclick = e => { e.preventDefault(); try { localStorage.removeItem("pie-evals-token"); } catch {} me = null; renderWho(); if (tab === "My setup") setup(); };
  if (i) i.onclick = e => { e.preventDefault(); tab = "My setup"; draw(); };
}

function draw() {
  charts.forEach(c => c.destroy()); charts = [];
  document.getElementById("tabs").innerHTML = TABS.map(t => `<button class="${t === tab ? "on" : ""}">${t}</button>`).join("");
  document.querySelectorAll("#tabs button").forEach(b => b.onclick = () => { tab = b.textContent; draw(); });
  modelSel.style.visibility = tab === "Overview" || tab === "Pushes" ? "visible" : "hidden";
  unitSel.style.visibility = tab === "Overview" ? "visible" : "hidden";
  ({ "Overview": overview, "Pushes": pushes, "Macs": pool, "People": people, "My setup": setup })[tab]();
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
