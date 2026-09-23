# Coverage — smoke

| status | cells |
|---|---|
| pass | 6 |
| fail | 11 |
| declared_unsupported | 220 |
| not_run | 346 |
| noisy | 2 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | fail | harness_invalid | no output_tok_s in bench output |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | noisy |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | l40s-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | deepseek-v4-flash-mini5 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp2 | not_run |  |  |
| pie | l40s-x2 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | prefill-rows | tp2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
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
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
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
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | dflash-speculative-bench | tp1,dflash2 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gemma-4-e4b-bf16 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | qwen3.5-0.8b-bf16 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
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
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | pro4500-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx4090-x1 | deepseek-v4-flash-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-8k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gemma-4-e4b-bf16 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx4090-x1 | gpt-oss-20b-mxfp4-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | mixed-256 | text-completion-bench | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | prefill-rows | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | prefix-1k-x64 | prefix-tree-kv-cache | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | mtp-speculative-decoding | tp1,mtp | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | cacheback-speculative-decoding | tp1,ngram | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-h2o | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | lc-2k-128 | trackb-snapkv | tp1 | not_run |  |  |
| pie | rtx4090-x1 | qwen3.6-35b-a3b-mini5 | ss-128-64 | lora-probe | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|
| pie/mini-dit is not an HF repo; needs a checkpoint source | 72 |
| pie has no llama family reader | 62 |
| shrink_checkpoint.py has no nemotron_h reader (supported: deepseek_v4, glm_moe_dsa, gpt_oss, kimi, muse_glimmer, qwen3_5_moe, qwen4_exp) | 62 |
| CUDA engine exposes no draft head (Metal only) — wiki speculative-decoding/ | 24 |

## pie pass rate by family × platform

| family | l40s-x1 | l40s-x2 | m1-max-32g | m4-pro-48g | pro4500-x1 | rtx4090-x1 |
|---|---|---|---|---|---|---|
| deepseek_v4 | 0/12 | 0/5 | 0/13 | 0/13 | 0/12 | 0/12 |
| gemma4 | 0/14 | · | 0/15 | 0/15 | 0/14 | 2/14 |
| gpt_oss | 0/12 | 0/5 | 0/13 | 0/13 | 0/12 | 0/12 |
| qwen3_5 | 0/15 | 0/5 | 0/16 | 0/16 | 0/15 | 4/15 |
| qwen3_6_moe | 0/14 | 0/5 | 0/15 | 0/15 | 0/14 | 0/14 |
