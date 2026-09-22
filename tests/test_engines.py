"""Engine adapters: argv shape + drift guard against the real bench scripts.

No GPU, no pie run. Every adapter is built against /root/pie and dummy specs;
``build_argv`` is checked for the flags a fair comparison needs, and every
``--flag`` it emits is checked against the set of option strings the
corresponding script (plus benches/common.py) actually registers with
argparse - parsed from source with ``ast`` so a renamed flag in pie fails here
rather than at 3am on a runner.
"""

from __future__ import annotations

import ast
import os
import re
from pathlib import Path

import pytest

from pie_evals.node.engines import get_engine
from pie_evals.node.engines.base import Engine
from pie_evals.node.engines.llamacpp import LlamacppEngine
from pie_evals.node.engines.mlxlm import MlxlmEngine
from pie_evals.node.engines.pie import PieEngine
from pie_evals.node.engines.recipes import load_recipe, recipe_names
from pie_evals.node.engines.sglang import SglangEngine
from pie_evals.node.engines.shape import max_model_len_for, workload_concurrency
from pie_evals.node.engines.vllm import VllmEngine
from pie_evals.node.workloads import common_args_for
from pie_evals.schema import ArtifactSpec, Backend, Mode, PlatformSpec, WorkloadSpec

PIE_ROOT = Path(os.environ.get("PIE_ROOT", "/root/pie"))
BENCHES = PIE_ROOT / "benches"

pytestmark = pytest.mark.skipif(not BENCHES.is_dir(), reason=f"pie checkout not at {PIE_ROOT}")


# ---- argparse flag extraction (the drift guard) -------------------------------


def _first_arg_flags(call: ast.Call, loop_iters: list[ast.AST]) -> list[str]:
    if not call.args:
        return []
    first = call.args[0]
    if isinstance(first, ast.Constant) and isinstance(first.value, str):
        return [first.value]
    if isinstance(first, ast.Name):
        # `for flag, dest, help in ((...), ...): sp.add_argument(flag, ...)`
        out = []
        for it in loop_iters:
            for node in ast.walk(it):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value.startswith("--"):
                    out.append(node.value)
        return out
    return []


def _flags_in(node: ast.AST, loop_iters: list[ast.AST] | None = None) -> set[str]:
    """Every ``--option`` string registered by ``add_argument`` calls under
    ``node``, including the ``--no-`` twin of each ``BooleanOptionalAction``."""
    flags: set[str] = set()
    loop_iters = list(loop_iters or [])

    def visit(n: ast.AST, iters: list[ast.AST]) -> None:
        if isinstance(n, ast.For):
            iters = iters + [n.iter]
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "add_argument":
            names = _first_arg_flags(n, iters)
            boolean_optional = any(
                kw.arg == "action" and isinstance(kw.value, ast.Attribute) and kw.value.attr == "BooleanOptionalAction"
                for kw in n.keywords
            )
            for name in names:
                if not name.startswith("--"):
                    continue
                flags.add(name)
                if boolean_optional:
                    flags.add("--no-" + name[2:])
        for child in ast.iter_child_nodes(n):
            visit(child, iters)

    visit(node, loop_iters)
    return flags


def _called_names(node: ast.AST) -> set[str]:
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def common_flags_by_function() -> dict[str, tuple[set[str], set[str]]]:
    """common.py: function name -> (flags it registers, names it references)."""
    tree = ast.parse((BENCHES / "common.py").read_text())
    out = {}
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef):
            out[fn.name] = (_flags_in(fn), _called_names(fn))
    return out


