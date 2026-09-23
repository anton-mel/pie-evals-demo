"""Machine hygiene around a measurement. Everything is best-effort and
string-valued: the goal is to *record* the state and to refuse to read a
number taken on a machine that was not in the expected state.

Linux: the GPU must be drained before an engine loads (vLLM's EngineCore
outlives its parent; a leftover holds memory and compute). macOS: thermal
pressure, battery vs AC, low power mode and a second display all change the
GPU clock, so they are captured before and after each model.
"""

from __future__ import annotations

import os
import platform
import re
import shutil
import signal
import subprocess
import time
from typing import Any


def _run(argv: list[str], timeout: float = 20.0) -> str | None:
    if shutil.which(argv[0]) is None:
        return None
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if p.returncode != 0:
        return None
    return p.stdout


# ---- linux -----------------------------------------------------------------------


def gpu_memory_used_mib() -> list[float] | None:
    out = _run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"])
    if out is None:
        return None
    vals = []
    for line in out.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            vals.append(float(line))
        except ValueError:
            continue
    return vals


def await_free_gpu(threshold_mib: float = 1500, timeout_s: float = 180, poll_s: float = 2.0) -> float:
    """Block until every GPU reports ``memory.used <= threshold_mib``; return
    the seconds waited. No nvidia-smi -> nothing to wait for (0.0).
    Raises ``TimeoutError`` with the offending readings."""
    t0 = time.monotonic()
    last: list[float] | None = None
    while True:
        last = gpu_memory_used_mib()
        if last is None or all(v <= threshold_mib for v in last):
            return time.monotonic() - t0
        if time.monotonic() - t0 >= timeout_s:
            raise TimeoutError(
                f"GPU memory still in use after {timeout_s:.0f}s: {last} MiB (threshold {threshold_mib})"
            )
        time.sleep(poll_s)


def gpu_processes() -> list[dict[str, str]]:
    out = _run(["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv,noheader,nounits"])
    if not out:
        return []
    procs = []
    for line in out.strip().splitlines():
        parts = [x.strip() for x in line.split(",")]
        if len(parts) >= 2:
            procs.append({"pid": parts[0], "name": parts[1], "used_mib": parts[2] if len(parts) > 2 else ""})
    return procs


def _ancestors(pid: int | None = None) -> set[int]:
    """Our own pid, our process group, and the whole parent chain up to init.
    These must NEVER be killed — the runner, its shell, and the session that
    launched it all live here. (An early version used ``pkill -f pie`` and
    killed the interactive session itself, because its cwd matched.)"""
    protected: set[int] = set()
    cur = pid if pid is not None else os.getpid()
    try:
        protected.add(os.getpgrp())
    except OSError:
        pass
    seen = 0
    while cur and cur > 0 and seen < 64:
        protected.add(cur)
        seen += 1
        try:
            with open(f"/proc/{cur}/stat") as f:
                cur = int(f.read().split(") ", 1)[1].split()[1])  # PPID, robust to spaces in comm
        except (OSError, IndexError, ValueError):
            break
    return protected


def _proc_basename(pid: int) -> str | None:
    try:
        with open(f"/proc/{pid}/comm") as f:
            return f.read().strip()
    except OSError:
        return None


def kill_leftovers(names: list[str], threshold_mib: float = 1500, timeout_s: float = 180) -> dict[str, Any]:
    """Kill GPU-holding orphans whose executable basename is one of ``names``,
    then wait for the GPU to drain.

    Safety, learned the hard way: we only kill PIDs that nvidia-smi reports as
    *currently holding a GPU*, matched by **executable basename** (not a
    command-line substring), and never a PID in our own ancestor/group set. A
    broad ``pkill -f`` is forbidden here — the runner's cwd and argv contain
    "pie", so it would kill the runner and the interactive session.

    This is also the only way to catch the detached child the wiki warns about
    (vLLM's ``EngineCore`` does not show up under ``pgrep -f vllm_bench`` but
    does hold the GPU)."""
    wanted = {n.strip() for n in names if n and n.strip()}
    protected = _ancestors()
    killed: list[dict[str, Any]] = []
    if wanted:
        targets: list[int] = []
        for p in gpu_processes():
            try:
                pid = int(p["pid"])
            except (KeyError, ValueError):
                continue
            if pid in protected:
                continue
            base = _proc_basename(pid) or os.path.basename(p.get("name", ""))
            # match on basename equality, or the reported process_name basename
            if base in wanted or os.path.basename(p.get("name", "")) in wanted:
                targets.append(pid)
                killed.append({"pid": pid, "name": base, "used_mib": p.get("used_mib", "")})
        for pid in targets:
            try:
                os.kill(pid, signal.SIGTERM)
            except (ProcessLookupError, PermissionError):
                pass
        if targets:
            time.sleep(5.0)
            for pid in targets:
                try:
                    os.kill(pid, signal.SIGKILL)
                except (ProcessLookupError, PermissionError):
                    pass
    waited = await_free_gpu(threshold_mib=threshold_mib, timeout_s=timeout_s)
    return {"killed": killed, "gpu_drain_wait_s": round(waited, 2)}


