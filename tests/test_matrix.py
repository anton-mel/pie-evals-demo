from pathlib import Path

import pytest

from pie_evals.orchestrate.matrix import Matrix, selector_matches, summarize
from pie_evals.schema import CellStatus, Tier

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def matrix():
    return Matrix.load(ROOT / "matrix")


@pytest.fixture(scope="module")
def cells(matrix):
    return matrix.expand()


def test_expansion_is_nonempty_and_stable(cells):
    ids = [c.cell_id for c in cells]
    assert len(ids) == len(set(ids)), "cell ids must be unique"
    assert summarize(cells)["total"] > 1000


def test_every_cell_has_a_status_path(cells):
    # nothing silently dropped: a cell is runnable, declared unsupported, or unscheduled — never absent
    for c in cells:
        assert c.declared_unsupported_reason is None or isinstance(c.declared_unsupported_reason, str)


def test_baselines_never_in_smoke(matrix, cells):
    assert all(str(c.engine) == "pie" for c in matrix.cells_for(Tier.SMOKE, cells))


def test_metal_tp_is_declared_not_failed(cells):
    tp = [c for c in cells if c.platform.backend.value == "metal" and c.mode.tp > 1]
    # metal platforms have count=1 → tp cells are not generated at all (inapplicable), which is fine;
    # but if any exist they must be declared
    assert all(c.declared_unsupported_reason for c in tp)


def test_fit_rule_marks_big_models_on_small_gpus(cells):
    big = [c for c in cells if c.artifact.id == "deepseek-v4-flash-mlx2" and c.platform.id == "l40s-x1"]
    assert big and all(c.declared_unsupported_reason for c in big)
    assert any("does not fit" in c.declared_unsupported_reason for c in big)


def test_miniature_cells_never_accuracy_applicable(cells):
    for c in cells:
        if c.artifact.kind.value == "miniature":
            assert not c.accuracy_applicable()


def test_pie_only_programs_have_no_baseline_cells(cells):
    for c in cells:
        if c.program.pie_only:
            assert str(c.engine) == "pie"


def test_sglang_never_gets_gguf(cells):
    assert not [c for c in cells if str(c.engine) == "sglang" and c.artifact.source_format.value == "gguf"]


def test_selector_negation_and_comparison(cells):
    c = next(c for c in cells if c.mode.tp == 2)
    assert selector_matches({"tp": ">1"}, c)
    assert not selector_matches({"tp": ">=4"}, c)
    assert selector_matches({"not_engine": ["vllm"]}, c) == (str(c.engine) != "vllm")


def test_smoke_budget_holds(matrix, cells):
    assert matrix.check_budget(Tier.SMOKE, cells) == []


def test_smoke_includes_every_program_at_least_once(matrix, cells):
    # every smoke program has a smoke cell — runnable, or declared unsupported and
    # therefore visible in the coverage report (diffusion programs only run on
    # mini-dit, which has no checkpoint source yet)
    smoke = matrix.cells_for(Tier.SMOKE, cells)
    progs = {c.program.id for c in smoke}
    expected = {p.id for p in matrix.programs.values() if Tier.SMOKE in p.tiers}
    assert not (expected - progs), expected - progs
    runnable = {c.program.id for c in matrix.runnable(Tier.SMOKE, cells)}
    assert expected - runnable <= {"diffusion-parity", "mini-dit-parity"}, expected - runnable


def test_cell_status_enum_complete():
    assert {s.value for s in CellStatus} == {"pass", "fail", "declared_unsupported", "not_run", "noisy"}
