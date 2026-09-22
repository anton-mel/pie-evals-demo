# RunPod image

pie-evals runs on **`pieproject/runpod-ci-runner`** — github.com/pie-project/runpod-ci-runner,
the same image pie's own CUDA CI uses. Nothing to build here.

What pie-evals adds on top, at pod start (`orchestrate/runpod.py::startup_script`):
the runner is ephemeral and serves one job, then the pod terminates itself; a
self-destruct timer fires at `kill_minutes` regardless; the pie work tree and
cargo target are pod-local (`/tmp/pie`, `/tmp/target`) because the network
volume is shared by every concurrent pod; build artifacts are shared through
`/workspace/pie-evals-cache/builds/<commit>-<features>` and produced once by
the tier workflow's `build` job.

Baselines (vLLM, SGLang, llama.cpp) are not in the image. They are installed
lazily by the node into venvs on the volume (`/workspace/.venv/<engine>-<version>`)
the first time a nightly needs them, and reused after that.
