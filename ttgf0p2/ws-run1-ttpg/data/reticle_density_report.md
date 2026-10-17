# Tiny Tapeout GF 0.2 on wafer.space Run 1 — Standard Cell & SRAM Density Report

**GF180MCU Process (GlobalFoundries 180nm), Shuttle TTPG**

## Introduction

This report analyzes the standard cell and SRAM density achieved by the 52 unique public chip designs on the Tiny Tapeout GF 0.2 on wafer.space Run 1 reticle. The reticle has 52 slots; the public layout contains 52 slot placements (some designs appear more than once, and private designs are not included).

All designs were fabricated on GlobalFoundries' GF180MCU process, a 180-nanometer (0.18um) technology node. This is a mature, relatively large-geometry process — for comparison, modern smartphone chips use 3nm or 5nm processes with features roughly 50x smaller.

> **Note on counting methodology:** All standard cell counts in this report count only **logic cells** — cells that perform actual computation (gates, flip-flops, buffers, multiplexers, etc.). Infrastructure cells are excluded: filler cells (fill, fillcap, endcap, filltie), well taps, antenna fix diodes, ESD diodes, and tie-high/tie-low cells. These infrastructure cells are inserted by automated tools to satisfy manufacturing rules but perform no logic function. On this reticle there are 311k infrastructure cell instances and 197k logic cell instances across the unique designs — 1.6 infrastructure cells for every logic cell.

## What Are Standard Cells?

A "standard cell" is a pre-designed, pre-verified building block used to construct digital circuits. Think of them like LEGO bricks for chip design: each cell performs one simple logic function (an AND gate, a flip-flop for storing one bit, a buffer for boosting signal strength), and a chip designer assembles thousands or millions of them to build complex circuits.

Standard cells in a library all share the same height (so they line up in rows) but vary in width depending on their function. Automated tools place these cells in rows and then route wires between them.

The "density" of standard cells — how many fit per square millimeter — is a key measure of how efficiently a design uses its silicon area. Higher density generally means more logic functionality packed into less chip area, which reduces cost.

## Standard Cell Libraries on This Reticle

