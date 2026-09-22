"""RunPod launcher, on the ``pieproject/runpod-ci-runner`` image
(github.com/pie-project/runpod-ci-runner: CUDA 13 runtime + NVRTC + NCCL,
build tools, uv, Node, actions-runner at ``/opt/actions-runner``; Rust and
every cache on the volume at ``/workspace``).

That image's own ``runner.sh`` serves a *persistent* pod that pie's CI
resumes and stops. pie-evals instead creates an ephemeral pod per job, so
the start command is overridden with ``startup_script``: same env layout as
``runner.sh`` (``/workspace/.cargo``, ``.pie``, ``.hf`` …), but the token is
minted in-pod from ``GH_RUNNER_PAT`` exactly as the image does, the runner
is ``--ephemeral`` and serves ONE job, and the pod terminates itself
afterwards — and, unconditionally, at ``kill_minutes``.

Shared network volume + N concurrent pods means two things must be
pod-local: the pie work tree (cloned from a bare mirror on the volume into
the container disk) and the cargo target dir. Build artifacts are shared
through ``$PIE_EVALS_CACHE/builds/<commit>-<features>`` (see
``node/build.py``); the tier workflow builds once before the fan-out.

API: RunPod REST (``https://rest.runpod.io/v1``), the same API pie's CI
already uses against this image.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass

from pie_evals.schema import PlatformSpec

REST = "https://rest.runpod.io/v1"
DEFAULT_IMAGE = "pieproject/runpod-ci-runner:latest"
VOLUME = "/workspace"


@dataclass
class PodHandle:
    id: str
    labels: list[str]
    data_center: str | None = None


def _req(method: str, path: str, body: dict | None = None, api_key: str | None = None, params: dict | None = None) -> dict | list:
    import requests

    key = api_key or os.environ["RUNPOD_API_KEY"]
    r = requests.request(method, f"{REST}{path}", json=body, params=params, timeout=60,
                         headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    if r.status_code >= 400:
        raise RuntimeError(f"runpod {method} {path}: {r.status_code} {r.text[:500]}")
    return r.json() if r.text.strip() else {}


# ---- discovery -------------------------------------------------------------------

def gpu_types(api_key: str | None = None) -> list[dict]:
    """GPU types: ``id`` is what a pod request's ``gpuTypeIds`` wants."""
    return list(_req("GET", "/gputypes", api_key=api_key))


def validate_platforms(platforms: dict[str, PlatformSpec], api_key: str | None = None) -> list[str]:
    known = {g["id"] for g in gpu_types(api_key)}
    return [f"platform {p.id}: runpod_gpu_type {p.runpod_gpu_type!r} is not a RunPod GPU type id" for p in platforms.values() if p.runpod_gpu_type and p.runpod_gpu_type not in known]


def network_volume(volume_id: str, api_key: str | None = None) -> dict:
    """The volume record; pods must be created in its ``dataCenterId`` to mount it."""
    return dict(_req("GET", f"/networkvolumes/{volume_id}", api_key=api_key))


# ---- startup ----------------------------------------------------------------------

