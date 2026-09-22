"""Accuracy preservation: is pie producing the *same* tokens as a reference
implementation of the same weights?

Tiers:

* **T0 — token parity.** Greedy decode of a fixed prompt set on the engine
  and on a reference (HF transformers, or mlx_lm for MLX checkpoints). The
  first divergent token is *adjudicated* with teacher-forced logits: a gap
  within one bf16 ulp (~0.125) between the two candidates is a legitimate
  reduction-order flip; a large gap is a bug.
* **T1 — distributional.** Mean KL, top-k agreement and perplexity against the
  reference's teacher-forced logits.
* **T2 — task scores** with bootstrap confidence intervals.

Everything in :mod:`.parity` is pure numpy so the package imports without
torch; the heavy references live behind lazy imports in :mod:`.reference`.
"""

from .parity import (  # noqa: F401
    COSINE_GATE,
    adjudicate_divergence,
    bootstrap_ci,
    cosine,
    first_divergence,
    kl_divergence,
    perplexity_from_logits,
    psnr,
    scores_differ,
    t0_verdict,
    topk_agreement,
)
