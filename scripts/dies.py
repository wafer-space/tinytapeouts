# The Tiny Tapeout dies on wafer.space runs: which chip each is, and where its release comes from.
#   python3 dies.py <CODE>    prints the die's settings as shell variables, for build_tt.sh
import shlex, sys

RUNS = {"ws-run1": ("Run 1", "G801"), "ws-run2": ("Run 2", "G802")}
DIES = {
    "TTP2": dict(run="ws-run1", ttid="ttgf0p2", repo="tinytapeout-gf-0p2", tag="tapeout-ws2512", note="the standard build"),
    "TTPG": dict(run="ws-run1", ttid="ttgf0p2", repo="tinytapeout-gf-0p2", tag="tapeout-ws2512-powergate",
                 note="the power-gated build, made from the same projects with the `powergate` configuration"),
    "T0P3": dict(run="ws-run2", ttid="ttgf0p3", repo="tinytapeout-gf-0p3", tag="tapeout-ws2607", note=""),
    "T26A": dict(run="ws-run2", ttid="ttgf26a", repo="tinytapeout-gf-26a", tag="tapeout-ws2607", note=""),
    "T26B": dict(run="ws-run2", ttid="ttgf26b", repo="tinytapeout-gf-26b", tag="tapeout-ws2607", note=""),
}
for d in DIES.values():
    d["run_name"], d["shuttle"] = RUNS[d["run"]]

if __name__ == "__main__":
    d = DIES[sys.argv[1]]
    for k in ("run", "ttid", "repo", "tag", "shuttle"):
        print(f"{k}={shlex.quote(d[k])}")
