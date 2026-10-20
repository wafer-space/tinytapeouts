# Tiny Tapeout GF 26a on wafer.space Run 2 — Standard Cell & SRAM Density Report

**GF180MCU Process (GlobalFoundries 180nm), Shuttle T26A**

## Introduction

This report analyzes the standard cell and SRAM density achieved by the 95 unique public chip designs on the Tiny Tapeout GF 26a on wafer.space Run 2 reticle. The reticle has 95 slots; the public layout contains 95 slot placements (some designs appear more than once, and private designs are not included).

All designs were fabricated on GlobalFoundries' GF180MCU process, a 180-nanometer (0.18um) technology node. This is a mature, relatively large-geometry process — for comparison, modern smartphone chips use 3nm or 5nm processes with features roughly 50x smaller.

> **Note on counting methodology:** All standard cell counts in this report count only **logic cells** — cells that perform actual computation (gates, flip-flops, buffers, multiplexers, etc.). Infrastructure cells are excluded: filler cells (fill, fillcap, endcap, filltie), well taps, antenna fix diodes, ESD diodes, and tie-high/tie-low cells. These infrastructure cells are inserted by automated tools to satisfy manufacturing rules but perform no logic function. On this reticle there are 263k infrastructure cell instances and 138k logic cell instances across the unique designs — 1.9 infrastructure cells for every logic cell.

## What Are Standard Cells?

A "standard cell" is a pre-designed, pre-verified building block used to construct digital circuits. Think of them like LEGO bricks for chip design: each cell performs one simple logic function (an AND gate, a flip-flop for storing one bit, a buffer for boosting signal strength), and a chip designer assembles thousands or millions of them to build complex circuits.

Standard cells in a library all share the same height (so they line up in rows) but vary in width depending on their function. Automated tools place these cells in rows and then route wires between them.

The "density" of standard cells — how many fit per square millimeter — is a key measure of how efficiently a design uses its silicon area. Higher density generally means more logic functionality packed into less chip area, which reduces cost.

## Standard Cell Libraries on This Reticle