def linux_machine_state() -> dict[str, Any]:
    state: dict[str, Any] = {"os": "linux"}
    out = _run(["nvidia-smi", "--query-gpu=name,driver_version,memory.total,memory.used",
                "--format=csv,noheader,nounits"])
    if out:
        gpus = []
        for line in out.strip().splitlines():
            parts = [x.strip() for x in line.split(",")]
            if len(parts) >= 4:
                gpus.append({"name": parts[0], "driver": parts[1], "memory_total_mib": parts[2],
                             "memory_used_mib": parts[3]})
        state["gpus"] = gpus
        if gpus:
            state["driver"] = gpus[0]["driver"]
    procs = gpu_processes()
    state["gpu_process_count"] = str(len(procs))
    state["gpu_processes"] = [p["name"] for p in procs][:20]
    try:
        la = os.getloadavg()
        state["loadavg"] = ",".join(f"{x:.2f}" for x in la)
    except (OSError, AttributeError):
        pass
    return state


# ---- macOS ----------------------------------------------------------------------


def _parse_pmset_therm(text: str | None) -> dict[str, str]:
    """``pmset -g therm``: 'CPU_Scheduler_Limit = 100', 'CPU_Available_CPUs = 10',
    'CPU_Speed_Limit = 100', and on notebooks a line about thermal warning level."""
    d: dict[str, str] = {}
    if not text:
        return d
    for line in text.splitlines():
        m = re.match(r"\s*(CPU_\w+)\s*=\s*(\d+)", line)
        if m:
            d[m.group(1).lower()] = m.group(2)
    lower = text.lower()
    if "thermal warning level" in lower:
        m = re.search(r"thermal warning level\s*[:=]?\s*(\d+)", lower)
        d["thermal_warning_level"] = m.group(1) if m else "unknown"
    limit = d.get("cpu_speed_limit")
    sched = d.get("cpu_scheduler_limit")
    warned = (
        (limit is not None and limit != "100")
        or (sched is not None and sched != "100")
        or (d.get("thermal_warning_level") not in (None, "0", "unknown"))
    )
    d["thermal_warning"] = "yes" if warned else "no"
    return d


def _parse_pmset_batt(text: str | None) -> dict[str, str]:
    d: dict[str, str] = {}
    if not text:
        return d
    lower = text.lower()
    if "ac power" in lower:
        d["power_source"] = "ac"
    elif "battery power" in lower:
        d["power_source"] = "battery"
    m = re.search(r"(\d+)%", text)
    if m:
        d["battery_pct"] = m.group(1)
    return d


def _parse_lowpowermode(text: str | None) -> str | None:
    if not text:
        return None
    m = re.search(r"lowpowermode\s+(\d)", text)
    return {"0": "off", "1": "on"}.get(m.group(1), m.group(1)) if m else None


def _parse_display_count(text: str | None) -> str | None:
    if not text:
        return None
    # each display is a block with a 'Resolution:' line under 'Displays:'
    n = len(re.findall(r"^\s*Resolution:", text, flags=re.MULTILINE))
    return str(n) if n else None


def mac_machine_state() -> dict[str, Any]:
    state: dict[str, Any] = {"os": "macos"}
    state.update(_parse_pmset_therm(_run(["pmset", "-g", "therm"])))
    state.update(_parse_pmset_batt(_run(["pmset", "-g", "batt"])))
    lpm = _parse_lowpowermode(_run(["pmset", "-g"]))
    if lpm is not None:
        state["low_power_mode"] = lpm
    disp = _parse_display_count(_run(["system_profiler", "SPDisplaysDataType"], timeout=60))
    if disp is not None:
        state["displays"] = disp
    try:
        la = os.getloadavg()
        state["loadavg"] = ",".join(f"{x:.2f}" for x in la)
    except (OSError, AttributeError):
        pass
    return state


