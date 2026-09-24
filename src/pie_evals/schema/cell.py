"""The cell: the unit everything in pie-evals hangs off.

    cell = (engine@version, platform, artifact, workload, program, mode)

Every measurement is a record attached to one cell. Every cell is always in
exactly one status (see ``CellStatus``); a cell that was never run shows up as
``not_run`` rather than silently disappearing — that is how missing coverage
is surfaced.
"""

from __future__ import annotations

import hashlib
import json
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field, model_validator


class StrEnumBase(StrEnum):
    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.value


class EngineName(StrEnumBase):
    PIE = "pie"
    VLLM = "vllm"
    SGLANG = "sglang"
    LLAMACPP = "llamacpp"
    MLXLM = "mlxlm"


class Backend(StrEnumBase):
    """pie driver / device backend. Baseline engines map onto the same values."""

    CUDA = "cuda"
    METAL = "metal"
    VULKAN = "vulkan"
    WGPU = "wgpu"


class QuantScheme(StrEnumBase):
    BF16 = "bf16"
    FP8 = "fp8"
    MXFP4 = "mxfp4"
    AFFINE_U4_G64 = "affine_u4_g64"  # mlx-community 4-bit, group 64
    MLX_2BIT = "mlx_2bit"
    W4A16_MARLIN = "w4a16_marlin"
    GGUF_Q4_K_M = "gguf_q4_k_m"
    GGUF_Q8_0 = "gguf_q8_0"
    AWQ = "awq"
    GPTQ = "gptq"


class SourceFormat(StrEnumBase):
    HF_SAFETENSORS = "hf_safetensors"
    GGUF = "gguf"
    MLX = "mlx"


class ArtifactKind(StrEnumBase):
    FULL = "full"
    MINIATURE = "miniature"


class WorkloadKind(StrEnumBase):
    SINGLE_STREAM = "single_stream"
    CONCURRENCY = "concurrency"
    LONG_CONTEXT = "long_context"
    PREFIX_SHARED = "prefix_shared"
    MIXED_LENGTH = "mixed_length"
    REPLAY = "replay"
    CONTROL_AA = "control_aa"  # harness self-check: engine vs itself


class Tier(StrEnumBase):
    SMOKE = "smoke"
    NIGHTLY = "nightly"
    WEEKLY = "weekly"


class CellStatus(StrEnumBase):
    PASS = "pass"
    FAIL = "fail"
    DECLARED_UNSUPPORTED = "declared_unsupported"
    NOT_RUN = "not_run"
    NOISY = "noisy"  # ran, but the harness refuses to read the numbers


class ErrorClass(StrEnumBase):
    LOAD_FAIL = "load_fail"
    CRASH = "crash"
    HANG = "hang"  # only ever observed via timeout
    OOM = "oom"
    DOESNT_FIT = "doesnt_fit"  # refused before load by the fit check
    GATE_FAIL = "gate_fail"  # ran, produced wrong output
    HARNESS_INVALID = "harness_invalid"  # preflight/control failed; not the engine's fault
    INPUT_MISMATCH = "input_mismatch"  # prompt/output token parity across engines broke
    INCOMPATIBLE = "incompatible"  # the program's contract does not fit the model (e.g. attention-only inferlet on a hybrid model)


class AccuracyStatus(StrEnumBase):
    PASS = "pass"
    FAIL = "fail"
    SKIPPED_MINIATURE = "skipped_miniature"
    SKIPPED_NO_REFERENCE = "skipped_no_reference"
    NOT_RUN = "not_run"


class MiniatureRecipe(BaseModel):
    """Layer/expert truncation recipe, executed by pie's
    ``scripts/bench/shrink_checkpoint.py`` (HTTP range requests against the HF
    shards; the result is a real checkpoint of the same architecture that
    loads unmodified in pie and vLLM). Width dimensions are always kept;
    ``layers`` selects source layers so that the family's per-layer pattern
    is covered in whole periods, ``experts`` keeps the first N routed experts,
    ``repeat`` aliases the selected block to get depth for free."""

    layers: str = Field(description="source layer selection, e.g. '0-4' or '0-5,39'")
    experts: int | None = Field(default=None, description="routed experts kept per MoE layer (None = all)")
    repeat: int = 1
    text_only: bool = False  # --text-only renames tensors (drops the language_model. prefix) and pie's readers then miss embed_tokens
    period: int = Field(default=1, description="layer-type pattern period the selection must be a multiple of")
    engram_vocab: int | None = Field(default=None, description="DeepSeek-V4.1: re-carve each Engram hash table to this bucket base (--engram-vocab)")
    attn_res_block_size: int | None = Field(default=None, description="Kimi-K3: AttnRes block stride of the cut (--attn-res-block-size)")
    note: str = ""

    @property
    def recipe_hash(self) -> str:
        key = json.dumps([self.layers, self.experts, self.repeat, self.text_only, self.engram_vocab, self.attn_res_block_size], sort_keys=True)
        return hashlib.sha256(key.encode()).hexdigest()[:10]

    @property
    def tag(self) -> str:
        t = f"mini-l{self.layers.replace(',', '_')}"
        if self.experts is not None:
            t += f"-e{self.experts}"
        if self.repeat > 1:
            t += f"-r{self.repeat}"
        if self.text_only:
            t += "-txt"
        if self.engram_vocab is not None:
            t += f"-g{self.engram_vocab}"
        if self.attn_res_block_size is not None:
            t += f"-b{self.attn_res_block_size}"
        return t