def argparse_flags(path: Path) -> set[str]:
    """Flags ``path`` accepts: those it registers itself plus those registered
    by the common.py helpers it (transitively) calls. ``add_output_dump_args``
    is a common.py helper only vllm/sglang call, so its flags count for them
    and not for llamacpp/mlx - the guard has to see that difference."""
    tree = ast.parse(path.read_text(), filename=str(path))
    flags = _flags_in(tree)
    if path.resolve() == (BENCHES / "common.py").resolve():
        return flags
    common = common_flags_by_function()
    todo = [n for n in _called_names(tree) if n in common]
    seen: set[str] = set()
    while todo:
        fn = todo.pop()
        if fn in seen:
            continue
        seen.add(fn)
        fn_flags, refs = common[fn]
        flags |= fn_flags
        todo += [n for n in refs if n in common]
    return flags


def accepted_flags(script: str) -> set[str]:
    return argparse_flags(PIE_ROOT / script)


_FLAG_RE = re.compile(r"^--[a-z0-9][a-z0-9-]*$")


def emitted_flags(argv: list[str]) -> list[str]:
    """Tokens that are flags (a value like ``--server-extra "--batch-size 2048"``
    is one token with a space and is not a flag)."""
    return [a for a in argv if _FLAG_RE.match(a)]


def flag_value(argv: list[str], flag: str) -> str:
    i = argv.index(flag)
    return argv[i + 1]


# ---- fixtures ------------------------------------------------------------------


def platform(backend: Backend = Backend.CUDA, arch: str = "ada", count: int = 2) -> PlatformSpec:
    return PlatformSpec(
        id=f"{backend}-{arch}", os="macos" if backend == Backend.METAL else "linux", backend=backend,
        accelerator="dummy", arch=arch, count=count, memory_gib=48.0, tp_capable=count > 1,
    )


def artifact(**over) -> ArtifactSpec:
    base = {"id": "qwen3-8b-bf16", "base_model": "Qwen/Qwen3-8B", "family": "qwen3", "scheme": "bf16"}
    base.update(over)
    return ArtifactSpec(**base)


WORKLOADS = {
    "ss-128-64": WorkloadSpec(id="ss-128-64", kind="single_stream", params={"prefill": 128, "decode": 64}),
    "c32": WorkloadSpec(id="c32", kind="concurrency", params={"concurrency": 32, "num_requests": 128, "prefill": 128, "decode": 128}),
    "lc-8k-128": WorkloadSpec(id="lc-8k-128", kind="long_context", params={"prefill": 8192, "decode": 128, "concurrency": 1}),
    "prefix-1k-x64": WorkloadSpec(
        id="prefix-1k-x64", kind="prefix_shared",
        params={"shared_prefix": 1024, "unique_suffix": 64, "variants": 64, "decode": 64, "concurrency": 16},
    ),
    "mixed-256": WorkloadSpec(
        id="mixed-256", kind="mixed_length",
        params={"num_requests": 256, "concurrency": 32, "prompt_lognormal": [6.0, 0.8], "output_lognormal": [5.0, 0.7], "max_prompt": 4096, "max_output": 1024},
    ),
    "replay": WorkloadSpec(id="replay", kind="replay", params={"arrival_rate": 4.0, "concurrency": 16, "num_requests": 64}),
}


def make(cls: type[Engine], *, plat: PlatformSpec | None = None, art: ArtifactSpec | None = None, mode: Mode | None = None,
         recipe_name: str = "competitive", workload: WorkloadSpec | None = None, **kw) -> Engine:
    plat = plat or platform()
    workload = workload or WORKLOADS["c32"]
    recipe = load_recipe(str(cls.name), recipe_name, plat, workload)
    return cls(pie_root=PIE_ROOT, artifact=art or artifact(), platform=plat, mode=mode or Mode(), recipe=recipe, **kw)


def argv_for(engine: Engine, workload: WorkloadSpec, tmp_path: Path) -> list[str]:
    return engine.build_argv(workload, common_args_for(workload), tmp_path / "bench.json")


