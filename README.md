# pie-evals

Benchmark & evaluation framework for [pie](https://github.com/pie-project/pie):
performance against vLLM / SGLang / llama.cpp / mlx-lm on every supported
platform, accuracy preservation against a same-weights reference, and a
coverage matrix in which nothing goes missing silently.

Read `docs/design.md` first.

## Layout

- `matrix/` — what exists: engines, platforms, models (incl. miniatures), workloads, inferlets, modes, support declarations, tier suites.
- `src/pie_evals/node/` — runs on the machine under test: `pie-evals-node run --job <spec.json>`.
- `src/pie_evals/orchestrate/` — `pie-evals expand | check | jobs | collect | report | watch-baselines | launch-pod | reap-pods`.
- `store/records/` — parquet results, append-only, committed. `reports/` — rendered coverage / regressions / baselines.
- `infra/` — RunPod runner image and Mac runner setup. `.github/workflows/` — tiers and bookkeeping.

## Quick start

```sh
uv venv && uv pip install -e ".[dev,orchestrate]"
.venv/bin/pytest -q
.venv/bin/pie-evals expand                      # matrix summary + budgets
.venv/bin/pie-evals jobs --tier smoke --pie-commit <sha> --platform l40s-x1 --out jobs
PIE_ROOT=/root/pie .venv/bin/pie-evals-node run --job jobs/<job>.json --out out/<job>
.venv/bin/pie-evals collect --tier smoke out/<job> && .venv/bin/pie-evals report --tier smoke
```

Node prerequisites: the pie checkout (built at the pinned commit by the node), the checkpoints in the HF cache (`resolve_local_model` refuses to download), baseline venvs at the pins in `matrix/engines.yaml` (`VLLM_PY`, `SGLANG_PY`, `LLAMA_SERVER_BIN`, `MLX_PY`).
