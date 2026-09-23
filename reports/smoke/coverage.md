# Coverage — smoke

| status | cells |
|---|---|
| pass | 14 |
| fail | 39 |
| declared_unsupported | 402 |
| not_run | 239 |
| noisy | 4 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: prompt + reserve needs 2192 KV slots, past the published attn_score ceiling of 2048 |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prompt + reserve needs 2192 KV slots, past the published attn_score ceiling of 2048 |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | fail | crash | all 8 requests failed: prefill submit @0: pipeline: register+bind: load failed: the adapter bank `lora_a` was seeded 157 |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: prompt + reserve needs 2208 KV slots, past the published attn_score ceiling of 2048 |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prompt + reserve needs 2208 KV slots, past the published attn_score ceiling of 2048 |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | fail | crash | all 8 requests failed: prefill submit @0: pipeline: register+bind: load failed: the adapter bank `lora_a` was seeded 157 |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: prompt + reserve needs 2208 KV slots, past the published attn_score ceiling of 2048 |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prompt + reserve needs 2208 KV slots, past the published attn_score ceiling of 2048 |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | fail | crash | all 8 requests failed: KeyError: 'num_output_tokens' |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | fail | load_fail | pie serve exited before ready: RuntimeError: start: boot embedded worker: creating engine for model "default" group 0: " |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro6000-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|
| pie has no llama family reader | 74 |
| pie/mini-dit is not an HF repo; needs a checkpoint source | 62 |
| shrink_checkpoint.py has no nemotron_h reader (supported: deepseek_v4, glm_moe_dsa, gpt_oss, kimi, muse_glimmer, qwen3_5_moe, qwen4_exp) | 50 |
| prefill-rows takes its own input (`ids`); pie_bench.py cannot drive it | 46 |
| returns non-JSON to pie_bench.py (JSONDecodeError); on hybrid models also needs forward-hybrid | 42 |
| return envelope lacks num_output_tokens (pie_bench.py KeyError); on hybrid models also needs forward-hybrid | 42 |
| return envelope lacks num_output_tokens (pie_bench.py KeyError) | 42 |
| CUDA engine exposes no draft head (Metal only) — wiki speculative-decoding/ | 32 |
| shape needs 8320 tokens > the artifact's max_context 4096 | 12 |

## pie pass rate by family × platform

| family | l40s-x1 | l40s-x2 | m1-max-32g | m4-pro-48g | pro4500-x1 | pro6000-x1 | rtx4090-x1 |
|---|---|---|---|---|---|---|---|
| deepseek_v4 | 0/8 | 0/4 | 0/9 | 0/9 | 0/8 | 0/8 | 0/8 |
| gemma4 | 0/9 | · | 0/10 | 0/10 | 0/9 | 0/9 | 3/9 |
| gpt_oss | 0/8 | 0/4 | 0/9 | 0/9 | 0/8 | 0/8 | 5/8 |
| qwen3_5 | 0/10 | 0/4 | 0/11 | 0/11 | 0/10 | 0/10 | 6/10 |
| qwen3_6_moe | 0/10 | 0/4 | 0/11 | 0/11 | 0/10 | 0/10 | 0/10 |
