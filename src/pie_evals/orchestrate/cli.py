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
from . import dashboard as dash
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
@click.option("--program", "programs", multiple=True, help="restrict to these program ids")
@click.option("--artifact", "artifacts", multiple=True, help="restrict to these artifact ids")
@click.option("--workload", "workloads", multiple=True, help="restrict to these workload ids (the control A/A always stays)")
@click.option("--max-jobs", type=int, default=None, help="cap the number of jobs (shards) written, baseline-bearing first")
@click.option("--max-jobs-per-platform", type=int, default=None, help="cap per platform, so a capped dispatch spans every platform")
@click.option("--out", type=click.Path(), default="jobs")
@click.option("--label", default=None)
@click.option("--skip-unavailable", is_flag=True, help="drop platforms with no RunPod type and no online runner (needs gh + a token with actions:read)")
@click.option("--repo", default=None, help="owner/name for --skip-unavailable (default: $GITHUB_REPOSITORY)")
@click.option("--skip-recorded", is_flag=True, help="drop cells the store already holds at this pie commit (a re-dispatch after lost launches)")
@click.option("--run-label", default=None, help="extra runner label on every pod shard and its pod, so a run's pods take only its own jobs")
@click.pass_obj
def jobs(obj, tier, pie_commit, platforms, engines, programs, artifacts, workloads, max_jobs, max_jobs_per_platform, out, label, skip_unavailable, repo, skip_recorded, run_label):
    """Write one JobSpec JSON per platform shard, plus a GitHub Actions matrix file."""
    from .jobs import available_platforms, plan_pods, recorded_cell_keys

    m: Matrix = obj["matrix"]
    st: Store = obj["store"]
    outp = Path(out)
    outp.mkdir(parents=True, exist_ok=True)
    plats = list(platforms) or None
    if skip_unavailable:
        ok, skipped = available_platforms(m, repo or os.environ.get("GITHUB_REPOSITORY", "pie-project/pie-evals"))
        plats = [p for p in (plats or list(m.platforms))] if plats else list(m.platforms)
        plats = [p for p in plats if p in ok]
        (outp / "skipped-platforms.json").write_text(json.dumps(skipped, indent=1))
        for pid, why in skipped.items():
            click.echo(f"skip platform {pid}: {why}", err=True)
    cells = m.expand()
    if programs:
        cells = [c for c in cells if c.program.id in programs]
    if artifacts:
        cells = [c for c in cells if c.artifact.id in artifacts]
    if workloads:
        cells = [c for c in cells if c.workload.id in workloads or str(c.workload.kind) == "control_aa"]
    if skip_recorded and pie_commit:
        done = recorded_cell_keys(st, Tier(tier), pie_commit, {e.id: e.pin for e in m.engines.values() if getattr(e, "pin", None)})
        before = len(cells)
        cells = [c for c in cells if c.cell_key not in done]
        click.echo(f"skip {before - len(cells)} cells already recorded at {pie_commit[:8]}", err=True)
    js = make_jobs(m, Tier(tier), pie_commit=pie_commit, store=st, platforms=plats, engines=list(engines) or None, cells=cells, label=label)
    if max_jobs_per_platform is not None:
        seen: dict[str, int] = {}
        kept = []
        for j in js:
            if seen.get(j.platform_id, 0) < max_jobs_per_platform:
                kept.append(j)
                seen[j.platform_id] = seen.get(j.platform_id, 0) + 1
        js = kept
    if max_jobs is not None:
        js = js[:max_jobs]
    gh = []
    for j in js:
        (outp / f"{j.job_id}.json").write_text(j.model_dump_json(indent=1))
        plat = m.platforms[j.platform_id]
        # a pod's runner carries the run's label too, so two runs on one GPU type never trade shards
        extra = [run_label] if run_label and plat.runpod_gpu_type else []
        gh.append({"job_id": j.job_id, "platform": j.platform_id, "pod": plat.pod or plat.id, "shard": j.shard, "labels": plat.runner_labels + extra, "os": plat.os, "runpod": bool(plat.runpod_gpu_type), "cells": len(j.cells), "est_minutes": round(j.est_minutes, 1)})
    pods = plan_pods(m, js)
    if run_label:
        for p in pods:
            p["labels"] = sorted(set(p["labels"]) | {run_label})
    (outp / "gh-matrix.json").write_text(json.dumps({"include": gh}))
    (outp / "pods.json").write_text(json.dumps({"include": pods}))
    (outp / "policy.json").write_text(json.dumps({"job_budget_minutes": m.job_budget_minutes, "kill_minutes": m.kill_minutes}))
    click.echo(json.dumps(gh, indent=1))
    for p in pods:
        click.echo(f"pod {p['pod']}: {len(p['jobs'])} jobs, {p['est_minutes']} est min, kill {p['kill_minutes']} min, labels {','.join(p['labels'])}", err=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"kill_minutes={m.kill_minutes}\nbench_timeout_minutes={int(m.kill_minutes) + 15}\njobs={len(js)}\n")  # workflow expressions cannot add
            f.write(f"pods={json.dumps({'include': pods})}\n")


