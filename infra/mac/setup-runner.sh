#!/bin/bash
# Register this Mac as a resident GitHub self-hosted runner for pie-evals.
# Usage: PLATFORM_ID=m1-max-32g REPO=pie-project/pie-evals ./setup-runner.sh <registration-token>
# One runner per Mac (a second concurrent job would be noise, not a measurement).
set -euo pipefail
TOKEN="${1:?registration token}"
PLATFORM_ID="${PLATFORM_ID:?platform id from matrix/platforms.yaml}"
REPO="${REPO:-pie-project/pie-evals}"
RUNNER_VERSION="${RUNNER_VERSION:-2.321.0}"
DIR="$HOME/actions-runner"
mkdir -p "$DIR" && cd "$DIR"
[ -f run.sh ] || curl -sL "https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-osx-arm64-${RUNNER_VERSION}.tar.gz" | tar xz
./config.sh --unattended --url "https://github.com/$REPO" --token "$TOKEN" --name "$(scutil --get ComputerName)-$PLATFORM_ID" \
  --labels "self-hosted,macos,$PLATFORM_ID" --work _work --replace
./svc.sh install && ./svc.sh start
cat <<MSG
Registered. Before the first benchmark on this machine:
  * AC power, Low Power Mode off, High Power mode where available (the node checks pmset and records it)
  * nothing else on the GPU; note the number of external displays
  * install: brew install uv rustup && rustup target add wasm32-wasip2; /tmp/pievenv with mlx-lm at the pin; llama.cpp at the pin
  * if this chip is not in pie's device_tuning table, run pie's tune sweep first (see docs/design.md §platforms)
MSG
