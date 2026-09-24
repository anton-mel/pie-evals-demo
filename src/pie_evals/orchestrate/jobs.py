"""Turn cells into JobSpecs: one job per platform per tier, carrying the
pins and the history each cell needs for adaptive repetition."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from pie_evals.schema import Cell, JobSpec, RepetitionPolicy, Tier

from .store import Store

if TYPE_CHECKING:
    from .matrix import Matrix


def process_key(c: Cell) -> tuple:
    return (str(c.engine), c.artifact.artifact_key, c.mode.key)



#: minutes a cell costs on top of its workload: vLLM and SGLang boot a fresh
#: server per cell (2–3 min of import, CUDA graph capture and warm-up on an
#: L40S; nightly 35926457671 lost 33 of 78 vLLM cells to the soft budget
#: because shards were packed on workload time alone); pie serves one
#: process per model, so its per-cell overhead is a few seconds
ENGINE_CELL_MINUTES = {"vllm": 4.0, "sglang": 3.5}  # measured: 12 vLLM Qwen3.5-0.8B cells took 3860 s on an L40S (nightly 35935510089)


def cell_minutes(c: Cell) -> float:
    return float(c.workload.est_minutes) + ENGINE_CELL_MINUTES.get(str(c.engine), 0.0)

def shard_groups(cells: list[Cell], budget_minutes: float) -> list[list[Cell]]:
    """Bin-pack cells into jobs of ~budget_minutes. A process group (same
    engine, artifact, mode = one loaded model) is never split; groups are
    placed largest-first into the first shard with room (first-fit
    decreasing), so a shard holds a few whole models and nothing else."""
    groups: dict[tuple, list[Cell]] = {}
    for c in cells:
        groups.setdefault(process_key(c), []).append(c)
    # a group larger than the budget is split into budget-sized pieces (the
    # model loads once per piece; pieces after the first carry no control-aa
    # cell, so they run without the A/A gate — recorded in the job's notes)
    pieces: list[list[Cell]] = []
    for g in groups.values():
        if sum(cell_minutes(c) for c in g) <= budget_minutes:
            pieces.append(g)
            continue
        g = sorted(g, key=lambda c: (0 if c.workload.kind.value == "control_aa" else 1, -cell_minutes(c)))
        cur: list[Cell] = []
        load = 0.0
        for c in g:
            if cur and load + cell_minutes(c) > budget_minutes:
                pieces.append(cur)
                cur, load = [], 0.0
            cur.append(c)
            load += cell_minutes(c)
        if cur:
            pieces.append(cur)
    ordered = sorted(pieces, key=lambda g: -sum(cell_minutes(c) for c in g))
    shards: list[list[Cell]] = []
    loads: list[float] = []
    for g in ordered:
        need = sum(cell_minutes(c) for c in g)
        for i, load in enumerate(loads):
            if load + need <= budget_minutes:
                shards[i].extend(g)
                loads[i] += need
                break
        else:
            shards.append(list(g))
            loads.append(need)
    return shards


def make_jobs(
    matrix: Matrix,
    tier: Tier,
    *,
    pie_commit: str | None,
    store: Store | None = None,
    platforms: list[str] | None = None,
    engines: list[str] | None = None,
    cells: list[Cell] | None = None,
    label: str | None = None,
) -> list[JobSpec]:
    cells = matrix.runnable(tier, cells)
    if platforms:
        cells = [c for c in cells if c.platform.id in platforms]
    if engines:
        cells = [c for c in cells if str(c.engine) in engines]
    history = store.history(limit=20) if store else {}
    by_plat: dict[str, list[Cell]] = {}
    for c in cells:
        by_plat.setdefault(c.platform.id, []).append(c)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    budget = matrix.job_budget_minutes
    kill_s = int(budget * matrix.kill_factor * 60)
    jobs = []
    for plat, plat_cells in sorted(by_plat.items()):
        for idx, shard in enumerate(shard_groups(plat_cells, budget)):
            # one model per process: order by (engine, artifact, mode) so the node loads each model once
            shard.sort(key=lambda c: (str(c.engine), c.artifact.id, c.mode.key, c.program.id, c.workload.id))
            pins = {e.id: e.pin for e in matrix.engines.values() if e.pin and any(str(c.engine) == e.id for c in shard)}
            seed = f"{tier}|{plat}|{idx}|{pie_commit}|{stamp}|{label or ''}"
            job_id = f"{tier}-{plat}-s{idx:02d}-{stamp}-" + hashlib.sha256(seed.encode()).hexdigest()[:6]
            est = sum(cell_minutes(c) for c in shard)
            jobs.append(
                JobSpec(
                    job_id=job_id,
                    tier=tier,
                    platform_id=plat,
                    shard=idx,
                    pie_commit=pie_commit,
                    pie_build_features=[_feature_for(shard[0].platform.backend.value)],
                    baseline_versions=pins,
                    cells=shard,
                    repetition=RepetitionPolicy(min_rounds=1 if tier in (Tier.SMOKE, Tier.TARGETED) else 3),
                    history={c.cell_id: history.get(c.cell_id, []) for c in shard if c.cell_id in history},
                    per_cell_timeout_s=min(1800 if tier in (Tier.SMOKE, Tier.TARGETED) else 5400, kill_s),
                    budget_s=int(budget * 60),
                    kill_s=kill_s,
                    est_minutes=est,
                )
            )
    # baseline comparisons first: a capped dispatch (--max-jobs) must not end up pie-only
    jobs.sort(key=lambda j: (-len({str(c.engine) for c in j.cells}), -j.est_minutes))
    return jobs


def available_platforms(matrix: Matrix, repo: str, token: str | None = None) -> tuple[list[str], dict[str, str]]:
    """Platforms a job can actually land on right now: RunPod ones (an
    ephemeral runner is created per job) and resident ones with an *online*
    registered runner carrying the platform's label. Everything else is
    skipped with a reason — a job queued for a runner that never comes sits
    in GitHub's queue for 24 h and holds the workflow's concurrency group."""
    env = {**os.environ, **({"GH_TOKEN": token} if token else {})}
    try:
        out = subprocess.run(["gh", "api", f"repos/{repo}/actions/runners?per_page=100"], capture_output=True, text=True, env=env, check=True).stdout
        runners = json.loads(out).get("runners", [])
    except Exception as e:  # no gh / no token: only RunPod platforms are known-schedulable
        runners, note = [], f"runner list unavailable ({e}); resident platforms skipped"
    else:
        note = ""
    online = {lab["name"] for r in runners if r.get("status") == "online" for lab in r.get("labels", [])}
    ok, skipped = [], {}
    for p in matrix.platforms.values():
        if p.runpod_gpu_type:
            ok.append(p.id)
        elif p.id in online:
            ok.append(p.id)
        else:
            skipped[p.id] = note or f"no online runner with label '{p.id}'"
    return ok, skipped


def _feature_for(backend: str) -> str:
    return {"cuda": "cuda", "metal": "metal", "vulkan": "vulkan", "wgpu": "wgpu"}[backend]