| Library | Row Height | Rows per mm | Relative Density | Logic instances | Share |
|---|---|---|---|---|---|
| [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3.92 um | 255 rows | 100% | 194k | 98% |
| [mcu9t5v0 (9-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | 5.04 um | 198 rows | 78% | 4k | 2% |

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
- **(b) Infrastructure cells** — fillers, taps, antenna diodes, and tie cells make up 61% of cell instances on this reticle
- **(c) Mixed cell types** — designs use a mix of small and large cells
- **(d) Power planning** — power/ground straps consume area
- **(e) Clock distribution** — clock tree buffers and wiring take space

## Achieved Standard Cell Density — Design Averages

The following tables show the average logic standard cell density for each design's "core area" — the interior of the chip excluding the I/O pad ring (a 350um border of large pads around the perimeter used for external connections).

"% of max" compares against the buffer theoretical maximum for the design's primary library. "Cell area" is the share of the core area actually covered by logic cells — the placement utilisation of the die as a whole, including any area left empty or given to SRAM.

### High Density (above 10k logic SC/mm² core average)

| Design | Library | Core SC/mm² | % of max | Cell area | Logic SC | SRAM | Project |
|---|---|---|---|---|---|---|---|
| [101](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/101.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 74% | 23k | 0 | [SCµM-BLE-RX](https://github.com/ZDYnb/ttgf-BLE_Receiver) |
| [519](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/519.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 27k | 35% | 70% | 2k | 0 | [Simon Says memory game](https://github.com/urish/tt-simon-game) |
| [547](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/547.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 35% | 69% | 1k | 0 | [WokwiPWM](https://github.com/kdp1965/ttgf-um-wokwi-pwm) |
| [130](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/130.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 34% | 78% | 3k | 0 | [USB CDC (Serial) Device](https://github.com/urish/tt-usbcdc-device) |
| [039](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/039.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 33% | 74% | 20k | 0 | [TinyQV Risc-V SoC](https://github.com/MichaelBell/ttgf0p2-tinyQV) |
| [579](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/579.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 33% | 69% | 1k | 0 | [PRISM 8 with TinySnake](https://github.com/kdp1965/ttgf-um-pettit-prism) |
| [391](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/391.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 32% | 62% | 9k | 0 | [megabytebeat](https://github.com/proppy/ttgf-bytebeat) |
| [513](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/513.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 32% | 69% | 1k | 0 | [Classic 8-bit era Programmable Sound Generator SN76489](https://github.com/rejunity/tt05-psg-sn76489) |
| [288](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/288.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 31% | 71% | 3k | 0 | [Notre Dame - Lockpick Game TT Example](https://github.com/mmorri22/lockpick) |
| [129](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/129.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 31% | 64% | 3k | 0 | [2x2 MAC Systolic array with DFT](https://github.com/Essenceia/Systolic_MAC_with_DFT) |
| [359](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/359.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 78% | 11k | 0 | [Simple RISC-V](https://github.com/urish/TTGF0p2) |
| [199](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/199.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 63% | 3k | 0 | [VGA Nyan Cat](https://github.com/a1k0n/ttgf0p2-a1k0n-nyan) |
| [032](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/032.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 69% | 1k | 0 | [Zedulo TestChip1](https://github.com/ZeduloTech/ttgf-zed_tc1) |
| [611](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/611.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 73% | 1k | 0 | [Video mode tester](https://github.com/htfab/ttgf0p2-vga-tester) |
| [545](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/545.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 61% | 1k | 0 | [Flame demo](https://github.com/kbeckmann/ttgf0p2-kbeckmann-flame) |
| [197](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/197.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 28% | 62% | 17k | 0 | [LISA 8-Bit Microcontroller](https://github.com/kdp1965/ttgf-um-lisa) |
| [103](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/103.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 28% | 62% | 2k | 0 | [Simon's Caterpillar](https://github.com/htfab/ttgf0p2-caterpillar) |
| [455](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/455.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 28% | 61% | 5k | 0 | [Zilog Z80](https://github.com/rejunity/z80-open-silicon) |
| [102](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/102.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 27% | 56% | 10k | 0 | [Silly-Faust](https://github.com/Bynaryman/ttgf0p2-faust-mlir-silicon) |
| [135](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/135.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 27% | 59% | 16k | 0 | [raybox-zero TTGF0p2 edition](https://github.com/algofoogle/ttgf0p2-raybox-zero) |
| [551](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/551.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 26% | 55% | 1k | 0 | [PVTMonitorSuite](https://github.com/zacky1972/ttgf0p2-PVTMonitorSuite) |
| [194](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/194.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 26% | 54% | 5k | 0 | [2048 sliding tile puzzle game (VGA)](https://github.com/urish/tt-2048-game) |
| [481](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/481.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 26% | 53% | 2k | 0 | [ROTFPGA v2](https://github.com/htfab/ttgf0p2-rotfpga) |
| [515](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/515.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 26% | 51% | 1k | 0 | [VGA Tiny Logo](https://github.com/rejunity/ttgf-vga-tiny-tapeout-animated-logo) |
| [033](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/033.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 2k | 0 | [Wafer.space Logo VGA Screensaver](https://github.com/TinyTapeout/tt-waferspace-vga-screensaver) |
| [295](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/295.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 58% | 20k | 0 | [KianV uLinux SoC](https://github.com/TinyTapeout/KianV-RV32IMA-RISC-V-uLinux-SoC) |
| [549](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/549.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 48% | 1k | 0 | [Dog Battle Game](https://github.com/jorgenkraghjakobsen/tt_gf_dog_fight) |
| [358](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/358.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 18k | 23% | 43% | 2k | 0 | [Notre Dame - CSE 30342 - DIC - Advanced FSM Final Project Example](https://github.com/mmorri22/tt_um_mmorri22_cse_30342) |
| [451](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/451.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 17k | 23% | 53% | 4k | 0 | [Asicle v2](https://github.com/htfab/ttgf0p2-asicle2) |
| [038](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/038.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 16k | 22% | 48% | 6k | 0 | [Wildcat RISC-V](https://github.com/schoeberl/ttgf-wildcat) |
| [198](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/198.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 16k | 22% | 61% | 2k | 0 | [easy PAL](https://github.com/kdp1965/ttgf-um-easy-PAL) |
| [134](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/134.html) | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) | 15k | 26% | 45% | 4k | 0 | [VGA Drop (audio/visual demo)](https://github.com/rejunity/tt08-vga-drop) |
| [196](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/196.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 20% | 52% | 2k | 0 | [Quickscope](https://github.com/TheZoq2/tt-um-thezoq2-quickscope) |
| [384](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/384.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 11k | 15% | 32% | 1k | 0 | [LEDs Racer](https://github.com/KerCrafter/FPGA-LEDs-Racer) |
| [454](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/454.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 11k | 14% | 36% | 1k | 0 | [CAN Controller for Rocket](https://github.com/noritsuna/ttgf0p2-tt_um_noritsuna_CAN_CTRL) |
| [385](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/385.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 10k | 13% | 27% | 1k | 0 | [Frequency Counter SSD1306 OLED](https://github.com/embelon/ttgf-frequency-counter-oled) |

### Minimal (analog, custom or test structures)

These designs contain fewer than 1,000 logic standard cells:

| Design | Logic SC | Transistors | SRAM | Pads | Project |
|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/000.html) | 236 | 12k | 0 | 0 | [Chip ROM](https://github.com/TinyTapeout/tt-chip-rom) |
| [001](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/001.html) | 90 | 12k | 0 | 0 | [Tiny Tapeout Factory Test](https://github.com/TinyTapeout/ttgf0p2-factory-test) |
| [128](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/128.html) | 860 | 15k | 0 | 0 | [VGA clock](https://github.com/mattvenn/GF180-VGA-clock-waferspace) |
| [483](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/483.html) | 746 | 14k | 0 | 0 | [7-Segment Digital Desk Clock](https://github.com/sellicott/digital_clock_gf0p2) |
| [485](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/485.html) | 726 | 15k | 0 | 0 | [MarcoPolo](https://github.com/javiBajoCero/ttgf-verilog-template) |
| [487](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/487.html) | 777 | 14k | 0 | 0 | [Linear Timecode (LTC) generator](https://github.com/flummer/tt-um-flummer-ltc) |
| [517](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/517.html) | 61 | 12k | 0 | 0 | [Ring Oscillator (5 inverter)](https://github.com/dlmiles/ttgf0p2-ringosc-5inv) |
| [577](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/577.html) | 82 | 12k | 0 | 0 | [PILIPINAS_IC](https://github.com/alexandercoabad/PILIPINAS_IC) |
| [581](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/581.html) | 897 | 15k | 0 | 0 | [Register bank accessible through SPI and I2C](https://github.com/calonso88/tt_spi_i2c_reg_bank) |
| [583](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/583.html) | 677 | 15k | 0 | 0 | [Cell mux](https://github.com/htfab/ttgf0p2-cells) |
| [609](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/609.html) | 761 | 15k | 0 | 0 | [Super-Simple-SPI-CPU](https://github.com/Sheffield-Chip-Design-Team/SPI-CPU-Final) |
| [610](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/610.html) | 62 | 12k | 0 | 0 | [Example of Bad Synchronizer](https://github.com/dlmiles/ttgf25a-bad-synchronizer) |
| [612](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/612.html) | 977 | 14k | 0 | 0 | [One Bit PUF](https://github.com/Capulus123/ttihp03-multi-bit-puf) |
| [613](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/613.html) | 90 | 12k | 0 | 0 | [DDR throughput and flop aperature test](https://github.com/dlmiles/ttgf25a-ddr-throughput-test) |
| [614](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/614.html) | 473 | 12k | 0 | 0 | [Ring osc on VGA](https://github.com/algofoogle/ttgf0p2-vga-ring-osc) |
| [615](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/615.html) | 81 | 12k | 0 | 0 | [GF180MCU loopback tile with input skew measurement](https://github.com/dlmiles/ttgf25a-loopback-with-skew) |

## Achieved Density — Peak 100um x 100um Regions

While the averages above include sparse regions, the densest 100um x 100um square found anywhere on a design shows the highest density it achieved. The square slides over the die in 20um steps and may not touch an SRAM macro.

| Design | Peak Logic SC/mm² | % of buffer max | Library |
|---|---|---|---|
| [391](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/391.html) | 42k | 55% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [101](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/101.html) | 39k | 52% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [519](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/519.html) | 38k | 50% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [194](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/194.html) | 38k | 50% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [039](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/039.html) | 37k | 49% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [102](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/102.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [513](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/513.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [129](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/129.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [358](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/358.html) | 35k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [135](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/135.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [199](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/199.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [515](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/515.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [130](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/130.html) | 34k | 45% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [038](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/038.html) | 34k | 45% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [451](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/451.html) | 34k | 45% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

The highest achieved density on this reticle is 55% of the buffer theoretical maximum, observed in the densest 100um square region of [391](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/391.html). The rest of that area is consumed by larger cells, infrastructure cells and the gaps left for routing.

## Library Comparison

Comparing designs that use one library exclusively:

| Metric | [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [mcu9t5v0 (9-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html) |
|---|---|---|
| Designs using this library | 51 | 1 |
| Best core density | 28k SC/mm² · 37% of max ([101](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/101.html)) | 15k SC/mm² · 26% of max ([134](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/134.html)) |
| Best peak grid cell | 42k SC/mm² · 55% of max ([391](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/391.html)) | 27k SC/mm² · 46% of max ([134](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/134.html)) |
| Median core density | 19k SC/mm² · 25% of max | 15k SC/mm² · 26% of max |

Differences between libraries here reflect which designs chose which library as much as the libraries themselves; the theoretical difference from row height alone is in the table above.

## Most Common Logic Cell Types

The 15 most-used logic cell types across all unique designs on the reticle:

| Cell Type | Library | Instances | What it does |
|---|---|---|---|
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 2-input NAND gate |
| [`oai21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai21/gf180mcu_fd_sc_mcu7t5v0__oai21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 14k | OR-AND-Invert compound gate |
| [`nor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nor2/gf180mcu_fd_sc_mcu7t5v0__nor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 13k | 2-input NOR gate |
| [`aoi21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi21/gf180mcu_fd_sc_mcu7t5v0__aoi21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 11k | AND-OR-Invert compound gate |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 10k | D flip-flop (1 bit storage) |
| [`xor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/xor2/gf180mcu_fd_sc_mcu7t5v0__xor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 8k | 2-input XOR gate |
| [`buf_4`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_4.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | Buffer (4x drive) |
| [`buf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | Buffer (2x drive) |
| [`dffq_4`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_4.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | D flip-flop (1 bit storage) (4x drive) |
| [`mux2_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/mux2/gf180mcu_fd_sc_mcu7t5v0__mux2_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 6k | 2-input multiplexer (2x drive) |
| [`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/inv/gf180mcu_fd_sc_mcu7t5v0__inv_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | Inverter |
| [`aoi22_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi22/gf180mcu_fd_sc_mcu7t5v0__aoi22_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | AND-OR-Invert (2x2 inputs) |
| [`clkinv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkinv/gf180mcu_fd_sc_mcu7t5v0__clkinv_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | Clock inverter |
| [`and2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/and2/gf180mcu_fd_sc_mcu7t5v0__and2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | 2-input AND gate |
| [`oai211_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai211/gf180mcu_fd_sc_mcu7t5v0__oai211_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | OR-AND-Invert compound gate |

Across the reticle there are 28k 2-input NAND gates and 24k flip-flops — 1.2 NAND2 gates per flip-flop.

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
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html) | 3.36 um | 76k | 4 | 304k/mm² |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | 16.24 um | 16k | 24 | 377k/mm² |

| Cell ([9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html)) | Width | Cells/mm² | Trans/cell | Trans/mm² theoretical max |
|---|---|---|---|---|
| [`inv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/inv/gf180mcu_fd_sc_mcu9t5v0__inv_1.html) | 2.24 um | 89k | 2 | 177k/mm² |
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/nand2/gf180mcu_fd_sc_mcu9t5v0__nand2_1.html) | 2.80 um | 71k | 4 | 283k/mm² |
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/buf/gf180mcu_fd_sc_mcu9t5v0__buf_1.html) | 3.36 um | 59k | 4 | 236k/mm² |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/cells/dffq/gf180mcu_fd_sc_mcu9t5v0__dffq_1.html) | 15.68 um | 13k | 24 | 304k/mm² |

### Best Standard Cell Regions

| Design | Peak 1mm² Trans/mm² | % of flip-flop max | Library |
|---|---|---|---|
| [130](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/130.html) | 354k/mm² | 94% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [103](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/103.html) | 354k/mm² | 94% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [583](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/583.html) | 353k/mm² | 94% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [199](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/199.html) | 352k/mm² | 94% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [032](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/032.html) | 352k/mm² | 93% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [513](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/513.html) | 349k/mm² | 93% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [391](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/391.html) | 348k/mm² | 92% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [359](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/359.html) | 346k/mm² | 92% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

Infrastructure cells are excluded from logic cell counts but their transistors (decoupling capacitors in particular) are included in transistor counts.

## Key Findings

1. The densest logic standard cell design, [101](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/101.html) (SCµM-BLE-RX), achieves **28k logic SC/mm²** averaged over its core (37% of buffer max), with a peak of **39k logic SC/mm²** in its densest 1mm² region.

2. Standard cell libraries in use: **[7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)** (98% of logic cells), **[9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html)** (2% of logic cells).

3. The median digital design achieves **21k logic SC/mm²** over its core. 36 of 36 designs exceed 10k logic SC/mm².

4. Infrastructure cells (fillers, taps, antenna diodes, ties) outnumber logic cells **1.6 to 1** across the reticle (311k vs 197k). Any density analysis must exclude these to avoid dramatically overstating actual logic content.

5. The most common logic cell is **[`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html)** (24k instances in [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)).

## Per-Design Details

| Design | Cell | Die (mm) | Core mm² | Placements | Pads | Logic SC | Infra SC | Transistors | SRAM | Libraries |
|---|---|---|---|---|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/000.html) | `000_tt_um_chip_rom` | 0.35 x 0.16 | 0.1 | 1 | 0 | 236 | 1,654 | 11,858 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 236 |
| [001](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/001.html) | `001_tt_um_factory_test` | 0.35 x 0.16 | 0.1 | 1 | 0 | 90 | 1,244 | 11,851 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 90 |
| [032](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/032.html) | `032_tt_um_zedtc1_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,242 | 1,219 | 16,817 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,242 |
| [033](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/033.html) | `033_tt_um_waferspace_vga_screensaver` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,228 | 4,301 | 32,311 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,228 |
| [038](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/038.html) | `038_tt_um_schoeberl_wildcat` | 1.08 x 0.33 | 0.4 | 1 | 0 | 5,867 | 11,364 | 98,496 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 5,867 |
| [039](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/039.html) | `039_tt_um_MichaelBell_tinyQV` | 1.08 x 0.74 | 0.8 | 1 | 0 | 20,084 | 25,932 | 254,546 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 20,084 |
| [101](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/101.html) | `101_tt_um_BLE_RX` | 1.08 x 0.74 | 0.8 | 1 | 0 | 22,709 | 26,034 | 245,576 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 22,709 |
| [102](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/102.html) | `102_tt_um_gf0p2_faust_top` | 1.44 x 0.33 | 0.5 | 1 | 0 | 9,814 | 13,494 | 135,918 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 9,814 |
| [103](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/103.html) | `103_tt_um_htfab_caterpillar` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,486 | 3,418 | 33,261 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,486 |
| [128](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/128.html) | `128_tt_um_vga_clock` | 0.35 x 0.16 | 0.1 | 1 | 0 | 860 | 1,742 | 14,565 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 860 |
| [129](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/129.html) | `129_tt_um_essen` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,711 | 3,477 | 33,358 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,711 |
| [130](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/130.html) | `130_tt_um_urish_usb_cdc` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,943 | 2,885 | 35,855 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,943 |
| [134](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/134.html) | `134_tt_um_rejunity_vga_test01` | 0.71 x 0.33 | 0.2 | 1 | 0 | 3,625 | 5,988 | 47,884 | 0 | [9t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu9t5v0/index.html): 3,625 |
| [135](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/135.html) | `135_tt_um_algofoogle_raybox_zero` | 1.08 x 0.74 | 0.8 | 1 | 0 | 16,500 | 29,025 | 234,151 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16,500 |
| [194](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/194.html) | `194_tt_um_2048_vga_game` | 0.71 x 0.33 | 0.2 | 1 | 0 | 4,680 | 6,375 | 66,457 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4,680 |
| [196](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/196.html) | `196_tt_um_thezoq2_quickscope` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,718 | 3,368 | 31,831 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,718 |
| [197](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/197.html) | `197_tt_um_lisa` | 1.08 x 0.74 | 0.8 | 1 | 0 | 17,231 | 30,872 | 238,706 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 17,231 |
| [198](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/198.html) | `198_tt_um_MATTHIAS_M_PAL_TOP_WRAPPER` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,890 | 2,935 | 33,566 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,890 |
| [199](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/199.html) | `199_tt_um_a1k0n_nyancat` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,662 | 3,786 | 33,356 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,662 |
| [288](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/288.html) | `288_tt_um_mmorri22_lockpick_game` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,722 | 3,510 | 34,534 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,722 |
| [295](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/295.html) | `295_tt_um_kianV_rv32ima_uLinux_SoC` | 1.44 x 0.74 | 1.1 | 1 | 0 | 20,266 | 42,242 | 315,831 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 20,266 |
| [358](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/358.html) | `358_tt_um_mmorri22_cse_30342` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,044 | 3,232 | 30,124 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,044 |
| [359](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/359.html) | `359_tt_um_simple_riscv` | 1.44 x 0.33 | 0.5 | 1 | 0 | 11,000 | 11,807 | 152,245 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 11,000 |
| [384](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/384.html) | `384_tt_um_kercrafter_leds_racer` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,315 | 3,292 | 28,288 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,315 |
| [385](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/385.html) | `385_tt_um_frequency_counter` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,157 | 3,114 | 27,576 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,157 |
| [391](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/391.html) | `391_tt_um_proppy_megabytebeat` | 1.08 x 0.33 | 0.4 | 1 | 0 | 8,785 | 8,464 | 104,977 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8,785 |
| [451](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/451.html) | `451_tt_um_htfab_asicle2` | 0.71 x 0.33 | 0.2 | 1 | 0 | 4,018 | 6,871 | 66,358 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4,018 |
| [454](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/454.html) | `454_tt_um_noritsuna_CAN_CTRL` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,218 | 3,515 | 29,075 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,218 |
| [455](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/455.html) | `455_tt_um_rejunity_z80` | 0.71 x 0.33 | 0.2 | 1 | 0 | 4,918 | 7,193 | 69,170 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4,918 |
| [481](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/481.html) | `481_tt_um_htfab_rotfpga2` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,269 | 3,893 | 31,514 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,269 |
| [483](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/483.html) | `483_tt_um_digital_clock_example` | 0.35 x 0.16 | 0.1 | 1 | 0 | 746 | 1,654 | 13,901 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 746 |
| [485](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/485.html) | `485_tt_um_javibajocero_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 726 | 1,727 | 14,620 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 726 |
| [487](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/487.html) | `487_tt_um_flummer_ltc` | 0.35 x 0.16 | 0.1 | 1 | 0 | 777 | 1,713 | 14,250 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 777 |
| [513](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/513.html) | `513_tt_um_rejunity_sn76489` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,380 | 1,010 | 14,397 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,380 |
| [515](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/515.html) | `515_tt_um_rejunity_vga_logo` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,095 | 1,765 | 15,005 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,095 |
| [517](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/517.html) | `517_tt_um_dlmiles_ringosc_5inv` | 0.35 x 0.16 | 0.1 | 1 | 0 | 61 | 1,250 | 11,604 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 61 |
| [519](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/519.html) | `519_tt_um_urish_simon` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,507 | 1,281 | 14,521 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,507 |
| [545](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/545.html) | `545_tt_um_kbeckmann_flame` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,230 | 1,770 | 15,681 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,230 |
| [547](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/547.html) | `547_tt_um_wokwi_445338187869298689` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,481 | 1,814 | 15,974 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,481 |
| [549](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/549.html) | `549_tt_um_SophusAndreassen_dogbattle` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,047 | 1,963 | 14,619 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,047 |
| [551](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/551.html) | `551_tt_um_zacky1972_PVTMonitorSuite` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,123 | 1,907 | 14,810 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,123 |
| [577](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/577.html) | `577_tt_um_wokwi_392873974467527681` | 0.35 x 0.16 | 0.1 | 1 | 0 | 82 | 1,309 | 11,535 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 82 |
| [579](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/579.html) | `579_tt_um_wokwi_442081253563458561` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,401 | 1,766 | 15,989 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,401 |
| [581](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/581.html) | `581_tt_um_calonso88_spi_i2c_reg_bank` | 0.35 x 0.16 | 0.1 | 1 | 0 | 897 | 1,750 | 15,079 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 897 |
| [583](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/583.html) | `583_tt_um_htfab_cells` | 0.35 x 0.16 | 0.1 | 1 | 0 | 677 | 1,386 | 15,037 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 677 |
| [609](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/609.html) | `609_tt_um_spi_cpu_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 761 | 1,535 | 14,616 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 761 |
| [610](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/610.html) | `610_tt_um_dlmiles_bad_synchronizer` | 0.35 x 0.16 | 0.1 | 1 | 0 | 62 | 1,268 | 11,676 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 62 |
| [611](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/611.html) | `611_tt_um_htfab_vga_tester` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,234 | 1,504 | 17,233 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,234 |
| [612](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/612.html) | `612_tt_um_multi_bit_puf_wrapper` | 0.35 x 0.16 | 0.1 | 1 | 0 | 977 | 1,914 | 14,020 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 977 |
| [613](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/613.html) | `613_tt_um_dlmiles_ddr_throughput_test` | 0.35 x 0.16 | 0.1 | 1 | 0 | 90 | 1,284 | 11,581 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 90 |
| [614](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/614.html) | `614_tt_um_algofoogle_vgaringosc` | 0.35 x 0.16 | 0.1 | 1 | 0 | 473 | 1,651 | 11,899 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 473 |
| [615](https://wafer.space/tinytapeouts/ttgf0p2/ws-run1-ttpg/projects/615.html) | `615_tt_um_dlmiles_loopback` | 0.35 x 0.16 | 0.1 | 1 | 0 | 81 | 1,246 | 11,839 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 81 |

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

*Generated by [ws-run-reports](https://github.com/wafer-space/ws-run-reports) from `TTPG.oas` (md5 `b6494ef5f5770752906c875739b2f09f`) in [wafer-space/tinytapeouts/ttgf0p2/ws-run1-ttpg](https://github.com/wafer-space/tinytapeouts/tree/main/ttgf0p2/ws-run1-ttpg). Analysis method: [KLayout](https://www.klayout.de/) boolean geometry operations on GDS layers. Grid resolution: 100um x 100um. Density figures are rounded to the nearest 1k.*
