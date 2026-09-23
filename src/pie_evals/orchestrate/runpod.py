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

GRAPHQL = "https://api.runpod.io/graphql"


def _gql(query: str, api_key: str | None = None) -> dict:
    """The REST API has no GPU-type listing (verified: /v1/gputypes is not in
    its spec); discovery stays on GraphQL, which the same key authorizes."""
    import requests

    key = api_key or os.environ["RUNPOD_API_KEY"]
    r = requests.post(GRAPHQL, params={"api_key": key}, json={"query": query}, timeout=60)
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]


def gpu_types(api_key: str | None = None) -> list[dict]:
    """GPU types: ``id`` is what a pod request's ``gpuTypeIds`` wants."""
    return _gql("{ gpuTypes { id displayName memoryInGb secureCloud communityCloud } }", api_key)["gpuTypes"]


def data_centers(api_key: str | None = None) -> list[dict]:
    return _gql("{ dataCenters { id name location storageSupport } }", api_key)["dataCenters"]


def stock(gpu_type_id: str, data_center_id: str, gpu_count: int = 1, api_key: str | None = None) -> str:
    q = f'{{ gpuTypes(input:{{id:"{gpu_type_id}"}}) {{ lowestPrice(input:{{gpuCount:{gpu_count}, secureCloud:true, dataCenterId:"{data_center_id}"}}) {{ stockStatus }} }} }}'
    g = _gql(q, api_key)["gpuTypes"] or [{}]
    return ((g[0].get("lowestPrice") or {}).get("stockStatus")) or "None"


def validate_platforms(platforms: dict[str, PlatformSpec], api_key: str | None = None) -> list[str]:
    known = {g["id"] for g in gpu_types(api_key)}
    return [f"platform {p.id}: runpod_gpu_type {p.runpod_gpu_type!r} is not a RunPod GPU type id" for p in platforms.values() if p.runpod_gpu_type and p.runpod_gpu_type not in known]


def network_volume(volume_id: str, api_key: str | None = None) -> dict:
    """The volume record; pods must be created in its ``dataCenterId`` to mount it."""
    return dict(_req("GET", f"/networkvolumes/{volume_id}", api_key=api_key))


def create_network_volume(name: str, size_gb: int, data_center_id: str, api_key: str | None = None) -> dict:
    return dict(_req("POST", "/networkvolumes", {"name": name, "size": size_gb, "dataCenterId": data_center_id}, api_key))


# ---- startup ----------------------------------------------------------------------

