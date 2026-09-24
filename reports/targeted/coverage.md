# Coverage — targeted

| status | cells |
|---|---|
| pass | 12 |
| fail | 0 |
| declared_unsupported | 0 |
| not_run | 18 |
| noisy | 0 |

## Gaps (expected supported, but not passing)

| engine | platform | artifact | workload | program | mode | status | error | message |
|---|---|---|---|---|---|---|---|---|
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m1-max-32g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m2-max | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | control-aa | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | c32 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | not_run |  |  |
| pie | m4-pro-48g | qwen3.5-0.8b-bf16 | lc-2k-128 | text-completion-bench | tp1 | not_run |  |  |

## Declared unsupported

| reason | cells |
|---|---|

## pie pass rate by family × platform

| family | m1-max-32g | m2-max | m4-pro-48g | m5-max-48g | rtx4090-x1 |
|---|---|---|---|---|---|
| qwen3_5 | 0/6 | 0/6 | 0/6 | 6/6 | 6/6 |
