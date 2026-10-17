# Tiny Tapeout GF 0.3 on wafer.space Run 2 — Standard Cell & SRAM Density Report

**GF180MCU Process (GlobalFoundries 180nm), Shuttle T0P3**

## Introduction

This report analyzes the standard cell and SRAM density achieved by the 32 unique public chip designs on the Tiny Tapeout GF 0.3 on wafer.space Run 2 reticle. The reticle has 32 slots; the public layout contains 32 slot placements (some designs appear more than once, and private designs are not included).

All designs were fabricated on GlobalFoundries' GF180MCU process, a 180-nanometer (0.18um) technology node. This is a mature, relatively large-geometry process — for comparison, modern smartphone chips use 3nm or 5nm processes with features roughly 50x smaller.

> **Note on counting methodology:** All standard cell counts in this report count only **logic cells** — cells that perform actual computation (gates, flip-flops, buffers, multiplexers, etc.). Infrastructure cells are excluded: filler cells (fill, fillcap, endcap, filltie), well taps, antenna fix diodes, ESD diodes, and tie-high/tie-low cells. These infrastructure cells are inserted by automated tools to satisfy manufacturing rules but perform no logic function. On this reticle there are 170k infrastructure cell instances and 113k logic cell instances across the unique designs — 1.5 infrastructure cells for every logic cell.

## What Are Standard Cells?

A "standard cell" is a pre-designed, pre-verified building block used to construct digital circuits. Think of them like LEGO bricks for chip design: each cell performs one simple logic function (an AND gate, a flip-flop for storing one bit, a buffer for boosting signal strength), and a chip designer assembles thousands or millions of them to build complex circuits.

Standard cells in a library all share the same height (so they line up in rows) but vary in width depending on their function. Automated tools place these cells in rows and then route wires between them.

The "density" of standard cells — how many fit per square millimeter — is a key measure of how efficiently a design uses its silicon area. Higher density generally means more logic functionality packed into less chip area, which reduces cost.

## Standard Cell Libraries on This Reticle

