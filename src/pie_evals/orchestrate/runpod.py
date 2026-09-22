"""RunPod launcher. A pod is created with a startup command that registers an
*ephemeral* GitHub self-hosted runner carrying the platform's labels; the
workflow's bench job then lands on it. The pod is torn down by the workflow
(`if: always()`), and ``reap`` kills orphans older than a TTL by label.

Only outbound connectivity is needed: the runner polls GitHub, the node
uploads results as job artifacts.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass

from pie_evals.schema import PlatformSpec

API = "https://api.runpod.io/graphql"


@dataclass
class PodHandle:
    id: str
    labels: list[str]


def _gql(query: str, variables: dict | None = None, api_key: str | None = None) -> dict:
    import requests

    key = api_key or os.environ["RUNPOD_API_KEY"]
    r = requests.post(API, params={"api_key": key}, json={"query": query, "variables": variables or {}}, timeout=60)
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]


def startup_script(labels: list[str], *, repo: str, runner_token: str, image_version: str, network_volume_mount: str = "/workspace") -> str:
    """Bash run inside the pod: register an ephemeral runner and start it."""
    lab = ",".join(labels + [f"img-{image_version}"])
    return f"""#!/bin/bash
set -euo pipefail
export HF_HUB_CACHE={network_volume_mount}/hf
export PIE_EVALS_CACHE={network_volume_mount}/pie-evals-cache
mkdir -p "$HF_HUB_CACHE" "$PIE_EVALS_CACHE"
cd /actions-runner
./config.sh --unattended --ephemeral --url https://github.com/{repo} --token {runner_token} \\
  --name "runpod-$(hostname)" --labels "{lab}" --work _work
./run.sh
"""


def create_pod(
    platform: PlatformSpec,
    *,
    image: str,
    repo: str,
    runner_token: str,
    image_version: str,
    network_volume_id: str | None = None,
    volume_gb: int = 200,
    container_disk_gb: int = 100,
    cloud_type: str = "SECURE",
    api_key: str | None = None,
) -> PodHandle:
    if not platform.runpod_gpu_type:
        raise ValueError(f"platform {platform.id} has no runpod_gpu_type")
    name = f"pie-evals-{platform.id}-{int(time.time())}"
    script = startup_script(platform.runner_labels, repo=repo, runner_token=runner_token, image_version=image_version)
    q = """
    mutation($input: PodFindAndDeployOnDemandInput!) {
      podFindAndDeployOnDemand(input: $input) { id name }
    }"""
    inp = {
        "name": name,
        "imageName": image,
        "gpuTypeId": platform.runpod_gpu_type,
        "gpuCount": platform.count,
        "cloudType": cloud_type,
        "volumeInGb": 0 if network_volume_id else volume_gb,
        "containerDiskInGb": container_disk_gb,
        "dockerArgs": f"bash -lc {json.dumps(script)}",
        "env": [{"key": "PIE_EVALS_PLATFORM", "value": platform.id}],
    }
    if network_volume_id:
        inp["networkVolumeId"] = network_volume_id
        inp["volumeMountPath"] = "/workspace"
    data = _gql(q, {"input": inp}, api_key)
    return PodHandle(id=data["podFindAndDeployOnDemand"]["id"], labels=platform.runner_labels)


def terminate_pod(pod_id: str, api_key: str | None = None) -> None:
    _gql("mutation($id: String!) { podTerminate(input: {podId: $id}) }", {"id": pod_id}, api_key)


def list_pods(api_key: str | None = None) -> list[dict]:
    data = _gql("query { myself { pods { id name desiredStatus lastStatusChange } } }", api_key=api_key)
    return data["myself"]["pods"]


def reap(max_age_s: int = 6 * 3600, api_key: str | None = None, dry_run: bool = False) -> list[str]:
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
