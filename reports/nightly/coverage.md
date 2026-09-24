# Coverage — nightly

| status | cells |
|---|---|
| pass | 627 |
| fail | 694 |
| declared_unsupported | 8933 |
| not_run | 4882 |
| noisy | 184 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submissio |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: "checkpoint openai/gpt-oss-20b not in HF cache /workspace/.hf/hub (run `pi |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: "checkpoint openai/gpt-oss-20b not in HF cache /workspace/.hf/hub (run `pi |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | hang | timed out (hang is only ever observed via timeout) |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 814.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.47 GiB. GPU 0 has a total capacity of 79.25 GiB of which |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.46 GiB. GPU 0 has a total capacity of 79.25 GiB of which |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.49 GiB. GPU 0 has a total capacity of 79.25 GiB of which |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.48 GiB. GPU 0 has a total capacity of 79.25 GiB of which |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.50 GiB. GPU 0 has a total capacity of 79.25 GiB of which |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 836.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.49 GiB. GPU 0 has a total capacity of 79.25 GiB of which |
| pie | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | fail |  |  |
| pie | a100-x2 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| vllm | a100-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | a100-x2 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| pie | a100-x2 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 122] Disk quota exceeded' |
| pie | a100-x2 | kimi-k3-mini8 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| pie | a100-x2 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: Unable to dynamically load the "nccl" shared library - searc |
| sglang | a100-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 688.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 748.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 764.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 762.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 766.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 764.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| sglang | a100-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | fail | oom | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 762.00 MiB. GPU 0 has a total capacity of 79.25 GiB of whi |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | fail | doesnt_fit | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-sglang-0.5.20/bi |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-sglang-0.5.20/bi |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-sglang-0.5.20/bi |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-sglang-0.5.20/bi |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-sglang-0.5.20/bi |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-sglang-0.5.20/bi |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-26b-a4b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | l40s-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | checkpoint unavailable for gemma-4-31b-mlx4: 'Task error: File reconstruction error: IO Error: No space left on device ( |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-vllm-0.30.0/bin/ |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-vllm-0.30.0/bin/ |
| pie | l40s-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 5 |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 2 |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | l40s-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Invalid control character at: line 1 column 9 (char 8) |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-vllm-0.30.0/bin/ |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-vllm-0.30.0/bin/ |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | AttributeError: type object 'ServerArgs' has no attribute '__dataclass_fields__' |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | fail | crash | AttributeError: type object 'ServerArgs' has no attribute '__dataclass_fields__' |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | AttributeError: type object 'ServerArgs' has no attribute '__dataclass_fields__' |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | crash | AttributeError: type object 'ServerArgs' has no attribute '__dataclass_fields__' |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_output_tokens' |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_output_tokens' |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_output_tokens' |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 28] No space left on device' |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4-mini5: 'OSError: [Errno 28] No space left on device' |
| vllm | l40s-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'RuntimeError: GET https://huggingface.co/moonshotai/Kimi-K3/resolve/main/conf |
| vllm | l40s-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'OSError: [Errno 28] No space left on device' |
| vllm | l40s-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for kimi-k3-mini8: 'OSError: [Errno 28] No space left on device' |
| sglang | l40s-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | crash | ValueError: The repository /workspace/.hf/hub/models--moonshotai--Kimi-K3/snapshots/mini-l0-7-e32-b4 contains custom cod |
| sglang | l40s-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | crash | ValueError: The repository /workspace/.hf/hub/models--moonshotai--Kimi-K3/snapshots/mini-l0-7-e32-b4 contains custom cod |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | fail |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-vllm-0.30.0/bin/ |
| vllm | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | engine setup: Command '['uv', 'pip', 'install', '--quiet', '--python', '/workspace/pie-evals-cache/venv-vllm-0.30.0/bin/ |
| sglang | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for qwen3.5-0.8b-bf16: '[Errno 28] No space left on device' |
| sglang | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for qwen3.5-0.8b-bf16: '[Errno 28] No space left on device' |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | fail | crash | all 128 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | fail | crash | all 256 requests failed: out take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admissio |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | fail | crash | all 1024 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admissio |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission a |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 5 |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 2 |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | all 64 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | fail | crash | all 256 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | fail | crash | all 256 requests failed: drain prefill chunk @0: drop_tok_c take: channel is poisoned: pipeline: forward failed: direct  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | fail |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: verify-and-extend: pipeline: frame slot 0: pipeline: KV capacity: state pool starved: 1 slots ask |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: KeyError: 'num_output_tokens' |
| pie | l40s-x2 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | all 8 requests failed: verify-and-extend: pipeline: register+bind: device: this tensor-parallel group is poisoned: rank  |
| pie | l40s-x2 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp2 | fail | load_fail | checkpoint unavailable for glm-5.3-flash-mini8: 'OSError: [Errno 28] No space left on device' |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | fail | load_fail | artifact import: ✗ decoding failed: checkpoint: cannot spool 'layer.0.expert_gate_up_bank' to /workspace/pie-evals-cache |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| pie | l40s-x2 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | all 8 requests failed: verify-and-extend: pipeline: register+bind: device: this tensor-parallel group is poisoned: rank  |
| pie | l40s-x2 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating cuda TP engine group for model "defau |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | l40s-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | fail | load_fail | pie build failed: Command '['cargo', 'build', '--release', '-p', 'pie', '--bin', 'pie', '--features', 'metal']' returned |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie build failed: Command '['cargo', 'build', '--release', '-p', 'pie', '--bin', 'pie', '--features', 'metal']' returned |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | fail | load_fail | pie build failed: Command '['cargo', 'build', '--release', '-p', 'pie', '--bin', 'pie', '--features', 'metal']' returned |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | fail | load_fail | pie build failed: Command '['cargo', 'build', '--release', '-p', 'pie', '--bin', 'pie', '--features', 'metal']' returned |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | pie build failed: Command '['cargo', 'build', '--release', '-p', 'pie', '--bin', 'pie', '--features', 'metal']' returned |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie build failed: Command '['cargo', 'build', '--release', '-p', 'pie', '--bin', 'pie', '--features', 'metal']' returned |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_prompt_tokens' |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_prompt_tokens' |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: truth take: channel is poisoned: pipeline: forward failed: direct launch rejected: load failed: t |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 5 |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 2 |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Invalid control character at: line 1 column 10 (char 9) |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | pro6000-x1 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: truth take: channel is poisoned: pipeline: forward failed: direct launch rejected: load failed: t |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | crash | ConnectionError: WebSocket connection closed |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | does not fit beside the short shapes: pie serve exited before ready: RuntimeError: start: boot embedded worker: creating |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | does not fit beside the short shapes: pie serve exited before ready: RuntimeError: start: boot embedded worker: creating |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: d |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | fail | crash | all 8 requests failed: decode frame submit: pipeline: frame slot 0: pipeline: pipeline failed: pipeline: forward failed: |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | fail | crash | all 128 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | fail | crash | all 256 requests failed: out take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admissio |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | fail | crash | all 1024 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: impossible sub |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 5 |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | all 64 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | fail | crash | all 256 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | fail | crash | all 256 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: impossible subm |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: @0: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admi |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | all 4 requests failed: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admi |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_output_tokens' |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame ad |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: uncond_prefill_logits take: channel is poisoned: pipeline: forward failed: direct launch rejected |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submissio |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: truth take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submis |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: @0: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | fail | crash | all 4 requests failed: @0: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: uncond_prefill_logits take: channel is poisoned: pipeline: forward failed: direct launch rejected |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | crash | RuntimeError: No accelerator (CUDA, XPU, HPU, NPU, MUSA, MPS) or platform plugin is available. |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: reading the model metadata for "default": cann |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | fail |  |  |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | fail |  |  |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 5 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | harness_invalid | GPU preflight: cuInit answered 999 |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail |  |  |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: truth take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submis |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: truth take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admissio |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | pie serve exited before ready: pyo3_runtime.PanicException: value 55 is weight 16, a split-plane bank; it resolves throu |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission a |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission a |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission a |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | fail | crash | all 32 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission  |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | fail | crash | all 128 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | fail | crash | all 256 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | fail | crash | all 1024 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admissio |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission a |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission a |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 5 |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | all 4 requests failed: prefill chunk submit @0: pipeline: frame slot 0: pipeline: this fire would grow its sequence to 2 |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | all 64 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission  |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | crash | all 256 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | crash | all 256 requests failed: decode frame submit: pipeline: frame slot 0: pipeline: pipeline failed: pipeline: forward faile |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: @0: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame  |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | fail | crash | all 4 requests failed: @0: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame  |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | fail | crash | all 4 requests failed: first_token take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid  |
| pie | rtx5090-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: uncond_prefill_logits take: channel is poisoned: pipeline: forward failed: direct launch rejected |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | fail | load_fail | checkpoint unavailable for gpt-oss-20b-mxfp4: 'Task error: File reconstruction error: Internal Writer Error: Background  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | fail | crash | RuntimeError: Cannot find any model weights with `/workspace/.hf/hub/models--openai--gpt-oss-20b/snapshots/6cee5e81ee839 |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | crash | vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. |
| pie | rtx5090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | all 8 requests failed: JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore': 1} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | fail | crash | RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx5090-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | fail | crash | pie serve exited before ready: FileNotFoundError: no local snapshot for '/workspace/.hf/hub/models--unsloth--Qwen3.6-27B |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | crash | all 8 requests failed: truth take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submis |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | fail | load_fail | artifact import: ✗ cannot read /workspace/.hf/hub/models--mlx-community--Qwen3.6-35B-A3B-4bit/snapshots/38740b847e4cb78f |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | fail | load_fail | checkpoint unavailable for qwen3.6-35b-a3b-mlx4: 'Task error: File reconstruction error: Internal Writer Error: Backgrou |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | noisy |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | noisy |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | noisy |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | noisy |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp2,ngram | noisy |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | noisy |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | noisy |  |  |
| sglang | a100-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | noisy |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | noisy |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | noisy |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | noisy |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | noisy |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | noisy |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | noisy |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | noisy |  |  |
| pie | l40s-x1 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| pie | l40s-x1 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| sglang | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | noisy |  |  |
| sglang | l40s-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x2 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp2 | noisy |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | noisy |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp2,rs | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp2 | noisy |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | noisy |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | noisy |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| sglang | pro6000-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | noisy |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| sglang | rtx4090-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx4090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | noisy |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | noisy |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | noisy |  |  |
| pie | rtx5090-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx5090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | noisy |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | a100-pcie-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | a100-pcie-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | a100-pcie-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | a100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | a100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-pcie-x2 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-pcie-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-pcie-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | a100-pcie-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-x2 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | a100-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | a100-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | a100-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | h100-pcie-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | h100-pcie-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | h100-pcie-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | h100-pcie-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | h100-pcie-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | l40s-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | l40s-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | l40s-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | l40s-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | l40s-x2 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | l40s-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | l40s-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | l40s-x2 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | deepseek-v4-flash-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-26b-a4b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | gemma-4-31b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | glm-5.3-flash-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| llamacpp | m1-max-32g | qwen3.6-27b-gguf-q4km | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-27b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4-flash-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | deepseek-v4-flash-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | deepseek-v4.1-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | gemma-4-26b-a4b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | gemma-4-31b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | glm-5.3-flash-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | gpt-oss-20b-mlx-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| llamacpp | m2-max | qwen3.6-27b-gguf-q4km | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | qwen3.6-27b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m2-max | qwen3.6-35b-a3b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | gemma-4-31b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | glm-5.3-flash-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| llamacpp | m4-pro-48g | qwen3.6-27b-gguf-q4km | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-27b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4-flash-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | deepseek-v4-flash-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-26b-a4b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | gemma-4-31b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | glm-5.3-flash-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| llamacpp | m5-max-48g | qwen3.6-27b-gguf-q4km | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-27b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c8 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | dflash-block-acceptance | tp1,dflash2 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| mlxlm | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-26b-a4b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro4500-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro4500-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro6000-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro6000-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | pro6000-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | pro6000-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | pro6000-x2 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp2 | not_run |  |  |
| pie | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | pro6000-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| vllm | pro6000-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp2 | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| sglang | pro6000-x2 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp2,ngram | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp2 | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp2,rs | not_run |  |  |
| pie | pro6000-x2 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp2 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| vllm | pro6000-x4 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-h2o | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | trackb-snapkv | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | snapkv-eviction | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | tova-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | attention-sink | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | sliding-window-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | snapkv-eviction | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | tova-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | attention-sink | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | sliding-window-attention | tp4 | not_run |  |  |
| pie | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| vllm | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | c8 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | c32 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | c64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | c256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| vllm | pro6000-x4 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | c8 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | c32 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | c64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | c256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| vllm | pro6000-x4 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp4 | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| sglang | pro6000-x4 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp4,ngram | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-gguf-q4km | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp4 | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | rs-speculative-decoding | tp4,rs | not_run |  |  |
| pie | pro6000-x4 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp4 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-31b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx4090-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx4090-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx4090-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-27b-gguf-q4km | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | snapkv-eviction | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | tova-attention | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | attention-sink | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | sliding-window-attention | tp1 | not_run |  |  |
| pie | rtx5090-x1 | gemma-4-e4b-bf16 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx5090-x1 | gemma-4-e4b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | rtx5090-x1 | glm-5.3-flash-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx5090-x1 | kimi-k3-mini8 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| vllm | rtx5090-x1 | qwen3.5-0.8b-bf16 | c8 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | c64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | c256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| sglang | rtx5090-x1 | qwen3.5-0.8b-bf16 | mixed-256 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-27b-mlx4 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | ss-512-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | c64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | c256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | lc-32k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | kv-oversub | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | rs-speculative-decoding | tp1,rs | not_run |  |  |
| pie | rtx5090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | classifier-free-guidance | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|
| pie has no llama family reader | 952 |
| prefill-rows takes its own input (`ids`); pie_bench.py cannot drive it | 898 |
| pie/mini-dit is not an HF repo; needs a checkpoint source | 808 |
| CUDA engine exposes no draft head (Metal only) — wiki speculative-decoding/ | 764 |
| shrink_checkpoint.py has no nemotron_h reader (supported: deepseek_v4, deepseek_v41, glm_moe_dsa, gpt_oss, kimi, muse_glimmer, qwen3_5_moe, qwen4_exp) | 680 |
| returns non-JSON to pie_bench.py (JSONDecodeError); on hybrid models also needs forward-hybrid | 484 |
| return envelope lacks num_output_tokens (pie_bench.py KeyError); on hybrid models also needs forward-hybrid | 484 |
| return envelope lacks num_output_tokens (pie_bench.py KeyError) | 484 |
| seeds a fixed-size adapter bank (1572864 bytes) that must match the model's layer count; needs a per-model input contract | 484 |
| engine-cuda refuses attention.pool_lse_selected (dsv4 flash rows are CANNOT_SERVE on CUDA; Metal/Vulkan/wgpu only) | 444 |
| engine-cuda refuses attention.pool_lse_selected (dsv41 rows are CANNOT_SERVE on CUDA; Metal/Vulkan/wgpu only) | 396 |
| SGLang 0.5.20 gemma-4 crashes in its attention/view path on every card tried; revisit at the next pin | 204 |
| runner image has no nvcc; no CUDA llama.cpp build on pods yet | 204 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the qwen3_6_moe forward pass is hybrid | 192 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the qwen3_6 forward pass is hybrid | 192 |
| vLLM 0.30.0 has no deepseek_v41 (CSA2/Engram) model; revisit at the next pin | 180 |
| SGLang 0.5.20 has no deepseek_v41 (CSA2/Engram) model; revisit at the next pin | 180 |
| gemma4-26b-a4b's 2112-wide dense intermediate halves to 1056, not whole u4g64 groups, so its down plane cannot band (pie #674) | 165 |
| shape needs 8320 tokens > the artifact's max_context 4096 | 148 |
| shape needs 32896 tokens > the artifact's max_context 4096 | 148 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the qwen3_5 forward pass is hybrid | 96 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the glm5_next forward pass is hybrid | 96 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the nemotron_h forward pass is hybrid | 96 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the kimi_k3 forward pass is hybrid | 90 |
| does not fit: 27.5 GiB per device > 24.0 GiB | 64 |

## pie pass rate by family × platform

| family | a100-pcie-x1 | a100-pcie-x2 | a100-x2 | h100-pcie-x1 | l40s-x1 | l40s-x2 | m1-max-32g | m2-max | m4-pro-48g | m5-max-48g | pro4500-x1 | pro6000-x1 | pro6000-x2 | pro6000-x4 | rtx4090-x1 | rtx5090-x1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepseek_v4 | · | · | · | · | · | · | 0/25 | 0/25 | 0/25 | 0/25 | · | · | · | · | · | · |
| deepseek_v41 | · | · | · | · | · | · | 0/23 | 0/23 | 0/23 | 0/23 | · | · | · | · | · | · |
| gemma4 | 0/42 | 0/42 | 0/42 | 0/42 | 18/42 | 0/42 | 0/50 | 0/50 | 0/50 | 0/50 | 0/42 | 6/42 | 0/42 | 0/42 | 5/42 | 0/42 |
| gemma4_moe | 0/21 | · | · | 0/21 | 0/21 | · | 0/25 | 0/25 | 0/25 | 0/25 | 0/21 | 0/21 | · | · | 1/21 | 0/21 |
| glm5_next | 0/14 | 0/14 | 0/14 | 0/14 | 13/14 | 3/14 | 0/18 | 0/18 | 0/18 | 0/18 | 6/14 | 11/14 | 0/14 | 0/14 | 0/14 | 0/14 |
| gpt_oss | 0/63 | 0/63 | 0/63 | 0/63 | 24/63 | 17/63 | 0/75 | 0/75 | 0/75 | 0/75 | 0/63 | 21/63 | 0/63 | 0/63 | 24/63 | 17/63 |
| kimi_k3 | 0/14 | 0/14 | 0/14 | 0/14 | 12/14 | 12/14 | 0/18 | 0/18 | 0/18 | 0/18 | 6/14 | 6/14 | 0/14 | 0/14 | · | 0/14 |
| qwen3_5 | 11/16 | 0/16 | 0/16 | 0/16 | 14/16 | 1/16 | 0/20 | 0/20 | 0/20 | 0/20 | 8/16 | 7/16 | 0/16 | 0/16 | 12/16 | 13/16 |
| qwen3_6 | 5/32 | 0/32 | 0/32 | 0/32 | 2/32 | 0/32 | 0/40 | 0/40 | 0/40 | 0/40 | 0/32 | 0/32 | 0/32 | 0/32 | 2/32 | 0/32 |
| qwen3_6_moe | 0/32 | 0/32 | 0/32 | 14/32 | 0/32 | 22/32 | 0/40 | 0/40 | 0/40 | 0/40 | 0/32 | 8/32 | 0/32 | 0/32 | 12/32 | 0/32 |
