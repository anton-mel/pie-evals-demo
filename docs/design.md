# pie-evals — design

Benchmark & evaluation framework for pie. Two goals, one structure:

1. **Performance lead, everywhere.** Against vLLM / SGLang / llama.cpp / mlx-lm,
   on every supported platform, across workload shapes, model sizes and
   architectures, quantization schemes and tensor-parallel degrees.
2. **Accuracy preserved.** Token-level parity with a reference and unchanged
   evaluation-benchmark scores.

And as a by-product: errors, missing coverage (a platform where something
does not run, a regression) are surfaced instead of discovered by hand.

The wiki pages this design is built on: `pie-bench.md` (the L40S three-way
protocol and its two discarded rounds), `macos-bench.md` (the Apple Silicon
protocol, what invalidates a run), `tp-verification.md` (first-divergence +
logit-gap adjudication), `alto/streaming-verification-l40s.md`,
`issues/sep-4.md` (six retracted findings), `plex/` (workload survey).

---

## 1. The cell

```
cell = (engine@version, platform, artifact, workload, program, mode)
```

| component | what it is | declared in |
|---|---|---|
| engine | pie, vllm, sglang, llamacpp, mlxlm | `matrix/engines.yaml` |
| platform | hardware + backend: L40S×1/×2, RTX PRO 6000×4, H100 SXM×4, M1 Max, M4 Pro … | `matrix/platforms.yaml` |
| artifact | base model × quant scheme × source format × kind(full \| miniature) | `matrix/models.yaml` |
| workload | shape: single stream, concurrency sweep, long context, prefix-shared, length mix, KV oversubscription, trace replay, control A/A | `matrix/workloads.yaml` |
| program | the inferlet: `text-completion-bench` is the serving path; every other inferlet is its own ETA program and its own cell | `matrix/programs.yaml` |
| mode | tp degree, speculative mode | `matrix/modes.yaml` |

Every measurement is a `Record` attached to one cell (`schema/record.py`).
A cell is always in exactly one status:

| status | meaning |
|---|---|
| `pass` | ran, numbers read, gates passed |
| `fail` | ran or tried to; classified `ErrorClass` (load_fail, crash, hang, oom, doesnt_fit, gate_fail, harness_invalid, input_mismatch) |
| `declared_unsupported` | listed in `matrix/support.yaml` (or fails the fit rule); shown, not run |
| `not_run` | expected to work, never scheduled or never reached |
| `noisy` | ran, but the harness refuses to read the number (CoV over policy, control A/A disagreed, thermal event, GPU not drained) |

The coverage report is the list of cells whose status is not `pass` and not
`declared_unsupported`. The wiki's "real LLMs at tp>1 are blocked by
`register_program`" is therefore a `fail`, not an unsupported — the first
run of the framework is expected to show it.

### Expansion

`orchestrate/matrix.py` takes the product of the six components and prunes
in three steps: *inapplicable* combinations are not cells (an engine that
cannot load the format, TP on a one-device platform, a pie-only program on a
baseline); *declared unsupported* combinations stay as cells; tiers are the
intersection of each component's `tiers`, adjusted by `matrix/suites.yaml`
`include`/`exclude` selectors (`not_<field>` negates, `tp: ">1"` compares).
The expander enforces a per-platform time budget per tier from
`est_minutes`; `pie-evals check` fails CI when a tier grows past it.

Current size (from `pie-evals expand`): ~21.7k cells, ~3.8k declared
unsupported, ~650 in smoke, ~12.8k in nightly.

---

## 2. Performance

**Same client.** Every adapter drives the bench scripts in the pinned pie
checkout (`benches/pie_bench.py`, `vllm_bench.py`, `sglang_bench.py`,
`llamacpp_bench.py`, `mlx_bench.py`), which share `benches/common.py`: one
prompt construction, one arrival schedule, one JSON envelope. The adapter
builds argv, runs under a timeout, classifies failure, lifts the JSON into
`PerfMetrics`. (`node/engines/base.py`.)

**Input parity is checked, not assumed.** Shapes are defined in tokens and
realised as seeded word blocks (`node/workloads/synthetic.py`); after a run
the prompt/output token totals every engine reported are compared and a
mismatch marks the cell `input_mismatch` — the tok/s column is then not a
comparison. (Follow-up in pie: `--prompt-tokens-file` on `common.py`, so
shapes are pre-tokenized once.)

