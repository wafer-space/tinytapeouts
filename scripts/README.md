# How the die directories are made

Each `<chip>/<run>-<code>/` directory is generated from public inputs by the scripts here:

| Input | Used for |
|---|---|
| [wafer-space/ws-run1](https://github.com/wafer-space/ws-run1), [wafer-space/ws-run2](https://github.com/wafer-space/ws-run2) | the reticle, `layout/<shuttle>.oas`, that the die is cut from |
| The Tiny Tapeout shuttle repository's release (e.g. [tinytapeout-gf-0p3 `tapeout-ws2607`](https://github.com/TinyTapeout/tinytapeout-gf-0p3/releases/tag/tapeout-ws2607)) | `shuttle_index.json`, and each project's `info.yaml` at the commit the release was built from |
| [wafer-space/reticle-stitcher](https://github.com/wafer-space/reticle-stitcher) | `scripts/lay2img.py` and `reticle.lyp`, for `images/<CODE>.png` |
| [wafer-space/ws-run-reports](https://github.com/wafer-space/ws-run-reports) | `ws-run-reports tt-manifest`, which writes `data/manifest.csv` and `data/tt_shuttle.json` |

## Build a die

Add the die to `DIES` in `dies.py` (its chip, run, Tiny Tapeout repository and release tag), then:

```bash
scripts/build_tt.sh T0P3
```

The run repository, reticle-stitcher and ws-run-reports are expected as checkouts next to this
repository; set `RUN_REPO`, `RS` or `WS_RUN_REPORTS` to use others. The Tiny Tapeout repository is
cloned into `scripts/work/` (not committed) unless `TT_GIT` names a clone. `KL` is the command that runs
a Python script with the `klayout` module (default `python3`); the reticles are large, so run it with a
memory limit. To check the scripts against what is committed, build into another directory with
`TT_OUT=<dir>` and compare.

| Script | What it does |
|---|---|
| `build_tt.sh` | Runs the steps below for one die |
| `dies.py` | The dies: chip, run, Tiny Tapeout repository, release tag |
| `cut_die.py` | Cuts the die's cell out of the reticle, with everything below it, as OASIS |
| `tt_slots.py` | The bounding box of each project: the outermost placement of each macro in `shuttle_index.json` |
| `gen_tt_repo.py` | `data/`, `images/<CODE>.svg`, `README.md` and `PROVENANCE.md` |
| `gen_tt_index.py` | The repository's `README.md`, one row per die |
| `ttcmp.py` | Fingerprints a layout (shape count per layer, every `tt_um_*` placement) to compare a die with its release |

The web pages at <https://wafer.space/tinytapeouts/> are built by ws-run-reports from these
directories (`runs/tinytapeouts-*.toml` there).

## Comparison with the Tiny Tapeout releases

`ttcmp/` has the `ttcmp.py` fingerprints of each die as cut from the reticle (`<CODE>-reticle.json`) and of
the layouts in its release: the submitted `tt_gf_wrapper.oas` (`-wrapper.json`) and the precheck output
(`-output.json`). File names in them are relative to a working directory holding `<run>/<CODE>/layout/`
and the release assets under `<run>/<CODE>/releases/<tag>/`. `report.txt` compares them layer by layer;
`report-comp.txt` checks that the only difference from the precheck output is the dummy COMP (22/4)
merged into COMP (22/0) on the reticle, and that every project placement is the same. These are what
the claims in each `PROVENANCE.md` rest on. The code that wrote the two reports from the
fingerprints was not kept.