def startup_script(labels: list[str], *, repo: str, kill_minutes: int, image_version: str = "latest", volume: str = VOLUME, debug: bool = False) -> str:
    """Runs as the pod's start command on the runpod-ci-runner image.

    Every step is logged to ``/tmp/pie-evals-logs/start.log`` (never the
    token). With ``debug`` the log directory is served on port 8080 — reachable
    through RunPod's proxy at ``https://<pod>-8080.proxy.runpod.net/start.log``
    — and a failed registration keeps the pod alive for 10 minutes instead of
    terminating at once, so the log can be read."""
    lab = ",".join(labels + [f"img-{image_version}"])
    hold = "600" if debug else "0"
    return f"""#!/usr/bin/env bash
set -o pipefail
V={volume}
mkdir -p /tmp/pie-evals-logs
exec > >(tee -a /tmp/pie-evals-logs/start.log) 2>&1
echo "== start $(date -u +%FT%TZ) pod=${{RUNPOD_POD_ID:-?}} platform=${{PIE_EVALS_PLATFORM:-?}}"
echo "== $(nvidia-smi --query-gpu=name,driver_version,compute_cap,memory.total --format=csv,noheader 2>/dev/null || echo 'no GPU visible')"
{"(cd /tmp/pie-evals-logs && python3 -m http.server 8080 >/dev/null 2>&1 &)" if debug else ""}
terminate() {{ echo "== terminate $(date -u +%FT%TZ)"; curl -fsS -X DELETE -H "Authorization: Bearer ${{RUNPOD_API_KEY:-}}" "https://rest.runpod.io/v1/pods/${{RUNPOD_POD_ID:-}}" >/dev/null 2>&1 || true; }}
( sleep $(( {kill_minutes} * 60 )); echo "== self-destruct: {kill_minutes} min"; terminate ) &
if [ ! -x "$V/.cargo/bin/rustup" ]; then
  echo "== installing rustup on $V"; mkdir -p "$V"
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | RUSTUP_HOME=$V/.rustup CARGO_HOME=$V/.cargo sh -s -- -y --profile minimal --default-toolchain none --no-modify-path || echo "== rustup install failed (non-fatal)"
fi
mkdir -p /tmp/_work "$V/.pie" "$V/.hf" "$V/.uv" "$V/.npm" "$V/pie-evals-cache" /tmp/target /tmp/pie
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
PIE_EVALS_PLATFORM=${{PIE_EVALS_PLATFORM:-}}
PATH=$V/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV
echo "== env written; volume: $(df -h $V 2>/dev/null | tail -1)"
# a pre-minted registration token (1 h, can only register a runner) is preferred over a PAT in the pod
if [ -n "${{PIE_EVALS_EXEC:-}}" ]; then
  echo "== exec mode"; set -a; . /opt/actions-runner/.env; set +a
  echo "== disk:"; df -h / /tmp $V 2>/dev/null | tail -n +1; echo "== mem:"; free -g | head -2
  bash -c "$PIE_EVALS_EXEC"; RC=$?; echo "== exec exit $RC $(date -u +%FT%TZ)"; echo "== disk after:"; df -h / /tmp $V 2>/dev/null
  sleep {hold}; terminate; exit $RC
fi
TOKEN="${{GH_RUNNER_TOKEN:-}}"
if [ -z "$TOKEN" ]; then
  echo "== minting registration token from PAT"
  TOKEN=$(curl -fsS -X POST -H "Authorization: Bearer ${{GH_RUNNER_PAT:-}}" -H "Accept: application/vnd.github+json" "https://api.github.com/repos/{repo}/actions/runners/registration-token" | jq -r .token)
fi
echo "== token present: $([ -n "$TOKEN" ] && [ "$TOKEN" != null ] && echo yes || echo NO)"
cd /opt/actions-runner || {{ echo "== no /opt/actions-runner"; sleep {hold}; terminate; exit 1; }}
export RUNNER_ALLOW_RUNASROOT=1
./config.sh --unattended --replace --ephemeral --disableupdate --url "https://github.com/{repo}" --token "$TOKEN" \
  --name "runpod-${{RUNPOD_POD_ID:-$(hostname)}}" --labels "{lab}" --work /tmp/_work
RC=$?; echo "== config.sh exit $RC"
if [ $RC -ne 0 ]; then sleep {hold}; terminate; exit $RC; fi
./run.sh; RC=$?; echo "== run.sh exit $RC $(date -u +%FT%TZ)"
terminate
sleep 60
"""


# ---- placement --------------------------------------------------------------------

@dataclass
class Placement:
    data_center: str | None
    volume_id: str | None
    stock: str
    note: str


def choose_placement(gpu_type_id: str, gpu_count: int, *, volumes: dict[str, str], preferred: list[str] | None = None, api_key: str | None = None) -> Placement:
    """Pick where a pod goes: the first data center, in preference order,
    that has stock for the GPU **and** a volume; else any storage-capable
    data center with stock (no volume — cold caches, still a valid run);
    else let RunPod place it anywhere (no pin, no volume)."""
    order = [dc for dc in (preferred or []) if dc in volumes] + [dc for dc in volumes if dc not in (preferred or [])]
    seen: dict[str, str] = {}
    for dc in order:
        st = stock(gpu_type_id, dc, gpu_count, api_key)
        seen[dc] = st
        if st not in ("None", "-", ""):
            return Placement(dc, volumes[dc], st, f"volume DC with stock ({st})")
    for dc in [d["id"] for d in data_centers(api_key) if d.get("storageSupport") and d["id"] not in seen]:
        st = stock(gpu_type_id, dc, gpu_count, api_key)
        if st not in ("None", "-", ""):
            return Placement(dc, None, st, f"no volume in any DC with stock; using {dc} without volume (checked {seen})")
    return Placement(None, None, "None", f"no secure stock anywhere for {gpu_type_id} x{gpu_count} right now (checked {seen}); unpinned request")


