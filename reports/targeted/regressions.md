# Regressions / improvements

| kind | engine | platform | artifact | workload | program | mode | metric | value | Δ | threshold | commit/version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| improvement | pie | m5-max-48g | qwen3.5-0.8b-bf16 | lc-1k-128 | text-completion-bench | tp1 | decode_tok_s | 265.4 | +1.7% | ±1.6% | cb95a9dadf786b9e72b8d99a8ae05fa1fb921dd1 |
| improvement | pie | m5-max-48g | qwen3.5-0.8b-bf16 | ss-128-64 | text-completion-bench | tp1 | decode_tok_s | 284 | +2.2% | ±1.6% | cb95a9dadf786b9e72b8d99a8ae05fa1fb921dd1 |