@pytest.fixture
def hf_cache(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A fake HF hub cache with a GGUF repo (tokenizer-less) and an MLX repo."""
    hub = tmp_path / "hub"
    monkeypatch.setenv("HF_HUB_CACHE", str(hub))
    gguf = hub / "models--Qwen--Qwen3-8B-GGUF"
    (gguf / "snapshots" / "abc123").mkdir(parents=True)
    (gguf / "refs").mkdir()
    (gguf / "refs" / "main").write_text("abc123")
    (gguf / "snapshots" / "abc123" / "Qwen3-8B-Q4_K_M.gguf").write_bytes(b"GGUF")
    mlx = hub / "models--mlx-community--Qwen3.6-27B-4bit"
    (mlx / "snapshots" / "def456").mkdir(parents=True)
    (mlx / "refs").mkdir()
    (mlx / "refs" / "main").write_text("def456")
    (mlx / "snapshots" / "def456" / "tokenizer.json").write_text("{}")
    return hub


# ---- registry / recipes -------------------------------------------------------


def test_registry_resolves_every_engine():
    assert get_engine("pie") is PieEngine
    assert get_engine("vllm") is VllmEngine
    assert get_engine("sglang") is SglangEngine
    assert get_engine("llamacpp") is LlamacppEngine
    assert get_engine("mlxlm") is MlxlmEngine


@pytest.mark.parametrize("engine", ["pie", "vllm", "sglang", "llamacpp", "mlxlm"])
def test_recipes_have_default_and_competitive_with_rationale(engine):
    names = recipe_names(engine)
    assert "default" in names and "competitive" in names
    for wl in WORKLOADS.values():
        r = load_recipe(engine, "competitive", platform(), wl)
        assert r["_recipe"] == "competitive"
        assert r["_rationale"], f"{engine}: competitive recipe carries no rationale"
        for k, v in r.items():
            assert not (isinstance(v, str) and v.startswith("$")), f"{engine}.{k} left unresolved: {v}"


def test_recipe_resolves_concurrency_and_overrides():
    r = load_recipe("sglang", "competitive", platform(), WORKLOADS["c32"])
    assert r["cuda_graph_max_bs"] == 32
    r = load_recipe("sglang", "competitive", platform(), WORKLOADS["ss-128-64"])
    assert r["cuda_graph_max_bs"] == 1
    r = load_recipe("vllm", "competitive", platform(arch="hopper"), WORKLOADS["c32"])
    assert r["attention_backend"] == "FLASH_ATTN"
    r = load_recipe("vllm", "competitive", platform(arch="ada"), WORKLOADS["prefix-1k-x64"])
    assert r["prefix_caching"] is True
    r = load_recipe("pie", "competitive", platform(Backend.METAL, "apple9", count=1), WORKLOADS["c32"])
    assert r["gpu_mem_util"] is None and r["max_forward_requests"] == 32


def test_shape_helpers():
    assert workload_concurrency(WORKLOADS["ss-128-64"]) == 1
    assert workload_concurrency(WORKLOADS["c32"]) == 32
    assert max_model_len_for(WORKLOADS["c32"]) == 2048
    assert max_model_len_for(WORKLOADS["lc-8k-128"]) == 10240
    assert max_model_len_for(WORKLOADS["mixed-256"]) == 6144
    assert max_model_len_for(WORKLOADS["prefix-1k-x64"]) == 2048


# ---- pie --------------------------------------------------------------------


def test_pie_cuda_tp2(tmp_path):
    eng = make(PieEngine, mode=Mode(id="tp2", tp=2))
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert argv[1].endswith("benches/pie_bench.py") and argv[2] == "tput"
    assert flag_value(argv, "--engine") == "cuda_native"
    assert flag_value(argv, "--tp-size") == "2"
    # one --device flag carrying both ranks (pie_bench splits on ",")
    assert argv.count("--device") == 1
    assert flag_value(argv, "--device").split(",") == ["cuda:0", "cuda:1"]
    assert flag_value(argv, "--max-model-len") == "2048"
    assert flag_value(argv, "--gpu-mem-util") == "0.9"
    assert flag_value(argv, "--concurrency") == "32"
    assert "--report-timing" in argv
    assert "--dump-all-token-ids" in argv and "--json-out" in argv
    assert flag_value(argv, "--inferlet-dir") == str(PIE_ROOT / "tests/inferlets/text-completion-bench")
    assert eng.env["PIE_BENCH_INFERLET_DIR"] == str(PIE_ROOT / "tests/inferlets/text-completion-bench")
    assert eng.env["PYTHONPATH"].startswith(f"{PIE_ROOT}/sdk/client/python/src:{PIE_ROOT}/sdk/server/python/python")
    assert "--kv-pages" not in argv  # documented dead for cuda_native


def test_pie_program_path_is_settable(tmp_path):
    eng = make(PieEngine)
    eng.program_path = "tests/inferlets/dflash-speculative-bench"
    assert eng.env["PIE_BENCH_INFERLET_DIR"].endswith("dflash-speculative-bench")
    argv = argv_for(eng, WORKLOADS["ss-128-64"], tmp_path)
    assert flag_value(argv, "--inferlet-dir").endswith("dflash-speculative-bench")
    assert argv[2] == "latency" and flag_value(argv, "--requests") == "8"
    eng2 = make(PieEngine, recipe_name="default")
    eng2.recipe["program_path"] = "x/y"
    eng3 = PieEngine(pie_root=PIE_ROOT, artifact=artifact(), platform=platform(), mode=Mode(), recipe={"program_path": "x/y"})
    assert eng3.program_path == "x/y" and eng3.inferlet_dir == PIE_ROOT / "x/y"


def test_pie_metal_and_recipe_passthrough(tmp_path):
    plat = platform(Backend.METAL, "apple9", count=1)
    eng = make(PieEngine, plat=plat, workload=WORKLOADS["c32"])
    eng.recipe.update({"frame_submit_depth": 4, "engine_option": {"max_state_slots": 128, "sku": "$pie_sku"}, "pretokenized_prompts": False})
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert flag_value(argv, "--engine") == "metal"
    assert "--gpu-mem-util" not in argv and "--tp-size" not in argv and "--device" not in argv
    assert flag_value(argv, "--frame-submit-depth") == "4"
    assert flag_value(argv, "--max-forward-requests") == "32"
    assert "--no-pretokenized-prompts" in argv
    i = argv.index("--engine-option")
    assert argv[i + 1] == "max_state_slots=128"
    assert argv.count("--engine-option") == 1  # $pie_sku skipped when the artifact has none
    eng.artifact = artifact(pie_sku="qwen3-8b-bf16-kv-bf16")
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert "sku=qwen3-8b-bf16-kv-bf16" in argv


def test_pie_counters_from_summary():
    eng = make(PieEngine)
    summary = {
        "wall_s": 2.0,
        "config": {
            "total batches": 400, "device idle us": 200_000, "cumulative_batch_latency_us": 1_600_000,
            "avg batch latency us": 4000.0, "fire.execute.engine_fire_us": 3500.0,
            "turnaround sum us": 90_000, "turnaround n": 300, "wave fires": 400,
        },
    }
    c = eng.counters_from_summary(summary)
    assert c["batches"] == 400
    assert c["device_idle_pct"] == pytest.approx(10.0)
    assert c["host_us_per_step"] == pytest.approx(500.0)
    assert c["guest_turnaround_us"] == pytest.approx(300.0)
    assert c["batch_latency_us"] == pytest.approx(4000.0)
    assert eng.counters_from_summary({"wall_s": 1.0, "config": {}}) == {}
    # raw status keys are accepted as well
    c = eng.counters_from_summary({"wall_s": 1.0, "config": {"default.total_batches": 10, "default.fire.quorum.device_idle_us": 100_000}})
    assert c["batches"] == 10 and c["device_idle_pct"] == pytest.approx(10.0)


def test_pie_version_is_git_short_sha():
    v = make(PieEngine).version()
    assert re.fullmatch(r"[0-9a-f]{7,12}", v), v


def test_pie_serve_only_for_cli_engines_is_noop(tmp_path):
    eng = make(PieEngine, plat=platform(Backend.METAL, "apple9", count=1))
    assert eng.serve(WORKLOADS["c32"], tmp_path / "serve.log", 5) is None
    assert eng.server_url is None and eng._server_proc is None


def test_pie_serve_parses_url_and_stop(tmp_path, monkeypatch):
    """Drive serve() against a stand-in script that behaves like pie_bench
    under PIE_BENCH_SERVE_ONLY=1: announce the URL, then park."""
    fake_root = tmp_path / "pie"
    (fake_root / "benches").mkdir(parents=True)
    (fake_root / "benches" / "pie_bench.py").write_text(
        "import os, sys, time\n"
        "assert os.environ.get('PIE_BENCH_SERVE_ONLY') == '1'\n"
        "assert 'PIE_BENCH_SERVER_URL' not in os.environ\n"
        "print('booting', flush=True)\n"
        "print('PIE_BENCH_SERVER_URL=ws://127.0.0.1:43210', flush=True)\n"
        "time.sleep(60)\n"
    )
    eng = PieEngine(pie_root=fake_root, artifact=artifact(), platform=platform(), mode=Mode(),
                    recipe=load_recipe("pie", "competitive", platform(), WORKLOADS["c32"]))
    eng.serve(WORKLOADS["c32"], tmp_path / "serve.log", timeout_s=30)
    assert eng.server_url == "ws://127.0.0.1:43210"
    assert eng._server_proc is not None and eng._server_proc.poll() is None
    eng.stop()
    assert eng.server_url is None and eng._server_proc is None
    assert "PIE_BENCH_SERVER_URL=" in (tmp_path / "serve.log").read_text()


# ---- vllm -------------------------------------------------------------------


def test_vllm_args(tmp_path):
    eng = make(VllmEngine, mode=Mode(id="tp2", tp=2))
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert argv[1].endswith("benches/vllm_bench.py")
    assert flag_value(argv, "--model") == "Qwen/Qwen3-8B"
    assert flag_value(argv, "--tp-size") == "2"
    assert flag_value(argv, "--gpu-mem-util") == "0.9"
    assert flag_value(argv, "--max-model-len") == "2048"
    assert flag_value(argv, "--attention-backend") == "FLASHINFER"
    assert "--report-timing" in argv
    assert "--no-prefix-caching" in argv
    assert "--no-chunked-prefill" not in argv
    assert "--kv-cache-dtype" not in argv
    # prefix workload turns the cache on; hopper picks FA3
    eng = make(VllmEngine, plat=platform(arch="hopper"), workload=WORKLOADS["prefix-1k-x64"])
    argv = argv_for(eng, WORKLOADS["prefix-1k-x64"], tmp_path)
    assert "--prefix-caching" in argv and flag_value(argv, "--attention-backend") == "FLASH_ATTN"
    assert flag_value(argv, "--shared-prefix-words") == "737"
    # fp8 KV from the artifact; ngram mode maps onto vLLM's ngram speculation
    eng = make(VllmEngine, art=artifact(kv_dtype="fp8"), mode=Mode(id="ngram", spec_dec="ngram"))
    argv = argv_for(eng, WORKLOADS["ss-128-64"], tmp_path)
    assert flag_value(argv, "--kv-cache-dtype") == "fp8"
    assert flag_value(argv, "--spec-method") == "ngram" and flag_value(argv, "--spec-tokens") == "4"


def test_vllm_defaults():
    eng = make(VllmEngine)
    assert eng.python.endswith("python")
    assert "EngineCore" in eng.leftover_process_names()


# ---- sglang -----------------------------------------------------------------


def test_sglang_cuda_graph_max_bs_tracks_concurrency(tmp_path):
    eng = make(SglangEngine, workload=WORKLOADS["c32"])
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert flag_value(argv, "--sglang-cuda-graph-max-bs") == "32"
    assert flag_value(argv, "--tp-size") == "1"
    assert flag_value(argv, "--gpu-mem-util") == "0.9"
    assert flag_value(argv, "--max-model-len") == "2048"
    assert flag_value(argv, "--sglang-page-size") == "16"
    assert "--report-timing" in argv
    assert "--sglang-disable-hybrid-swa-memory" not in argv
    eng = make(SglangEngine, workload=WORKLOADS["ss-128-64"])
    argv = argv_for(eng, WORKLOADS["ss-128-64"], tmp_path)
    assert flag_value(argv, "--sglang-cuda-graph-max-bs") == "1"
    assert argv[2] == "latency"
    # gemma (sliding window) gets one uniform KV pool
    eng = make(SglangEngine, art=artifact(id="gemma-4-e4b-bf16", base_model="google/gemma-4-E4B-it", family="gemma4"))
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert "--sglang-disable-hybrid-swa-memory" in argv


# ---- llama.cpp ---------------------------------------------------------------


def test_llamacpp_args(tmp_path, hf_cache, monkeypatch):
    monkeypatch.setenv("LLAMA_SERVER_BIN", "/opt/llama/llama-server")
    art = artifact(id="qwen3-8b-gguf-q4km", base_model="Qwen/Qwen3-8B-GGUF", scheme="gguf_q4_k_m",
                   source_format="gguf", gguf_file="Qwen3-8B-Q4_K_M.gguf")
    eng = make(LlamacppEngine, art=art, workload=WORKLOADS["c32"])
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert argv[1].endswith("benches/llamacpp_bench.py")
    assert flag_value(argv, "--gguf-model") == str(hf_cache / "models--Qwen--Qwen3-8B-GGUF/snapshots/abc123/Qwen3-8B-Q4_K_M.gguf")
    assert flag_value(argv, "--server-bin") == "/opt/llama/llama-server"
    assert flag_value(argv, "--gpu-layers") == "all"
    # the GGUF repo ships no tokenizer -> --model is the base checkpoint
    assert flag_value(argv, "--model") == "Qwen/Qwen3-8B"
    extra = flag_value(argv, "--server-extra").split()
    assert extra[:4] == ["--batch-size", "2048", "--ubatch-size", "512"]
    assert "--dump-all-token-ids" not in argv  # not parsed by llamacpp_bench.py
    assert "--ignore-eos" in argv
    # prefix shape asks for cache reuse
    eng = make(LlamacppEngine, art=art, workload=WORKLOADS["prefix-1k-x64"])
    argv = argv_for(eng, WORKLOADS["prefix-1k-x64"], tmp_path)
    assert "--cache-reuse" in flag_value(argv, "--server-extra").split()
    # metal recipe drops --no-mmap
    eng = make(LlamacppEngine, art=art, plat=platform(Backend.METAL, "apple9", count=1))
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert "--no-mmap" not in flag_value(argv, "--server-extra").split()


def test_llamacpp_missing_gguf_is_load_fail(hf_cache):
    art = artifact(base_model="Qwen/Qwen3-8B-GGUF", scheme="gguf_q4_k_m", source_format="gguf", gguf_file="nope.gguf")
    eng = make(LlamacppEngine, art=art)
    from pie_evals.node.engines import EngineLaunchError

    with pytest.raises(EngineLaunchError) as e:
        eng.gguf_path()
    assert str(e.value.error_class) == "load_fail"


# ---- mlx-lm -----------------------------------------------------------------


def test_mlxlm_args(tmp_path, hf_cache, monkeypatch):
    monkeypatch.setenv("MLX_PY", "/opt/mlx/bin/python")
    art = artifact(id="qwen3.6-27b-mlx4", base_model="mlx-community/Qwen3.6-27B-4bit", family="qwen3_6",
                   scheme="affine_u4_g64", source_format="mlx")
    plat = platform(Backend.METAL, "apple9", count=1)
    eng = make(MlxlmEngine, art=art, plat=plat, workload=WORKLOADS["c32"])
    argv = argv_for(eng, WORKLOADS["c32"], tmp_path)
    assert argv[0] == "/opt/mlx/bin/python" and argv[1].endswith("benches/mlx_bench.py")
    assert flag_value(argv, "--model") == str(hf_cache / "models--mlx-community--Qwen3.6-27B-4bit/snapshots/def456")
    assert flag_value(argv, "--python") == "/opt/mlx/bin/python"
    assert flag_value(argv, "--prompt-cache-size") == "0"
    assert "--no-ignore-eos" in argv and "--ignore-eos" not in argv
    assert "--dump-all-token-ids" not in argv
    eng = make(MlxlmEngine, art=art, plat=plat, workload=WORKLOADS["prefix-1k-x64"])
    argv = argv_for(eng, WORKLOADS["prefix-1k-x64"], tmp_path)
    assert flag_value(argv, "--prompt-cache-size") == "64"


# ---- drift guard: every emitted flag exists in the real script ------------------

_CASES = []
for _wl in WORKLOADS:
    _CASES += [
        ("pie", PieEngine, _wl, {}),
        ("pie-metal", PieEngine, _wl, {"plat": platform(Backend.METAL, "apple9", count=1)}),
        ("pie-tp2", PieEngine, _wl, {"mode": Mode(id="tp2", tp=2)}),
        ("vllm", VllmEngine, _wl, {}),
        ("vllm-ngram-fp8", VllmEngine, _wl, {"mode": Mode(id="ngram", spec_dec="ngram"), "art": artifact(kv_dtype="fp8")}),
        ("sglang", SglangEngine, _wl, {}),
        ("sglang-gemma", SglangEngine, _wl, {"art": artifact(family="gemma4")}),
        ("llamacpp", LlamacppEngine, _wl, {"art": artifact(base_model="Qwen/Qwen3-8B-GGUF", scheme="gguf_q4_k_m", source_format="gguf", gguf_file="Qwen3-8B-Q4_K_M.gguf")}),
        ("mlxlm", MlxlmEngine, _wl, {"plat": platform(Backend.METAL, "apple9", count=1), "art": artifact(base_model="mlx-community/Qwen3.6-27B-4bit", scheme="affine_u4_g64", source_format="mlx")}),
    ]


@pytest.mark.parametrize("label,cls,wl,over", _CASES, ids=[f"{c[0]}/{c[2]}" for c in _CASES])
def test_every_emitted_flag_is_parsed_by_the_script(label, cls, wl, over, tmp_path, hf_cache):
    workload = WORKLOADS[wl]
    eng = make(cls, workload=workload, **over)
    argv = argv_for(eng, workload, tmp_path)
    accepted = accepted_flags(cls.script)
    assert accepted, f"no flags parsed from {cls.script}"
    unknown = sorted(set(emitted_flags(argv)) - accepted)
    assert not unknown, f"{label}/{wl}: {cls.script} does not accept {unknown}"


def test_argparse_flag_extraction_sees_loop_registered_and_boolean_optional_flags():
    flags = argparse_flags(PIE_ROOT / "benches/pie_bench.py")
    assert {"--inferlet-dir", "--engine", "--wasm-warm-slots", "--frame-submit-depth", "--pretokenized-prompts", "--no-pretokenized-prompts"} <= flags
    common = argparse_flags(BENCHES / "common.py")
    assert {"--model", "--ignore-eos", "--no-ignore-eos", "--tp-size", "--sglang-cuda-graph-max-bs", "--json-out"} <= common
    # common flags reach a script only through the helpers it calls
    for script in ("llamacpp_bench.py", "mlx_bench.py"):
        got = argparse_flags(BENCHES / script)
        assert {"--model", "--max-tokens", "--concurrency", "--num-requests", "--requests"} <= got, script
        assert "--dump-all-token-ids" not in got, script
    assert "--dump-all-token-ids" in argparse_flags(BENCHES / "vllm_bench.py")
    assert "--dump-all-token-ids" in argparse_flags(BENCHES / "sglang_bench.py")
    assert "--dump-all-token-ids" in flags
