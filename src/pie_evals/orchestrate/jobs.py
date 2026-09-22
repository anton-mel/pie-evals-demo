"""Turn cells into JobSpecs: one job per platform per tier, carrying the
pins and the history each cell needs for adaptive repetition."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from pie_evals.schema import Cell, JobSpec, RepetitionPolicy, Tier

from .matrix import Matrix
from .store import Store


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
    jobs = []
    for plat, plat_cells in sorted(by_plat.items()):
        # one model per process: order by (engine, artifact, mode) so the node loads each model once
        plat_cells.sort(key=lambda c: (str(c.engine), c.artifact.id, c.mode.key, c.program.id, c.workload.id))
        pins = {e.id: e.pin for e in matrix.engines.values() if e.pin and any(str(c.engine) == e.id for c in plat_cells)}
        seed = f"{tier}|{plat}|{pie_commit}|{stamp}|{label or ''}"
        job_id = f"{tier}-{plat}-{stamp}-" + hashlib.sha256(seed.encode()).hexdigest()[:6]
        jobs.append(
            JobSpec(
                job_id=job_id,
                tier=tier,
                platform_id=plat,
                pie_commit=pie_commit,
                pie_build_features=[_feature_for(plat_cells[0].platform.backend.value)],
                baseline_versions=pins,
                cells=plat_cells,
                repetition=RepetitionPolicy(min_rounds=1 if tier == Tier.SMOKE else 3),
                history={c.cell_id: history.get(c.cell_id, []) for c in plat_cells if c.cell_id in history},
                per_cell_timeout_s=1800 if tier == Tier.SMOKE else 5400,
            )
        )
    return jobs


def _feature_for(backend: str) -> str:
    return {"cuda": "cuda", "metal": "metal", "vulkan": "vulkan", "wgpu": "wgpu"}[backend]