**Protocol, as code.**
- GPU drained between engine processes (`preflight.await_free_gpu`; vLLM's
  `EngineCore` child is looked for by name).
- One model per process; workloads and programs interleaved inside it; a
  fresh process per model.
- macOS: AC power, Low Power Mode off, thermal log compared before/after
  each model, display count recorded; any change invalidates the model's
  cells (`preflight.Preflight.after_model`).
- Baseline knobs that silently change the comparison are recipe entries
  with a rationale (`node/engines/recipes/*.yaml`): SGLang's
  `--sglang-cuda-graph-max-bs <concurrency>` (the wiki's 4,642 → 14,042
  tok/s), vLLM's `max-num-seqs`, llama.cpp's `-fa on`, mlx-lm's readback
  barrier. Every baseline runs its **competitive** recipe; a `default`
  cell is kept nightly so the report can say what tuning bought.
- **Control A/A**: the first cell of every process is the engine against
  itself; if the two arms disagree beyond policy the rest of the process is
  `harness_invalid`. Six of the wiki's retracted findings were the harness.

**Statistics.** Median of rounds; CoV recorded; a cell whose rounds spread
more than `cov_noisy_threshold` (2%) is `noisy`. Regression detection is
noise-aware: the threshold is the cell's own historical CoV × σ (default 3),
never a fixed percentage (`node/metrics/stats.py`). **Adaptive repetition**
(smoke): one round; only a value outside the historical band triggers two
confirmation rounds.

**Metrics.** decode tok/s (single-stream headline), aggregate output tok/s
(concurrency headline), prefill tok/s, TTFT / ITL / latency p50 & p99,
resident GiB (LM-only), load time, and `ms_per_token_per_layer` so miniature
cells can be eyeballed against full ones. pie's internal counters (device
idle %, host µs per step, guest turnaround, ETA compile) ride along in
`counters` — they are lower-noise than tok/s and are where an ETA regression
shows first.

---

## 3. Accuracy

Three tiers; an upper tier only runs when the lower passed. Miniature
artifacts are `skipped_miniature` by construction and can never `pass`.

| tier | what | reference | data |
|---|---|---|---|
| **T0** token parity | greedy, `ignore_eos`, 8 fixed prompts (incl. a 1k-token one); first divergence; every divergence teacher-forced and adjudicated by logit gap: ≤ 1 bf16 ulp (0.125) with both candidates top-2 is benign, else FAIL | HF transformers on Linux, mlx-lm on macOS, on the **same** weights | `node/accuracy/prompts.py` |
| **T1** distribution | mean KL, top-k agreement, perplexity vs reference | same | wikitext-2 slice + mixed corpus |
| **T2** tasks | GSM8K, HumanEval, IFEval, MATH-500 (generation); MMLU/ARC/HellaSwag (loglikelihood) | same quant weights, same harness, same sample; bootstrap CI on the difference | stratified 200/nightly, full/weekly |

Rules:
- The reference is the **same quantized weights** on a reference engine,
  never a published number. `gate.SAME_WEIGHTS_REFERENCE` maps scheme →
  reference; a scheme with no same-weights reference uses a declared
  *degradation budget* vs the bf16 artifact (`ArtifactSpec.degradation_budget`).
- **Cross-backend parity** is the cheapest strong gate: the same `.zt` on
  CUDA / Metal / Vulkan / wgpu must agree token-for-token (the wiki's Metal
  rounding defect was found exactly this way, with no external reference).
- The reference tokenizes the same rendering as `benches/common.py`
  (`gate.render_like_bench`); if the engine's reported prompt-token count
  differs from the reference's, the gate is `skipped_no_reference` with the
  detail — a template difference must never be reported as a model failure.
- The quant-block census (`provenance.quant_block_hash`) hashes the **whole**
  quantization block including per-tensor overrides: the router-at-8-bit
  defect that produced wrong tokens for a week came from reading only the
  top-level entry.

**Blocked:** per-token logprobs. `text-completion-bench` returns token ids,
text and timing only; logits are a trace-time intrinsic inside the ETA
program. T1 and loglikelihood T2 need a `logprob-probe` inferlet that
gathers the chosen token's logprob in-graph and returns it through a channel
(see `tests/inferlets/entropy-adaptive-temperature` for the pattern). Until
it exists T2 is generation-only.

