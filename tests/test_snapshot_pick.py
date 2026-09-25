from pathlib import Path

from pie_evals.node.snapshots import snapshot_dir_if_present
from pie_evals.schema.cell import ArtifactSpec


def _art(**over) -> ArtifactSpec:
    base = dict(id="qwen3.6-35b-a3b-mlx4", base_model="mlx-community/Qwen3.6-35B-A3B-4bit", family="qwen3_6", scheme="affine_u4_g64", source_format="mlx")
    base.update(over)
    return ArtifactSpec(**base)


def test_a_full_row_never_picks_the_miniature_built_beside_it(tmp_path: Path):
    snaps = tmp_path / "models--mlx-community--Qwen3.6-35B-A3B-4bit" / "snapshots"
    rev = "38740b847e4cb78f352aba30aa41c76e08e6eb46"
    for d in (rev, "mini-l0-4-e16"):
        (snaps / d).mkdir(parents=True)
        (snaps / d / "config.json").write_text("{}")
    assert snapshot_dir_if_present(_art(), tmp_path) == snaps / rev
    # a pinned revision still wins, a cache holding only the mini yields nothing for a full row
    assert snapshot_dir_if_present(_art(revision=rev), tmp_path) == snaps / rev
    (snaps / rev / "config.json").unlink()
    assert snapshot_dir_if_present(_art(), tmp_path) is None
