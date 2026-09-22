"""Turn cells into JobSpecs: one job per platform per tier, carrying the
pins and the history each cell needs for adaptive repetition."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from pie_evals.schema import Cell, JobSpec, RepetitionPolicy, Tier

from .store import Store

if TYPE_CHECKING:
    from .matrix import Matrix


def process_key(c: Cell) -> tuple:
    return (str(c.engine), c.artifact.artifact_key, c.mode.key)


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
        if sum(c.workload.est_minutes for c in g) <= budget_minutes:
            pieces.append(g)
            continue
        g = sorted(g, key=lambda c: (0 if c.workload.kind.value == "control_aa" else 1, -c.workload.est_minutes))
        cur: list[Cell] = []
        load = 0.0
        for c in g:
            if cur and load + c.workload.est_minutes > budget_minutes:
                pieces.append(cur)
                cur, load = [], 0.0
            cur.append(c)
            load += c.workload.est_minutes
        if cur:
            pieces.append(cur)
    ordered = sorted(pieces, key=lambda g: -sum(c.workload.est_minutes for c in g))
    shards: list[list[Cell]] = []
    loads: list[float] = []
    for g in ordered:
        need = sum(c.workload.est_minutes for c in g)
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
            est = sum(c.workload.est_minutes for c in shard)
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
                    repetition=RepetitionPolicy(min_rounds=1 if tier == Tier.SMOKE else 3),
                    history={c.cell_id: history.get(c.cell_id, []) for c in shard if c.cell_id in history},
                    per_cell_timeout_s=min(1800 if tier == Tier.SMOKE else 5400, kill_s),
                    budget_s=int(budget * 60),
                    kill_s=kill_s,
                    est_minutes=est,
                )
            )
    return jobs


def _feature_for(backend: str) -> str:
    return {"cuda": "cuda", "metal": "metal", "vulkan": "vulkan", "wgpu": "wgpu"}[backend]
