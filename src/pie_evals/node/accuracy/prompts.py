"""The fixed T0 prompt set.

Eight deterministic prompts covering the shapes that catch different bugs:
short factual (position 0..8 arithmetic), code (indentation / rare tokens),
multilingual (multi-byte tokenisation), chat-ish, and a ~1k-token prose block
(long-prefill reductions, RoPE at depth, sliding-window boundaries). The long
prompt is built from a seeded shuffle of a fixed sentence bank so it is the
same bytes on every node.
"""

from __future__ import annotations

import random
from pathlib import Path

_SENTENCES = [
    "The river bent twice before it reached the mill, and the miller counted both turns every morning.",
    "A ledger kept in pencil can be corrected, which is exactly why the auditor preferred ink.",
    "Nobody in the village remembered who had planted the walnut trees along the northern road.",
    "The telescope was older than the observatory, and the observatory was older than the town.",
    "Rain arrived on schedule for the first time in a decade, and the almanac took the credit.",
    "Each apprentice learned to sharpen a chisel before touching a single plank of oak.",
    "The lighthouse keeper logged the wind in knots and the visitors in first names only.",
    "Between the second and third bridge the water ran clear enough to count the stones.",
    "Her grandfather's compass pointed slightly east of north, and so did every map he drew.",
    "The choir rehearsed on Thursdays because the organist worked the market on Wednesdays.",
    "A copper kettle, once dented, will sing a different note for the rest of its life.",
    "The cartographer left the marsh blank and wrote, in small letters, that it moved.",
]

LONG_PROMPT_TARGET_WORDS = 1000


def _long_prompt(seed: int = 0, target_words: int = LONG_PROMPT_TARGET_WORDS) -> str:
    rng = random.Random(seed)
    bank = list(_SENTENCES)
    out: list[str] = []
    words = 0
    while words < target_words:
        rng.shuffle(bank)
        for s in bank:
            out.append(s)
            words += len(s.split())
            if words >= target_words:
                break
    return " ".join(out) + "\n\nSummary of the passage above:"


T0_PROMPTS: list[tuple[str, str]] = [
    ("capital", "The capital of France is"),
    ("arith", "Q: What is 17 times 23?\nA:"),
    ("code", 'def fibonacci(n):\n    """Return the n-th Fibonacci number."""\n'),
    ("json", 'Convert to JSON: name=Ada, born=1815, fields=["math", "computing"]\n{'),
    ("story", "Once upon a time, in a small village by the river,"),
    ("zh", "请用一句话解释什么是机器学习。答："),
    ("mixed", "Die Hauptstadt von Japan ist Tokio. La capitale de l'Italie est Rome. The capital of Canada is"),
    ("long-1k", _long_prompt()),
]


def t0_prompts() -> list[tuple[str, str]]:
    """``[(id, text)]`` — a fresh copy each call."""
    return list(T0_PROMPTS)


def tokenize(snapshot_dir: str | Path, text: str, add_special_tokens: bool = True) -> list[int]:
    """Prompt ids from the checkpoint's own tokenizer (``transformers`` is
    imported lazily). The same ids are handed to every engine so token
    parity is measured on identical input."""
    from transformers import AutoTokenizer  # lazy

    tok = AutoTokenizer.from_pretrained(str(snapshot_dir), trust_remote_code=True)
    return [int(i) for i in tok.encode(text, add_special_tokens=add_special_tokens)]