| Library | Row Height | Rows per mm | Relative Density | Logic instances | Share |
|---|---|---|---|---|---|
| [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3.92 um | 255 rows | 100% | 138k | 100% |
| [mcu9t5v0 (9-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | 5.04 um | 198 rows | 78% | 48 | <1% |

Row height is the height of the cells' placement boundary, which is what rows are stacked at. Taller rows hold fewer cells per mm² but leave more room for wiring inside the cell.

## Theoretical Maximum Standard Cell Density

If you filled an entire square millimeter with nothing but one type of logic standard cell (no wiring, no gaps, no infrastructure cells), the theoretical maximum density would be:

| Cell Type | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | What it does |
|---|---|---|---|
| Inverter | 114k/mm² ([`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html), 2.24um) | 89k/mm² ([`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/inv/gf180mcu_fd_sc_mcu9t5v0__inv_1.html), 2.24um) | Flips a signal |
| NAND gate | 91k/mm² ([`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html), 2.80um) | 71k/mm² ([`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/nand2/gf180mcu_fd_sc_mcu9t5v0__nand2_1.html), 2.80um) | Basic logic gate |
| Buffer | 76k/mm² ([`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html), 3.36um) | 59k/mm² ([`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/buf/gf180mcu_fd_sc_mcu9t5v0__buf_1.html), 3.36um) | Strengthens a signal |
| Flip-flop | 16k/mm² ([`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html), 16.24um) | 13k/mm² ([`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/dffq/gf180mcu_fd_sc_mcu9t5v0__dffq_1.html), 15.68um) | Stores one bit |

These are hard upper bounds — the density if you packed cells edge-to-edge with zero routing overhead. For each library the smallest cell of that kind is used; the 3.3V library has no drive strength 1 cells, so its smallest cells are the `_2` variants.

In practice, real designs achieve significantly less because:

- **(a) Routing overhead** — wires connecting cells need room, which limits how tightly cells can be placed
- **(b) Infrastructure cells** — fillers, taps, antenna diodes, and tie cells make up 66% of cell instances on this reticle
- **(c) Mixed cell types** — designs use a mix of small and large cells
- **(d) Power planning** — power/ground straps consume area
- **(e) Clock distribution** — clock tree buffers and wiring take space

## Achieved Standard Cell Density — Design Averages

The following tables show the average logic standard cell density for each design's "core area" — the interior of the chip excluding the I/O pad ring (a 350um border of large pads around the perimeter used for external connections).

"% of max" compares against the buffer theoretical maximum for the design's primary library. "Cell area" is the share of the core area actually covered by logic cells — the placement utilisation of the die as a whole, including any area left empty or given to SRAM.

### High Density (above 10k logic SC/mm² core average)

| Design | Library | Core SC/mm² | % of max | Cell area | Logic SC | SRAM | Project |
|---|---|---|---|---|---|---|---|
| [353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 34k | 45% | 81% | 2k | 0 | [DOTTEE VGA demo (TTGF26a)](https://github.com/algofoogle/dottee-demo) |
| [486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 33k | 43% | 85% | 2k | 0 | [BioPulse Tile](https://github.com/RobMBSos/tt_um_roberto_tiny_radar_tile) |
| [390](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/390.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 30k | 39% | 81% | 3k | 0 | [GPS_Accelerator](https://github.com/jpigdon/ttgf_gnss_accelerator) |
| [129](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/129.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 29k | 39% | 69% | 3k | 0 | [7-Segment Neural Predictor](https://github.com/Nontinium/ttgf-machine-learning) |
| [551](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/551.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 29k | 38% | 73% | 2k | 0 | [Tiny Quantum Circuit Simulator](https://github.com/ohuettenhofer/tiny-qsim-ttgf26a) |
| [352](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/352.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 79% | 3k | 0 | [Hardware Entropy Explorer: UART/SPI TRNG and PUF](https://github.com/gojimmypi/ttgf-UART-FSM-TRNG-Lab) |
| [036](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/036.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 77% | 3k | 0 | [FSK Modem](https://github.com/vvedn/hydrocomms-tt) |
| [135](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/135.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 81% | 10k | 0 | [serv_soc_wb](https://github.com/divadnauj-GB/tt_um_divadnauj-GB_serv_soc_wb) |
| [005](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/005.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 27k | 36% | 80% | 2k | 0 | [2x2 CNN Accelerator PE Grid with UART](https://github.com/Vidhyanandhan-01/tinytapeout-gf) |
| [545](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/545.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 27k | 36% | 77% | 2k | 0 | [BF](https://github.com/Josephwann/jj-tinytapeout) |
| [578](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/578.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 34% | 71% | 1k | 0 | [Balanced Ternary Multiplier](https://github.com/lanserge/tt-ternary-multiplier-tiny) |
| [454](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/454.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 34% | 70% | 3k | 0 | [Tensor Processing Unit For GF](https://github.com/mocusez/ttgf-tpu) |
| [038](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/038.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 32% | 76% | 3k | 0 | [RRAM Characterization Platform (DC sweep + endurance + retention + hi…](https://github.com/SanthoshSivasubramani/tt_um_santhosh_rsd_char_gf_pub) |
| [356](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/356.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 32% | 83% | 3k | 0 | [RHD2164-MCU-SPI Bridge](https://github.com/manuel-monge/tt2606) |
| [611](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/611.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 31% | 65% | 1k | 0 | [UNIZG-FER VGA project](https://github.com/hofi505/fer-vga-tt26a) |
| [384](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/384.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 31% | 61% | 3k | 0 | [teenytpu](https://github.com/joannec34/teenytpu) |
| [355](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/355.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 31% | 64% | 1k | 0 | [Simon Says memory game](https://github.com/urish/tt-simon-game) |
| [615](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/615.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 75% | 1k | 0 | [Video mode tester](https://github.com/htfab/ttgf-vga-tester) |
| [549](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/549.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 70% | 1k | 0 | [Ring Oscillator PVT Sensor & TRNG (GF180)](https://github.com/SanthoshSivasubramani/tt_um_santhosh_ring_osc_gf_pub) |
| [034](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/034.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 65% | 3k | 0 | [2x2 MAC Systolic array with DFT](https://github.com/Eulerianial/tt_gf_systolic_array) |
| [450](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/450.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 65% | 3k | 0 | [Simple MAC Engine w/ Postproc](https://github.com/Arty3/ttgf-mac-engine) |
| [547](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/547.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 70% | 1k | 0 | [Memristive Crossbar Peripheral Controller (GF180)](https://github.com/SanthoshSivasubramani/tt_um_santhosh_xbar_ctrl_gf_pub) |
| [032](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/032.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 51% | 1k | 0 | [Hardware UTF Encoder/Decoder](https://github.com/RebeccaRGB/ttgf-hardware-utf8) |
| [039](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/039.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 65% | 23k | 0 | [Programmable_Pipeline-RISC-V](https://github.com/PrmBRana/ttgf_prem_programmable_RISC_v) |
| [482](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/482.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 77% | 1k | 0 | [SAP 8 Bit Computer](https://github.com/navneetprasad1311/ttgf180-8bitcomputer) |
| [577](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/577.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 28% | 54% | 1k | 0 | [Custom DVD Screensaver for VGA](https://github.com/AlanPandaSK/tt_um_uacj_bouncing_DVD_screensaver) |
| [358](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/358.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 28% | 69% | 2k | 0 | [Stochastic neuron + STDP controller (merged, GF180)](https://github.com/SanthoshSivasubramani/tt_um_santhosh_stoch_stdp_pair_gf_pub) |
| [070](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/070.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 28% | 48% | 1k | 0 | [xoroshiro64](https://github.com/ChiranjitPatel/ttgf_xoroshiro64) |
| [195](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/195.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 27% | 64% | 5k | 0 | [Tiny Pixel Processor](https://github.com/vogelhubersimon/Tiny-Pixel-Processor) |
| [096](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/096.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 2k | 0 | [Wafer.space Logo VGA Screensaver](https://github.com/TinyTapeout/tt-waferspace-vga-screensaver) |
| [102](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/102.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 24% | 48% | 1k | 0 | [Custom DVD Screensaver for VGA](https://github.com/nayelikensy930-lang/tt_um_uacj_) |
| [448](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/448.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 16k | 22% | 42% | 2k | 0 | [APA102 to WS2812 Translator](https://github.com/squidgeefish/TT09) |
| [354](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/354.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 20% | 43% | 2k | 0 | [8-bit RISC CPU](https://github.com/hofi505/risc-v-tt26a) |
| [452](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/452.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 19% | 47% | 2k | 0 | [Simple Signal Generator](https://github.com/mattvenn/simple-signal-generator) |
| [295](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/295.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 14k | 19% | 42% | 15k | 0 | [UTOSS RISC-V core](https://github.com/UTOSS/risc-v-ttgf) |
| [388](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/388.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 13k | 17% | 41% | 2k | 0 | [Tiny TPU Systolic Array](https://github.com/bgao43-wq/tt-tiny-tpu-gf180) |
| [199](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/199.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 12k | 16% | 39% | 3k | 0 | [Very Low Resource Digital Implementation of Bioimpedance Analysis](https://github.com/fabien-soulier/tt-gf26A-bioimpedance) |

### Medium Density (3k–10k logic SC/mm² core average)

| Design | Library | Core SC/mm² | % of max | Cell area | Logic SC | SRAM | Project |
|---|---|---|---|---|---|---|---|
| [386](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/386.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 10k | 13% | 26% | 1k | 0 | [Pong in Verilog](https://github.com/ColdC5/TinyTapeoutGFPong) |
| [103](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/103.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 9k | 12% | 24% | 4k | 2 | [Minimal RV32E SoC with UART Loader](https://github.com/KLuterIRV/INNOVA-IRV-ULP-RISCV) |

### Minimal (analog, custom or test structures)

These designs contain fewer than 1,000 logic standard cells:

| Design | Logic SC | Transistors | SRAM | Pads | Project |
|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/000.html) | 233 | 12k | 0 | 0 | [Chip ROM](https://github.com/TinyTapeout/tt-chip-rom) |
| [001](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/001.html) | 108 | 12k | 0 | 0 | [Tiny Tapeout Factory Test](https://github.com/TinyTapeout/ttgf26a-factory-test) |
| [003](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/003.html) | 71 | 12k | 0 | 0 | [Counter16Outputs](https://github.com/AlvaroRub/tt-alvaros-first-wokwi) |
| [007](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/007.html) | 951 | 14k | 0 | 0 | [2x2 Systolic Array Matrix Multiplier](https://github.com/Irene-ux/tt-systolic-array-2x2) |
| [065](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/065.html) | 16 | 11k | 0 | 0 | [Antonio's first Wokwi design](https://github.com/aglcoin04/tt-antonios-first-wokwi) |
| [066](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/066.html) | 21 | 11k | 0 | 0 | [sdft wokwi 1](https://github.com/santidft/tt-sdft-wokwi-1) |
| [067](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/067.html) | 13 | 11k | 0 | 0 | [Guille's first Wokwi design.](https://github.com/guillermomillansolis-rgb/tt-guilles-first-wokwi) |
| [068](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/068.html) | 302 | 12k | 0 | 0 | [Line Follower Robot controller](https://github.com/Arvaloez/ECI_SEGUIDOR_LINEA_IEEE_BOOTCAMP) |
| [069](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/069.html) | 880 | 15k | 0 | 0 | [MIPS-Lite 8-bit Processor](https://github.com/jalperdev/tt-chip-design-nucleo) |
| [071](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/071.html) | 8 | 11k | 0 | 0 | [Juan`s first Worki design](https://github.com/JuanAndres6386/tt-juans-first-worki) |
| [098](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/098.html) | 580 | 13k | 0 | 0 | [happyhop](https://github.com/deadcast2/tt_um_happyhop) |
| [100](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/100.html) | 983 | 14k | 0 | 0 | [Dino-7: 7-Segment Runner Game](https://github.com/DrSopes/Dino-7-GF) |
| [128](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/128.html) | 16 | 11k | 0 | 0 | [Tiny Tapeout Template Copy](https://github.com/pabloruizlopez2001-cloud/tt-template-copy) |
| [130](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/130.html) | 13 | 11k | 0 | 0 | [El primer diseño](https://github.com/02mariasv/tt-el-primer-diseo) |
| [132](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/132.html) | 12 | 11k | 0 | 0 | [Mi copia del Tiny Tapeout](https://github.com/VallejoPretelA/tt-mi-copia-del) |
| [134](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/134.html) | 13 | 11k | 0 | 0 | [test1](https://github.com/aperezfer/tt-test1) |
| [192](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/192.html) | 224 | 12k | 0 | 0 | [Gen1 Digital Companion Tile](https://github.com/JuanCarlosFdezMlg/tt-juan-carloss-first) |
| [194](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/194.html) | 27 | 11k | 0 | 0 | [Tiny Tapeout Template Ayman](https://github.com/aymanhq96/tt-template-ayman) |
| [196](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/196.html) | 12 | 11k | 0 | 0 | [Julian_Proyecto](https://github.com/jpachecorub/tt-julianproyecto) |
| [198](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/198.html) | 18 | 11k | 0 | 0 | [Tiny Tapeout Template Copy](https://github.com/AliciaRRs/tt-template-copy) |
| [357](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/357.html) | 8 | 11k | 0 | 0 | [First Tinytapeout](https://github.com/raullopez54/tt-first-tinytapeout) |
| [359](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/359.html) | 21 | 11k | 0 | 0 | [Tiny Tapeout testtest 111233](https://github.com/idatarm/tt-testtest-111233) |
| [385](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/385.html) | 8 | 11k | 0 | 0 | [Tiny Tapeout Workshop JuanF](https://github.com/jfm92/tt-workshop-juanf) |
| [387](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/387.html) | 16 | 11k | 0 | 0 | [Tiny Tapeout Template_1234](https://github.com/neshla/tt-template1234) |
| [389](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/389.html) | 20 | 11k | 0 | 0 | [Arturo's first Wokwi design](https://github.com/Artcraftx107/tt-arturos-first-wokwi) |
| [391](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/391.html) | 8 | 11k | 0 | 0 | [Pacos first design](https://github.com/flozgom/tt-pacos-first-design) |
| [449](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/449.html) | 12 | 11k | 0 | 0 | [Rafa’s first Wokwi design](https://github.com/RafaMG10/tt-rafas-first-wokwi) |
| [451](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/451.html) | 15 | 11k | 0 | 0 | [7 segment Display Fli-Flop Try-out](https://github.com/CarlosDavidTorresRico/tt-7-segment-display) |
| [453](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/453.html) | 4 | 11k | 0 | 0 | [DiseñoCursoTiny](https://github.com/joserdElectronics/tt-diseocursotiny) |
| [455](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/455.html) | 20 | 11k | 0 | 0 | [Matt’s first Wokwi design](https://github.com/pedro-adasilva/tt-matts-first-wokwi) |
| [480](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/480.html) | 710 | 14k | 0 | 0 | [spiPWMio](https://github.com/FHW-Appel/TTgf26a-spiPWMio) |
| [481](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/481.html) | 14 | 11k | 0 | 0 | [Basic Circuit](https://github.com/izanamador/tt-basic-circuit) |
| [483](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/483.html) | 14 | 11k | 0 | 0 | [El primer diseño de Matt para Wokwi](https://github.com/marcosgafer/tt-el-primer-diseo) |
| [484](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/484.html) | 325 | 13k | 0 | 0 | [BIST-8: Built-In Self-Test for 8-bit CLA Adder](https://github.com/mgarciajimenezAirzone/tt-mmggjj) |
| [485](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/485.html) | 12 | 11k | 0 | 0 | [Tiny Tapeout Template flip flop](https://github.com/nsuarezparrilla3/tt-template-flip-flop) |
| [487](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/487.html) | 28 | 12k | 0 | 0 | [Tiny Tapeout RJAP](https://github.com/rodalvar23/tt-rjap) |
| [512](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/512.html) | 38 | 12k | 0 | 0 | [Tiny Tapeout JMCG](https://github.com/jmcanogarcia/tt-jmcg) |
| [513](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/513.html) | 832 | 15k | 0 | 0 | [rgb_mixer](https://github.com/divadnauj-GB/tt_um_divadnaujGB_rgb_muxer_pb) |
| [514](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/514.html) | 13 | 11k | 0 | 0 | [Paula's first Wokwi design](https://github.com/paulagarcianm-cmd/tt-paulas-first-wokwi) |
| [515](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/515.html) | 365 | 12k | 0 | 0 | [microlane demo project](https://github.com/htfab/ttgf-microlane-demo) |
| [516](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/516.html) | 8 | 11k | 0 | 0 | [Pedro Template](https://github.com/PitBarber/tt-pedro-template) |
| [517](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/517.html) | 906 | 14k | 0 | 0 | [Ball Display](https://github.com/danielpenas42/ttgf-verilog-danielpenas42) |
| [518](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/518.html) | 168 | 12k | 0 | 0 | [ocxpkeWokwiDesign](https://github.com/ocxpke/tt-ocxpkewokwidesign) |
| [519](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/519.html) | 787 | 15k | 0 | 0 | [Number Memory Game](https://github.com/DanielGabai/ttgf26a-memory-game) |
| [576](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/576.html) | 618 | 13k | 0 | 0 | [Tiny Number Simon](https://github.com/ernestomgz/ernest-tiny-tapeout) |
| [579](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/579.html) | 868 | 14k | 0 | 0 | [VGA_screensaver_UACJ](https://github.com/angelicakoehn/tt_um_logoUACJ_MOGA) |
| [580](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/580.html) | 25 | 11k | 0 | 0 | [Tiny Tapeout Workshop Malaga 2jun2026](https://github.com/mgonzalezg/tt-workshop-malaga-2jun2026) |
| [581](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/581.html) | 994 | 16k | 0 | 0 | [SPI-Controlled 8-Channel LED Driver](https://github.com/gey16/tt_um_grace_spi_led_driver) |
| [582](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/582.html) | 11 | 11k | 0 | 0 | [Simple Sprinkler](https://github.com/noahzperez29/Noah_Simple_Sprinkler) |
| [583](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/583.html) | 606 | 14k | 0 | 0 | [Universal Binary to Segment Decoder](https://github.com/RebeccaRGB/ttgf-ubcd) |
| [608](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/608.html) | 7 | 11k | 0 | 0 | [Rhyloo’s first Wokwi design](https://github.com/rhyloo/tiny-tapeout-test) |
| [609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html) | 48 | 3k | 0 | 0 | [VCO driven by DAC](https://github.com/algofoogle/ttgf26a-vco) |
| [610](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/610.html) | 10 | 11k | 0 | 0 | [Tiny Tapeout Marcos Fernandez](https://github.com/marcosfdez99/tt-marcos-fernandez) |
| [612](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/612.html) | 16 | 11k | 0 | 0 | [Tiny Tapeout Template](https://github.com/sankori-ai/tt-template) |
| [613](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/613.html) | 704 | 14k | 0 | 0 | [Dyadic PWM](https://github.com/maqsudbek/ttgf-dyadic-pwm-iot) |
| [614](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/614.html) | 22 | 11k | 0 | 0 | [ram 1 bit Copy](https://github.com/siningua/tt-ram-1-bit) |

## Achieved Density — Peak 100um x 100um Regions

While the averages above include sparse regions, the densest 100um x 100um square found anywhere on a design shows the highest density it achieved. The square slides over the die in 20um steps and may not touch an SRAM macro.

| Design | Peak Logic SC/mm² | % of buffer max | Library |
|---|---|---|---|
| [486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html) | 42k | 55% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [352](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/352.html) | 40k | 53% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html) | 40k | 53% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [355](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/355.html) | 37k | 49% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [390](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/390.html) | 37k | 49% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [384](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/384.html) | 37k | 49% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [032](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/032.html) | 36k | 48% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [036](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/036.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [135](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/135.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [005](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/005.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [070](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/070.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [545](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/545.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [295](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/295.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [039](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/039.html) | 34k | 45% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [129](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/129.html) | 34k | 45% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

The highest achieved density on this reticle is 55% of the buffer theoretical maximum, observed in the densest 100um square region of [486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html). The rest of that area is consumed by larger cells, infrastructure cells and the gaps left for routing.

## Library Comparison

Comparing designs that use one library exclusively:

| Metric | [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [mcu9t5v0 (9-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) |
|---|---|---|
| Designs using this library | 94 | 1 |
| Best core density | 34k SC/mm² · 45% of max ([353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html)) | 1k SC/mm² · 1% of max ([609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html)) |
| Best peak grid cell | 42k SC/mm² · 55% of max ([486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html)) | 3k SC/mm² · 5% of max ([609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html)) |
| Median core density | 12k SC/mm² · 15% of max | 1k SC/mm² · 1% of max |

Differences between libraries here reflect which designs chose which library as much as the libraries themselves; the theoretical difference from row height alone is in the table above.

## Most Common Logic Cell Types

The 15 most-used logic cell types across all unique designs on the reticle:

| Cell Type | Library | Instances | What it does |
|---|---|---|---|
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 2-input NAND gate |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 11k | D flip-flop (1 bit storage) |
| [`oai21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai21/gf180mcu_fd_sc_mcu7t5v0__oai21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 10k | OR-AND-Invert compound gate |
| [`nor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nor2/gf180mcu_fd_sc_mcu7t5v0__nor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 8k | 2-input NOR gate |
| [`dlyb_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dlyb/gf180mcu_fd_sc_mcu7t5v0__dlyb_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 7k | Delay buffer |
| [`mux2_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/mux2/gf180mcu_fd_sc_mcu7t5v0__mux2_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | 2-input multiplexer (2x drive) |
| [`aoi21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi21/gf180mcu_fd_sc_mcu7t5v0__aoi21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | AND-OR-Invert compound gate |
| [`clkinv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkinv/gf180mcu_fd_sc_mcu7t5v0__clkinv_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | Clock inverter |
| [`dffrnq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffrnq/gf180mcu_fd_sc_mcu7t5v0__dffrnq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | D flip-flop with reset |
| [`buf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | Buffer (2x drive) |
| [`clkbuf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkbuf/gf180mcu_fd_sc_mcu7t5v0__clkbuf_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | Clock buffer (2x drive) |
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | Buffer |
| [`aoi22_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi22/gf180mcu_fd_sc_mcu7t5v0__aoi22_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | AND-OR-Invert (2x2 inputs) |
| [`xor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/xor2/gf180mcu_fd_sc_mcu7t5v0__xor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | 2-input XOR gate |
| [`clkbuf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkbuf/gf180mcu_fd_sc_mcu7t5v0__clkbuf_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | Clock buffer |

Across the reticle there are 15k 2-input NAND gates and 18k flip-flops — 0.8 NAND2 gates per flip-flop.

## SRAM Block Usage

SRAM (Static Random-Access Memory) blocks are pre-designed memory macros. Unlike standard cells, which are composed by automated tools, SRAM blocks are hand-optimized fixed-size units designed to store data as densely as possible.

1 of the 95 designs include SRAM, holding 0 KiB of memory between them:

| Design | SRAM macros | SRAM bits | SRAM area | Logic SC | Project |
|---|---|---|---|---|---|
| [103](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/103.html) | 2 | 2,048 | 0.23 mm² (49% of core) | 4k | [Minimal RV32E SoC with UART Loader](https://github.com/KLuterIRV/INNOVA-IRV-ULP-RISCV) |

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

| Cell ([9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/nand2/gf180mcu_fd_sc_mcu9t5v0__nand2_1.html) | 2.80 um | 71k | 4 | 283k/mm² |
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/buf/gf180mcu_fd_sc_mcu9t5v0__buf_1.html) | 3.36 um | 59k | 4 | 236k/mm² |
| [`dffq_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/dffq/gf180mcu_fd_sc_mcu9t5v0__dffq_2.html) | 16.80 um | 12k | 26 | 307k/mm² |

### SRAM Macros

| Macro | Size | Trans/mm² | % of flip-flop max | Placements |
|---|---|---|---|---|
| [`gf180mcu_fd_ip_sram__sram128x8m8wm1`](https://gf180mcu-pdk.readthedocs.io/en/latest/IPs/SRAM/gf180mcu_fd_ip_sram/cells/gf180mcu_fd_ip_sram__sram128x8m8wm1/gf180mcu_fd_ip_sram__sram128x8m8wm1.html) | 432 x 269 um | 98k/mm² | 26% | 2 |

The macro density includes the peripheral circuits (address decoders, sense amplifiers, I/O drivers) around the bitcell array, which is why larger macros of a family are denser than smaller ones.

### Best Standard Cell Regions

| Design | Peak 1mm² Trans/mm² | % of flip-flop max | Library |
|---|---|---|---|
| [038](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/038.html) | 355k/mm² | 94% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [482](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/482.html) | 355k/mm² | 94% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [036](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/036.html) | 346k/mm² | 92% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [096](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/096.html) | 344k/mm² | 91% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [356](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/356.html) | 342k/mm² | 91% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [039](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/039.html) | 338k/mm² | 90% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [358](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/358.html) | 338k/mm² | 90% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [390](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/390.html) | 337k/mm² | 89% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

Infrastructure cells are excluded from logic cell counts but their transistors (decoupling capacitors in particular) are included in transistor counts.

## Process Features and Voltages

Which transistor voltages and optional devices of the GF180MCU process the 95 designs use. Voltages count both the libraries a design chose (standard cells and SRAM) and transistors the designer drew. Devices count only what the designer drew: standard cells, SRAM macros, I/O pads and fill are left out, because every die has them. A single test structure counts the same as a large block.

| Transistor voltage | Designs | Which |
|---|---|---|
| [3.3 V](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/spice/elec_specs/elec_specs_1.html) | 1 of 95 | [609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html) |
| [5 V](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/spice/elec_specs/elec_specs_3.html) | 95 of 95 | [000](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/000.html), [001](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/001.html), [003](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/003.html), [005](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/005.html), [007](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/007.html), [032](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/032.html), [034](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/034.html), [036](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/036.html), [038](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/038.html), [039](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/039.html), [065](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/065.html), [066](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/066.html), [067](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/067.html), [068](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/068.html), [069](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/069.html), [070](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/070.html), [071](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/071.html), [096](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/096.html), [098](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/098.html), [100](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/100.html), [102](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/102.html), [103](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/103.html), [128](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/128.html), [129](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/129.html), [130](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/130.html), [132](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/132.html), [134](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/134.html), [135](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/135.html), [192](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/192.html), [194](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/194.html), [195](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/195.html), [196](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/196.html), [198](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/198.html), [199](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/199.html), [295](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/295.html), [352](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/352.html), [353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html), [354](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/354.html), [355](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/355.html), [356](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/356.html), [357](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/357.html), [358](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/358.html), [359](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/359.html), [384](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/384.html), [385](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/385.html), [386](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/386.html), [387](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/387.html), [388](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/388.html), [389](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/389.html), [390](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/390.html), [391](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/391.html), [448](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/448.html), [449](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/449.html), [450](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/450.html), [451](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/451.html), [452](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/452.html), [453](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/453.html), [454](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/454.html), [455](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/455.html), [480](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/480.html), [481](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/481.html), [482](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/482.html), [483](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/483.html), [484](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/484.html), [485](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/485.html), [486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html), [487](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/487.html), [512](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/512.html), [513](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/513.html), [514](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/514.html), [515](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/515.html), [516](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/516.html), [517](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/517.html), [518](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/518.html), [519](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/519.html), [545](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/545.html), [547](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/547.html), [549](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/549.html), [551](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/551.html), [576](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/576.html), [577](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/577.html), [578](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/578.html), [579](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/579.html), [580](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/580.html), [581](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/581.html), [582](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/582.html), [583](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/583.html), [608](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/608.html), [609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html), [610](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/610.html), [611](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/611.html), [612](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/612.html), [613](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/613.html), [614](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/614.html), [615](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/615.html) |

| Device | Designs drawing it | Which |
|---|---|---|
| [High-resistance poly resistors](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_03.html) | 1 of 95 | [609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html) |
| [Native transistors](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_05.html) | 0 of 95 | — |
| [10 V LDMOS](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_12_1.html) | 0 of 95 | — |
| [MIM capacitors](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_4_2.html) | 0 of 95 | — |
| [MOS capacitors](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_6.html) | 0 of 95 | — |
| [Unsalicided poly resistors](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_01.html) | 0 of 95 | — |
| [Salicided poly resistors](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_4.html) | 0 of 95 | — |
| [Diffusion resistors](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_4.html) | 0 of 95 | — |
| [N-well resistors](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_4.html) | 0 of 95 | — |
| [Metal resistors](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_4.html) | 0 of 95 | — |
| [Diodes (DIODE_MK)](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_3.html) | 0 of 95 | — |
| [Well diodes](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_3.html) | 0 of 95 | — |
| [Deep N-well](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_07_03.html) | 0 of 95 | — |
| [Bipolar transistors](https://gf180mcu-pdk.readthedocs.io/en/latest/analog/model_parameters/LV/LV_5.html) | 0 of 95 | — |
| [Schottky diodes](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_14.html) | 0 of 95 | — |
| [Zener diodes](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html) | 0 of 95 | — |
| [eFuses](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_11.html) | 0 of 95 | — |
| [One-time programmable memory](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_10_10.html) | 0 of 95 | — |
| [Inductors](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html) | 0 of 95 | — |

| Design | Voltages | Custom transistors 3.3 / 5 / 6 V | Devices drawn | I/O library |
|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/000.html) | 5 V | 0 / 0 / 0 | — | — |
| [001](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/001.html) | 5 V | 0 / 0 / 0 | — | — |
| [003](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/003.html) | 5 V | 0 / 0 / 0 | — | — |
| [005](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/005.html) | 5 V | 0 / 0 / 0 | — | — |
| [007](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/007.html) | 5 V | 0 / 0 / 0 | — | — |
| [032](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/032.html) | 5 V | 0 / 0 / 0 | — | — |
| [034](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/034.html) | 5 V | 0 / 0 / 0 | — | — |
| [036](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/036.html) | 5 V | 0 / 0 / 0 | — | — |
| [038](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/038.html) | 5 V | 0 / 0 / 0 | — | — |
| [039](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/039.html) | 5 V | 0 / 0 / 0 | — | — |
| [065](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/065.html) | 5 V | 0 / 0 / 0 | — | — |
| [066](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/066.html) | 5 V | 0 / 0 / 0 | — | — |
| [067](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/067.html) | 5 V | 0 / 0 / 0 | — | — |
| [068](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/068.html) | 5 V | 0 / 0 / 0 | — | — |
| [069](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/069.html) | 5 V | 0 / 0 / 0 | — | — |
| [070](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/070.html) | 5 V | 0 / 0 / 0 | — | — |
| [071](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/071.html) | 5 V | 0 / 0 / 0 | — | — |
| [096](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/096.html) | 5 V | 0 / 0 / 0 | — | — |
| [098](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/098.html) | 5 V | 0 / 0 / 0 | — | — |
| [100](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/100.html) | 5 V | 0 / 0 / 0 | — | — |
| [102](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/102.html) | 5 V | 0 / 0 / 0 | — | — |
| [103](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/103.html) | 5 V | 0 / 0 / 0 | — | — |
| [128](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/128.html) | 5 V | 0 / 0 / 0 | — | — |
| [129](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/129.html) | 5 V | 0 / 0 / 0 | — | — |
| [130](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/130.html) | 5 V | 0 / 0 / 0 | — | — |
| [132](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/132.html) | 5 V | 0 / 0 / 0 | — | — |
| [134](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/134.html) | 5 V | 0 / 0 / 0 | — | — |
| [135](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/135.html) | 5 V | 0 / 0 / 0 | — | — |
| [192](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/192.html) | 5 V | 0 / 0 / 0 | — | — |
| [194](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/194.html) | 5 V | 0 / 0 / 0 | — | — |
| [195](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/195.html) | 5 V | 0 / 0 / 0 | — | — |
| [196](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/196.html) | 5 V | 0 / 0 / 0 | — | — |
| [198](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/198.html) | 5 V | 0 / 0 / 0 | — | — |
| [199](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/199.html) | 5 V | 0 / 0 / 0 | — | — |
| [295](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/295.html) | 5 V | 0 / 0 / 0 | — | — |
| [352](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/352.html) | 5 V | 0 / 0 / 0 | — | — |
| [353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html) | 5 V | 0 / 0 / 0 | — | — |
| [354](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/354.html) | 5 V | 0 / 0 / 0 | — | — |
| [355](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/355.html) | 5 V | 0 / 0 / 0 | — | — |
| [356](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/356.html) | 5 V | 0 / 0 / 0 | — | — |
| [357](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/357.html) | 5 V | 0 / 0 / 0 | — | — |
| [358](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/358.html) | 5 V | 0 / 0 / 0 | — | — |
| [359](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/359.html) | 5 V | 0 / 0 / 0 | — | — |
| [384](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/384.html) | 5 V | 0 / 0 / 0 | — | — |
| [385](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/385.html) | 5 V | 0 / 0 / 0 | — | — |
| [386](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/386.html) | 5 V | 0 / 0 / 0 | — | — |
| [387](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/387.html) | 5 V | 0 / 0 / 0 | — | — |
| [388](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/388.html) | 5 V | 0 / 0 / 0 | — | — |
| [389](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/389.html) | 5 V | 0 / 0 / 0 | — | — |
| [390](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/390.html) | 5 V | 0 / 0 / 0 | — | — |
| [391](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/391.html) | 5 V | 0 / 0 / 0 | — | — |
| [448](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/448.html) | 5 V | 0 / 0 / 0 | — | — |
| [449](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/449.html) | 5 V | 0 / 0 / 0 | — | — |
| [450](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/450.html) | 5 V | 0 / 0 / 0 | — | — |
| [451](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/451.html) | 5 V | 0 / 0 / 0 | — | — |
| [452](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/452.html) | 5 V | 0 / 0 / 0 | — | — |
| [453](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/453.html) | 5 V | 0 / 0 / 0 | — | — |
| [454](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/454.html) | 5 V | 0 / 0 / 0 | — | — |
| [455](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/455.html) | 5 V | 0 / 0 / 0 | — | — |
| [480](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/480.html) | 5 V | 0 / 0 / 0 | — | — |
| [481](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/481.html) | 5 V | 0 / 0 / 0 | — | — |
| [482](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/482.html) | 5 V | 0 / 0 / 0 | — | — |
| [483](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/483.html) | 5 V | 0 / 0 / 0 | — | — |
| [484](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/484.html) | 5 V | 0 / 0 / 0 | — | — |
| [485](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/485.html) | 5 V | 0 / 0 / 0 | — | — |
| [486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html) | 5 V | 0 / 0 / 0 | — | — |
| [487](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/487.html) | 5 V | 0 / 0 / 0 | — | — |
| [512](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/512.html) | 5 V | 0 / 0 / 0 | — | — |
| [513](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/513.html) | 5 V | 0 / 0 / 0 | — | — |
| [514](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/514.html) | 5 V | 0 / 0 / 0 | — | — |
| [515](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/515.html) | 5 V | 0 / 0 / 0 | — | — |
| [516](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/516.html) | 5 V | 0 / 0 / 0 | — | — |
| [517](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/517.html) | 5 V | 0 / 0 / 0 | — | — |
| [518](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/518.html) | 5 V | 0 / 0 / 0 | — | — |
| [519](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/519.html) | 5 V | 0 / 0 / 0 | — | — |
| [545](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/545.html) | 5 V | 0 / 0 / 0 | — | — |
| [547](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/547.html) | 5 V | 0 / 0 / 0 | — | — |
| [549](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/549.html) | 5 V | 0 / 0 / 0 | — | — |
| [551](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/551.html) | 5 V | 0 / 0 / 0 | — | — |
| [576](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/576.html) | 5 V | 0 / 0 / 0 | — | — |
| [577](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/577.html) | 5 V | 0 / 0 / 0 | — | — |
| [578](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/578.html) | 5 V | 0 / 0 / 0 | — | — |
| [579](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/579.html) | 5 V | 0 / 0 / 0 | — | — |
| [580](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/580.html) | 5 V | 0 / 0 / 0 | — | — |
| [581](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/581.html) | 5 V | 0 / 0 / 0 | — | — |
| [582](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/582.html) | 5 V | 0 / 0 / 0 | — | — |
| [583](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/583.html) | 5 V | 0 / 0 / 0 | — | — |
| [608](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/608.html) | 5 V | 0 / 0 / 0 | — | — |
| [609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html) | 3.3 V, 5 V | 51 / 0 / 0 | High-resistance poly resistors | — |
| [610](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/610.html) | 5 V | 0 / 0 / 0 | — | — |
| [611](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/611.html) | 5 V | 0 / 0 / 0 | — | — |
| [612](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/612.html) | 5 V | 0 / 0 / 0 | — | — |
| [613](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/613.html) | 5 V | 0 / 0 / 0 | — | — |
| [614](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/614.html) | 5 V | 0 / 0 / 0 | — | — |
| [615](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/615.html) | 5 V | 0 / 0 / 0 | — | — |

Detection uses the open GF180MCU layers: a transistor is gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) over diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), thick oxide inside Dualgate ([55/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), 5 V where V5_XTOR ([112/1](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) also covers it and 6 V where it does not; MIM capacitors are FuseTop ([75/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) shapes; poly resistors are Poly2 under RES_MK ([110/5](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), high resistance under the Resistor layer ([62/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and otherwise unsalicided under SAB ([49/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) or salicided. Other devices are found by their marker layers.

## Key Findings

1. The densest logic standard cell design, [353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html) (DOTTEE VGA demo (TTGF26a)), achieves **34k logic SC/mm²** averaged over its core (45% of buffer max), with a peak of **40k logic SC/mm²** in its densest 1mm² region.

2. Standard cell libraries in use: **[7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)** (100% of logic cells), **[9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html)** (<1% of logic cells).

3. The median digital design achieves **23k logic SC/mm²** over its core. 37 of 39 designs exceed 10k logic SC/mm².

4. The best standard cell region reaches **355k transistors/mm²** ([038](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/038.html)); the most used SRAM macro, [`gf180mcu_fd_ip_sram__sram128x8m8wm1`](https://gf180mcu-pdk.readthedocs.io/en/latest/IPs/SRAM/gf180mcu_fd_ip_sram/cells/gf180mcu_fd_ip_sram__sram128x8m8wm1/gf180mcu_fd_ip_sram__sram128x8m8wm1.html), is 98k transistors/mm².

5. Infrastructure cells (fillers, taps, antenna diodes, ties) outnumber logic cells **1.9 to 1** across the reticle (263k vs 138k). Any density analysis must exclude these to avoid dramatically overstating actual logic content.

6. The most common logic cell is **[`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html)** (15k instances in [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)).

## Per-Design Details

| Design | Cell | Die (mm) | Core mm² | Placements | Pads | Logic SC | Infra SC | Transistors | SRAM | Libraries |
|---|---|---|---|---|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/000.html) | `000_tt_um_chip_rom$1` | 0.35 x 0.16 | 0.1 | 1 | 0 | 233 | 1,650 | 11,868 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 233 |
| [001](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/001.html) | `001_tt_um_factory_test$1` | 0.35 x 0.16 | 0.1 | 1 | 0 | 108 | 1,248 | 11,846 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 108 |
| [003](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/003.html) | `003_tt_um_AlvaroRub_ringcounter` | 0.35 x 0.16 | 0.1 | 1 | 0 | 71 | 1,294 | 11,630 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 71 |
| [005](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/005.html) | `005_tt_um_peg_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,536 | 1,307 | 17,224 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,536 |
| [007](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/007.html) | `007_tt_um_systolic_mac_2x2` | 0.35 x 0.16 | 0.1 | 1 | 0 | 951 | 1,986 | 14,398 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 951 |
| [032](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/032.html) | `032_tt_um_rebeccargb_hardware_utf8` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,220 | 1,898 | 15,028 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,220 |
| [034](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/034.html) | `034_tt_um_systolic_array` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,611 | 3,599 | 34,068 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,611 |
| [036](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/036.html) | `036_tt_um_hydrocomms` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,243 | 3,188 | 35,104 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,243 |
| [038](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/038.html) | `038_tt_um_santhosh_rsd_char_gf` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,807 | 3,116 | 35,791 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,807 |
| [039](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/039.html) | `039_tt_um_prem_pipeline_test` | 1.44 x 0.74 | 1.1 | 1 | 0 | 23,196 | 35,492 | 318,349 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 23,196 |
| [065](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/065.html) | `065_tt_um_wokwi_465731440267947009` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,256 | 11,382 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [066](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/066.html) | `066_tt_um_wokwi_465731403724006401` | 0.35 x 0.16 | 0.1 | 1 | 0 | 21 | 1,261 | 11,398 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 21 |
| [067](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/067.html) | `067_tt_um_wokwi_465732706576877569` | 0.35 x 0.16 | 0.1 | 1 | 0 | 13 | 1,269 | 11,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 13 |
| [068](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/068.html) | `068_tt_um_line_follower_arvaloez` | 0.35 x 0.16 | 0.1 | 1 | 0 | 302 | 1,447 | 12,348 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 302 |
| [069](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/069.html) | `069_tt_um_wokwi_465731481873367041` | 0.35 x 0.16 | 0.1 | 1 | 0 | 880 | 1,802 | 14,792 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 880 |
| [070](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/070.html) | `070_tt_um_xoroshiro64plus_v2` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,174 | 1,875 | 14,176 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,174 |
| [071](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/071.html) | `071_tt_um_wokwi_465736612213902337` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,249 | 11,374 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [096](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/096.html) | `096_tt_um_waferspace_vga_screensaver$1` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,228 | 4,301 | 32,311 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,228 |
| [098](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/098.html) | `098_tt_um_happyhop_deadcast2` | 0.35 x 0.16 | 0.1 | 1 | 0 | 580 | 1,773 | 13,190 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 580 |
| [100](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/100.html) | `100_tt_um_dino7` | 0.35 x 0.16 | 0.1 | 1 | 0 | 983 | 2,086 | 14,220 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 983 |
| [102](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/102.html) | `102_tt_um_uacj` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,039 | 1,941 | 14,728 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,039 |
| [103](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/103.html) | `103_tt_um_kluterirv_rv32e_core` | 1.44 x 0.33 | 0.5 | 1 | 0 | 4,459 | 9,829 | 76,559 | 2 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4,459 |
| [128](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/128.html) | `128_tt_um_wokwi_465731521356457985` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,257 | 11,380 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [129](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/129.html) | `129_tt_um_machinelearning` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,389 | 4,050 | 33,388 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,389 |
| [130](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/130.html) | `130_tt_um_wokwi_465731520738845697` | 0.35 x 0.16 | 0.1 | 1 | 0 | 13 | 1,259 | 11,380 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 13 |
| [132](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/132.html) | `132_tt_um_wokwi_465731458628527105` | 0.35 x 0.16 | 0.1 | 1 | 0 | 12 | 1,260 | 11,374 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 12 |
| [134](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/134.html) | `134_tt_um_wokwi_465736691688630273` | 0.35 x 0.16 | 0.1 | 1 | 0 | 13 | 1,257 | 11,378 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 13 |
| [135](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/135.html) | `135_tt_um_divadnauj_GB_serv_soc_wb` | 1.08 x 0.33 | 0.4 | 1 | 0 | 9,987 | 9,349 | 112,309 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 9,987 |
| [192](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/192.html) | `192_tt_um_gen1_digital_companion_tile` | 0.35 x 0.16 | 0.1 | 1 | 0 | 224 | 1,332 | 12,180 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 224 |
| [194](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/194.html) | `194_tt_um_wokwi_465732827753495553` | 0.35 x 0.16 | 0.1 | 1 | 0 | 27 | 1,262 | 11,474 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 27 |
| [195](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/195.html) | `195_tt_um_pixel_processor` | 0.71 x 0.33 | 0.2 | 1 | 0 | 4,885 | 7,360 | 70,145 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4,885 |
| [196](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/196.html) | `196_tt_um_wokwi_465731394728267777` | 0.35 x 0.16 | 0.1 | 1 | 0 | 12 | 1,268 | 11,380 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 12 |
| [198](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/198.html) | `198_tt_um_wokwi_465731458535202817` | 0.35 x 0.16 | 0.1 | 1 | 0 | 18 | 1,262 | 11,384 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 18 |
| [199](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/199.html) | `199_tt_um_bioimpedance` | 0.71 x 0.33 | 0.2 | 1 | 0 | 2,825 | 6,993 | 60,553 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,825 |
| [295](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/295.html) | `295_tt_um_utoss_riscv` | 1.44 x 0.74 | 1.1 | 1 | 0 | 15,124 | 30,510 | 285,436 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 15,124 |
| [352](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/352.html) | `352_tt_um_gojimmypi_ttgf_UART_FSM_TRNG_Lab` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,272 | 3,069 | 35,378 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,272 |
| [353](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/353.html) | `353_tt_um_algofoogle_dottee` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,919 | 1,345 | 17,247 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,919 |
| [354](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/354.html) | `354_tt_um_8bit_risc_cpu` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,728 | 3,500 | 29,828 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,728 |
| [355](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/355.html) | `355_tt_um_urish_simon$1` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,301 | 1,358 | 13,356 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,301 |
| [356](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/356.html) | `356_tt_um_top` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,793 | 2,434 | 37,171 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,793 |
| [357](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/357.html) | `357_tt_um_wokwi_465483277165299713` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,251 | 11,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [358](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/358.html) | `358_tt_um_santhosh_stoch_stdp_pair_gf` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,435 | 3,670 | 34,534 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,435 |
| [359](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/359.html) | `359_tt_um_wokwi_467219410242853889` | 0.35 x 0.16 | 0.1 | 1 | 0 | 21 | 1,260 | 11,392 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 21 |
| [384](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/384.html) | `384_tt_um_joannec34_teenytpu` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,687 | 3,047 | 32,817 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,687 |
| [385](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/385.html) | `385_tt_um_wokwi_465736492859711489` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,251 | 11,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [386](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/386.html) | `386_tt_um_main` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,136 | 3,307 | 27,532 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,136 |
| [387](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/387.html) | `387_tt_um_wokwi_465732744934845441` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,269 | 11,392 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [388](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/388.html) | `388_tt_um_bgao43` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,529 | 3,351 | 29,952 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,529 |
| [389](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/389.html) | `389_tt_um_wokwi_465731371445677057` | 0.35 x 0.16 | 0.1 | 1 | 0 | 20 | 1,277 | 11,392 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 20 |
| [390](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/390.html) | `390_tt_um_jpigdon_gps_accelerator_top` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,457 | 2,818 | 35,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,457 |
| [391](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/391.html) | `391_tt_um_wokwi_465549494272929793` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,251 | 11,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [448](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/448.html) | `448_tt_um_apa102_ws2812_squidgeefish` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,899 | 3,793 | 29,567 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,899 |
| [449](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/449.html) | `449_tt_um_wokwi_465731430225727489` | 0.35 x 0.16 | 0.1 | 1 | 0 | 12 | 1,265 | 11,378 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 12 |
| [450](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/450.html) | `450_tt_um_arty3_mac_engine` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,601 | 3,930 | 33,555 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,601 |
| [451](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/451.html) | `451_tt_um_wokwi_465731458365332481` | 0.35 x 0.16 | 0.1 | 1 | 0 | 15 | 1,255 | 11,386 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 15 |
| [452](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/452.html) | `452_tt_um_mattvenn_signal_generator$1` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,704 | 3,420 | 31,174 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,704 |
| [453](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/453.html) | `453_tt_um_wokwi_465732744245929985` | 0.35 x 0.16 | 0.1 | 1 | 0 | 4 | 1,259 | 11,366 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4 |
| [454](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/454.html) | `454_tt_um_tpu` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,941 | 3,701 | 34,529 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,941 |
| [455](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/455.html) | `455_tt_um_wokwi_465731490568160257` | 0.35 x 0.16 | 0.1 | 1 | 0 | 20 | 1,266 | 11,390 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 20 |
| [480](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/480.html) | `480_tt_um_fhw_appel_spiPWMio` | 0.35 x 0.16 | 0.1 | 1 | 0 | 710 | 1,873 | 13,588 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 710 |
| [481](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/481.html) | `481_tt_um_wokwi_465732847401723905` | 0.35 x 0.16 | 0.1 | 1 | 0 | 14 | 1,266 | 11,378 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 14 |
| [482](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/482.html) | `482_tt_um_8bitcustomcomputer` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,214 | 1,320 | 17,672 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,214 |
| [483](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/483.html) | `483_tt_um_wokwi_465731452481768449` | 0.35 x 0.16 | 0.1 | 1 | 0 | 14 | 1,260 | 11,380 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 14 |
| [484](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/484.html) | `484_tt_um_mgj_bist8` | 0.35 x 0.16 | 0.1 | 1 | 0 | 325 | 1,430 | 12,510 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 325 |
| [485](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/485.html) | `485_tt_um_wokwi_465731502018614273` | 0.35 x 0.16 | 0.1 | 1 | 0 | 12 | 1,263 | 11,378 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 12 |
| [486](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/486.html) | `486_tt_um_roberto_tiny_radar_tile` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,822 | 1,112 | 17,364 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,822 |
| [487](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/487.html) | `487_tt_um_wokwi_465732616714924033` | 0.35 x 0.16 | 0.1 | 1 | 0 | 28 | 1,277 | 11,524 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 28 |
| [512](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/512.html) | `512_tt_um_wokwi_465731455677830145` | 0.35 x 0.16 | 0.1 | 1 | 0 | 38 | 1,263 | 11,518 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 38 |
| [513](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/513.html) | `513_tt_um_rgb_mixer` | 0.35 x 0.16 | 0.1 | 1 | 0 | 832 | 1,983 | 14,785 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 832 |
| [514](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/514.html) | `514_tt_um_wokwi_465731858252480513` | 0.35 x 0.16 | 0.1 | 1 | 0 | 13 | 1,265 | 11,384 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 13 |
| [515](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/515.html) | `515_tt_um_microlane_demo` | 0.35 x 0.16 | 0.1 | 1 | 0 | 365 | 1,935 | 11,616 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 365 |
| [516](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/516.html) | `516_tt_um_wokwi_465732880722332673` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,251 | 11,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [517](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/517.html) | `517_tt_um_danielpenas42` | 0.35 x 0.16 | 0.1 | 1 | 0 | 906 | 1,977 | 14,336 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 906 |
| [518](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/518.html) | `518_tt_um_wokwi_465731575275296769` | 0.35 x 0.16 | 0.1 | 1 | 0 | 168 | 1,388 | 11,892 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 168 |
| [519](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/519.html) | `519_tt_um_memory_game_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 787 | 1,724 | 15,098 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 787 |
| [545](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/545.html) | `545_tt_um_joseph_bf` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,521 | 1,458 | 17,097 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,521 |
| [547](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/547.html) | `547_tt_um_santhosh_xbar_ctrl_gf` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,228 | 1,720 | 16,551 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,228 |
| [549](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/549.html) | `549_tt_um_santhosh_ring_osc_gf` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,266 | 1,706 | 16,457 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,266 |
| [551](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/551.html) | `551_tt_um_ohuettenhofer_tiny_qsim` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,600 | 1,790 | 16,446 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,600 |
| [576](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/576.html) | `576_tt_um_wokwi_465737601403996161` | 0.35 x 0.16 | 0.1 | 1 | 0 | 618 | 1,835 | 12,914 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 618 |
| [577](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/577.html) | `577_tt_um_uacj_bouncing_DVD_screensaver` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,204 | 2,175 | 15,040 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,204 |
| [578](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/578.html) | `578_tt_um_ttmul` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,452 | 1,780 | 16,453 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,452 |
| [579](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/579.html) | `579_tt_um_logoUACJ_MOGA` | 0.35 x 0.16 | 0.1 | 1 | 0 | 868 | 1,950 | 14,196 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 868 |
| [580](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/580.html) | `580_tt_um_wokwi_465731466664816641` | 0.35 x 0.16 | 0.1 | 1 | 0 | 25 | 1,253 | 11,476 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 25 |
| [581](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/581.html) | `581_tt_um_grace_spi_led_driver` | 0.35 x 0.16 | 0.1 | 1 | 0 | 994 | 1,764 | 16,198 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 994 |
| [582](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/582.html) | `582_tt_um_wokwi_451184391728659457` | 0.35 x 0.16 | 0.1 | 1 | 0 | 11 | 1,272 | 11,370 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 11 |
| [583](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/583.html) | `583_tt_um_rebeccargb_universal_decoder` | 0.35 x 0.16 | 0.1 | 1 | 0 | 606 | 1,296 | 13,773 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 606 |
| [608](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/608.html) | `608_tt_um_wokwi_465731439156454401` | 0.35 x 0.16 | 0.1 | 1 | 0 | 7 | 1,252 | 11,366 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 7 |
| [609](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/609.html) | `609_tt_um_algofoogle_ttgf26a_vco` | 0.35 x 0.16 | 0.1 | 1 | 0 | 48 | 347 | 2,583 | 0 | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html): 48 |
| [610](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/610.html) | `610_tt_um_wokwi_465732536551273473` | 0.35 x 0.16 | 0.1 | 1 | 0 | 10 | 1,276 | 11,370 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 10 |
| [611](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/611.html) | `611_tt_um_fer_logo_music_vga` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,334 | 1,907 | 16,155 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,334 |
| [612](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/612.html) | `612_tt_um_wokwi_465737290543084545` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,257 | 11,380 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [613](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/613.html) | `613_tt_um_maqsudbek_dyadic_pwm` | 0.35 x 0.16 | 0.1 | 1 | 0 | 704 | 1,548 | 14,328 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 704 |
| [614](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/614.html) | `614_tt_um_wokwi_465630130495825921` | 0.35 x 0.16 | 0.1 | 1 | 0 | 22 | 1,277 | 11,476 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 22 |
| [615](https://wafer.space/tinytapeouts/ttgf26a/ws-run2-t26a/projects/615.html) | `615_tt_um_htfab_vga_tester` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,287 | 1,603 | 17,263 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,287 |

## Methodology

- **Logic cell counts** come from walking the layout hierarchy and counting instances of every cell whose name contains a standard cell library prefix, excluding types starting with `fill`, `endcap`, `filltie`, `fillcap`, `decap`, `tap`, `antenna`, `diode`, `tiel`, `tieh`.
- **Transistor counts** are the number of merged polygons in the boolean AND of the diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) layers, leaving out dummy fill cells, whose diffusion and polysilicon squares overlap without forming transistors.
- **Core area** is (die width − 0.70mm) x (die height − 0.70mm), removing a 350um pad ring from each side.
- **Cell dimensions** are the width and height of each standard cell's placement boundary ([GDS 0/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), measured from the cells present in this layout.
- **Theoretical maximum** = (1000um / cell width) x (1000um / row height).
- **Pads** are openings on the pad layer ([37/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) at least 20um across. Those in the pad ring (within 400um of the die edge) or in a second ring of pads inside it are bond pads; the others are probe pads, shown as "+ N probe". Letters and logos on the pad layer are not pads.
- **Peak figures** are the densest 100um x 100um square anywhere inside each die, found by sliding the square in 20um steps over the die and skipping positions that touch an SRAM macro. Logic cells are placed by their origin and transistors by the centre of their gate. They are given per mm².
- **SRAM macros** are counted by cell name. The `sram_block_count` column of the summary CSV is kept for comparison with earlier results; it counts SramCore marker shapes, of which each GF180MCU macro has two.
- Designs placed more than once on the reticle are counted once.

---

*Generated by [ws-run-reports](https://github.com/wafer-space/ws-run-reports) from `T26A.oas` (md5 `8fdfc77220918a548aa0b9707aa0e5ff`) in [wafer-space/tinytapeouts/ttgf26a/ws-run2-t26a](https://github.com/wafer-space/tinytapeouts/tree/main/ttgf26a/ws-run2-t26a). Analysis method: [KLayout](https://www.klayout.de/) boolean geometry operations on GDS layers. Grid resolution: 100um x 100um. Density figures are rounded to the nearest 1k.*
