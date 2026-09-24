"""``pie-evals-node`` — what runs on the machine under test."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import click

from pie_evals.schema import JobSpec


@click.group()
def main():
    pass


def mask_gpus(job: JobSpec, env: dict | None = None) -> str | None:
    """A pod hosts every platform of its GPU type, so an x1 job on an x2 pod sees
    both cards: mask CUDA to the platform's count (the first devices). Set once,
    before any engine starts, so every subprocess inherits it; an explicit
    CUDA_VISIBLE_DEVICES from the runner is left alone."""
    import shutil
    import subprocess

    env = os.environ if env is None else env
    if env.get("CUDA_VISIBLE_DEVICES") or not job.cells or not shutil.which("nvidia-smi"):
        return None
    count = job.cells[0].platform.count
    try:
        visible = len([ln for ln in subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True, timeout=20).stdout.splitlines() if ln.startswith("GPU ")])
    except (OSError, subprocess.SubprocessError):
        return None
    if visible <= count:
        return None
    env["CUDA_VISIBLE_DEVICES"] = ",".join(str(i) for i in range(count))
    click.echo(f"{visible} GPUs visible, platform {job.platform_id} uses {count}: CUDA_VISIBLE_DEVICES={env['CUDA_VISIBLE_DEVICES']}", err=True)
    return env["CUDA_VISIBLE_DEVICES"]


@main.command("run")
@click.option("--job", "job_path", type=click.Path(exists=True), required=True)
@click.option("--pie-root", type=click.Path(exists=True), default=os.environ.get("PIE_ROOT", "/root/pie"))
@click.option("--out", type=click.Path(), default="out")
@click.option("--hf-cache", type=click.Path(), default=None)
@click.option("--no-build", is_flag=True, help="use the pie binary already in target/release")
@click.option("--only", multiple=True, help="restrict to cells whose key contains this substring")
@click.option("--download", is_flag=True, help="fetch missing full checkpoints here (default: no — `prepare` does that once before the fan-out)")
def run(job_path, pie_root, out, hf_cache, no_build, only, download):
    """Execute a JobSpec and write records.jsonl under --out."""
    from .runner import NodeRunner

    job = JobSpec.model_validate_json(Path(job_path).read_text())
    mask_gpus(job)
    if only:
        job = job.model_copy(update={"cells": [c for c in job.cells if any(s in c.cell_key for s in only)]})
    runner = NodeRunner(job, pie_root=Path(pie_root), out_dir=Path(out), hf_cache=Path(hf_cache) if hf_cache else None, build=not no_build, download=download)
    recs = runner.run()
    by = {}
    for r in recs:
        by[str(r.status)] = by.get(str(r.status), 0) + 1
    click.echo(json.dumps({"run_id": runner.run_id, "records": len(recs), "by_status": by}))


@main.command("build")
@click.option("--pie-commit", required=True)
@click.option("--features", default="cuda", show_default=True, help="comma-separated pie cargo features")
@click.option("--pie-root", type=click.Path(), default=os.environ.get("PIE_ROOT", "/root/pie"))
@click.option("--mirror", type=click.Path(), default=os.environ.get("PIE_MIRROR"), help="bare mirror on the shared volume; updated, then used as clone source")
@click.option("--target-dir", type=click.Path(), default=os.environ.get("CARGO_TARGET_DIR"))
@click.option("--force", is_flag=True)
def build_cmd(pie_commit, features, pie_root, mirror, target_dir, force):
    """Build pie at a commit and cache the artifacts (binary, engine wheel, bench wasm) under $PIE_EVALS_CACHE/builds.
    The tier workflow runs this once before the bench fan-out."""
    from . import build as pb

    feats = [f for f in features.split(",") if f]
    if mirror:
        pb.update_mirror(Path(mirror))
    pb.ensure_checkout(Path(pie_root), pie_commit, mirror=Path(mirror) if mirror else None)
    if pb.is_cached(pie_commit, feats) and not force:
        click.echo(f"cache hit: {pb.cache_dir(pie_commit, feats)}")
        return
    out = pb.build(Path(pie_root), pie_commit, feats, target_dir=Path(target_dir) if target_dir else None, python=os.environ.get("PIE_PY", "python3"))
    click.echo(str(out))


@main.command("prepare")
@click.option("--tier", type=click.Choice(["smoke", "nightly", "weekly", "targeted"]), required=True)
@click.option("--matrix", "matrix_dir", default="matrix")
@click.option("--platform", "platforms", multiple=True, help="restrict to artifacts these platforms run (default: all of the tier)")
@click.option("--engine", "engines_f", multiple=True)
@click.option("--program", "programs_f", multiple=True)
@click.option("--pie-root", type=click.Path(), default=os.environ.get("PIE_ROOT", "/root/pie"))
@click.option("--pie-commit", default=None, help="import quantized checkpoints as .zt artifacts for this commit (needs the built pie binary)")
@click.option("--hf-cache", type=click.Path(), default=None)
def prepare_cmd(tier, matrix_dir, platforms, engines_f, programs_f, pie_root, pie_commit, hf_cache):
    """Fetch every checkpoint a tier needs (downloads + miniatures) so bench pods find them on the volume.
    Failures are reported per artifact and never abort the rest; exit 1 if any failed."""
    from pie_evals.orchestrate.matrix import Matrix
    from pie_evals.schema import Tier

    from .snapshots import ensure_snapshot, hf_cache_dir

    m = Matrix.load(matrix_dir)
    cells = m.runnable(Tier(tier))
    if platforms:
        cells = [c for c in cells if c.platform.id in platforms]
    if engines_f:
        cells = [c for c in cells if str(c.engine) in engines_f]
    if programs_f:
        cells = [c for c in cells if c.program.id in programs_f]
    arts = {c.artifact.id: c.artifact for c in cells}
    cache = Path(hf_cache) if hf_cache else hf_cache_dir()
    failed = {}
    from .build import bench_python
    from .importer import ensure_artifact, needs_import

    pie_bin = Path(pie_root) / "target/release/pie"
    shrink_py = os.environ.get("PIE_PY") or str(bench_python(log=lambda m_: click.echo(m_, err=True)))  # shrink_checkpoint needs numpy
    for aid, art in sorted(arts.items()):
        try:
            p = ensure_snapshot(art, cache, pie_root=Path(pie_root), python=shrink_py, log=lambda m_: click.echo(m_, err=True))
            if pie_commit and needs_import(art) and pie_bin.exists():
                p = ensure_artifact(art, p, pie_bin, pie_commit, log=lambda m_: click.echo(m_, err=True))
            click.echo(f"ok    {aid}: {p}")
        except Exception as e:
            failed[aid] = str(e).strip().splitlines()[-1][:200] if str(e).strip() else repr(e)
            click.echo(f"FAIL  {aid}: {failed[aid]}", err=True)
    from .baselines import SPECS, ensure_baseline

    engines = {str(c.engine) for c in cells}
    for e in sorted(engines & set(SPECS)):
        pin = m.engines[e].pin
        try:
            ensure_baseline(e, pin, log=lambda m_: click.echo(m_, err=True))
            click.echo(f"ok    baseline {e}=={pin}")
        except Exception as ex:
            failed[f"baseline:{e}"] = str(ex)[:200]
            click.echo(f"FAIL  baseline {e}=={pin}: {failed[f'baseline:{e}']}", err=True)
    click.echo(json.dumps({"prepared": len(arts) - len(failed), "failed": failed}))
    sys.exit(1 if failed else 0)


@main.command("preflight")
def preflight_cmd():
    """Print the hardware fingerprint and machine state checks."""
    from . import preflight as pf
    from . import provenance as prov

    click.echo(json.dumps({"fingerprint": prov.hardware_fingerprint(), "versions": prov.versions(), "state": pf.Preflight().before_job(None)}, indent=1, default=str))


@main.command("miniature")
@click.option("--artifact", required=True, help="artifact id from matrix/models.yaml")
@click.option("--matrix", "matrix_dir", default="matrix")
@click.option("--pie-root", type=click.Path(exists=True), default=os.environ.get("PIE_ROOT", "/root/pie"))
@click.option("--hf-cache", type=click.Path(), default=None)
def miniature_cmd(artifact, matrix_dir, pie_root, hf_cache):
    """Build (or find) a miniature checkpoint in the HF cache."""
    from pie_evals.orchestrate.matrix import Matrix

    from .miniature import ensure_miniature

    m = Matrix.load(matrix_dir)
    art = m.artifacts[artifact]
    cache = Path(hf_cache or os.environ.get("HF_HUB_CACHE") or Path.home() / ".cache/huggingface/hub")
    click.echo(str(ensure_miniature(art, Path(pie_root), cache, python=os.environ.get("PIE_PY", "python3"))))


if __name__ == "__main__":
    main()
