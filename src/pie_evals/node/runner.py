"""Execute a JobSpec on this machine.

Order of operations, per job:

1. preflight: hardware fingerprint, machine state (thermal/power on macOS,
   GPU drain on Linux), the pie build for the pinned commit.
2. group cells into processes: one model per process; within a process the
   workloads/programs are interleaved (ABBA when repeating), and every cell
   in the group shares the same loaded weights.
3. per cell: run once; consult history (adaptive repetition); confirm if
   outside the band; compute CoV; NOISY if the spread is above policy.
4. accuracy gate (T0) for FULL artifacts whose program has a token-parity
   gate and for which a reference exists; miniature cells are
   SKIPPED_MINIATURE by construction.
5. write ``records.jsonl`` incrementally so a killed job still leaves what
   it finished.

Every failure is classified into ``ErrorClass``; a hang is a timeout.
"""

from __future__ import annotations

import os
import random
import signal
import threading
import time
import traceback
import uuid
from datetime import datetime, timezone
from pathlib import Path

from pie_evals.schema import (
    AccuracyMetrics,
    AccuracyStatus,
    Cell,
    CellStatus,
    ErrorClass,
    JobSpec,
    PerfMetrics,
    Record,
    Tier,
)

from . import preflight as pf
from . import provenance as prov
from .engines import EngineLaunchError, get_engine
from .engines.recipes import load_recipe
from .metrics.stats import cov, decide_repetition, median
from .engines.shape import serve_envelope
from .workloads import common_args_for


