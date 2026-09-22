"""kill_leftovers must never touch our own process tree, and must never fall
back to a broad pkill -f (which once killed the interactive session because
its cwd contained 'pie')."""

import os

from pie_evals.node import preflight as pf


def test_ancestors_include_self_and_group():
    anc = pf._ancestors()
    assert os.getpid() in anc
    assert os.getpgrp() in anc
    assert len(anc) >= 2  # self + at least one parent


def test_kill_leftovers_never_kills_ancestors(monkeypatch):
    # nvidia-smi reports OUR OWN pid as a GPU holder whose basename matches.
    my = os.getpid()
    base = pf._proc_basename(my)
    monkeypatch.setattr(pf, "gpu_processes", lambda: [{"pid": str(my), "name": f"/usr/bin/{base}", "used_mib": "40000"}])
    monkeypatch.setattr(pf, "await_free_gpu", lambda **k: 0.0)
    killed = []
    monkeypatch.setattr(pf.os, "kill", lambda pid, sig: killed.append((pid, sig)))
    r = pf.kill_leftovers([base])
    assert killed == [], "must not kill a process in our ancestor set"
    assert r["killed"] == []


def test_kill_leftovers_targets_matching_orphan(monkeypatch):
    fake_pid = 999999  # not us, not an ancestor
    monkeypatch.setattr(pf, "gpu_processes", lambda: [{"pid": str(fake_pid), "name": "/opt/pie/target/release/pie", "used_mib": "41000"}])
    monkeypatch.setattr(pf, "_proc_basename", lambda pid: "pie" if pid == fake_pid else None)
    monkeypatch.setattr(pf, "await_free_gpu", lambda **k: 0.0)
    monkeypatch.setattr(pf, "time", type("T", (), {"sleep": staticmethod(lambda s: None)}))
    sent = []
    monkeypatch.setattr(pf.os, "kill", lambda pid, sig: sent.append((pid, sig)))
    r = pf.kill_leftovers(["pie"])
    assert (fake_pid, pf.signal.SIGTERM) in sent
    assert r["killed"] and r["killed"][0]["pid"] == fake_pid


def test_kill_leftovers_ignores_unmatched_names(monkeypatch):
    monkeypatch.setattr(pf, "gpu_processes", lambda: [{"pid": "999998", "name": "/usr/bin/python3", "used_mib": "40000"}])
    monkeypatch.setattr(pf, "_proc_basename", lambda pid: "python3")
    monkeypatch.setattr(pf, "await_free_gpu", lambda **k: 0.0)
    sent = []
    monkeypatch.setattr(pf.os, "kill", lambda pid, sig: sent.append((pid, sig)))
    r = pf.kill_leftovers(["pie", "EngineCore"])  # python3 is neither
    assert sent == [] and r["killed"] == []


def test_no_pkill_invocation():
    """pkill may be *named* in comments (explaining why it is banned) but must
    never be *invoked* — no code line passes it to a subprocess."""
    with open(pf.__file__) as f:
        for line in f:
            code = line.split("#", 1)[0]
            if "```" in line or line.lstrip().startswith('"'):
                continue
            assert '"pkill"' not in code and "'pkill'" not in code, f"pkill invoked: {line!r}"
