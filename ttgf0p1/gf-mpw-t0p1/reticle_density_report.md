# Tiny Tapeout GF 0.1 on a GlobalFoundries private MPW run — Standard Cell & SRAM Density Report

**GF180MCU Process (GlobalFoundries 180nm), Shuttle T0P1**

## Introduction

This report analyzes the standard cell and SRAM density achieved by the 10 unique public chip designs on the Tiny Tapeout GF 0.1 on a GlobalFoundries private MPW run reticle. The reticle has 10 slots; the public layout contains 10 slot placements (some designs appear more than once, and private designs are not included).

All designs were fabricated on GlobalFoundries' GF180MCU process, a 180-nanometer (0.18um) technology node. This is a mature, relatively large-geometry process — for comparison, modern smartphone chips use 3nm or 5nm processes with features roughly 50x smaller.

> **Note on counting methodology:** All standard cell counts in this report count only **logic cells** — cells that perform actual computation (gates, flip-flops, buffers, multiplexers, etc.). Infrastructure cells are excluded: filler cells (fill, fillcap, endcap, filltie), well taps, antenna fix diodes, ESD diodes, and tie-high/tie-low cells. These infrastructure cells are inserted by automated tools to satisfy manufacturing rules but perform no logic function. On this reticle there are 118k infrastructure cell instances and 72k logic cell instances across the unique designs — 1.6 infrastructure cells for every logic cell.

## What Are Standard Cells?

A "standard cell" is a pre-designed, pre-verified building block used to construct digital circuits. Think of them like LEGO bricks for chip design: each cell performs one simple logic function (an AND gate, a flip-flop for storing one bit, a buffer for boosting signal strength), and a chip designer assembles thousands or millions of them to build complex circuits.

Standard cells in a library all share the same height (so they line up in rows) but vary in width depending on their function. Automated tools place these cells in rows and then route wires between them.

The "density" of standard cells — how many fit per square millimeter — is a key measure of how efficiently a design uses its silicon area. Higher density generally means more logic functionality packed into less chip area, which reduces cost.

## Standard Cell Libraries on This Reticle