# ---- lifecycle --------------------------------------------------------------------

def create_pod(
    platform: PlatformSpec,
    *,
    repo: str,
    runner_pat: str | None,
    kill_minutes: int,
    runner_token: str | None = None,
    image: str = DEFAULT_IMAGE,
    image_version: str = "latest",
    network_volume_id: str | None = None,
    volumes: dict[str, str] | None = None,
    preferred_data_centers: list[str] | None = None,
    container_disk_gb: int = 40,
    cloud_type: str = "SECURE",
    allowed_cuda_versions: list[str] | None = None,
    api_key: str | None = None,
    debug: bool = False,
    exec_script: str | None = None,
    log=print,
) -> PodHandle:
    if not platform.runpod_gpu_type:
        raise ValueError(f"platform {platform.id} has no runpod_gpu_type")
    if not (runner_pat or runner_token or exec_script):
        raise ValueError("need runner_token (pre-minted registration token) or runner_pat, or an exec script")
    key = api_key or os.environ["RUNPOD_API_KEY"]
    name = f"pie-evals-{platform.id}-{int(time.time())}"
    script = startup_script(platform.runner_labels, repo=repo, kill_minutes=kill_minutes, image_version=image_version, debug=debug)
    body: dict = {
        "name": name,
        "imageName": image,
        "gpuTypeIds": [platform.runpod_gpu_type],
        "gpuCount": platform.count,
        "cloudType": cloud_type,
        "computeType": "GPU",
        "containerDiskInGb": container_disk_gb,
        "volumeInGb": 0,
        "ports": ["8080/http"] if debug else [],
        "dockerStartCmd": ["bash", "-lc", script],
        "env": {
            "PIE_EVALS_PLATFORM": platform.id,
            "PIE_EVALS_KILL_MINUTES": str(kill_minutes),
            **({"GH_RUNNER_TOKEN": runner_token} if runner_token else {}),
            **({"PIE_EVALS_EXEC": exec_script} if exec_script else {}),
            **({"GH_RUNNER_PAT": runner_pat} if runner_pat else {}),
            "RUNPOD_API_KEY": key,  # self-termination only
        },
    }
    if allowed_cuda_versions:
        body["allowedCudaVersions"] = allowed_cuda_versions
    data_center = None
    if network_volume_id:  # explicit volume: pin to its DC, no stock check
        vol = network_volume(network_volume_id, key)
        data_center = vol.get("dataCenterId")
        body["networkVolumeId"] = network_volume_id
        body["volumeMountPath"] = VOLUME
        if data_center:
            body["dataCenterIds"] = [data_center]
    elif volumes:
        pl = choose_placement(platform.runpod_gpu_type, platform.count, volumes=volumes, preferred=preferred_data_centers, api_key=key)
        log(f"placement for {platform.id}: dc={pl.data_center} volume={pl.volume_id} — {pl.note}")
        data_center = pl.data_center
        if pl.data_center:
            body["dataCenterIds"] = [pl.data_center]
        if pl.volume_id:
            body["networkVolumeId"] = pl.volume_id
            body["volumeMountPath"] = VOLUME
    data = None
    for attempt in range(1, 4):  # RunPod answers 500 "Something went wrong" transiently
        try:
            data = _req("POST", "/pods", body, key)
            break
        except RuntimeError as e:
            if attempt == 3 or " 5" not in str(e)[:40]:
                raise
            log(f"create pod attempt {attempt} failed ({str(e)[:120]}); retrying in 20 s")
            time.sleep(20)
    assert data is not None
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