def startup_script(labels: list[str], *, repo: str, kill_minutes: int, image_version: str = "latest", volume: str = VOLUME) -> str:
    """Runs as the pod's start command on the runpod-ci-runner image."""
    lab = ",".join(labels + [f"img-{image_version}"])
    return f"""#!/usr/bin/env bash
set -uo pipefail
V={volume}
echo "== $(nvidia-smi --query-gpu=name,driver_version,compute_cap,memory.total --format=csv,noheader 2>/dev/null || echo 'no GPU visible')"
terminate() {{ curl -fsS -X DELETE -H "Authorization: Bearer $RUNPOD_API_KEY" "https://rest.runpod.io/v1/pods/$RUNPOD_POD_ID" >/dev/null 2>&1 || true; }}
( sleep $(( {kill_minutes} * 60 )); echo "self-destruct: {kill_minutes} min"; terminate ) &
# Rust on the volume (shared, read-mostly); the repo's rust-toolchain.toml picks the version
[ -x "$V/.cargo/bin/rustup" ] || curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --default-toolchain none --no-modify-path
mkdir -p "$V/_work" "$V/.pie" "$V/.hf" "$V/.uv" "$V/.npm" "$V/pie-evals-cache" /tmp/target /tmp/pie
cat > /opt/actions-runner/.env <<ENV
RUSTUP_HOME=$V/.rustup
CARGO_HOME=$V/.cargo
CARGO_TARGET_DIR=/tmp/target
PIE_ROOT=/tmp/pie
PIE_MIRROR=$V/pie.git
PIE_HOME=$V/.pie
HF_HOME=$V/.hf
HF_HUB_CACHE=$V/.hf/hub
UV_CACHE_DIR=$V/.uv
npm_config_cache=$V/.npm
PIE_EVALS_CACHE=$V/pie-evals-cache
PIE_EVALS_PLATFORM=$PIE_EVALS_PLATFORM
PATH=$V/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV
TOKEN=$(curl -fsS -X POST -H "Authorization: Bearer $GH_RUNNER_PAT" -H "Accept: application/vnd.github+json" \\
  "https://api.github.com/repos/{repo}/actions/runners/registration-token" | jq -r .token)
cd /opt/actions-runner
./config.sh --unattended --replace --ephemeral --disableupdate --url "https://github.com/{repo}" --token "$TOKEN" \\
  --name "runpod-${{RUNPOD_POD_ID:-$(hostname)}}" --labels "{lab}" --work "$V/_work"
./run.sh || true
terminate
sleep 60
"""


# ---- lifecycle --------------------------------------------------------------------

def create_pod(
    platform: PlatformSpec,
    *,
    repo: str,
    runner_pat: str,
    kill_minutes: int,
    image: str = DEFAULT_IMAGE,
    image_version: str = "latest",
    network_volume_id: str | None = None,
    container_disk_gb: int = 40,
    cloud_type: str = "SECURE",
    allowed_cuda_versions: list[str] | None = None,
    api_key: str | None = None,
) -> PodHandle:
    if not platform.runpod_gpu_type:
        raise ValueError(f"platform {platform.id} has no runpod_gpu_type")
    key = api_key or os.environ["RUNPOD_API_KEY"]
    name = f"pie-evals-{platform.id}-{int(time.time())}"
    script = startup_script(platform.runner_labels, repo=repo, kill_minutes=kill_minutes, image_version=image_version)
    body: dict = {
        "name": name,
        "imageName": image,
        "gpuTypeIds": [platform.runpod_gpu_type],
        "gpuCount": platform.count,
        "cloudType": cloud_type,
        "computeType": "GPU",
        "containerDiskInGb": container_disk_gb,
        "volumeInGb": 0,
        "ports": [],
        "dockerStartCmd": ["bash", "-lc", script],
        "env": {
            "PIE_EVALS_PLATFORM": platform.id,
            "PIE_EVALS_KILL_MINUTES": str(kill_minutes),
            "GH_RUNNER_PAT": runner_pat,
            "RUNPOD_API_KEY": key,  # self-termination only
        },
    }
    if allowed_cuda_versions:
        body["allowedCudaVersions"] = allowed_cuda_versions
    data_center = None
    if network_volume_id:
        vol = network_volume(network_volume_id, key)
        data_center = vol.get("dataCenterId")
        body["networkVolumeId"] = network_volume_id
        body["volumeMountPath"] = VOLUME
        if data_center:
            body["dataCenterIds"] = [data_center]
    data = _req("POST", "/pods", body, key)
    return PodHandle(id=data["id"], labels=platform.runner_labels, data_center=data_center)


def terminate_pod(pod_id: str, api_key: str | None = None) -> None:
    _req("DELETE", f"/pods/{pod_id}", api_key=api_key)


def list_pods(api_key: str | None = None) -> list[dict]:
    return list(_req("GET", "/pods", api_key=api_key))


def reap(max_age_s: int, api_key: str | None = None, dry_run: bool = False) -> list[str]:
    """Terminate pie-evals pods older than ``max_age_s`` (orphans from failed workflows)."""
    killed = []
    now = time.time()
    for p in list_pods(api_key):
        name = p.get("name", "")
        if not name.startswith("pie-evals-"):
            continue
        try:
            created = int(name.rsplit("-", 1)[-1])
        except ValueError:
            continue
        if now - created > max_age_s:
            if not dry_run:
                terminate_pod(p["id"], api_key)
            killed.append(p["id"])
    return killed


def to_json(x) -> str:
    return json.dumps(x, indent=1)