| Library | Row Height | Rows per mm | Relative Density | Logic instances | Share |
|---|---|---|---|---|---|
| [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3.92 um | 255 rows | 100% | 64k | 89% |
| [as_sc_mcu7t3v3 (AS 7-track, 3.3V)](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 3.92 um | 255 rows | 100% | 2k | 3% |
| [osu_sc_gp12t3v3 (OSU 12-track, 3.3V)](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3) | 8.30 um | 120 rows | 47% | 1k | 2% |
| [osu_sc_gp9t3v3 (OSU 9-track, 3.3V)](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3) | 6.35 um | 157 rows | 62% | 1k | 2% |
| hfd_sc_mcu7t5v0 (7-track 5V cells made as 3.3V transistors) | 3.92 um | 255 rows | 100% | 1k | 1% |
| [mcu9t5v0 (9-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | 5.04 um | 198 rows | 78% | 1k | 1% |
| hfd_sc_mcu9t5v0 (9-track 5V cells made as 3.3V transistors) | 5.04 um | 198 rows | 78% | 1k | 1% |

Row height is the height of the cells' placement boundary, which is what rows are stacked at. Taller rows hold fewer cells per mm² but leave more room for wiring inside the cell.

## Theoretical Maximum Standard Cell Density

If you filled an entire square millimeter with nothing but one type of logic standard cell (no wiring, no gaps, no infrastructure cells), the theoretical maximum density would be:

| Cell Type | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | [OSU 12t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3) | [OSU 9t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3) | 7t-5V as 3.3V | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | 9t-5V as 3.3V | What it does |
|---|---|---|---|---|---|---|---|---|
| Inverter | 114k/mm² ([`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html), 2.24um) | 114k/mm² ([`inv_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 2.24um) | — | — | 114k/mm² (`inv_1`, 2.24um) | 89k/mm² ([`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/inv/gf180mcu_fd_sc_mcu9t5v0__inv_1.html), 2.24um) | 89k/mm² (`inv_1`, 2.24um) | Flips a signal |
| NAND gate | 91k/mm² ([`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html), 2.80um) | 65k/mm² ([`nand2_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 3.92um) | 39k/mm² ([`nand2_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp12t3v3_TT_25C.ccs.pdf#page=172), 3.10um) | 51k/mm² ([`nand2_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp9t3v3_TT_25C.ccs.pdf#page=127), 3.10um) | 91k/mm² (`nand2_1`, 2.80um) | 71k/mm² ([`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/nand2/gf180mcu_fd_sc_mcu9t5v0__nand2_1.html), 2.80um) | 71k/mm² (`nand2_1`, 2.80um) | Basic logic gate |
| Buffer | 76k/mm² ([`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html), 3.36um) | 76k/mm² ([`buff_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 3.36um) | — | — | 76k/mm² (`buf_1`, 3.36um) | 59k/mm² ([`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/buf/gf180mcu_fd_sc_mcu9t5v0__buf_1.html), 3.36um) | 59k/mm² (`buf_1`, 3.36um) | Strengthens a signal |
| Flip-flop | 16k/mm² ([`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html), 16.24um) | 17k/mm² ([`dfxtp_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 15.12um) | 9k/mm² ([`dff_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp12t3v3_TT_25C.ccs.pdf#page=130), 13.00um) | 11k/mm² ([`dff_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp9t3v3_TT_25C.ccs.pdf#page=91), 14.50um) | 16k/mm² (`dffq_1`, 16.24um) | 13k/mm² ([`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/dffq/gf180mcu_fd_sc_mcu9t5v0__dffq_1.html), 15.68um) | 13k/mm² (`dffq_1`, 15.68um) | Stores one bit |

These are hard upper bounds — the density if you packed cells edge-to-edge with zero routing overhead. For each library the smallest cell of that kind is used; the 3.3V library has no drive strength 1 cells, so its smallest cells are the `_2` variants.

In practice, real designs achieve significantly less because:

- **(a) Routing overhead** — wires connecting cells need room, which limits how tightly cells can be placed
- **(b) Infrastructure cells** — fillers, taps, antenna diodes, and tie cells make up 62% of cell instances on this reticle
- **(c) Mixed cell types** — designs use a mix of small and large cells
- **(d) Power planning** — power/ground straps consume area
- **(e) Clock distribution** — clock tree buffers and wiring take space

## Achieved Standard Cell Density — Design Averages

The following tables show the average logic standard cell density for each design's "core area" — the interior of the chip excluding the I/O pad ring (a 442um border of large pads around the perimeter used for external connections).

"% of max" compares against the buffer theoretical maximum for the design's primary library. "Cell area" is the share of the core area actually covered by logic cells — the placement utilisation of the die as a whole, including any area left empty or given to SRAM.

### High Density (above 10k logic SC/mm² core average)

| Design | Library | Core SC/mm² | % of max | Cell area | Logic SC | SRAM | Project |
|---|---|---|---|---|---|---|---|
| [MAIN](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/MAIN.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 32% | 72% | 63k | 0 | [The 24 Tiny Tapeout projects](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/main) |
| [CEL5](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL5.html) | [OSU 12t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3) | 20k | 0% | 41% | 1k | 0 | [Cell test: OSU 12-track 3.3 V cells](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell5) |
| [CEL4](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL4.html) | [OSU 9t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3) | 20k | 0% | 32% | 1k | 0 | [Cell test: OSU 9-track 3.3 V cells](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell4) |
| [CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 20k | 27% | 20% | 1k | 0 | [Cell test: AS 7-track 3.3 V cells](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell6) |
| [CEL7](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL7.html) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 20k | 27% | 20% | 1k | 0 | [Cell test: AS 7-track 3.3 V cells, second copy](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell7) |
| [CEL0](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL0.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 27% | 29% | 1k | 0 | [Cell test: GF 7-track 5 V cells](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell0) |
| [CEL2](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL2.html) | 7t-5V as 3.3V | 20k | 27% | 29% | 1k | 0 | [Cell test: GF 7-track cells as 3.3 V transistors](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell2) |
| [CEL1](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL1.html) | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | 20k | 34% | 29% | 1k | 0 | [Cell test: GF 9-track 5 V cells](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell1) |
| [CEL3](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL3.html) | 9t-5V as 3.3V | 20k | 34% | 29% | 1k | 0 | [Cell test: GF 9-track cells as 3.3 V transistors](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/cells/cell3) |

### Minimal (analog, custom or test structures)

These designs contain fewer than 1,000 logic standard cells:

| Design | Logic SC | Transistors | SRAM | Pads | Project |
|---|---|---|---|---|---|
| [BUFR](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/BUFR.html) | 4 | 2k | 0 | 0 | [Pad test buffer](https://github.com/TinyTapeout/tinytapeout-gf-0p1/tree/37caa2d6ece538cdcb29e79477f80d16c21cc52e/buffer) |

## Achieved Density — Peak 100um x 100um Regions

While the averages above include sparse regions, the densest 100um x 100um square found anywhere on a design shows the highest density it achieved. The square slides over the die in 20um steps and may not touch an SRAM macro.

| Design | Peak Logic SC/mm² | % of buffer max | Library |
|---|---|---|---|
| [CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html) | 48k | 63% of 76k | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [CEL7](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL7.html) | 48k | 63% of 76k | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [CEL0](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL0.html) | 45k | 59% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [CEL2](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL2.html) | 45k | 59% of 76k | 7t-5V as 3.3V |
| [CEL1](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL1.html) | 44k | 75% of 59k | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) |
| [CEL3](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL3.html) | 44k | 75% of 59k | 9t-5V as 3.3V |
| [MAIN](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/MAIN.html) | 43k | 57% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [CEL4](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL4.html) | 32k | 0% of 0 | [OSU 9t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3) |
| [CEL5](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL5.html) | 30k | 0% of 0 | [OSU 12t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3) |
| [BUFR](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/BUFR.html) | <1k | 1% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

The highest achieved density on this reticle is 63% of the buffer theoretical maximum, observed in the densest 100um square region of [CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html). The rest of that area is consumed by larger cells, infrastructure cells and the gaps left for routing.

## Library Comparison

Comparing designs that use one library exclusively:

| Metric | [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [as_sc_mcu7t3v3 (AS 7-track, 3.3V)](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | [osu_sc_gp12t3v3 (OSU 12-track, 3.3V)](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3) | [osu_sc_gp9t3v3 (OSU 9-track, 3.3V)](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3) | hfd_sc_mcu7t5v0 (7-track 5V cells made as 3.3V transistors) | [mcu9t5v0 (9-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | hfd_sc_mcu9t5v0 (9-track 5V cells made as 3.3V transistors) |
|---|---|---|---|---|---|---|---|
| Designs using this library | 3 | 2 | 1 | 1 | 1 | 1 | 1 |
| Best core density | 25k SC/mm² · 32% of max ([MAIN](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/MAIN.html)) | 20k SC/mm² · 27% of max ([CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html)) | 20k SC/mm² · 0% of max ([CEL5](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL5.html)) | 20k SC/mm² · 0% of max ([CEL4](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL4.html)) | 20k SC/mm² · 27% of max ([CEL2](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL2.html)) | 20k SC/mm² · 34% of max ([CEL1](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL1.html)) | 20k SC/mm² · 34% of max ([CEL3](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL3.html)) |
| Best peak grid cell | 45k SC/mm² · 59% of max ([CEL0](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL0.html)) | 48k SC/mm² · 63% of max ([CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html)) | 30k SC/mm² · 0% of max ([CEL5](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL5.html)) | 32k SC/mm² · 0% of max ([CEL4](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL4.html)) | 45k SC/mm² · 59% of max ([CEL2](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL2.html)) | 44k SC/mm² · 75% of max ([CEL1](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL1.html)) | 44k SC/mm² · 75% of max ([CEL3](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL3.html)) |
| Median core density | 20k SC/mm² · 27% of max | 20k SC/mm² · 27% of max | 20k SC/mm² · 0% of max | 20k SC/mm² · 0% of max | 20k SC/mm² · 27% of max | 20k SC/mm² · 34% of max | 20k SC/mm² · 34% of max |

Differences between libraries here reflect which designs chose which library as much as the libraries themselves; the theoretical difference from row height alone is in the table above.

## Most Common Logic Cell Types

The 15 most-used logic cell types across all unique designs on the reticle:

| Cell Type | Library | Instances | What it does |
|---|---|---|---|
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 9k | 2-input NAND gate |
| [`dffq_4`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_4.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | D flip-flop (1 bit storage) (4x drive) |
| [`oai21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai21/gf180mcu_fd_sc_mcu7t5v0__oai21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | OR-AND-Invert compound gate |
| [`nor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nor2/gf180mcu_fd_sc_mcu7t5v0__nor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | 2-input NOR gate |
| [`aoi21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi21/gf180mcu_fd_sc_mcu7t5v0__aoi21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | AND-OR-Invert compound gate |
| [`buf_4`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_4.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | Buffer (4x drive) |
| [`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | Inverter |
| [`xor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/xor2/gf180mcu_fd_sc_mcu7t5v0__xor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 2k | 2-input XOR gate |
| [`inv_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 2k | Inverter (2x drive) |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 2k | D flip-flop (1 bit storage) |
| [`mux2_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/mux2/gf180mcu_fd_sc_mcu7t5v0__mux2_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 2k | 2-input multiplexer (2x drive) |
| [`aoi22_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi22/gf180mcu_fd_sc_mcu7t5v0__aoi22_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 2k | AND-OR-Invert (2x2 inputs) |
| [`clkbuf_8`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkbuf/gf180mcu_fd_sc_mcu7t5v0__clkbuf_8.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 1k | Clock buffer (8x drive) |
| [`oai211_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai211/gf180mcu_fd_sc_mcu7t5v0__oai211_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 1k | OR-AND-Invert compound gate |
| [`nand3_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand3/gf180mcu_fd_sc_mcu7t5v0__nand3_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 1k | 3-input NAND gate |

Across the reticle there are 11k 2-input NAND gates and 8k flip-flops — 1.3 NAND2 gates per flip-flop.

## SRAM Block Usage

SRAM (Static Random-Access Memory) blocks are pre-designed memory macros. Unlike standard cells, which are composed by automated tools, SRAM blocks are hand-optimized fixed-size units designed to store data as densely as possible.

None of the designs on this reticle include SRAM blocks.

## SRAM vs Standard Cell Transistor Density

"Transistor density" here counts the number of distinct regions where a gate electrode (polysilicon, [GDS 30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) crosses an active area (diffusion, [GDS 22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) — each such crossing forms one transistor.

### Theoretical Maximum Transistor Density for Standard Cells

| Cell ([7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html) | 2.24 um | 114k | 2 | 228k/mm² |
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | 2.80 um | 91k | 4 | 364k/mm² |
| [`buf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_2.html) | 4.48 um | 57k | 6 | 342k/mm² |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | 16.24 um | 16k | 24 | 377k/mm² |

| Cell ([AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`inv_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 2.24 um | 114k | 4 | 456k/mm² |
| [`nand2_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 3.92 um | 65k | 8 | 521k/mm² |
| [`dfxtp_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 15.12 um | 17k | 26 | 439k/mm² |

| Cell ([OSU 12t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`nand2_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp12t3v3_TT_25C.ccs.pdf#page=172) | 3.10 um | 39k | 4 | 155k/mm² |
| [`dff_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp12t3v3_TT_25C.ccs.pdf#page=130) | 13.00 um | 9k | 26 | 241k/mm² |

| Cell ([OSU 9t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`nand2_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp9t3v3_TT_25C.ccs.pdf#page=127) | 3.10 um | 51k | 4 | 203k/mm² |
| [`dff_1`](https://cdn.jsdelivr.net/gh/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc@8a2f58f283a2eaa725314c9e1b8b7d1d343f23a3/docs/gf180mcu_osu_sc_gp9t3v3_TT_25C.ccs.pdf#page=91) | 14.50 um | 11k | 26 | 282k/mm² |

| Cell (7t-5V as 3.3V) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| `inv_1` | 2.24 um | 114k | 2 | 228k/mm² |
| `nand2_1` | 2.80 um | 91k | 4 | 364k/mm² |
| `buf_2` | 4.48 um | 57k | 6 | 342k/mm² |
| `dffq_1` | 16.24 um | 16k | 24 | 377k/mm² |

| Cell ([9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/inv/gf180mcu_fd_sc_mcu9t5v0__inv_1.html) | 2.24 um | 89k | 2 | 177k/mm² |
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/nand2/gf180mcu_fd_sc_mcu9t5v0__nand2_1.html) | 2.80 um | 71k | 4 | 283k/mm² |
| [`buf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/buf/gf180mcu_fd_sc_mcu9t5v0__buf_2.html) | 4.48 um | 44k | 6 | 266k/mm² |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/dffq/gf180mcu_fd_sc_mcu9t5v0__dffq_1.html) | 15.68 um | 13k | 24 | 304k/mm² |

| Cell (9t-5V as 3.3V) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| `inv_1` | 2.24 um | 89k | 2 | 177k/mm² |
| `nand2_1` | 2.80 um | 71k | 4 | 283k/mm² |
| `buf_2` | 4.48 um | 44k | 6 | 266k/mm² |
| `dffq_1` | 15.68 um | 13k | 24 | 304k/mm² |

### Best Standard Cell Regions

| Design | Peak 1mm² Trans/mm² | % of flip-flop max | Library |
|---|---|---|---|
| [MAIN](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/MAIN.html) | 292k/mm² | 66% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [CEL0](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL0.html) | 272k/mm² | 62% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [CEL2](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL2.html) | 272k/mm² | 62% | 7t-5V as 3.3V |
| [CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html) | 236k/mm² | 54% | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [CEL7](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL7.html) | 236k/mm² | 54% | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [CEL1](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL1.html) | 174k/mm² | 40% | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) |
| [CEL3](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL3.html) | 174k/mm² | 40% | 9t-5V as 3.3V |
| [BUFR](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/BUFR.html) | 98k/mm² | 22% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

Infrastructure cells are excluded from logic cell counts but their transistors (decoupling capacitors in particular) are included in transistor counts.

## Key Findings

1. The densest logic standard cell design, [MAIN](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/MAIN.html) (The 24 Tiny Tapeout projects), achieves **25k logic SC/mm²** averaged over its core (32% of buffer max), with a peak of **43k logic SC/mm²** in its densest 1mm² region.

2. Standard cell libraries in use: **[7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)** (89% of logic cells), **[AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3)** (3% of logic cells), **[OSU 12t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3)** (2% of logic cells), **[OSU 9t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3)** (2% of logic cells), **7t-5V as 3.3V** (1% of logic cells), **[9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html)** (1% of logic cells), **9t-5V as 3.3V** (1% of logic cells).

3. The median digital design achieves **20k logic SC/mm²** over its core. 9 of 9 designs exceed 10k logic SC/mm².

4. Infrastructure cells (fillers, taps, antenna diodes, ties) outnumber logic cells **1.6 to 1** across the reticle (118k vs 72k). Any density analysis must exclude these to avoid dramatically overstating actual logic content.

5. The most common logic cell is **[`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html)** (9k instances in [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)).

## Per-Design Details

| Design | Cell | Die (mm) | Core mm² | Placements | Pads | Logic SC | Infra SC | Transistors | SRAM | Libraries |
|---|---|---|---|---|---|---|---|---|---|---|
| [BUFR](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/BUFR.html) | `BUFR_tt_buffer_macro` | 0.23 x 0.07 | 0.0 | 1 | 0 | 4 | 248 | 1,836 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4 |
| [CEL0](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL0.html) | `CEL0_tt_cell_macro_0` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,074 | 1,432 | 9,084 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,074 |
| [CEL1](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL1.html) | `CEL1_tt_cell_macro_1` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,071 | 1,208 | 6,542 | 0 | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html): 1,071 |
| [CEL2](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL2.html) | `CEL2_tt_cell_macro_2` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,074 | 1,432 | 9,084 | 0 | 7t-5V as 3.3V: 1,074 |
| [CEL3](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL3.html) | `CEL3_tt_cell_macro_3` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,071 | 1,208 | 6,542 | 0 | 9t-5V as 3.3V: 1,071 |
| [CEL4](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL4.html) | `CEL4_tt_cell_macro_4` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,081 | 2,531 | 2,742 | 0 | [OSU 9t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp9t3v3): 1,081 |
| [CEL5](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL5.html) | `CEL5_tt_cell_macro_5` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,082 | 2,237 | 2,754 | 0 | [OSU 12t-3.3V](https://github.com/stineje/globalfoundries-pdk-libs-gf180mcu_osu_sc/tree/main/gf180mcu_osu_sc_gp12t3v3): 1,082 |
| [CEL6](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL6.html) | `CEL6_tt_cell_macro_6` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,080 | 1,843 | 6,902 | 0 | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3): 1,080 |
| [CEL7](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/CEL7.html) | `CEL7_tt_cell_macro_7` | 0.23 x 0.23 | 0.1 | 1 | 0 | 1,080 | 1,843 | 6,902 | 0 | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3): 1,080 |
| [MAIN](https://wafer.space/tinytapeouts/ttgf0p1/gf-mpw-t0p1/projects/MAIN.html) | `MAIN_tt_main_macro` | 1.60 x 1.60 | 2.6 | 1 | 0 | 63,000 | 103,553 | 747,240 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 63,000 |

## Methodology

- **Logic cell counts** come from walking the layout hierarchy and counting instances of every cell whose name contains a standard cell library prefix, excluding types starting with `fill`, `endcap`, `filltie`, `fillcap`, `decap`, `tap`, `antenna`, `diode`, `tiel`, `tieh`.
- **Transistor counts** are the number of merged polygons in the boolean AND of the diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) layers, leaving out dummy fill cells, whose diffusion and polysilicon squares overlap without forming transistors.
- **Core area** is each design's whole area.
- **Cell dimensions** are the width and height of each standard cell's placement boundary ([GDS 0/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), measured from the cells present in this layout.
- **Theoretical maximum** = (1000um / cell width) x (1000um / row height).
- **Pads** are openings on the pad layer ([37/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) at least 20um across. Those in the pad ring (within 400um of the die edge) or in a second ring of pads inside it are bond pads; the others are probe pads, shown as "+ N probe". Letters and logos on the pad layer are not pads.
- **Peak figures** are the densest 100um x 100um square anywhere inside each die, found by sliding the square in 20um steps over the die and skipping positions that touch an SRAM macro. Logic cells are placed by their origin and transistors by the centre of their gate. They are given per mm².
- **SRAM macros** are counted by cell name. The `sram_block_count` column of the summary CSV is kept for comparison with earlier results; it counts SramCore marker shapes, of which each GF180MCU macro has two.
- Designs placed more than once on the reticle are counted once.

---

*Generated by [ws-run-reports](https://github.com/wafer-space/ws-run-reports) from `T0P1.oas` (md5 `1064ed9cfa033b91c1a45309a916fa83`) in [wafer-space/tinytapeouts/ttgf0p1/gf-mpw-t0p1](https://github.com/wafer-space/tinytapeouts/tree/main/ttgf0p1/gf-mpw-t0p1). Analysis method: [KLayout](https://www.klayout.de/) boolean geometry operations on GDS layers. Grid resolution: 100um x 100um. Density figures are rounded to the nearest 1k.*
