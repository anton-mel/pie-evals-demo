#!/bin/bash
# Build and push the runner image. Version = short sha of this repo + baseline pins.
set -euo pipefail
cd "$(dirname "$0")/../.."
VLLM=$(python3 -c "import yaml;print({e['id']:e.get('pin') for e in yaml.safe_load(open('matrix/engines.yaml'))['engines']}['vllm'])")
SGL=$(python3 -c "import yaml;print({e['id']:e.get('pin') for e in yaml.safe_load(open('matrix/engines.yaml'))['engines']}['sglang'])")
LCP=$(python3 -c "import yaml;print({e['id']:e.get('pin') for e in yaml.safe_load(open('matrix/engines.yaml'))['engines']}['llamacpp'])")
VER="$(git rev-parse --short HEAD)-vllm${VLLM}-sgl${SGL}-lcp${LCP}"
IMAGE="${RUNPOD_IMAGE_REPO:?set RUNPOD_IMAGE_REPO, e.g. ghcr.io/pie-project/pie-evals-runner}:${VER}"
docker build -f infra/runpod/Dockerfile --build-arg VLLM_VERSION="$VLLM" --build-arg SGLANG_VERSION="$SGL" --build-arg LLAMACPP_TAG="$LCP" -t "$IMAGE" .
docker push "$IMAGE"
echo "$IMAGE"
echo "set repo variables: RUNPOD_IMAGE=$IMAGE RUNPOD_IMAGE_VERSION=$VER"
