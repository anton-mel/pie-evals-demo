"""``pie-evals-node`` — what runs on the machine under test."""

from __future__ import annotations

import json
import os
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
def run(job_path, pie_root, out, hf_cache, no_build, only):
    """Execute a JobSpec and write records.jsonl under --out."""
    from .runner import NodeRunner

    job = JobSpec.model_validate_json(Path(job_path).read_text())
    if only:
        job = job.model_copy(update={"cells": [c for c in job.cells if any(s in c.cell_key for s in only)]})
    runner = NodeRunner(job, pie_root=Path(pie_root), out_dir=Path(out), hf_cache=Path(hf_cache) if hf_cache else None, build=not no_build)
    recs = runner.run()
    by = {}
    for r in recs:
        by[str(r.status)] = by.get(str(r.status), 0) + 1
    click.echo(json.dumps({"run_id": runner.run_id, "records": len(recs), "by_status": by}))


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