---

## 4. Programs (inferlets) as a coverage axis

An ETA regression is independent of model and hardware: the compiler
lowers a different prologue/epilogue and one inferlet gets slower on the
same GPU. So `program` is its own axis. Categories in `programs.yaml`:
serving (`text-completion-bench`, `prefill-rows`, `prefix-tree-kv-cache`),
speculative (dflash, mtp, cacheback/ngram, eagle — gate = acceptance rate),
kv_policy (h2o, snapkv, snapkv-eviction, quest — gate = token parity after
eviction), adapter (lora-probe, CFG), diffusion (parity gates = cosine ≥
0.9999). In smoke each non-serving program runs on exactly one
representative shape; nightly runs its full list. Baseline cells exist only
where a comparable feature exists (`baseline_equivalents`); otherwise the
baseline is pie's own history.

---

## 5. Miniatures

Big architectures are benchmarked cheaply as *miniatures* built by pie's
`benches/shrink_checkpoint.py`: width dimensions kept exactly (every kernel
sees production shapes), a handful of source layers chosen to cover the
family's per-layer pattern in whole periods, the first N routed experts,
optional repeat. The result is a real checkpoint that loads unmodified in
pie and vLLM, placed in the HF cache as a snapshot named by the recipe tag
(`node/miniature.py`).

What is preserved: per-layer kernel shapes, TP communication pattern, ETA
program structure — so per-layer time and ETA regressions are valid.
What is not: memory footprint, so high-concurrency throughput is
over-estimated. Hence: accuracy is always skipped, `ms_per_token_per_layer`
is recorded, regression comparison is only against the same recipe hash,
and the report never lines a miniature up against a full cell. Miniatures
are what make TP coverage cheap: an 8-layer DSV4 on 2×L40S exercises every
sharding code path per commit.

---

## 6. Quantization and TP

Quantization is part of the artifact (scheme × kv dtype × source format);
pie carries it in the SKU name (`ArtifactSpec.pie_sku`). The (scheme × GPU
generation) table is where `declared_unsupported` and `fail` must be kept
apart (FP4 native only on Blackwell; MXFP4 on Ada takes the dequant path
that produced the gpt-oss metadata bug). Each scheme has one *home*
baseline: bf16/fp8 → vLLM & SGLang, GGUF → llama.cpp, mlx → mlx-lm.

TP is a mode (1/2/4/8) × interconnect (PCIe vs NVLink) × NCCL version. All
TP cells run under a timeout because a rank that throws leaves its peers
in NCCL forever — a hang is only ever observed as a timeout. Recorded per
cell: scaling efficiency (tpN ÷ N×tp1) and latency speedup; the only
absolute expectation is the cell's own history. `NCCL_*` env is recorded and
applied identically to pie and baselines.

Product coverage by tier: smoke = family miniature × {bf16, one 4-bit} ×
tp2 on CUDA; nightly = small models × all schemes × tp{1,2,4}; weekly = big
models × main schemes × tp4/8 on NVLink.

---

## 7. Datasets

Performance: synthetic pre-tokenized shapes (seeded) for everything fast;
trace replay (Azure LLM 2024, BurstGPT v2, Mooncake) weekly, open-loop with
arrivals honoured — the only honest way to read TTFT/ITL p99. Prefix
sharing is synthetic (shared system block + N variants). Agentic shapes are
synthetic until SWE-agent trajectory replay lands (the plex survey found no
public source with both arrivals and a workflow DAG).

Accuracy: T0 fixed prompts; T1 wikitext-2 + mixed corpus; T2 as in §3, with
stratified seeded subsets. Dataset hashes go into provenance.

---

## 8. Tiers and speed

