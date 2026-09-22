"""RunPod launcher.

A pod is created with a startup command that registers an *ephemeral*
GitHub self-hosted runner carrying the platform's labels; the tier
workflow's bench job then lands on it. Three layers enforce the time policy
(job budget × kill_factor):

1. the node runner's watchdog (leaves records behind),
2. the workflow's ``timeout-minutes`` (cancels the job; the teardown job
   terminates the pod),
3. the pod's own self-destruct timer, started by the startup script, which
   terminates the pod through the API even if GitHub never reaches it.

``reap`` is the fourth, hourly, for anything that slipped through.

Network volume: pods are pinned to the volume's data center and mount it at
``/workspace``; the HF cache, pie build cache, miniatures and reference
cache all live there, so a fresh pod starts warm.

Only outbound connectivity is needed: the runner polls GitHub, results go
up as job artifacts.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass

from pie_evals.schema import PlatformSpec

API = "https://api.runpod.io/graphql"
RUNNER_VERSION = "2.321.0"


@dataclass
class PodHandle:
    id: str
    labels: list[str]
    data_center: str | None = None


def _gql(query: str, variables: dict | None = None, api_key: str | None = None) -> dict:
    import requests

    key = api_key or os.environ["RUNPOD_API_KEY"]
    r = requests.post(API, params={"api_key": key}, json={"query": query, "variables": variables or {}}, timeout=60)
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]


# ---- discovery -------------------------------------------------------------------

def gpu_types(api_key: str | None = None) -> list[dict]:
    """Every GPU type RunPod knows: id (the string ``gpuTypeId`` wants),
    display name, memory, secure/community availability."""
    q = """query { gpuTypes { id displayName memoryInGb secureCloud communityCloud
             lowestPrice(input: {gpuCount: 1}) { minimumBidPrice uninterruptablePrice stockStatus } } }"""
    return _gql(q, api_key=api_key)["gpuTypes"]


def validate_platforms(platforms: dict[str, PlatformSpec], api_key: str | None = None) -> list[str]:
    """Return problems for platforms whose ``runpod_gpu_type`` is not a known id."""
    known = {g["id"] for g in gpu_types(api_key)}
    return [f"platform {p.id}: runpod_gpu_type {p.runpod_gpu_type!r} is not a RunPod GPU type id" for p in platforms.values() if p.runpod_gpu_type and p.runpod_gpu_type not in known]


def network_volume(volume_id: str, api_key: str | None = None) -> dict:
    """The volume's data center — pods must be created there to mount it."""
    q = "query { myself { networkVolumes { id name size dataCenterId } } }"
    for v in _gql(q, api_key=api_key)["myself"]["networkVolumes"]:
        if v["id"] == volume_id:
            return v
    raise RuntimeError(f"network volume {volume_id} not found on this account")


# ---- startup ----------------------------------------------------------------------

def startup_script(
    labels: list[str],
    *,
    repo: str,
    runner_token: str,
    image_version: str,
    kill_minutes: int,
    network_volume_mount: str = "/workspace",
    runner_version: str = RUNNER_VERSION,
) -> str:
    """Bash run inside the pod: self-destruct timer, caches on the volume,
    install the Actions runner if the image lacks it, register ephemeral,
    run one job, then terminate the pod."""
    lab = ",".join(labels + [f"img-{image_version}"])
    return f"""#!/bin/bash
set -uo pipefail
export HF_HUB_CACHE={network_volume_mount}/hf
export PIE_EVALS_CACHE={network_volume_mount}/pie-evals-cache
export PIE_ROOT={network_volume_mount}/pie
mkdir -p "$HF_HUB_CACHE" "$PIE_EVALS_CACHE"
self_destruct() {{ sleep $(( {kill_minutes} * 60 )); echo "self-destruct: {kill_minutes} min elapsed"; runpodctl remove pod "$RUNPOD_POD_ID" || true; }}
self_destruct &
if [ ! -x /actions-runner/run.sh ]; then
  mkdir -p /actions-runner && cd /actions-runner
  curl -sL https://github.com/actions/runner/releases/download/v{runner_version}/actions-runner-linux-x64-{runner_version}.tar.gz | tar xz
  ./bin/installdependencies.sh >/dev/null 2>&1 || true
fi
cd /actions-runner
export RUNNER_ALLOW_RUNASROOT=1
./config.sh --unattended --ephemeral --url https://github.com/{repo} --token {runner_token} \\
  --name "runpod-$(hostname)" --labels "{lab}" --work _work
./run.sh
runpodctl remove pod "$RUNPOD_POD_ID" || true
"""