@main.command("collect")
@click.option("--tier", type=click.Choice([t.value for t in Tier]), required=True)
@click.argument("node_out", nargs=-1, type=click.Path(exists=True))
@click.pass_obj
def collect(obj, tier, node_out):
    """Import node output directories (records.jsonl) into the store."""
    st: Store = obj["store"]
    problems = []
    for d in node_out:
        d = Path(d)
        run_id = (d / "run_id.txt").read_text().strip() if (d / "run_id.txt").exists() else d.name
        try:
            p = st.import_node_output(d, tier=Tier(tier), run_id=run_id)
        except Exception as e:
            problems.append(f"{d}: {e}")
            click.echo(f"{d}: IMPORT FAILED: {e}", err=True)
            continue
        click.echo(f"{d} -> {p if p else 'no records (node crashed before its first record)'}")
    if problems:
        sys.exit(1)


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


@main.command("dashboard")
@click.option("--out", type=click.Path(), default="site", show_default=True)
@click.option("--repo", default=None, help="owner/name of this repo, whose runners and collaborators the site shows (default: $GITHUB_REPOSITORY)")
@click.option("--pie-repo", default="pie-project/pie", show_default=True)
@click.pass_obj
def dashboard(obj, out, repo, pie_repo):
    """Render the pie evals site: pushes, machines and people."""
    repo = repo or os.environ.get("GITHUB_REPOSITORY", "pie-project/pie-evals")
    n = dash.render(obj["store"], obj["matrix"], Path(out), dash.runners(repo), repo=repo, pie_repo=pie_repo)
    click.echo(f"{n} pushes -> {out}/index.html")


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
@click.option("--platform", required=True, help="platform id, or a comma-separated fallback list tried in order (build pods: any GPU will do)")
@click.option("--repo", required=True, help="owner/name the runner registers with")
@click.option("--runner-pat", envvar="GH_RUNNER_PAT", default=None, help="PAT with Administration: read/write on --repo; minted into a registration token inside the pod")
@click.option("--runner-token", envvar="GH_RUNNER_TOKEN", default=None, help="pre-minted registration token (preferred: 1 h, registration-only); one of --runner-pat/--runner-token is required")
@click.option("--image", default=None, help="default: pieproject/runpod-ci-runner:latest")
@click.option("--image-version", default="latest")
@click.option("--network-volume-id", envvar="RUNPOD_NETWORK_VOLUME_ID", default=None)
@click.option("--kill-minutes", type=int, default=None, help="pod self-destruct; default = job budget × kill_factor")
@click.option("--cuda", "cuda_versions", multiple=True, default=["13.0"], show_default=True, help="allowed host CUDA versions (pie pins cudarc cuda-13000)")
@click.option("--debug", is_flag=True, help="serve the start log on the pod's :8080 proxy and hold a failed pod 10 min")
@click.option("--exec", "exec_script", default=None, help="run this bash script on the pod (same env as a job) instead of a runner, then terminate; volume maintenance")
@click.option("--wait-runner", type=int, default=0, help="seconds to wait for the pod's runner to register (needs GH_RUNNER_PAT); a pod that never registers is terminated and the next platform tried")
@click.option("--labels", default=None, help="comma-separated runner labels (default: the platform's); a pod hosting several platforms carries all of theirs")
@click.option("--idle-minutes", type=int, default=20, show_default=True, help="the pod terminates itself after this long without a job")
@click.option("--reuse", is_flag=True, help="if a live pod already carries every label, queue on it instead of renting another (needs GH_RUNNER_PAT)")
@click.pass_obj
def launch_pod(obj, platform, repo, runner_pat, runner_token, image, image_version, network_volume_id, kill_minutes, cuda_versions, debug, exec_script, wait_runner, labels, idle_minutes, reuse):
    from . import runpod

    m: Matrix = obj["matrix"]
    rp = m.runpod
    if not (runner_pat or runner_token or exec_script):
        raise click.UsageError("set GH_RUNNER_PAT or GH_RUNNER_TOKEN (the workflow saw GH_RUNNER_PAT empty: check the org secret's name and its repository access list)")
    h = None
    plat = None
    errors = []
    want = [x.strip() for x in labels.split(",") if x.strip()] if labels else None
    lab = None
    if reuse and runner_pat and not exec_script:
        try:
            runners = runpod.list_runners(repo, runner_pat)
        except Exception as e:
            runners = []
            click.echo(f"runner list unavailable ({str(e)[:80]}); launching", err=True)
        # the pod as planned first, then what a fallback pod would have seated
        for pid in [x.strip() for x in platform.split(",") if x.strip()]:
            p = m.platforms[pid]
            lab = [x for x in want if x not in m.platforms or m.platforms[x].count <= p.count] if want else p.runner_labels
            found = runpod.reusable_pod(lab, runners)
            if found:
                pod_id, have = found
                click.echo(f"reusing pod {pod_id} ({','.join(have)}): its runner carries every label {pid} needs", err=True)
                click.echo(pod_id)
                if os.environ.get("GITHUB_OUTPUT"):
                    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                        f.write(f"pod_id={pod_id}\nplatform={pid}\nlabels={','.join(lab)}\nreused=true\n")
                return
    for pid in [x.strip() for x in platform.split(",") if x.strip()]:
        plat = m.platforms[pid]
        # a fallback pod seats only the hosted platforms that fit on it
        lab = [x for x in want if x not in m.platforms or m.platforms[x].count <= plat.count] if want else None
        try:
            h = runpod.create_pod(plat, repo=repo, runner_pat=runner_pat, runner_token=runner_token, kill_minutes=kill_minutes or m.kill_minutes,
                                  image=image or runpod.DEFAULT_IMAGE, image_version=image_version, network_volume_id=network_volume_id,
                                  volumes=rp.get("volumes") or None, preferred_data_centers=rp.get("preferred_data_centers"),
                                  container_disk_gb=int(rp.get("container_disk_gb", 40)), cloud_type=str(rp.get("cloud_type", "SECURE")),
                                  allowed_cuda_versions=list(cuda_versions) or None, debug=debug, exec_script=exec_script,
                                  community_fallback=bool(rp.get("community_fallback", True)), log=lambda m_: click.echo(m_, err=True),
                                  labels=lab, idle_minutes=idle_minutes)
            click.echo(f"launched on {pid}", err=True)
            if wait_runner and runner_pat and not exec_script:
                if not runpod.wait_for_runner(h.id, repo, runner_pat, wait_runner, log=lambda m_: click.echo(m_, err=True)):
                    click.echo(f"pod {h.id} on {pid} never registered a runner within {wait_runner}s; terminating it", err=True)
                    try:
                        runpod.terminate_pod(h.id)
                    except RuntimeError as e:
                        click.echo(f"terminate {h.id}: {str(e)[:120]}", err=True)
                    errors.append(f"{pid}: runner not registered within {wait_runner}s")
                    h = None
                    continue
            break
        except RuntimeError as e:
            errors.append(f"{pid}: {str(e)[:120]}")
            click.echo(f"no pod for {pid}: {str(e)[:600]}", err=True)
    if h is None or plat is None:
        raise click.ClickException("no instance on any platform: " + "; ".join(errors))
    click.echo(h.id)
    if debug:
        click.echo(f"start log: https://{h.id}-8080.proxy.runpod.net/start.log", err=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"pod_id={h.id}\nplatform={plat.id}\nlabels={','.join(lab or plat.runner_labels)}\n")


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
@click.option("--max-age-hours", type=float, default=2.0, help="a pod this old whose runner is not busy is an orphan")
@click.option("--hard-max-age-hours", type=float, default=30.0, help="even a busy pod ends here: a configuration's whole queue fits well inside")
@click.option("--repo", default=None, help="owner/name whose runners say which pods are busy (needs GH_TOKEN); default: $GITHUB_REPOSITORY")
@click.option("--dry-run", is_flag=True)
def reap_pods(max_age_hours, hard_max_age_hours, repo, dry_run):
    from . import runpod

    keep: set[str] = set()
    try:
        keep = runpod.busy_pods(runpod.list_runners(repo or os.environ.get("GITHUB_REPOSITORY", "pie-project/pie-evals")))
    except Exception as e:  # no token: age alone decides, as before
        click.echo(f"runner list unavailable ({str(e)[:80]}); busy pods are not spared", err=True)
    click.echo(json.dumps(runpod.reap(int(max_age_hours * 3600), dry_run=dry_run, keep=keep, hard_max_age_s=int(hard_max_age_hours * 3600))))


if __name__ == "__main__":
    main()
