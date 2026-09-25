# Coverage — targeted

| status | cells |
|---|---|
| pass | 0 |
| fail | 0 |
| declared_unsupported | 120 |
| not_run | 216 |
| noisy | 0 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-26b-a4b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-31b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gemma-4-e4b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mlx-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | gpt-oss-20b-mxfp4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-gguf-q4km | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-27b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m5-max-48g | qwen3.6-35b-a3b-mlx4 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|
| pie has no llama family reader | 24 |
| pie/mini-dit is not an HF repo; needs a checkpoint source | 24 |
| does not fit: 76.2 GiB per device > 48.0 GiB | 12 |
| does not fit: 112.4 GiB per device > 48.0 GiB | 12 |
| does not fit: 67.5 GiB per device > 48.0 GiB | 12 |
| does not fit: 76.2 GiB per device > 32.0 GiB | 6 |
| does not fit: 112.4 GiB per device > 32.0 GiB | 6 |
| does not fit: 67.5 GiB per device > 32.0 GiB | 6 |
| does not fit: 76.2 GiB per device > 64.0 GiB | 6 |
| does not fit: 112.4 GiB per device > 64.0 GiB | 6 |
| does not fit: 67.5 GiB per device > 64.0 GiB | 6 |

## pie pass rate by family × platform

| family | m1-max-32g | m2-max | m4-pro-48g | m5-max-48g |
|---|---|---|---|---|
| gemma4 | 0/12 | 0/12 | 0/12 | 0/12 |
| gemma4_moe | 0/6 | 0/6 | 0/6 | 0/6 |
| gpt_oss | 0/12 | 0/12 | 0/12 | 0/12 |
| qwen3_5 | 0/6 | 0/6 | 0/6 | 0/6 |
| qwen3_6 | 0/12 | 0/12 | 0/12 | 0/12 |
| qwen3_6_moe | 0/6 | 0/6 | 0/6 | 0/6 |