# ---- lifecycle --------------------------------------------------------------------

def create_pod(
    platform: PlatformSpec,
    *,
    image: str,
    repo: str,
    runner_token: str,
    image_version: str,
    kill_minutes: int,
    network_volume_id: str | None = None,
    volume_gb: int = 200,
    container_disk_gb: int = 100,
    cloud_type: str = "SECURE",
    allowed_cuda_versions: list[str] | None = None,
    api_key: str | None = None,
) -> PodHandle:
    if not platform.runpod_gpu_type:
        raise ValueError(f"platform {platform.id} has no runpod_gpu_type")
    key = api_key or os.environ["RUNPOD_API_KEY"]
    name = f"pie-evals-{platform.id}-{int(time.time())}"
    script = startup_script(platform.runner_labels, repo=repo, runner_token=runner_token, image_version=image_version, kill_minutes=kill_minutes)
    q = """
    mutation($input: PodFindAndDeployOnDemandInput!) {
      podFindAndDeployOnDemand(input: $input) { id name }
    }"""
    inp: dict = {
        "name": name,
        "imageName": image,
        "gpuTypeId": platform.runpod_gpu_type,
        "gpuCount": platform.count,
        "cloudType": cloud_type,
        "volumeInGb": 0 if network_volume_id else volume_gb,
        "containerDiskInGb": container_disk_gb,
        "dockerArgs": f"bash -lc {json.dumps(script)}",
        # the pod needs the key only to terminate itself (self-destruct + end of job)
        "env": [
            {"key": "PIE_EVALS_PLATFORM", "value": platform.id},
            {"key": "RUNPOD_API_KEY", "value": key},
            {"key": "PIE_EVALS_KILL_MINUTES", "value": str(kill_minutes)},
        ],
    }
    if allowed_cuda_versions:
        inp["allowedCudaVersions"] = allowed_cuda_versions
    data_center = None
    if network_volume_id:
        vol = network_volume(network_volume_id, key)
        data_center = vol["dataCenterId"]
        inp["networkVolumeId"] = network_volume_id
        inp["volumeMountPath"] = "/workspace"
        inp["dataCenterId"] = data_center
    data = _gql(q, {"input": inp}, key)
    return PodHandle(id=data["podFindAndDeployOnDemand"]["id"], labels=platform.runner_labels, data_center=data_center)


def terminate_pod(pod_id: str, api_key: str | None = None) -> None:
    _gql("mutation($id: String!) { podTerminate(input: {podId: $id}) }", {"id": pod_id}, api_key)


def list_pods(api_key: str | None = None) -> list[dict]:
    data = _gql("query { myself { pods { id name desiredStatus lastStatusChange runtime { uptimeInSeconds } } } }", api_key=api_key)
    return data["myself"]["pods"]


def reap(max_age_s: int, api_key: str | None = None, dry_run: bool = False) -> list[str]:
    """Terminate pie-evals pods older than ``max_age_s`` (orphans from failed workflows)."""
    killed = []
    now = time.time()
    for p in list_pods(api_key):
        if not p["name"].startswith("pie-evals-"):
            continue
        try:
            created = int(p["name"].rsplit("-", 1)[-1])
        except ValueError:
            continue
        if now - created > max_age_s:
            if not dry_run:
                terminate_pod(p["id"], api_key)
            killed.append(p["id"])
    return killed
