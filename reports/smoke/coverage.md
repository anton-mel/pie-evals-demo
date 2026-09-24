# Coverage — smoke

| status | cells |
|---|---|
| pass | 86 |
| fail | 16 |
| declared_unsupported | 701 |
| not_run | 186 |
| noisy | 24 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | l40s-x1 | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submissio |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_output_tokens' |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: KeyError: 'num_output_tokens' |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submissio |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | pro6000-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | pro6000-x1 | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submissio |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | fail | crash | all 128 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | fail | crash | all 64 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admission  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: @0: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: tok_out_p take: channel is poisoned: pipeline: forward failed: direct launch rejected: frame admi |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | fail | crash | all 8 requests failed: g0 take: channel is poisoned: pipeline: forward failed: direct launch rejected: invalid submissio |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | fail | crash | all 4 requests failed: bind failed: intrinsic attn_score is not advertised by the engine serving this model (`ModelProfi |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | fail | crash | all 4 requests failed: prefill submit @0: bind failed: intrinsic attn_score is not advertised by the engine serving this |
| pie | l40s-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | l40s-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | pro6000-x1 | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | noisy | harness_invalid | control A/A failed on this process; numbers not read |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | glm-5.3-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | kimi-k3-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4.1-flash-mini8 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | glm-5.3-flash-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | kimi-k3-mini8 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-1k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|
| pie has no llama family reader | 80 |
| pie/mini-dit is not an HF repo; needs a checkpoint source | 62 |
| engine-cuda refuses attention.pool_lse_selected (dsv4 flash rows are CANNOT_SERVE on CUDA; Metal/Vulkan/wgpu only) | 61 |
| engine-cuda refuses attention.pool_lse_selected (dsv41 rows are CANNOT_SERVE on CUDA; Metal/Vulkan/wgpu only) | 61 |
| prefill-rows takes its own input (`ids`); pie_bench.py cannot drive it | 51 |
| returns non-JSON to pie_bench.py (JSONDecodeError); on hybrid models also needs forward-hybrid | 51 |
| return envelope lacks num_output_tokens (pie_bench.py KeyError); on hybrid models also needs forward-hybrid | 51 |
| return envelope lacks num_output_tokens (pie_bench.py KeyError) | 51 |
| seeds a fixed-size adapter bank (1572864 bytes) that must match the model's layer count; needs a per-model input contract | 51 |
| shrink_checkpoint.py has no nemotron_h reader (supported: deepseek_v4, deepseek_v41, glm_moe_dsa, gpt_oss, kimi, muse_glimmer, qwen3_5_moe, qwen4_exp) | 38 |
| CUDA engine exposes no draft head (Metal only) — wiki speculative-decoding/ | 35 |
| does not fit: 27.5 GiB per device > 24.0 GiB | 14 |
| shape needs 8320 tokens > the artifact's max_context 4096 | 12 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the qwen3_5 forward pass is hybrid | 12 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the qwen3_6_moe forward pass is hybrid | 12 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the glm5_next forward pass is hybrid | 12 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the nemotron_h forward pass is hybrid | 12 |
| attention-only KV policies are not valid on a folded recurrent state (pie: use pie:inferlet/forward-hybrid); the kimi_k3 forward pass is hybrid | 10 |
| pie #633: the qwen3_5 import lands no sharded planes, so its tp-2 rows fail at load on engine-cuda (nightlies 35929921089/35942190398) | 5 |
| pie #633: the qwen3_6_moe import lands no sharded planes, so its tp-2 rows fail at load on engine-cuda (nightlies 35929921089/35942190398) | 5 |
| pie #633: the gpt_oss import lands no sharded planes, so its tp-2 rows fail at load on engine-cuda (nightlies 35929921089/35942190398) | 5 |
| pie #633: the glm5_next import lands no sharded planes, so its tp-2 rows fail at load on engine-cuda (nightlies 35929921089/35942190398) | 5 |
| pie #633: the kimi_k3 import lands no sharded planes, so its tp-2 rows fail at load on engine-cuda (nightlies 35929921089/35942190398) | 5 |

## pie pass rate by family × platform

| family | l40s-x1 | l40s-x2 | m1-max-32g | m4-pro-48g | pro4500-x1 | pro6000-x1 | rtx4090-x1 |
|---|---|---|---|---|---|---|---|
| deepseek_v4 | · | · | 0/9 | 0/9 | · | · | · |
| deepseek_v41 | · | · | 0/9 | 0/9 | · | · | · |
| gemma4 | 0/9 | · | 0/10 | 0/10 | 0/9 | 4/9 | 5/9 |
| glm5_next | 0/6 | · | 0/7 | 0/7 | 6/6 | 0/6 | 0/6 |
| gpt_oss | 6/8 | · | 0/9 | 0/9 | 0/8 | 6/8 | 5/8 |
| kimi_k3 | 0/6 | · | 0/7 | 0/7 | 6/6 | 0/6 | · |
| qwen3_5 | 8/8 | · | 0/9 | 0/9 | 8/8 | 8/8 | 8/8 |
| qwen3_6_moe | 0/8 | · | 0/9 | 0/9 | 0/8 | 8/8 | 8/8 |