| tier | trigger | what | fan-out cap |
|---|---|---|---|
| smoke | every pie commit | pie only, vs its own history; small real models + miniatures; ~10 shapes; every program once; tp2 on the 2-GPU platform | ≤ 2 jobs per platform |
| targeted | pie main commits of people who signed in to the site and selected models (`pie-eval.yml`, sent by pie's `evals.yml`), and manual runs from the site | pie only on the Macs; the models and Macs are the author's setup (`users/<login>.json`) or an `Evals:` line in the commit message; nobody runs by default; stored and shown on the site (`pages.yml`) | one job per Mac per model group |
| nightly | cron | subset of full; baselines at competitive + default recipes; all schemes; tp1/2/4 | ≤ 48 jobs per platform |
| weekly | cron | everything: big models, NVLink TP, replay traces, full T2 | ≤ 120 jobs per platform |

**Time policy (every tier).** Every job is ~60 min of estimated work
(`job_budget_minutes` in `matrix/suites.yaml`): the expander bin-packs a
platform's cells into shards, keeping a process group (one loaded model)
whole unless the group alone exceeds the budget, in which case it is split
and later pieces run without the A/A control. One job = one pod (or one Mac
slot); nightly on one GPU type is therefore ~40 pods in parallel rather
than one 36-hour pod, at the same GPU-minutes. A job that runs past
budget × `kill_factor` (1.5 → 90 min) is force-killed at three layers:

1. the node runner's watchdog — stops starting cells at the soft budget,
   records every unreached cell as `not_run` with the reason, and at the
   hard deadline kills its process group and exits 124;
2. the workflow's `timeout-minutes` (= kill minutes), whose teardown job
   terminates the pod;
3. the pod's own self-destruct timer, started by the startup script, which
   terminates the pod through the RunPod API even if GitHub never reaches it.

An hourly `reap` workflow terminates any pie-evals pod older than 2 h.
Multi-GPU platforms only ever run `tp>1` (tp1 is the single-GPU platform's
job; tp2 the 2-GPU platform's), which is what keeps the fan-out under the caps.

Speed levers in smoke: one process per model with all shapes inside it,
short outputs (64–128 tokens), adaptive repetition, internal counters as
the first regression signal, baselines excluded, pie builds cached by
(commit, features) on the network volume, warm pod during working hours.
**Escalation**: a confirmed smoke regression in a family promotes that
family's nightly cells into the next nightly run (`suites.yaml`).
**Calibration**: `reports/calibration.md` compares `est_minutes` with
recorded durations; the budgets are provisional until the first runs.

---

## 9. Where things run

Two halves, one repo, decoupled by a CLI boundary:

```
node/         runs on the machine under test. Input: one JobSpec JSON. Output: records.jsonl + logs.
orchestrate/  expand-matrix → jobs, launch-pod, collect, report, watch-baselines. CLIs, no daemon.
```

`node/` does not know about GitHub, RunPod or queues. Today the
orchestrator is **GitHub Actions**; every node is a **self-hosted runner**
with only outbound connectivity:

- Macs are resident runners (`infra/mac/setup-runner.sh`), one runner per
  machine, labels = platform id.
- RunPod pods are ephemeral runners on **`pieproject/runpod-ci-runner`**
  (github.com/pie-project/runpod-ci-runner — the image pie's own CUDA CI
  uses: CUDA 13 runtime + NVRTC + NCCL, build tools, uv, actions-runner).
  `pie-evals launch-pod` creates the pod through the RunPod REST API with a
  start command that mints a registration token in-pod from `GH_RUNNER_PAT`
  (as the image's own `runner.sh` does), registers an *ephemeral* runner
  with the platform's labels, serves one job and terminates the pod. Pods
  are pinned to the **network volume's data center** and mount it at
  `/workspace` with the image's layout (`.cargo`, `.rustup`, `.pie`, `.hf`,
  `.uv`). Two things are pod-local because N pods share the volume: the pie
  work tree (`/tmp/pie`, cloned from a bare mirror `/workspace/pie.git`) and
  the cargo target (`/tmp/target`). **Build once:** the tier workflow's
  `build` job builds pie at the pinned commit on one pod and caches the
  binary, the embedded-engine wheel and the bench wasm under
  `/workspace/pie-evals-cache/builds/<commit>-cuda`; bench pods restore
  from there. pie JIT-compiles its CUDA kernels with NVRTC, so one CUDA
  build serves every NVIDIA platform. Pods are requested with
  `allowedCudaVersions` 13.x because pie pins `cudarc cuda-13000`; teardown
  is `if: always()` and `reap.yml` kills orphans hourly.
  `platforms.yaml` covers L40S ×1/×2, RTX 4090, RTX 5090, L4, A40, A100
  PCIe/SXM ×2, H100 PCIe/SXM ×4, RTX PRO 6000 ×4; `pie-evals
  validate-platforms` checks every `runpod_gpu_type` against the live GPU
  list before anything launches. `runpod-check.yml` is the cheap first run:
  one pod on a stock image, preflight only, ~10 GPU-minutes.
- Bookkeeping is git: node outputs come back as job artifacts, `collect`
  lifts them into `store/records/<tier>/<month>/<run>.parquet` and renders
  `reports/`; both are committed. Provenance is mandatory — a record that
  cannot say what it measured is refused by the store.
- Baseline freshness: `watch-baselines` checks PyPI/GitHub against the pins
  in `engines.yaml`; a newer release re-runs baseline cells only (their
  results depend on engine version, not pie commit, and are cached).

When the decision loop (adaptive rounds, noisy-pod reassignment, bisect,
priority) outgrows workflow steps, a small resident coordinator calls the
same CLIs. Nothing in `node/` changes.

**Pinned pie.** Jobs carry `pie_commit`; the node checks it out and builds
with the platform's feature (`cuda|metal|vulkan|wgpu`), cached by commit —
which is also what makes automated bisect possible later.

---

## 10. Repository layout

```
matrix/           declarations: engines, platforms, models, workloads, programs, modes, support, suites
src/pie_evals/
  schema/         Cell, JobSpec, Record (+ parquet schema)
  node/           runner, engines/ (adapters + recipes), workloads/, metrics/, accuracy/, miniature, preflight, provenance
  orchestrate/    matrix, jobs, store, report, runpod, baselines, cli
store/records/    parquet, append-only, committed
reports/          rendered markdown/json, committed
infra/            RunPod runner image, Mac runner setup
.github/workflows tier.yml (reusable), smoke/nightly/weekly, collect, reap, ci
```

---

## 11a. Findings from the RunPod campaign (2026-09-23)

Everything below was learned from real pods; each item is now code.

**Stock is the scarce resource.** Secure-cloud stock for a given GPU type
in a given data center is momentary; "Low" often means the next create
fails with "no instances currently available". A network volume binds to
one data center, so the launcher tries: the preferred DC with a volume →
any DC with stock, unpinned and without the volume (cold caches) → the
community cloud. The build/prepare pod takes any GPU type from a fallback
list (`RUNPOD_BUILD_PLATFORM`), since pie's build is GPU-agnostic (NVRTC).
Cold pods shallow-fetch the pinned pie commit; the full-history mirror is
only maintained when the volume is mounted (a mirror clone over a flaky
host link died after 33 minutes).

**Pods die silently when the container disk fills.** Miniature raw-tensor
spans (tens of GB) went to `/tmp`; the runner then failed with "No space
left on device" and the job left no log. Spans live on the volume under a
per-process directory (deleted after the build), the container disk is 80
GB, and `build`/`prepare` tee their logs to `$PIE_EVALS_CACHE/logs/` so a
dead pod leaves a trace.

**Miniatures must keep the checkpoint's tensor names.** `--text-only`
strips the `language_model.` prefix and pie's readers then find no
`embed_tokens`; the doc-exact `shrink_checkpoint.py` invocation matches.
pie's catalog already ships 5-layer mini rows (`qwen36-35b-a3b-mini`,
`dsv4-flash-u4g64-u2g64`), so recipes are `--layers 0-4 --experts 16`; the
gpt-oss row is pie PR #623. A snapshot whose recipe changed is rebuilt.

**What pie 1a3b2e2a loads.** Matching = a catalog `Row {layers, vocab,
arch}` whose family reader lands every plane. Qwen3.5-0.8B and gemma-4-E4B
load and benchmark; dense qwen3 has no reader (not planned) and Llama none.
Both loaded SKUs report `max_context` 4096 regardless of `--max-model-len`;
artifacts carry `max_context` and longer shapes are declared unsupported.

**Inferlets pie_bench.py can drive.** Only those with text-completion-
bench's input/output contract: `prefill-rows` wants `ids`,
`prefix-tree-kv-cache` returns non-JSON, `mtp`/`cacheback` return no
`num_output_tokens`, and the attention-only ones need `forward-hybrid` on
hybrid models; sampling inferlets (`lora-probe`, `trackb-*`) reject
temperature 0 and get `bench_args`. Each is a declared cell, not a fail.

**One boot per model.** With `PIE_BENCH_SERVE_ONLY` the bench attaches to
one server per process; before that gemma-4-E4B spent ~7 min per round
loading. Smoke on one 4090 went from 75 min (16 cells unreached) to 36 min.

**Baselines.** vLLM 0.26.1 does not exist on PyPI; pins are vLLM 0.30.0 and
SGLang 0.5.20, installed once into venvs on the volume by `prepare`.

**First numbers (RTX 4090, pie 1a3b2e2a, single stream decode tok/s):**
Qwen3.5-0.8B 461–464, gemma-4-E4B 91.8; CoV ≤ 0.1 % across rounds; control
A/A passes. prefix-1k-x64's first round is cold (CoV 5–8 %, `noisy`).

## 11. Findings from the first real run (2026-09-22)

Validated end to end on this box (1× RTX PRO 4500 Blackwell, CUDA 13.0): pie
built at `fa2666956` with the `cuda` feature, the embedded-engine wheel and
the `text-completion-bench` wasm built, Qwen3-0.6B weights in the HF cache,
and the node runner driving the real `benches/pie_bench.py`. Confirmed
working: matrix expansion and budgets, job generation with one-model-per-
process grouping, the parquet store with mandatory provenance, all reports,
the control-A/A gate (a failed control isolates the rest of the process as
`harness_invalid`), and failure classification.

Two things the run surfaced, both for the pie author to decide:

1. **The shipped SKU catalog on `fa2666956` has 7 rows, all large/special
   models (dsv4, flux2, qwen36-27b, gpt-oss, …). A plain small dense
   checkpoint — Qwen3-0.6B — matches none**, so both the embedded bench and
   `pie model import` refuse it ("no SKU this build ships claims this
   checkpoint"), even though `tests/inferlets/conftest.py` still defaults to
   `Qwen/Qwen3-0.6B`. The harness caught and classified this as `load_fail`,
   which is the framework behaving correctly, but every small-model cell in
   `matrix/models.yaml` will be `fail` until the catalog carries their SKUs
   or the models are imported with an explicit one. **Decision needed:** the
   SKU names for the smoke-tier small models, or the intended import flow.
2. **`benches/pie_bench.py` has no `--sku` flag** (its `ModelConfig` omits
   the field), so a SKU cannot be passed through the bench even though
   `ArtifactSpec.pie_sku` is ready to carry it. Once (1) is settled this flag
   is the last wire.

### CRITICAL fix landed
`preflight.kill_leftovers` used `pkill -f <name>`; with pie's name it matched
the runner, its shell and the interactive session (whose cwd contains "pie")
and killed them — it happened twice. It now kills only PIDs nvidia-smi
reports as holding a GPU, matched by executable basename, never a PID in our
ancestor/process-group set, and `pkill` is banned by a test
(`tests/test_preflight.py`).

## 11. Open items

- Small-model SKU catalog / import flow on the current pie commit (blocks every smoke small-model cell — see §11).
- `benches/pie_bench.py --sku` so `ArtifactSpec.pie_sku` can reach the engine.
- `logprob-probe` inferlet in pie (unblocks T1 and loglikelihood T2).
- `--prompt-tokens-file` and `--trace` on `benches/common.py` (pre-tokenized
  shapes; true trace replay instead of Poisson at the trace's mean rate).
- Confirm HF repo ids for the newer families in `models.yaml`; fill in the
  actual Mac fleet in `platforms.yaml`; calibrate `est_minutes` (shard
  counts and the 60-min budget are only as good as these).
- Org setup for RunPod: `RUNPOD_API_KEY` is set; still needed are the
  `GH_RUNNER_PAT` secret (fine-grained, Administration: read/write on
  pie-evals — the same kind pie's CI already uses for its pod) and the
  `RUNPOD_NETWORK_VOLUME_ID` variable; optional `RUNPOD_IMAGE` (defaults to
  the runner image `:latest`) and `RUNPOD_BUILD_PLATFORM` (defaults to
  `l40s-x1`). Then run `runpod-check`.
- Baselines are not in the runner image; the node installs them lazily into
  venvs on the volume (`/workspace/.venv/<engine>-<version>`) — to write.
- Device-tuning gate for new Apple chips (`pie config tune` before the first
  benchmark on a chip not in the tuning table).
- Auto-bisect on confirmed regression (builds are already cached by commit).