class NodeRunner:
    def __init__(self, job: JobSpec, *, pie_root: Path, out_dir: Path, hf_cache: Path | None = None, runner_name: str | None = None, build: bool = True, download: bool = False):
        self.job = job
        # a pod without the shared volume never saw `prepare`: it must fetch for itself
        self.download = download or not os.environ.get("PIE_EVALS_VOLUME", "") and bool(os.environ.get("RUNPOD_POD_ID"))
        self.pie_root = Path(pie_root).resolve()
        # absolute: cell output paths are handed to bench subprocesses that run
        # with their own cwd (scripts/bench), and a relative --out made them
        # write bench.json somewhere the runner never looked
        self.out = Path(out_dir).resolve()
        self.out.mkdir(parents=True, exist_ok=True)
        self.hf_cache = Path(hf_cache or os.environ.get("HF_HUB_CACHE") or Path.home() / ".cache/huggingface/hub")
        self.runner_name = runner_name or os.environ.get("RUNNER_NAME") or os.uname().nodename
        self.run_id = f"{job.job_id}-{uuid.uuid4().hex[:6]}"
        self.records_path = self.out / "records.jsonl"
        self.build = build
        self.platform = job.cells[0].platform if job.cells else None
        self._log = open(self.out / "runner.log", "a")
        (self.out / "run_id.txt").write_text(self.run_id + "\n")
        self.t_start = time.monotonic()
        self._killed = threading.Event()
        self._done: set[str] = set()
        self._last_state: dict = {}
        self._start_watchdog()

    # ------------------------------------------------------------------ time policy
    def elapsed_s(self) -> float:
        return time.monotonic() - self.t_start

    def over_budget(self) -> bool:
        """Soft budget: no new cell starts after ``job.budget_s``."""
        return self.elapsed_s() >= self.job.budget_s

    def remaining_to_kill_s(self) -> float:
        return max(1.0, self.job.kill_s - self.elapsed_s())

    def cell_timeout_s(self, cell: Cell) -> int:
        """A round may take at most ten times the workload's estimate (floor
        ten minutes), under the job-wide cap and the kill deadline. Nightly
        35959142812 lost a whole 60-minute shard to one hung 30-second cell
        (pie #649): the flat 5400 s cap let it run to the client's timeout."""
        scaled = max(600.0, float(cell.workload.est_minutes) * 60.0 * 10.0)
        return int(min(self.job.per_cell_timeout_s, scaled, self.remaining_to_kill_s()))

    def _start_watchdog(self) -> None:
        """Hard deadline: at ``job.kill_s`` (= budget × kill_factor) kill every
        child in our process group and exit. The workflow's timeout-minutes
        and the pod's self-destruct are the two outer layers of the same
        limit; this is the one that leaves a record behind."""

        def _fire() -> None:
            self._killed.set()
            try:
                self.log(f"WATCHDOG: hard deadline {self.job.kill_s}s reached; killing children and exiting")
                self._emit_unreached("hard deadline reached (job.kill_s); force-killed")
                self._log.flush()
            finally:
                # kill children (not ourselves first): every subprocess we spawned shares our pgid
                try:
                    os.killpg(os.getpgrp(), signal.SIGTERM)
                    time.sleep(3)
                    os.killpg(os.getpgrp(), signal.SIGKILL)
                except OSError:
                    pass
                os._exit(124)

        t = threading.Timer(self.job.kill_s, _fire)
        t.daemon = True
        t.start()
        self._watchdog = t

    def _emit_unreached(self, reason: str) -> None:
        """Record every cell that has not been reached as NOT_RUN with the
        reason. Called once by the runner when the soft budget stops it, or by
        the watchdog. Idempotent per cell via ``_done``."""
        for c in self.job.cells:
            if c.cell_id in self._done:
                continue
            self._done.add(c.cell_id)
            self.emit(self._not_run(c, reason))

    # ------------------------------------------------------------------ logging
    def log(self, msg: str) -> None:
        line = f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}"
        print(line, flush=True)
        self._log.write(line + "\n")
        self._log.flush()

    def emit(self, rec: Record) -> None:
        with open(self.records_path, "a") as f:
            f.write(rec.model_dump_json() + "\n")

    # ------------------------------------------------------------------ setup
    def ensure_pie(self) -> None:
        """Pin the checkout to the job's commit and put the build artifacts in
        place: cache hit → restore; miss → build here (pod-local cargo target)
        and cache. The tier workflow runs a build job before the fan-out so
        bench pods normally hit the cache."""
        if not self.job.pie_commit:
            return
        from . import build as pb

        mirror = Path(os.environ["PIE_MIRROR"]) if os.environ.get("PIE_MIRROR") else None
        if not self.build:
            # --no-build: use the tree as it is; only pin it if it is a real checkout
            if (self.pie_root / ".git").exists():
                pb.ensure_checkout(self.pie_root, self.job.pie_commit, mirror=mirror)
            else:
                self.log(f"--no-build and {self.pie_root} is not a git checkout; using it as-is")
            return
        pb.ensure_checkout(self.pie_root, self.job.pie_commit, mirror=mirror)
        pb.ensure(self.pie_root, self.job.pie_commit, self.job.pie_build_features,
                  target_dir=Path(os.environ["CARGO_TARGET_DIR"]) if os.environ.get("CARGO_TARGET_DIR") else None,
                  python=os.environ.get("PIE_PY", "python3"), log=self.log)
        self.log(f"pie interpreter for the bench: {os.environ.get('PIE_PY', 'python3')}")

    def snapshot_dir(self, cell: Cell) -> Path:
        from .snapshots import ensure_snapshot

        try:
            py = os.environ.get("PIE_PY")
            if not py:
                from .build import bench_python

                py = str(bench_python(log=self.log))
            return ensure_snapshot(cell.artifact, self.hf_cache, pie_root=self.pie_root, python=py, download=self.download, log=self.log)
        except EngineLaunchError:
            raise
        except Exception as e:  # download / shrink failure: the model, not the harness
            raise EngineLaunchError(ErrorClass.LOAD_FAIL, f"checkpoint unavailable for {cell.artifact.id}: {str(e).strip().splitlines()[-1][:300] if str(e).strip() else e!r}") from e

    # ------------------------------------------------------------------ run
    def run(self) -> list[Record]:
        job = self.job
        try:
            os.setpgrp()  # our own process group, so the watchdog's killpg reaches only our children
        except OSError:
            pass
        self.log(f"job {job.job_id} tier={job.tier} platform={job.platform_id} cells={len(job.cells)} run_id={self.run_id}")
        broken = pf.cuda_init() if self.platform is not None and not pf._is_mac(str(self.platform.os)) else None
        if broken:
            self.log(f"GPU preflight failed: {broken}; this pod cannot reach the driver, so no cell is attempted")
            for c in job.cells:
                self.emit(self._failed(c, ErrorClass.HARNESS_INVALID, f"GPU preflight: {broken}", None))
            return []
        if self.platform is not None and not pf._is_mac(str(self.platform.os)) and os.geteuid() == 0:
            from .baselines import ensure_cuda_devkit

            ensure_cuda_devkit(log=self.log)  # nvcc + headers + libcudadevrt.a for pie's NVRTC and the baselines' JITs
        try:
            self.ensure_pie()
        except Exception as e:  # a build failure fails every pie cell identically
            self.log(f"pie build failed: {e}")
            for c in job.cells:
                if str(c.engine) == "pie":
                    self.emit(self._failed(c, ErrorClass.LOAD_FAIL, f"pie build failed: {e}", None))
            job = job.model_copy(update={"cells": [c for c in job.cells if str(c.engine) != "pie"]})
        pre = pf.Preflight()
        machine_before = pre.before_job(self.platform)
        self._last_state = machine_before  # failure records carry the state the card was in
        if machine_before.get("gpu_drain_error"):
            # a card that already holds someone else's memory (nightly 35963868578: 5.7 GiB,
            # no process) invalidates every number and refuses the big loads; give the shard back
            self.log(f"GPU not clean at job start: {machine_before['gpu_drain_error']}; no cell is attempted on this pod")
            for c in job.cells:
                self.emit(self._failed(c, ErrorClass.HARNESS_INVALID, f"GPU not clean at job start: {machine_before['gpu_drain_error']}", None))
            return []
        fingerprint = prov.hardware_fingerprint()
        records: list[Record] = []
        groups = job.cells_by_process()
        self.log(f"{len(groups)} engine processes to run")
        for gkey, cells in groups.items():
            engine_name, artifact_key, mode_key = gkey
            if self.over_budget():
                self.log(f"soft budget {job.budget_s}s exhausted after {self.elapsed_s():.0f}s; not starting {engine_name} {artifact_key}")
                continue
            self.log(f"--- process {engine_name} {artifact_key} {mode_key} ({len(cells)} cells) t+{self.elapsed_s():.0f}s")
            engine = None
            snapshot = None
            try:
                snapshot = self.snapshot_dir(cells[0])
            except EngineLaunchError as e:
                for c in cells:
                    self.emit(self._failed(c, e.error_class, str(e), fingerprint))
                continue
            except Exception as e:  # nothing about one model may take the job down
                self.log(f"process setup crashed: {e}\n{traceback.format_exc()}")
                for c in cells:
                    self.emit(self._failed(c, ErrorClass.HARNESS_INVALID, f"process setup: {e}", fingerprint))
                continue
            from .miniature import num_layers_of

            num_layers = num_layers_of(snapshot)
            first = cells[0]
            model_path = snapshot
            if str(first.engine) == "pie" and self.job.pie_commit:
                from .importer import ensure_artifact, needs_import

                if needs_import(first.artifact) or int(first.mode.tp) > 1:  # tp>1: the ranks band a stamped artifact at load (pie #633)
                    try:
                        model_path = ensure_artifact(first.artifact, snapshot, self.pie_root / "target/release/pie", self.job.pie_commit, log=self.log)
                    except Exception as e:
                        for c in cells:
                            self.emit(self._failed(c, ErrorClass.LOAD_FAIL, f"artifact import: {str(e).strip().splitlines()[-1][:300]}", fingerprint))
                        continue
            recipe_name = "competitive" if str(first.engine) != "pie" else "default"
            try:
                pre.between_engines(self.platform, [])
                cls = get_engine(first.engine)
                recipe = load_recipe(str(first.engine), recipe_name, first.platform, first.workload, family=first.artifact.family)
                recipe["program_path"] = first.program.path
                recipe["snapshot_dir"] = str(model_path)
                if str(first.engine) in self.job.baseline_versions:
                    from .baselines import SPECS, ensure_baseline

                    recipe["pin"] = self.job.baseline_versions[str(first.engine)]
                    if str(first.engine) in SPECS and not os.environ.get({"vllm": "VLLM_PY", "sglang": "SGLANG_PY"}.get(str(first.engine), "")):
                        ensure_baseline(str(first.engine), recipe["pin"], log=self.log)
                engine = cls(pie_root=self.pie_root, artifact=first.artifact, platform=first.platform, mode=first.mode, recipe=recipe, num_layers=num_layers)
                engine_version = engine.version()
                # one boot per model: the bench then attaches to this server for every
                # cell and round instead of reloading the weights each time (gemma-4 E4B
                # spent ~7 min per round loading; the measurement itself takes seconds)
                widest = serve_envelope([c.workload for c in cells])
                serve_log = self.out / "serve" / f"{artifact_key.replace('/', '_')}-{mode_key}.log"
                try:
                    engine.serve(widest, serve_log, int(min(self.job.load_timeout_s, self.remaining_to_kill_s())))
                except EngineLaunchError as e:
                    from .importer import RELAYOUT_MARK, ensure_artifact

                    if RELAYOUT_MARK not in str(e) or str(first.engine) != "pie" or not self.job.pie_commit or model_path != snapshot:
                        raise
                    self.log("pie refuses to serve this checkpoint directly; importing it as an artifact and retrying")
                    model_path = ensure_artifact(first.artifact, snapshot, self.pie_root / "target/release/pie", self.job.pie_commit, log=self.log)
                    recipe["snapshot_dir"] = str(model_path)
                    engine = cls(pie_root=self.pie_root, artifact=first.artifact, platform=first.platform, mode=first.mode, recipe=recipe, num_layers=num_layers)
                    engine.serve(widest, serve_log, int(min(self.job.load_timeout_s, self.remaining_to_kill_s())))
                if getattr(engine, "server_url", None):
                    self.log(f"serving {artifact_key} at {engine.server_url}")
            except EngineLaunchError as e:
                self.log(f"engine boot failed: {e.error_class} {e}")
                for c in cells:
                    self.emit(self._failed(c, e.error_class, str(e), fingerprint))
                if engine:
                    engine.stop()
                continue
            except Exception as e:
                self.log(f"engine setup failed: {e}\n{traceback.format_exc()}")
                for c in cells:
                    self.emit(self._failed(c, ErrorClass.LOAD_FAIL, f"engine setup: {e}", fingerprint))
                continue
            order = list(cells)
            if job.repetition.interleave:
                random.Random(self.run_id).shuffle(order)
            # control cell first: if the harness cannot agree with itself nothing else is read
            order.sort(key=lambda c: 0 if c.workload.kind.value == "control_aa" else 1)
            control_ok = True
            model_state = pre.before_model(self.platform) if hasattr(pre, "before_model") else machine_before
            self._last_state = model_state
            for cell in order:
                if cell.cell_id in self._done:
                    continue
                if self.over_budget():
                    self.log(f"soft budget exhausted at t+{self.elapsed_s():.0f}s; remaining cells of this process not started")
                    break
                if not control_ok and job.control_required:
                    rec = self._invalid(cell, "control A/A failed on this process; numbers not read", fingerprint)
                    records.append(rec)
                    self.emit(rec)
                    continue
                if hasattr(engine, "program_path"):
                    engine.program_path = cell.program.path  # the cell's own inferlet, not the process's first
                rec = self._run_cell(cell, engine, snapshot, engine_version, recipe, recipe_name, fingerprint, machine_before)
                if cell.workload.kind.value == "control_aa" and rec.status != CellStatus.PASS:
                    control_ok = False
                    self.log("control A/A failed; remaining cells in this process are HARNESS_INVALID")
                records.append(rec)
                self._done.add(cell.cell_id)
                self.emit(rec)
            try:
                if engine:
                    engine.stop()
                    pre.between_engines(self.platform, engine.leftover_process_names())
            except Exception as e:
                self.log(f"teardown: {e}")
            invalid = pre.after_model(self.platform, model_state)
            if invalid:
                self.log(f"model run invalidated: {invalid}")
                for r in [r for r in records if r.cell.artifact.artifact_key == artifact_key and r.status == CellStatus.PASS]:
                    r.status = CellStatus.NOISY
                    r.invalid_reason = "; ".join(invalid)
                    self.emit(r)
                # a GPU that was not ours to begin with (5.7 GB held by a foreign process on a
                # fresh 5090 pod, nightly 35942190398) fails the engine at boot: that is the
                # pod's fault, not the engine's, so the crash is recorded as harness-invalid
                for r in [r for r in records if r.cell.artifact.artifact_key == artifact_key and r.status == CellStatus.FAIL]:
                    r.error_class = ErrorClass.HARNESS_INVALID
                    r.invalid_reason = "; ".join(invalid)
                    self.emit(r)
        self._emit_unreached(f"job budget ({job.budget_s}s) exhausted before this cell was reached" if self.over_budget() else "not reached (earlier failure)")
        self._watchdog.cancel()
        self.log(f"done in {self.elapsed_s():.0f}s (budget {job.budget_s}s, kill {job.kill_s}s)")
        self._log.close()
        return records

    # ------------------------------------------------------------------ one cell
    def _run_cell(self, cell: Cell, engine, snapshot: Path, engine_version: str, recipe: dict, recipe_name: str, fingerprint: dict, machine_state: dict) -> Record:
        t0 = time.monotonic()
        cell = cell.model_copy(update={"engine_version": engine_version})
        cell_out = self.out / "cells" / cell.cell_id
        common = common_args_for(cell.workload, warmup=2 if self.job.tier == Tier.SMOKE else 3) + list(cell.program.bench_args)
        policy = self.job.repetition
        rounds: list[float] = []
        results = []
        try:
            for i in range(policy.min_rounds):
                res = engine.run(cell.workload, common, cell_out / f"r{i}", self.cell_timeout_s(cell))
                results.append(res)
                rounds.append(self._primary(res.perf))
            hist = self.job.history.get(cell.cell_id, [])
            if policy.min_rounds == 1:
                d = decide_repetition(rounds[0], hist, sigma=policy.history_sigma, confirm_rounds=policy.confirm_rounds)
                self.log(f"{cell.workload.id}/{cell.program.id}: {rounds[0]:.4g} — {d.reason}")
                for _ in range(d.more_rounds):
                    if len(rounds) >= policy.max_rounds:
                        break
                    res = engine.run(cell.workload, common, cell_out / f"r{len(rounds)}", self.cell_timeout_s(cell))
                    results.append(res)
                    rounds.append(self._primary(res.perf))
        except EngineLaunchError as e:
            self.log(f"{cell.workload.id}/{cell.program.id}: {e.error_class} {e}")
            return self._failed(cell, e.error_class, str(e), fingerprint, duration=time.monotonic() - t0)
        except Exception as e:
            self.log(f"{cell.workload.id}/{cell.program.id}: harness exception {e}\n{traceback.format_exc()}")
            return self._failed(cell, ErrorClass.HARNESS_INVALID, f"harness: {e}", fingerprint, duration=time.monotonic() - t0)
        # median round is the record; rounds and CoV travel with it
        med_idx = sorted(range(len(rounds)), key=lambda i: rounds[i])[len(rounds) // 2]
        perf: PerfMetrics = results[med_idx].perf
        perf.rounds = rounds
        perf.cov = cov(rounds)
        perf.load_s = results[0].duration_s - (results[med_idx].duration_s if len(results) > 1 else 0) if len(results) > 1 else None
        status = CellStatus.PASS
        invalid = None
        # a tensor-parallel process adds collective latency to every step, so its
        # single-stream rounds spread like a concurrent shape's (gemma-4-E4B tp2 on
        # L40S x2: A/A spread 2.1 % against the 2 % bound, every cell withheld)
        tight = policy.cov_noisy_threshold if int(cell.mode.tp) <= 1 else policy.cov_noisy_threshold_concurrent
        thr = tight if cell.workload.kind.value in ("single_stream", "control_aa", "long_context") else policy.cov_noisy_threshold_concurrent
        if perf.failed:
            status, invalid = CellStatus.FAIL, f"{perf.failed} of {perf.requests} requests failed"
        elif len(rounds) >= 2 and perf.cov > thr:
            status, invalid = CellStatus.NOISY, f"cov {perf.cov:.3%} > {thr:.1%}"
        if cell.workload.kind.value == "control_aa" and len(rounds) >= 2:
            spread = abs(rounds[0] - rounds[-1]) / median(rounds)
            if spread > tight:
                status, invalid = CellStatus.NOISY, f"control A/A spread {spread:.3%} > {tight:.1%}"
        accuracy = self._accuracy(cell, engine, snapshot)
        if accuracy.status == AccuracyStatus.FAIL and status == CellStatus.PASS:
            status = CellStatus.FAIL
        provenance = prov.build_provenance(self.pie_root, snapshot, engine_version, recipe, recipe_name, self.runner_name)
        provenance.hardware_fingerprint = fingerprint
        provenance.machine_state = machine_state
        provenance.pie_commit = self.job.pie_commit or provenance.pie_commit
        provenance.pie_build_features = self.job.pie_build_features
        return Record(
            run_id=self.run_id, job_id=self.job.job_id, tier=self.job.tier, cell_id=cell.cell_id, cell_key=cell.cell_key, cell=cell,
            status=status, error_class=ErrorClass.GATE_FAIL if accuracy.status == AccuracyStatus.FAIL else None,
            error_message=None, invalid_reason=invalid, perf=perf, accuracy=accuracy, provenance=provenance,
            duration_s=time.monotonic() - t0,
        )

    @staticmethod
    def _primary(perf: PerfMetrics) -> float:
        v = getattr(perf, perf.primary, None)
        if v is None:
            raise EngineLaunchError(ErrorClass.HARNESS_INVALID, f"no {perf.primary} in bench output")
        return float(v)

    def _accuracy(self, cell: Cell, engine, snapshot: Path) -> AccuracyMetrics:
        """T0 token parity, once per engine process: it is a property of the
        loaded model, not of the workload, so it rides on the ``ss-128-64``
        cell of each process and every other cell of that process is NOT_RUN."""
        from .accuracy.gate import skip_reason, t0_via_engine

        skip = skip_reason(cell)
        if skip is not None:
            return AccuracyMetrics(status=skip)
        if cell.program.accuracy_gate != "token_parity" or cell.workload.id != "ss-128-64":
            return AccuracyMetrics(status=AccuracyStatus.NOT_RUN)
        try:
            cache = Path(os.environ.get("PIE_EVALS_CACHE", Path.home() / ".cache/pie-evals")) / "refcache"
            return t0_via_engine(cell, engine, snapshot, self.platform.os, pie_root=self.pie_root, cache_dir=cache,
                                 out_dir=self.out / "cells" / cell.cell_id / "t0", timeout_s=self.job.per_cell_timeout_s)
        except Exception as e:  # a missing reference is not a pie failure
            self.log(f"accuracy gate skipped: {e}")
            return AccuracyMetrics(status=AccuracyStatus.SKIPPED_NO_REFERENCE, detail={"error": str(e)[:300]})

    def _not_run(self, cell: Cell, reason: str) -> Record:
        p = prov.Provenance(runner=self.runner_name, pie_commit=self.job.pie_commit)
        return Record(run_id=self.run_id, job_id=self.job.job_id, tier=self.job.tier, cell_id=cell.cell_id, cell_key=cell.cell_key, cell=cell,
                      status=CellStatus.NOT_RUN, invalid_reason=reason, provenance=p)

    def _failed(self, cell: Cell, cls: ErrorClass, msg: str, fingerprint: dict | None, duration: float | None = None) -> Record:
        self._done.add(cell.cell_id)
        p = prov.Provenance(hardware_fingerprint=fingerprint or {}, runner=self.runner_name, pie_commit=self.job.pie_commit, harness_commit=prov.git_commit(Path(__file__).resolve().parents[3]))
        p.machine_state = self._last_state  # a boot refusal on a card someone else holds 5 GiB of (nightly 35963868578) reads differently
        return Record(run_id=self.run_id, job_id=self.job.job_id, tier=self.job.tier, cell_id=cell.cell_id, cell_key=cell.cell_key, cell=cell,
                      status=CellStatus.FAIL, error_class=cls, error_message=msg[:1000], provenance=p, duration_s=duration)

    def _invalid(self, cell: Cell, reason: str, fingerprint: dict | None) -> Record:
        r = self._failed(cell, ErrorClass.HARNESS_INVALID, reason, fingerprint)
        r.status = CellStatus.NOISY
        r.invalid_reason = reason
        return r
