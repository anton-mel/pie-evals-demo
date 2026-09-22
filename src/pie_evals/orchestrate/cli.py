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
        gh.append({"job_id": j.job_id, "platform": j.platform_id, "shard": j.shard, "labels": plat.runner_labels, "os": plat.os, "runpod": bool(plat.runpod_gpu_type), "cells": len(j.cells), "est_minutes": round(j.est_minutes, 1)})
    (outp / "gh-matrix.json").write_text(json.dumps({"include": gh}))
    (outp / "policy.json").write_text(json.dumps({"job_budget_minutes": m.job_budget_minutes, "kill_minutes": m.kill_minutes}))
    click.echo(json.dumps(gh, indent=1))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"kill_minutes={m.kill_minutes}\njobs={len(js)}\n")


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
@click.option("--repo", required=True, help="owner/name the runner registers with")
@click.option("--runner-pat", envvar="GH_RUNNER_PAT", required=True, help="fine-grained PAT, Administration: read/write on --repo (minted into a registration token inside the pod)")
@click.option("--image", default=None, help="default: pieproject/runpod-ci-runner:latest")
@click.option("--image-version", default="latest")
@click.option("--network-volume-id", envvar="RUNPOD_NETWORK_VOLUME_ID", default=None)
@click.option("--kill-minutes", type=int, default=None, help="pod self-destruct; default = job budget × kill_factor")
@click.option("--cuda", "cuda_versions", multiple=True, default=["13.0", "13.1"], show_default=True, help="allowed host CUDA versions (pie pins cudarc cuda-13000)")
@click.pass_obj
def launch_pod(obj, platform, repo, runner_pat, image, image_version, network_volume_id, kill_minutes, cuda_versions):
    from . import runpod

    m: Matrix = obj["matrix"]
    plat = m.platforms[platform]
    rp = m.runpod
    h = runpod.create_pod(plat, repo=repo, runner_pat=runner_pat, kill_minutes=kill_minutes or m.kill_minutes,
                          image=image or runpod.DEFAULT_IMAGE, image_version=image_version, network_volume_id=network_volume_id,
                          volumes=rp.get("volumes") or None, preferred_data_centers=rp.get("preferred_data_centers"),
                          container_disk_gb=int(rp.get("container_disk_gb", 40)), cloud_type=str(rp.get("cloud_type", "SECURE")),
                          allowed_cuda_versions=list(cuda_versions) or None, log=lambda m_: click.echo(m_, err=True))
    click.echo(h.id)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"pod_id={h.id}\n")


@main.command("runpod-gpus")
def runpod_gpus():
    """List RunPod GPU type ids (what platforms.yaml runpod_gpu_type must use) with price/stock."""
    from . import runpod

    for g in sorted(runpod.gpu_types(), key=lambda g: str(g.get("id"))):
        click.echo(f"{g.get('id', ''):55s} {g.get('memoryInGb') or '':>4} GB  {g.get('displayName', '')}")


@main.command("runpod-stock")
@click.pass_obj
def runpod_stock(obj):
    """Secure-cloud stock per (platform GPU × volume data center) right now."""
    from . import runpod

    m: Matrix = obj["matrix"]
    dcs = list((m.runpod.get("volumes") or {}).keys()) or [d["id"] for d in runpod.data_centers() if d.get("storageSupport")]
    click.echo("platform".ljust(16) + "".join(dc.ljust(10) for dc in dcs))
    for p in m.platforms.values():
        if not p.runpod_gpu_type:
            continue
        click.echo(p.id.ljust(16) + "".join(runpod.stock(p.runpod_gpu_type, dc, p.count)[:8].ljust(10) for dc in dcs))


@main.command("runpod-volume")
@click.argument("action", type=click.Choice(["list", "create"]))
@click.argument("data_center", required=False)
@click.argument("size_gb", type=int, required=False)
def runpod_volume(action, data_center, size_gb):
    """List network volumes, or create one: runpod-volume create EUR-IS-1 200 (then add it to matrix/runpod.yaml)."""
    from . import runpod

    if action == "list":
        for v in runpod._req("GET", "/networkvolumes"):
            click.echo(f"{v['id']}  {v.get('dataCenterId')}  {v.get('size')} GB  {v.get('name')}")
    else:
        v = runpod.create_network_volume(f"pie-evals-{data_center.lower()}", size_gb, data_center)
        click.echo(f"{v['id']}  {v.get('dataCenterId')}  {v.get('size')} GB  — add to matrix/runpod.yaml volumes")


@main.command("validate-platforms")
@click.pass_obj
def validate_platforms(obj):
    """Check every runpod_gpu_type in platforms.yaml against the live GPU type list. Exit 1 on unknown ids."""
    from . import runpod

    problems = runpod.validate_platforms(obj["matrix"].platforms)
    for p in problems:
        click.echo(p, err=True)
    click.echo("ok" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


@main.command("terminate-pod")
@click.argument("pod_id")
def terminate_pod(pod_id):
    from . import runpod

    runpod.terminate_pod(pod_id)
    click.echo(f"terminated {pod_id}")


@main.command("reap-pods")
@click.option("--max-age-hours", type=float, default=2.0, help="anything past kill_minutes is an orphan; 2h covers the largest budget with slack")
@click.option("--dry-run", is_flag=True)
def reap_pods(max_age_hours, dry_run):
    from . import runpod

    click.echo(json.dumps(runpod.reap(int(max_age_hours * 3600), dry_run=dry_run)))


if __name__ == "__main__":
    main()