| Library | Row Height | Rows per mm | Relative Density | Logic instances | Share |
|---|---|---|---|---|---|
| [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3.92 um | 255 rows | 100% | 88k | 78% |
| [as_sc_mcu7t3v3 (AS 7-track, 3.3V)](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 3.92 um | 255 rows | 100% | 25k | 22% |

Row height is the height of the cells' placement boundary, which is what rows are stacked at. Taller rows hold fewer cells per mm² but leave more room for wiring inside the cell.

## Theoretical Maximum Standard Cell Density

If you filled an entire square millimeter with nothing but one type of logic standard cell (no wiring, no gaps, no infrastructure cells), the theoretical maximum density would be:

| Cell Type | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | What it does |
|---|---|---|---|
| Inverter | 114k/mm² ([`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html), 2.24um) | 114k/mm² ([`inv_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 2.24um) | Flips a signal |
| NAND gate | 91k/mm² ([`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html), 2.80um) | 65k/mm² ([`nand2_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 3.92um) | Basic logic gate |
| Buffer | 76k/mm² ([`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html), 3.36um) | 76k/mm² ([`buff_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 3.36um) | Strengthens a signal |
| Flip-flop | 16k/mm² ([`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html), 16.24um) | 17k/mm² ([`dfxtp_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3), 15.12um) | Stores one bit |

These are hard upper bounds — the density if you packed cells edge-to-edge with zero routing overhead. For each library the smallest cell of that kind is used; the 3.3V library has no drive strength 1 cells, so its smallest cells are the `_2` variants.

In practice, real designs achieve significantly less because:

- **(a) Routing overhead** — wires connecting cells need room, which limits how tightly cells can be placed
- **(b) Infrastructure cells** — fillers, taps, antenna diodes, and tie cells make up 60% of cell instances on this reticle
- **(c) Mixed cell types** — designs use a mix of small and large cells
- **(d) Power planning** — power/ground straps consume area
- **(e) Clock distribution** — clock tree buffers and wiring take space

## Achieved Standard Cell Density — Design Averages

The following tables show the average logic standard cell density for each design's "core area" — the interior of the chip excluding the I/O pad ring (a 350um border of large pads around the perimeter used for external connections).

"% of max" compares against the buffer theoretical maximum for the design's primary library. "Cell area" is the share of the core area actually covered by logic cells — the placement utilisation of the die as a whole, including any area left empty or given to SRAM.

### High Density (above 10k logic SC/mm² core average)

| Design | Library | Core SC/mm² | % of max | Cell area | Logic SC | SRAM | Project |
|---|---|---|---|---|---|---|---|
| [038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 79% | 3k | 0 | [Hardware Entropy Explorer: UART/SPI TRNG and PUF](https://github.com/gojimmypi/ttgf0p3-UART-FSM-TRNG-Lab) |
| [450](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/450.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 27k | 36% | 79% | 3k | 0 | [USB CDC (Serial) Device](https://github.com/urish/tt-usbcdc-device) |
| [358](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/358.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 35% | 75% | 3k | 0 | [Hardware Entropy Explorer: UART/SPI TRNG and PUF (Analog)](https://github.com/gojimmypi/ttgf0p3-analog-UART-FSM-TRNG-Lab) |
| [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 35% | 70% | 13k | 0 | [TinyQV Risc-V SoC](https://github.com/MichaelBell/ttgf0p3-tinyQV) |
| [359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 24k | 31% | 60% | 25k | 0 | [Tiny FABulous FPGA (3.3V version)](https://github.com/mole99/tt-fabulous-gf-0p3-3v3) |
| [519](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/519.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 31% | 64% | 1k | 0 | [Simon Says memory game](https://github.com/urish/tt-simon-game) |
| [003](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/003.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 63% | 3k | 0 | [VGA Nyan Cat](https://github.com/urish/ttgf0p2-a1k0n-nyan) |
| [258](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/258.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 28% | 58% | 2k | 0 | [Abad2048](https://github.com/alexandercoabad/Abad_2048) |
| [448](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/448.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 2k | 0 | [Wafer.space Logo VGA Screensaver](https://github.com/TinyTapeout/tt-waferspace-vga-screensaver) |
| [518](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/518.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 58% | 20k | 0 | [KianV uLinux SoC](https://github.com/TinyTapeout/KianV-RV32IMA-RISC-V-uLinux-SoC) |
| [356](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/356.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 7k | 0 | [2048 sliding tile puzzle game (VGA)](https://github.com/urish/tt-2048-game) |
| [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 18k | 24% | 47% | 2k | 0 | [PolyWave](https://github.com/ODGrip/ttgf-polywave) |
| [102](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/102.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 18k | 24% | 58% | 19k | 0 | [Tiny FABulous FPGA](https://github.com/mole99/tt-fabulous-gf-0p3) |
| [288](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/288.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 18k | 23% | 43% | 2k | 0 | [Philippine flag waving](https://github.com/alexandercoabad/PILIPINAS_waving) |
| [099](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/099.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 17k | 22% | 51% | 4k | 0 | [Until heat death do us part](https://github.com/Essenceia/Until_Heat_Death_Do_Us_Part) |
| [033](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/033.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 19% | 47% | 2k | 0 | [Simple Signal Generator](https://github.com/mattvenn/simple-signal-generator) |

### Minimal (analog, custom or test structures)

These designs contain fewer than 1,000 logic standard cells:

| Design | Logic SC | Transistors | SRAM | Pads | Project |
|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/000.html) | 234 | 12k | 0 | 0 | [Chip ROM](https://github.com/TinyTapeout/tt-chip-rom) |
| [001](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/001.html) | 108 | 12k | 0 | 0 | [Tiny Tapeout Factory Test](https://github.com/TinyTapeout/ttgf26a-factory-test) |
| [005](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/005.html) | 0 | 112 | 0 | 0 | [74HCT00 Quad 2-Input NAND (3.3 V)](https://github.com/engrvip123/tt_um_74hct00) |
| [007](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/007.html) | 0 | 240 | 0 | 0 | [TT GF180mcuD Analog Factory Test](https://github.com/smunaut/ttgf_analog_factory_test) |
| [035](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/035.html) | 284 | 3k | 0 | 0 | [GF R2R DAC](https://github.com/mattvenn/gf-r2r-dac) |
| [037](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/037.html) | 695 | 13k | 0 | 0 | [algofoogle analog stuff](https://github.com/algofoogle/ttgf0p3-algofoogle-analog) |
| [039](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/039.html) | 0 | 0 | 0 | 0 | [MoM capacitor](https://github.com/htfab/ttgf0p3-momcap) |
| [101](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/101.html) | 0 | 80 | 0 | 0 | [TT GF180mcuD Testbuffer](https://github.com/christoph-weiser/ttgf0p3-submission) |
| [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html) | 0 | 228 | 0 | 0 | [tnt's recreation of a 555 on GF180mcu](https://github.com/smunaut/tt_tnt_gf_555) |
| [256](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/256.html) | 96 | 26k | 1 | 0 | [256x8 SRAM](https://github.com/Essenceia/tt_gf_ocd_sram_test) |
| [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html) | 0 | 15 | 0 | 0 | [GF BGR](https://github.com/bhagwat-rahul/ttgf180-bandgap-reference) |
| [262](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/262.html) | 0 | 78 | 0 | 0 | [Quadrature VCO](https://github.com/smunaut/tt_tnt_gf_vco) |
| [290](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/290.html) | 0 | 96 | 0 | 0 | [Analog 4 bit Current DAC](https://github.com/Kiterai/ttgf-practice1) |
| [292](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/292.html) | 0 | 54 | 0 | 0 | [3.3V Folded Cascode OTA](https://github.com/chennakeshavadasa/LPCAS_TTGF0P3_TP1) |
| [294](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/294.html) | 16 | 300 | 0 | 0 | [Oscillating Bones](https://github.com/urish/ttgf-oscillating-bones) |
| [454](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/454.html) | 0 | 52 | 0 | 0 | [MCML VCO](https://github.com/namibj/tt_gf-0p3_mcml) |

## Achieved Density — Peak 100um x 100um Regions

While the averages above include sparse regions, the densest 100um x 100um square found anywhere on a design shows the highest density it achieved. The square slides over the die in 20um steps and may not touch an SRAM macro.

| Design | Peak Logic SC/mm² | % of buffer max | Library |
|---|---|---|---|
| [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html) | 44k | 58% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [358](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/358.html) | 41k | 54% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html) | 40k | 52% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html) | 37k | 49% of 76k | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [519](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/519.html) | 37k | 49% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [003](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/003.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [450](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/450.html) | 34k | 44% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [102](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/102.html) | 32k | 42% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [288](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/288.html) | 31k | 41% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [258](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/258.html) | 30k | 40% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [356](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/356.html) | 30k | 40% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [518](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/518.html) | 28k | 37% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [099](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/099.html) | 28k | 36% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [448](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/448.html) | 27k | 36% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

The highest achieved density on this reticle is 58% of the buffer theoretical maximum, observed in the densest 100um square region of [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html). The rest of that area is consumed by larger cells, infrastructure cells and the gaps left for routing.

## Library Comparison

Comparing designs that use one library exclusively:

| Metric | [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [as_sc_mcu7t3v3 (AS 7-track, 3.3V)](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
|---|---|---|
| Designs using this library | 21 | 1 |
| Best core density | 28k SC/mm² · 37% of max ([038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html)) | 24k SC/mm² · 31% of max ([359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html)) |
| Best peak grid cell | 44k SC/mm² · 58% of max ([452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html)) | 37k SC/mm² · 49% of max ([359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html)) |
| Median core density | 18k SC/mm² · 24% of max | 24k SC/mm² · 31% of max |

Differences between libraries here reflect which designs chose which library as much as the libraries themselves; the theoretical difference from row height alone is in the table above.

## Most Common Logic Cell Types

The 15 most-used logic cell types across all unique designs on the reticle:

| Cell Type | Library | Instances | What it does |
|---|---|---|---|
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 8k | 2-input NAND gate |
| [`mux2_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 7k | 2-input multiplexer (2x drive) |
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | Buffer |
| [`nor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nor2/gf180mcu_fd_sc_mcu7t5v0__nor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | 2-input NOR gate |
| [`latq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/latq/gf180mcu_fd_sc_mcu7t5v0__latq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | Latch (level-sensitive) |
| [`dlxfp_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 6k | Latch (level-sensitive) (2x drive) |
| [`aoi21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi21/gf180mcu_fd_sc_mcu7t5v0__aoi21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | AND-OR-Invert compound gate |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | D flip-flop (1 bit storage) |
| [`buff_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 5k | Buffer (2x drive) |
| [`oai21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai21/gf180mcu_fd_sc_mcu7t5v0__oai21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | OR-AND-Invert compound gate |
| [`clkinv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkinv/gf180mcu_fd_sc_mcu7t5v0__clkinv_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | Clock inverter |
| [`buf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | Buffer (2x drive) |
| [`mux4_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/mux4/gf180mcu_fd_sc_mcu7t5v0__mux4_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | 4-input multiplexer |
| [`dffq_4`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_4.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 2k | D flip-flop (1 bit storage) (4x drive) |
| [`oai211_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai211/gf180mcu_fd_sc_mcu7t5v0__oai211_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 2k | OR-AND-Invert compound gate |

Across the reticle there are 9k 2-input NAND gates and 9k flip-flops — 1.0 NAND2 gates per flip-flop.

## SRAM Block Usage

SRAM (Static Random-Access Memory) blocks are pre-designed memory macros. Unlike standard cells, which are composed by automated tools, SRAM blocks are hand-optimized fixed-size units designed to store data as densely as possible.

1 of the 32 designs include SRAM, holding 0 KiB of memory between them:

| Design | SRAM macros | SRAM bits | SRAM area | Logic SC | Project |
|---|---|---|---|---|---|
| [256](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/256.html) | 1 | 2,048 | 0.07 mm² (59% of core) | 96 | [256x8 SRAM](https://github.com/Essenceia/tt_gf_ocd_sram_test) |

SRAM macros are identified by cell name, and their area is the macro footprint. "custom" marks a design with SRAM marker shapes ([GDS 108/5](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) but no recognised macro, where the count and size are not known and the area is that of the marked bitcell arrays.

## SRAM vs Standard Cell Transistor Density

"Transistor density" here counts the number of distinct regions where a gate electrode (polysilicon, [GDS 30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) crosses an active area (diffusion, [GDS 22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) — each such crossing forms one transistor.

### Theoretical Maximum Transistor Density for Standard Cells

| Cell ([7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html) | 2.24 um | 114k | 2 | 228k/mm² |
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | 2.80 um | 91k | 4 | 364k/mm² |
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html) | 3.36 um | 76k | 4 | 304k/mm² |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | 16.24 um | 16k | 24 | 377k/mm² |

| Cell ([AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`inv_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 2.24 um | 114k | 4 | 456k/mm² |
| [`nand2_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 3.92 um | 65k | 8 | 521k/mm² |
| [`buff_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 3.36 um | 76k | 6 | 456k/mm² |
| [`dfxtp_2`](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 15.12 um | 17k | 26 | 439k/mm² |

### SRAM Macros

| Macro | Size | Trans/mm² | % of flip-flop max | Placements |
|---|---|---|---|---|
| [`gf180mcu_ocd_ip_sram__sram256x8m8wm1`](https://github.com/RTimothyEdwards/gf180mcu_ocd_ip_sram/blob/main/cells/gf180mcu_ocd_ip_sram__sram256x8m8wm1/gf180mcu_ocd_ip_sram__sram256x8m8wm1.rst) | 301 x 225 um | 270k/mm² | 62% | 1 |

The macro density includes the peripheral circuits (address decoders, sense amplifiers, I/O drivers) around the bitcell array, which is why larger macros of a family are denser than smaller ones.

### Best Standard Cell Regions

| Design | Peak 1mm² Trans/mm² | % of flip-flop max | Library |
|---|---|---|---|
| [359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html) | 429k/mm² | 98% | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [003](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/003.html) | 352k/mm² | 80% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [356](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/356.html) | 348k/mm² | 79% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [448](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/448.html) | 344k/mm² | 78% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html) | 335k/mm² | 76% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [519](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/519.html) | 328k/mm² | 75% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html) | 327k/mm² | 75% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [450](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/450.html) | 326k/mm² | 74% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

Infrastructure cells are excluded from logic cell counts but their transistors (decoupling capacitors in particular) are included in transistor counts.

## Process Features and Voltages

Which transistor voltages and optional devices of the GF180MCU process the 32 designs use. Voltages count both the libraries a design chose (standard cells and SRAM) and transistors the designer drew. Devices count only what the designer drew: standard cells, SRAM macros, I/O pads and fill are left out, because every die has them. A single test structure counts the same as a large block.

| Transistor voltage | Designs | Which |
|---|---|---|
| 3.3 V | 11 of 32 | [005](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/005.html), [007](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/007.html), [037](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/037.html), [256](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/256.html), [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html), [262](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/262.html), [290](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/290.html), [292](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/292.html), [294](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/294.html), [359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html), [454](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/454.html) |
| 5 V | 23 of 32 | [000](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/000.html), [001](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/001.html), [003](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/003.html), [007](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/007.html), [033](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/033.html), [035](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/035.html), [037](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/037.html), [038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html), [099](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/099.html), [102](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/102.html), [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html), [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html), [256](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/256.html), [258](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/258.html), [288](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/288.html), [294](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/294.html), [356](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/356.html), [358](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/358.html), [448](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/448.html), [450](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/450.html), [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html), [518](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/518.html), [519](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/519.html) |
| 6 V | 1 of 32 | [101](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/101.html) |

| Device | Designs drawing it | Which |
|---|---|---|
| High-resistance poly resistors | 8 of 32 | [035](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/035.html), [037](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/037.html), [101](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/101.html), [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html), [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html), [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html), [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html), [454](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/454.html) |
| MOS capacitors | 1 of 32 | [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html) |
| Unsalicided poly resistors | 1 of 32 | [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html) |
| Deep N-well | 1 of 32 | [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html) |
| Bipolar transistors | 1 of 32 | [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html) |
| Native transistors | 0 of 32 | — |
| 10 V LDMOS | 0 of 32 | — |
| MIM capacitors | 0 of 32 | — |
| Salicided poly resistors | 0 of 32 | — |
| Diffusion resistors | 0 of 32 | — |
| N-well resistors | 0 of 32 | — |
| Metal resistors | 0 of 32 | — |
| Diodes (DIODE_MK) | 0 of 32 | — |
| Well diodes | 0 of 32 | — |
| Schottky diodes | 0 of 32 | — |
| Zener diodes | 0 of 32 | — |
| eFuses | 0 of 32 | — |
| One-time programmable memory | 0 of 32 | — |
| Inductors | 0 of 32 | — |

| Design | Voltages | Custom transistors 3.3 / 5 / 6 V | Devices drawn | I/O library |
|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/000.html) | 5 V | 0 / 0 / 0 | — | — |
| [001](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/001.html) | 5 V | 0 / 0 / 0 | — | — |
| [003](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/003.html) | 5 V | 0 / 0 / 0 | — | — |
| [005](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/005.html) | 3.3 V | 112 / 0 / 0 | — | — |
| [007](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/007.html) | 3.3 V, 5 V | 8 / 232 / 0 | — | — |
| [033](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/033.html) | 5 V | 0 / 0 / 0 | — | — |
| [035](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/035.html) | 5 V | 0 / 0 / 0 | High-resistance poly resistors | — |
| [037](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/037.html) | 3.3 V, 5 V | 122 / 0 / 0 | High-resistance poly resistors | — |
| [038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html) | 5 V | 0 / 0 / 0 | — | — |
| [039](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/039.html) | — | 0 / 0 / 0 | — | — |
| [099](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/099.html) | 5 V | 0 / 0 / 0 | — | — |
| [101](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/101.html) | 6 V | 0 / 0 / 80 | High-resistance poly resistors | — |
| [102](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/102.html) | 5 V | 0 / 0 / 0 | — | — |
| [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html) | 5 V | 0 / 216 / 0 | MOS capacitors, High-resistance poly resistors, Unsalicided poly resistors | — |
| [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html) | 5 V | 0 / 0 / 0 | High-resistance poly resistors | — |
| [256](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/256.html) | 3.3 V, 5 V | 0 / 0 / 0 | — | — |
| [258](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/258.html) | 5 V | 0 / 0 / 0 | — | — |
| [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html) | 3.3 V | 15 / 0 / 0 | High-resistance poly resistors, Deep N-well, Bipolar transistors | — |
| [262](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/262.html) | 3.3 V | 78 / 0 / 0 | — | — |
| [288](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/288.html) | 5 V | 0 / 0 / 0 | — | — |
| [290](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/290.html) | 3.3 V | 96 / 0 / 0 | — | — |
| [292](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/292.html) | 3.3 V | 54 / 0 / 0 | — | — |
| [294](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/294.html) | 3.3 V, 5 V | 44 / 0 / 0 | — | — |
| [356](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/356.html) | 5 V | 0 / 0 / 0 | — | — |
| [358](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/358.html) | 5 V | 0 / 0 / 0 | — | — |
| [359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html) | 3.3 V | 0 / 0 / 0 | — | — |
| [448](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/448.html) | 5 V | 0 / 0 / 0 | — | — |
| [450](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/450.html) | 5 V | 0 / 0 / 0 | — | — |
| [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html) | 5 V | 0 / 0 / 0 | High-resistance poly resistors | — |
| [454](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/454.html) | 3.3 V | 52 / 0 / 0 | High-resistance poly resistors | — |
| [518](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/518.html) | 5 V | 0 / 0 / 0 | — | — |
| [519](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/519.html) | 5 V | 0 / 0 / 0 | — | — |

Detection uses the open GF180MCU layers: a transistor is gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) over diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), thick oxide inside Dualgate ([55/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), 5 V where V5_XTOR ([112/1](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) also covers it and 6 V where it does not; MIM capacitors are FuseTop ([75/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) shapes; poly resistors are Poly2 under RES_MK ([110/5](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), high resistance under the Resistor layer ([62/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and otherwise unsalicided under SAB ([49/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) or salicided. Other devices are found by their marker layers.

## Key Findings

1. The densest logic standard cell design, [038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html) (Hardware Entropy Explorer: UART/SPI TRNG and PUF), achieves **28k logic SC/mm²** averaged over its core (37% of buffer max), with a peak of **40k logic SC/mm²** in its densest 1mm² region.

2. Standard cell libraries in use: **[7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)** (78% of logic cells), **[AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3)** (22% of logic cells).

3. The median digital design achieves **20k logic SC/mm²** over its core. 16 of 16 designs exceed 10k logic SC/mm².

4. The best standard cell region reaches **429k transistors/mm²** ([359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html)); the most used SRAM macro, [`gf180mcu_ocd_ip_sram__sram256x8m8wm1`](https://github.com/RTimothyEdwards/gf180mcu_ocd_ip_sram/blob/main/cells/gf180mcu_ocd_ip_sram__sram256x8m8wm1/gf180mcu_ocd_ip_sram__sram256x8m8wm1.rst), is 270k transistors/mm².

5. Infrastructure cells (fillers, taps, antenna diodes, ties) outnumber logic cells **1.5 to 1** across the reticle (170k vs 113k). Any density analysis must exclude these to avoid dramatically overstating actual logic content.

6. The most common logic cell is **[`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html)** (8k instances in [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)).

## Per-Design Details

| Design | Cell | Die (mm) | Core mm² | Placements | Pads | Logic SC | Infra SC | Transistors | SRAM | Libraries |
|---|---|---|---|---|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/000.html) | `000_tt_um_chip_rom` | 0.35 x 0.16 | 0.1 | 1 | 0 | 234 | 1,590 | 11,848 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 234 |
| [001](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/001.html) | `001_tt_um_factory_test` | 0.35 x 0.16 | 0.1 | 1 | 0 | 108 | 1,248 | 11,846 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 108 |
| [003](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/003.html) | `003_tt_um_a1k0n_nyancat` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,662 | 3,786 | 33,356 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,662 |
| [005](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/005.html) | `005_tt_um_74hct00` | 0.35 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 112 | 0 | — |
| [007](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/007.html) | `007_tt_um_analog_factory_test` | 0.33 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 240 | 0 | — |
| [033](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/033.html) | `033_tt_um_mattvenn_signal_generator` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,704 | 3,420 | 31,174 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,704 |
| [035](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/035.html) | `035_tt_um_gf_r2r_dac` | 0.35 x 0.33 | 0.1 | 1 | 0 | 284 | 825 | 2,970 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 284 |
| [037](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/037.html) | `037_tt_um_algofoogle_gf_analog` | 0.35 x 0.33 | 0.1 | 1 | 0 | 695 | 1,897 | 13,000 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 695 |
| [038](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/038.html) | `038_tt_um_gojimmypi_ttgfa_UART_FSM_TRNG_Lab` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,281 | 3,029 | 35,342 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,281 |
| [039](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/039.html) | `039_tt_um_htfab_momcap` | 0.35 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 0 | 0 | — |
| [099](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/099.html) | `099_tt_um_coldbrew` | 0.71 x 0.33 | 0.2 | 1 | 0 | 3,961 | 7,642 | 64,761 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,961 |
| [101](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/101.html) | `101_tt_um_cw_testbuffer` | 0.33 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 80 | 0 | — |
| [102](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/102.html) | `102_tt_um_fabulous_gf_0p3` | 1.44 x 0.74 | 1.1 | 1 | 0 | 19,232 | 23,147 | 272,114 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 19,232 |
| [103](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/103.html) | `103_tt_um_tnt_gf_555` | 0.33 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 228 | 0 | — |
| [199](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/199.html) | `199_tt_um_MichaelBell_tinyQV` | 1.44 x 0.33 | 0.5 | 1 | 0 | 12,513 | 15,819 | 140,890 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 12,513 |
| [256](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/256.html) | `256_tt_um_essen` | 0.35 x 0.33 | 0.1 | 1 | 0 | 96 | 1,226 | 25,949 | 1 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 96 |
| [258](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/258.html) | `258_tt_um_AbAdA_2048` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,452 | 4,224 | 32,221 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,452 |
| [260](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/260.html) | `260_tt_um_rahulbhagwat_gf180_bandgap_reference` | 0.33 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 15 | 0 | — |
| [262](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/262.html) | `262_tt_um_tnt_gf_vco` | 0.35 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 78 | 0 | — |
| [288](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/288.html) | `288_tt_um_combined` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,028 | 3,974 | 29,712 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,028 |
| [290](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/290.html) | `290_tt_um_kiterai_current_dac` | 0.35 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 96 | 0 | — |
| [292](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/292.html) | `292_tt_um_LPCAS_TTGF0P3_TP1` | 0.33 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 54 | 0 | — |
| [294](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/294.html) | `294_tt_um_oscillating_bones` | 0.35 x 0.33 | 0.1 | 1 | 0 | 16 | 18 | 300 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [356](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/356.html) | `356_tt_um_2048_vga_game` | 1.08 x 0.33 | 0.4 | 1 | 0 | 6,736 | 11,639 | 100,459 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 6,736 |
| [358](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/358.html) | `358_tt_um_gojimmypi_ttgfa_UART_FSM_TRNG_Lab_analog` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,048 | 2,588 | 35,043 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,048 |
| [359](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/359.html) | `359_tt_um_fabulous_gf_0p3_3v3` | 1.44 x 0.74 | 1.1 | 1 | 0 | 25,184 | 31,777 | 329,158 | 0 | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3): 25,184 |
| [448](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/448.html) | `448_tt_um_waferspace_vga_screensaver` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,228 | 4,301 | 32,311 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,228 |
| [450](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/450.html) | `450_tt_um_urish_usb_cdc` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,155 | 2,986 | 35,599 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,155 |
| [452](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/452.html) | `452_tt_um_odgrip_polywave` | 0.33 x 0.33 | 0.1 | 1 | 0 | 1,985 | 1,191 | 18,922 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,985 |
| [454](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/454.html) | `454_tt_um_mcml_vco` | 0.35 x 0.33 | 0.1 | 1 | 0 | 0 | 0 | 52 | 0 | — |
| [518](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/518.html) | `518_tt_um_kianV_rv32ima_uLinux_SoC` | 1.44 x 0.74 | 1.1 | 1 | 0 | 20,266 | 42,242 | 315,831 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 20,266 |
| [519](https://wafer.space/tinytapeouts/ttgf0p3/ws-run2-t0p3/projects/519.html) | `519_tt_um_urish_simon` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,301 | 1,358 | 13,356 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,301 |

## Methodology

- **Logic cell counts** come from walking the layout hierarchy and counting instances of every cell whose name contains a standard cell library prefix, excluding types starting with `fill`, `endcap`, `filltie`, `fillcap`, `tap`, `antenna`, `diode`, `tiel`, `tieh`.
- **Transistor counts** are the number of merged polygons in the boolean AND of the diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) layers, leaving out dummy fill cells, whose diffusion and polysilicon squares overlap without forming transistors.
- **Core area** is (die width − 0.70mm) x (die height − 0.70mm), removing a 350um pad ring from each side.
- **Cell dimensions** are the width and height of each standard cell's placement boundary ([GDS 0/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), measured from the cells present in this layout.
- **Theoretical maximum** = (1000um / cell width) x (1000um / row height).
- **Peak figures** are the densest 100um x 100um square anywhere inside each die, found by sliding the square in 20um steps over the die and skipping positions that touch an SRAM macro. Logic cells are placed by their origin and transistors by the centre of their gate. They are given per mm².
- **SRAM macros** are counted by cell name. The `sram_block_count` column of the summary CSV is kept for comparison with earlier results; it counts SramCore marker shapes, of which each GF180MCU macro has two.
- Designs placed more than once on the reticle are counted once.

---

*Generated by [ws-run-reports](https://github.com/wafer-space/ws-run-reports) from `T0P3.oas` (md5 `bfd37b3547ee338c21a9689a031bbb0c`) in [wafer-space/tinytapeouts/ttgf0p3/ws-run2-t0p3](https://github.com/wafer-space/tinytapeouts/tree/main/ttgf0p3/ws-run2-t0p3). Analysis method: [KLayout](https://www.klayout.de/) boolean geometry operations on GDS layers. Grid resolution: 100um x 100um. Density figures are rounded to the nearest 1k.*
