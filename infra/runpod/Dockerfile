# RunPod runner image for pie-evals. One image serves every CUDA platform;
# the platform is a label. Baselines live in their own venvs (vLLM and
# SGLang pin different torch builds), pinned to matrix/engines.yaml.
ARG CUDA=13.0.1
FROM nvidia/cuda:${CUDA}-devel-ubuntu24.04
ARG VLLM_VERSION=0.26.1
ARG SGLANG_VERSION=0.5.16
ARG LLAMACPP_TAG=b10270
ARG RUNNER_VERSION=2.321.0
ENV DEBIAN_FRONTEND=noninteractive PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get install -y --no-install-recommends \
      git curl ca-certificates build-essential cmake pkg-config libssl-dev python3 python3-venv python3-pip \
      libcurl4-openssl-dev jq && rm -rf /var/lib/apt/lists/*
# rust (pinned by pie's rust-toolchain.toml at build time) + wasm target
RUN curl -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal && \
    /root/.cargo/bin/rustup target add wasm32-wasip2
ENV PATH=/root/.cargo/bin:$PATH
# uv + baseline venvs
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH=/root/.local/bin:$PATH
RUN uv venv /root/.venv/vllm   && uv pip install --python /root/.venv/vllm/bin/python   "vllm==${VLLM_VERSION}" && \
    uv venv /root/.venv/sglang && uv pip install --python /root/.venv/sglang/bin/python "sglang[all]==${SGLANG_VERSION}"
# llama.cpp server at the pinned tag
RUN git clone --depth 1 --branch ${LLAMACPP_TAG} https://github.com/ggml-org/llama.cpp /opt/llama.cpp && \
    cmake -S /opt/llama.cpp -B /opt/llama.cpp/build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release && \
    cmake --build /opt/llama.cpp/build --target llama-server -j && \
    ln -s /opt/llama.cpp/build/bin/llama-server /usr/local/bin/llama-server
# pie's python client deps (embedded server wheel is built from the pinned commit at job time)
RUN python3 -m pip install --break-system-packages websockets msgpack blake3 numpy transformers safetensors torch
# GitHub Actions runner
RUN mkdir /actions-runner && cd /actions-runner && \
    curl -sL https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz | tar xz && \
    ./bin/installdependencies.sh
ENV RUNNER_ALLOW_RUNASROOT=1 PIE_ROOT=/root/pie VLLM_PY=/root/.venv/vllm/bin/python SGLANG_PY=/root/.venv/sglang/bin/python \
    LLAMA_SERVER_BIN=/usr/local/bin/llama-server HF_HUB_CACHE=/workspace/hf PIE_EVALS_CACHE=/workspace/pie-evals-cache
WORKDIR /root
