# The Tiny Tapeout GF180MCU dies: which chip each is, and where its release comes from. Most were made on
# wafer.space runs and are cut from the run's reticle (build_tt.sh); Tiny Tapeout GF 0.1 was made elsewhere and
# its layout is the release's own (build_release_die.sh, with `asset`).
#   python3 dies.py <CODE>    prints the die's settings as shell variables, for the build scripts
import shlex, sys

RUNS = {"ws-run1": ("Run 1", "G801"), "ws-run2": ("Run 2", "G802"),
        "gf-mpw": ("a GlobalFoundries private MPW run", "")}
DIES = {
    "T0P1": dict(run="gf-mpw", ttid="ttgf0p1", repo="tinytapeout-gf-0p1", tag="v23", note="",
                 asset="ttgf0p1_v23.fill.gds", blocks_tag="v22"),
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
    for k in ("run", "ttid", "repo", "tag", "shuttle", "asset", "blocks_tag"):
        print(f"{k}={shlex.quote(d.get(k, ''))}")
