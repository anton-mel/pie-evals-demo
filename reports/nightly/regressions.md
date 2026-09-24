# Regressions / improvements

| kind | engine | platform | artifact | workload | program | mode | metric | value | Δ | threshold | commit/version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| regression | pie | l40s-x1 | qwen3.5-0.8b-bf16 | mixed-256 | text-completion-bench | tp1 | output_tok_s | 3694 | -4.1% | ±2.3% | 07206435344c91da3a7db0073dfda0612a056405 |
| regression | pie | l40s-x1 | qwen3.5-0.8b-bf16 | kv-oversub | text-completion-bench | tp1 | output_tok_s | 4371 | -4.1% | ±2.1% | 07206435344c91da3a7db0073dfda0612a056405 |
| regression | pie | l40s-x1 | qwen3.5-0.8b-bf16 | c8 | text-completion-bench | tp1 | output_tok_s | 5491 | -2.3% | ±1.0% | 07206435344c91da3a7db0073dfda0612a056405 |