class ArtifactSpec(BaseModel):
    id: str
    base_model: str = Field(description="HF repo id or local path of the checkpoint")
    revision: str | None = Field(default=None, description="checkpoint commit; resolved at run time if None")
    family: str = Field(description="model family key (qwen3, gemma4, deepseek_v4, ...)")
    scheme: QuantScheme
    kv_dtype: str = "bf16"
    source_format: SourceFormat = SourceFormat.HF_SAFETENSORS
    kind: ArtifactKind = ArtifactKind.FULL
    miniature: MiniatureRecipe | None = None
    expected_gib: float | None = Field(default=None, description="LM-only resident weight size")
    degradation_budget: dict[str, float] | None = Field(
        default=None,
        description="for quant schemes without a same-weights reference: allowed ppl ratio / score drop vs bf16",
    )
    chat_template: bool = False
    pie_sku: str | None = Field(default=None, description="pie SKU row name carrying the quantization (e.g. gptoss-20b-dflash-u4g64-mxfp4-kv-bf16)")
    max_context: int | None = Field(default=None, description="tokens one sequence may hold on this artifact as pie ships it (the SKU's max_context), when smaller than the HF config's")
    gguf_file: str | None = Field(default=None, description="file name inside a GGUF repo (the arm must be named, never the quant tag)")
    gguf_config_from: str | None = Field(default=None, description="HF repo whose config.json is copied next to the GGUF (pie reads the encoding from config.json; GGUF repos ship none)")
    tiers: list[Tier] = Field(default_factory=lambda: [Tier.NIGHTLY, Tier.WEEKLY])

    @model_validator(mode="after")
    def _miniature_needs_recipe(self) -> ArtifactSpec:
        if self.kind == ArtifactKind.MINIATURE and self.miniature is None:
            raise ValueError(f"artifact {self.id}: miniature artifacts need a recipe")
        return self

    @property
    def artifact_key(self) -> str:
        key = f"{self.base_model}@{self.scheme}/{self.source_format}"
        if self.kind == ArtifactKind.MINIATURE:
            key += f"#mini-{self.miniature.recipe_hash}"  # type: ignore[union-attr]
        return key


class PlatformSpec(BaseModel):
    id: str
    os: str  # linux | macos
    backend: Backend
    accelerator: str = Field(description="human name, e.g. 'NVIDIA L40S', 'Apple M1 Max'")
    arch: str = Field(description="ada | blackwell | hopper | ampere | apple7 | apple8 | apple9 ...")
    count: int = 1
    memory_gib: float
    interconnect: str = "pcie"  # pcie | nvlink | uma
    runner_labels: list[str] = Field(default_factory=list, description="GitHub self-hosted runner labels")
    runpod_gpu_type: str | None = None
    tp_capable: bool = False
    tiers: list[Tier] = Field(default_factory=lambda: [Tier.NIGHTLY, Tier.WEEKLY])


class WorkloadSpec(BaseModel):
    id: str
    kind: WorkloadKind
    params: dict[str, Any] = Field(default_factory=dict)
    tiers: list[Tier] = Field(default_factory=lambda: [Tier.NIGHTLY])
    est_minutes: float = 1.0


class ProgramSpec(BaseModel):
    """An inferlet (pie guest program). ``text-completion-bench`` is the
    serving-path default; every other entry exercises a different ETA
    program and is a coverage cell of its own."""

    id: str
    path: str = Field(description="path under the pie tree, e.g. examples/text-completion-bench")
    category: str  # serving | speculative | kv_policy | adapter | diffusion
    baseline_equivalents: dict[str, str] = Field(
        default_factory=dict, description="engine -> mode flag that is the comparable feature, if any"
    )
    accuracy_gate: str = "token_parity"  # token_parity | cosine | acceptance_rate | none
    pie_only: bool = True
    spec_dec: str | None = Field(default=None, description="speculative mode this program requires")
    bench_args: list[str] = Field(default_factory=list, description="extra bench flags this program needs (e.g. a sampling inferlet rejects temperature 0)")
    workloads: list[str] | None = Field(default=None, description="restrict to these workload ids (None = all)")
    families: list[str] | None = Field(default=None, description="restrict to these model families (None = all)")
    tiers: list[Tier] = Field(default_factory=lambda: [Tier.NIGHTLY, Tier.WEEKLY])


class Mode(BaseModel):
    id: str = "tp1"
    tp: int = 1
    spec_dec: str | None = None  # dflash2 | dspark | mtp | ngram | eagle | None
    extra: dict[str, Any] = Field(default_factory=dict)
    tiers: list[Tier] = Field(default_factory=lambda: [Tier.NIGHTLY, Tier.WEEKLY])

    @property
    def key(self) -> str:
        parts = [f"tp{self.tp}"]
        if self.spec_dec:
            parts.append(self.spec_dec)
        for k in sorted(self.extra):
            parts.append(f"{k}={self.extra[k]}")
        return ",".join(parts)


class Cell(BaseModel):
    engine: EngineName
    engine_version: str | None = Field(default=None, description="baseline version or pie commit; filled at run time")
    platform: PlatformSpec
    artifact: ArtifactSpec
    workload: WorkloadSpec
    program: ProgramSpec
    mode: Mode = Field(default_factory=Mode)
    tiers: list[Tier] = Field(default_factory=list)
    declared_unsupported_reason: str | None = None

    @property
    def cell_key(self) -> str:
        """Identity independent of engine version — used to line up history."""
        return "|".join(
            [
                str(self.engine),
                self.platform.id,
                self.artifact.artifact_key,
                self.workload.id,
                self.program.id,
                self.mode.key,
            ]
        )

    @property
    def cell_id(self) -> str:
        return hashlib.sha256(self.cell_key.encode()).hexdigest()[:16]

    @property
    def is_baseline(self) -> bool:
        return self.engine != EngineName.PIE

    def accuracy_applicable(self) -> bool:
        return self.artifact.kind == ArtifactKind.FULL and self.program.accuracy_gate != "none"
