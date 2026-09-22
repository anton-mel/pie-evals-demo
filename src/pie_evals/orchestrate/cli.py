"""``pie-evals`` — orchestration CLI. Thin, so that a workflow step and a
future coordinator service call the same functions."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import click

from pie_evals.schema import Tier

from . import baselines as bl
from . import report as rp
from .jobs import make_jobs
from .matrix import Matrix, summarize
from .store import Store


@click.group()
@click.option("--matrix", "matrix_dir", default="matrix", show_default=True)
@click.option("--store", "store_dir", default="store", show_default=True)
@click.pass_context
def main(ctx, matrix_dir, store_dir):
    ctx.obj = {"matrix": Matrix.load(matrix_dir), "store": Store(store_dir)}


@main.command("expand")
@click.option("--tier", type=click.Choice([t.value for t in Tier]), default=None)
@click.option("--json", "as_json", is_flag=True)
@click.pass_obj
def expand(obj, tier, as_json):
    """Expand the matrix; print a summary (or the cells as JSON)."""
    m: Matrix = obj["matrix"]
    cells = m.expand()
    if tier:
        cells = m.cells_for(Tier(tier), cells)
    if as_json:
        click.echo(json.dumps([c.model_dump(mode="json") | {"cell_id": c.cell_id, "cell_key": c.cell_key} for c in cells]))
    else:
        click.echo(json.dumps(summarize(cells), indent=1))
        for t in Tier:
            click.echo(f"{t}: budget {json.dumps(m.budget_report(t, cells))}")
        for p in [p for t in Tier for p in m.check_budget(t, cells)]:
            click.echo(f"BUDGET: {p}", err=True)


@main.command("check")
@click.pass_obj
def check(obj):
    """Validate the matrix: budgets per tier. Exit 1 on a violation in an enforced tier."""
    m: Matrix = obj["matrix"]
    cells = m.expand()
    for t in Tier:
        for p in m.check_budget(t, cells):
            click.echo(("ERROR " if m.suites[t.value].enforce_budget else "warn  ") + p, err=True)
    problems = [p for t in Tier for p in m.check_budget(t, cells, enforced_only=True)]
    click.echo(json.dumps(summarize(cells)))
    sys.exit(1 if problems else 0)


@main.command("jobs")
@click.option("--tier", type=click.Choice([t.value for t in Tier]), required=True)
@click.option("--pie-commit", default=None)
@click.option("--platform", "platforms", multiple=True)
@click.option("--engine", "engines", multiple=True)
@click.option("--out", type=click.Path(), default="jobs")
@click.option("--label", default=None)
@click.pass_obj
def jobs(obj, tier, pie_commit, platforms, engines, out, label):
    """Write one JobSpec JSON per platform, plus a GitHub Actions matrix file."""
    m: Matrix = obj["matrix"]
    st: Store = obj["store"]
    js = make_jobs(m, Tier(tier), pie_commit=pie_commit, store=st, platforms=list(platforms) or None, engines=list(engines) or None, label=label)
    outp = Path(out)
    outp.mkdir(parents=True, exist_ok=True)
    gh = []
    for j in js:
        (outp / f"{j.job_id}.json").write_text(j.model_dump_json(indent=1))
        plat = m.platforms[j.platform_id]
        gh.append({"job_id": j.job_id, "platform": j.platform_id, "labels": plat.runner_labels, "os": plat.os, "runpod": bool(plat.runpod_gpu_type), "cells": len(j.cells)})
    (outp / "gh-matrix.json").write_text(json.dumps({"include": gh}))
    click.echo(json.dumps(gh, indent=1))


@main.command("collect")
@click.option("--tier", type=click.Choice([t.value for t in Tier]), required=True)
@click.argument("node_out", nargs=-1, type=click.Path(exists=True))
@click.pass_obj
def collect(obj, tier, node_out):
    """Import node output directories (records.jsonl) into the store."""
    st: Store = obj["store"]
    for d in node_out:
        d = Path(d)
        run_id = (d / "run_id.txt").read_text().strip() if (d / "run_id.txt").exists() else d.name
        p = st.import_node_output(d, tier=Tier(tier), run_id=run_id)
        click.echo(f"{d} -> {p}")


@main.command("report")
@click.option("--tier", type=click.Choice([t.value for t in Tier]), required=True)
@click.option("--out", type=click.Path(), default="reports")
@click.pass_obj
def report(obj, tier, out):
    """Render coverage, regressions, baseline ratios, calibration."""
    m: Matrix = obj["matrix"]
    st: Store = obj["store"]
    t = Tier(tier)
    outp = Path(out) / t.value
    outp.mkdir(parents=True, exist_ok=True)
    views = rp.coverage(m, st, t)
    (outp / "coverage.md").write_text(rp.coverage_markdown(views, t))
    regs = rp.regressions(m, st, t)
    (outp / "regressions.md").write_text(rp.regressions_markdown(regs))
    (outp / "regressions.json").write_text(rp.to_json(regs))
    ratios = rp.baseline_ratios(m, st, t)
    (outp / "baselines.md").write_text(rp.baseline_markdown(ratios))
    (outp / "baselines.json").write_text(rp.to_json(ratios))
    (Path(out) / "calibration.md").write_text(rp.calibration(m, st))
    n_reg = sum(1 for r in regs if r["kind"] == "regression")
    trails = sum(1 for r in ratios if not r["pie_leads"])
    click.echo(json.dumps({"cells": len(views), "regressions": n_reg, "pie_trails": trails, "escalate_families": rp.escalation_families(m, st)}))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"regressions={n_reg}\npie_trails={trails}\n")


@main.command("watch-baselines")
@click.option("--lock", type=click.Path(), default="matrix/baselines.lock.json")
@click.pass_obj
def watch_baselines(obj, lock):
    """Check PyPI/GitHub for newer baseline releases than the pins."""
    checks = bl.check(obj["matrix"])
    bl.write_lock(checks, Path(lock))
    for c in checks:
        click.echo(f"{c.engine}: pinned {c.pinned} latest {c.latest}{'  <-- NEWER' if c.newer else ''}")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write("newer=" + ",".join(c.engine for c in checks if c.newer) + "\n")


@main.command("launch-pod")
@click.option("--platform", required=True)
@click.option("--image", required=True)
@click.option("--repo", required=True, help="owner/name")
@click.option("--runner-token", envvar="GH_RUNNER_TOKEN", required=True)
@click.option("--image-version", default="dev")
@click.option("--network-volume-id", envvar="RUNPOD_NETWORK_VOLUME_ID", default=None)
@click.pass_obj
def launch_pod(obj, platform, image, repo, runner_token, image_version, network_volume_id):
    from . import runpod

    plat = obj["matrix"].platforms[platform]
    h = runpod.create_pod(plat, image=image, repo=repo, runner_token=runner_token, image_version=image_version, network_volume_id=network_volume_id)
    click.echo(h.id)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"pod_id={h.id}\n")


@main.command("terminate-pod")
@click.argument("pod_id")
def terminate_pod(pod_id):
    from . import runpod

    runpod.terminate_pod(pod_id)
    click.echo(f"terminated {pod_id}")


@main.command("reap-pods")
@click.option("--max-age-hours", type=float, default=6)
@click.option("--dry-run", is_flag=True)
def reap_pods(max_age_hours, dry_run):
    from . import runpod

    click.echo(json.dumps(runpod.reap(int(max_age_hours * 3600), dry_run=dry_run)))


if __name__ == "__main__":
    main()