def mac_thermal_changed(before: dict[str, Any], after: dict[str, Any]) -> bool:
    """A thermal warning appeared, or the CPU speed/scheduler limit moved."""
    if before.get("thermal_warning") != after.get("thermal_warning"):
        return True
    for k in ("cpu_speed_limit", "cpu_scheduler_limit", "thermal_warning_level"):
        if before.get(k) != after.get(k):
            return True
    return False


# ---- orchestration ----------------------------------------------------------------


def _is_mac(platform_os: str | None) -> bool:
    if platform_os is None:
        return platform.system() == "Darwin"
    return str(platform_os).lower() in ("macos", "darwin", "mac")


def machine_state(platform_os: str | None = None) -> dict[str, Any]:
    return mac_machine_state() if _is_mac(platform_os) else linux_machine_state()


class Preflight:
    """Checks around a job / engine switch / model, returning the recorded
    state (goes into ``Provenance.machine_state``) and invalidation reasons."""

    def __init__(self, gpu_threshold_mib: float = 1500, gpu_timeout_s: float = 180):
        self.gpu_threshold_mib = gpu_threshold_mib
        self.gpu_timeout_s = gpu_timeout_s

    def before_job(self, platform_os: str | None = None) -> dict[str, Any]:
        state = machine_state(platform_os)
        if not _is_mac(platform_os):
            try:
                state["gpu_drain_wait_s"] = round(
                    await_free_gpu(self.gpu_threshold_mib, self.gpu_timeout_s), 2
                )
            except TimeoutError as e:
                state["gpu_drain_error"] = str(e)
        return state

    def between_engines(self, platform_os: str | None, leftover_names: list[str]) -> dict[str, Any]:
        state: dict[str, Any] = {}
        if not _is_mac(platform_os):
            try:
                state.update(kill_leftovers(leftover_names, self.gpu_threshold_mib, self.gpu_timeout_s))
            except TimeoutError as e:
                state["gpu_drain_error"] = str(e)
        state.update(machine_state(platform_os))
        return state

    def after_model(self, platform_os: str | None, before_state: dict[str, Any]) -> list[str]:
        """Reasons the numbers taken since ``before_state`` cannot be read."""
        reasons: list[str] = []
        after = machine_state(platform_os)
        if _is_mac(platform_os):
            if mac_thermal_changed(before_state, after):
                reasons.append(
                    f"thermal state changed during model: {before_state.get('thermal_warning')}"
                    f"->{after.get('thermal_warning')} "
                    f"(speed limit {before_state.get('cpu_speed_limit')}->{after.get('cpu_speed_limit')})"
                )
            if before_state.get("power_source") != after.get("power_source"):
                reasons.append(f"power source changed: {before_state.get('power_source')}->{after.get('power_source')}")
            if after.get("power_source") == "battery":
                reasons.append("running on battery")
            if after.get("low_power_mode") == "on":
                reasons.append("low power mode on")
            if before_state.get("displays") != after.get("displays"):
                reasons.append(f"display count changed: {before_state.get('displays')}->{after.get('displays')}")
        else:
            if before_state.get("gpu_drain_error"):
                reasons.append("GPU was not drained before the model: " + str(before_state["gpu_drain_error"]))
            b = int(before_state.get("gpu_process_count") or 0)
            a = int(after.get("gpu_process_count") or 0)
            if a > b:
                reasons.append(f"other GPU processes appeared during model: {b}->{a} ({after.get('gpu_processes')})")
        return reasons


def cuda_init() -> str | None:
    """None when the driver answers ``cuInit`` and reports a device; else the
    reason. Some RunPod hosts hand out a pod whose container cannot reach the
    driver (``cudaSetDevice answered 999`` in pie, torch's "CUDA unknown
    error" in SGLang, nightlies 35921789513 / 35926457671): every cell of
    the job would then fail for a reason that has nothing to do with the
    engine, so the job says so once and stops."""
    import ctypes
    import sys

    if sys.platform != "linux":
        return None
    try:
        lib = ctypes.CDLL("libcuda.so.1")
    except OSError:
        return None  # no driver at all (a CPU box, CI): not the broken-pod case; the engine says its own piece
    rc = lib.cuInit(0)
    if rc != 0:
        return f"cuInit answered {rc}"
    count = ctypes.c_int(0)
    rc = lib.cuDeviceGetCount(ctypes.byref(count))
    if rc != 0:
        return f"cuDeviceGetCount answered {rc}"
    if count.value < 1:
        return "cuDeviceGetCount says 0 devices"
    return None
