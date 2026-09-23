# Coverage — smoke

| status | cells |
|---|---|
| pass | 0 |
| fail | 31 |
| declared_unsupported | 166 |
| not_run | 398 |
| noisy | 60 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | control-aa | text-completion-bench | tp1 | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--deep |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--deep |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--deep |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | fail | harness_invalid | bench exited 0 without writing bench.json; last output: max forward requests: 2 \| batch size hist:   [0, 256, 0, 0, 0,  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | harness_invalid | bench exited 0 without writing bench.json; last output: batch size hist:   [8, 256, 0, 0, 0, 0, 0, 0] \| --------------- |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | harness_invalid | bench exited 0 without writing bench.json; last output: batch size hist:   [495, 0, 0, 0, 0, 0, 0, 0] \| --------------- |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | control-aa | text-completion-bench | tp1 | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--open |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--open |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--open |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | control-aa | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | c8 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | c32 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | lc-2k-128 | prefill-rows | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | lc-2k-128 | trackb-h2o | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | llama-3.2-1b-bf16 | ss-128-64 | lora-probe | tp1 | fail | load_fail | checkpoint unavailable for llama-3.2-1b-bf16: "checkpoint meta-llama/Llama-3.2-1B-Instruct not in HF cache /workspace/.h |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | control-aa | text-completion-bench | tp1 | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--Qwen |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--Qwen |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--Qwen |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | fail | harness_invalid | bench exited 0 without writing bench.json; last output: max forward requests: 2 \| batch size hist:   [0, 256, 0, 0, 0,  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | harness_invalid | bench exited 0 without writing bench.json; last output: batch size hist:   [0, 0, 0, 0, 0, 0, 0, 0] \| ----------------- |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | harness_invalid | bench exited 0 without writing bench.json; last output: batch size hist:   [8, 0, 0, 0, 0, 0, 0, 0] \| ----------------- |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | control-aa | text-completion-bench | tp1 | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--Qwen |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--Qwen |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | load_fail | RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: "/workspace/.hf/hub/models--Qwen |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | prefill-rows | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | deepseek-v4-flash-mini6 | ss-128-64 | lora-probe | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | prefill-rows | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | lora-probe | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | c32 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | lc-8k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | mixed-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | lc-2k-128 | prefill-rows | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | lc-2k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3-0.6b-bf16 | ss-128-64 | lora-probe | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | c32 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | mixed-256 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | prefill-rows | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-h2o | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-snapkv | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | lora-probe | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | llama-3.2-1b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3-0.6b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini6 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini6 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini6 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini6 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini6 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini6 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini6 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3-0.6b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3-0.6b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3-0.6b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3-0.6b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3-0.6b-bf16 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini8 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini8 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini8 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | llama-3.2-1b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3-0.6b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini8 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | llama-3.2-1b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3-0.6b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini8 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini6 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | llama-3.2-1b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3-0.6b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini8 | ss-128-64 | lora-probe | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|
| pie/mini-dit is not an HF repo; needs a checkpoint source | 72 |
| shrink_checkpoint.py has no nemotron_h reader (supported: deepseek_v4, glm_moe_dsa, gpt_oss, kimi, muse_glimmer, qwen3_5_moe, qwen4_exp) | 67 |
| CUDA engine exposes no draft head (Metal only) — wiki speculative-decoding/ | 27 |

## pie pass rate by family × platform

| family | l40s-x1 | l40s-x2 | m1-max-32g | m4-pro-48g | pro4500-x1 | rtx4090-x1 |
|---|---|---|---|---|---|---|
| deepseek_v4 | 0/12 | 0/5 | 0/13 | 0/13 | 0/12 | 0/12 |
| gemma4 | 0/12 | · | 0/13 | 0/13 | 0/12 | 0/12 |
| gpt_oss | 0/12 | 0/5 | 0/13 | 0/13 | 0/12 | 0/12 |
| llama | 0/13 | · | 0/14 | 0/14 | 0/13 | 0/13 |
| qwen3 | 0/15 | 0/5 | 0/16 | 0/16 | 0/15 | 0/15 |
| qwen3_5 | 0/13 | · | 0/14 | 0/14 | 0/13 | 0/13 |
| qwen3_6_moe | 0/14 | 0/5 | 0/15 | 0/15 | 0/14 | 0/14 |
