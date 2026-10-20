# Provenance of tinytapeouts/ttgf0p1/gf-mpw-t0p1

[Tiny Tapeout GF 0.1](https://github.com/TinyTapeout/tinytapeout-gf-0p1) is an experimental [Tiny Tapeout](https://tinytapeout.com/) chip made on a GlobalFoundries private MPW run: 24 projects from earlier Tiny Tapeout chips in one shared block behind a multiplexer, eight standard cell tests and a pad test.

# How This Repository Was Generated

- `layout/` is the release asset `ttgf0p1_v23.fill.gds` of [`v23`](https://github.com/TinyTapeout/tinytapeout-gf-0p1/releases/tag/v23) (commit `37caa2d6ec`), the final layout with fill, written as OASIS. `scripts/xor_check.py` finds no difference between the two on any layer.
- Its blocks are the same as the block layouts published with the previous release, `v22` (`main.tar.xz`, `cells.tar.xz`, `buffer.tar.xz`): every layer's shape count matches, block by block. `data/main_cells_by_project.csv` is counted from `v22`'s `main/runs/test/final/pnl/tt_main_macro.pnl.v`, the powered netlist of the shared block, by `scripts/netlist_projects.py`: a cell belongs to the project its nets are named after (`mux_inst.p<NN>_I`), or to the one project of the cells it is connected to. Cells of the multiplexer and controller, and of the purely combinational projects, which keep no names, are `shared`.
- `data/manifest.csv` has one row per block, `SLOT_SIZE` its size in mm and `TOP` its cell; the cell tests are described from `cells/` in the shuttle repository at `37caa2d6ec`. `data/projects.csv` has one row per project: title, author and description from `main/src/projects/<macro>/info.yaml` at `37caa2d6ec`, address, repository, commit and original tile size from `data/shuttle_index.json`, which is Tiny Tapeout's project index for the chip (<https://index.tinytapeout.com/ttgf0p1.json>) unchanged.
- `data/tt_shuttle.json` gives the release date for the timeline: when [`v23`](https://github.com/TinyTapeout/tinytapeout-gf-0p1/releases/tag/v23) was published.
- `images/T0P1.svg` draws each block; `images/T0P1.png` is rendered from the layout with `scripts/lay2img.py` and `reticle.lyp` from [reticle-stitcher](https://github.com/wafer-space/reticle-stitcher) (`--width 4096 --oversampling 4`), the same way as the other dies.
- Everything here was made by `scripts/build_release_die.sh T0P1` in this repository; see [scripts/README.md](../../scripts/README.md).
