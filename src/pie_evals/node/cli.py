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
@click.option("--tier", type=click.Choice(["smoke", "nightly", "weekly"]), required=True)
@click.option("--matrix", "matrix_dir", default="matrix")
@click.option("--platform", "platforms", multiple=True, help="restrict to artifacts these platforms run (default: all of the tier)")
@click.option("--pie-root", type=click.Path(), default=os.environ.get("PIE_ROOT", "/root/pie"))
@click.option("--hf-cache", type=click.Path(), default=None)
def prepare_cmd(tier, matrix_dir, platforms, pie_root, hf_cache):
    """Fetch every checkpoint a tier needs (downloads + miniatures) so bench pods find them on the volume.
    Failures are reported per artifact and never abort the rest; exit 1 if any failed."""
    from pie_evals.orchestrate.matrix import Matrix
    from pie_evals.schema import Tier

    from .snapshots import ensure_snapshot, hf_cache_dir

    m = Matrix.load(matrix_dir)
    cells = m.runnable(Tier(tier))
    if platforms:
        cells = [c for c in cells if c.platform.id in platforms]
    arts = {c.artifact.id: c.artifact for c in cells}
    cache = Path(hf_cache) if hf_cache else hf_cache_dir()
    failed = {}
    for aid, art in sorted(arts.items()):
        try:
            p = ensure_snapshot(art, cache, pie_root=Path(pie_root), python=os.environ.get("PIE_PY", "python3"), log=lambda m_: click.echo(m_, err=True))
            click.echo(f"ok    {aid}: {p}")
        except Exception as e:
            failed[aid] = str(e).strip().splitlines()[-1][:200] if str(e).strip() else repr(e)
            click.echo(f"FAIL  {aid}: {failed[aid]}", err=True)
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
