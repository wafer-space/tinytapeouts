# Tiny Tapeout GF 26b on wafer.space Run 2 — Standard Cell & SRAM Density Report

**GF180MCU Process (GlobalFoundries 180nm), Shuttle T26B**

## Introduction

This report analyzes the standard cell and SRAM density achieved by the 90 unique public chip designs on the Tiny Tapeout GF 26b on wafer.space Run 2 reticle. The reticle has 90 slots; the public layout contains 90 slot placements (some designs appear more than once, and private designs are not included).

All designs were fabricated on GlobalFoundries' GF180MCU process, a 180-nanometer (0.18um) technology node. This is a mature, relatively large-geometry process — for comparison, modern smartphone chips use 3nm or 5nm processes with features roughly 50x smaller.

> **Note on counting methodology:** All standard cell counts in this report count only **logic cells** — cells that perform actual computation (gates, flip-flops, buffers, multiplexers, etc.). Infrastructure cells are excluded: filler cells (fill, fillcap, endcap, filltie), well taps, antenna fix diodes, ESD diodes, and tie-high/tie-low cells. These infrastructure cells are inserted by automated tools to satisfy manufacturing rules but perform no logic function. On this reticle there are 273k infrastructure cell instances and 149k logic cell instances across the unique designs — 1.8 infrastructure cells for every logic cell.

## What Are Standard Cells?

A "standard cell" is a pre-designed, pre-verified building block used to construct digital circuits. Think of them like LEGO bricks for chip design: each cell performs one simple logic function (an AND gate, a flip-flop for storing one bit, a buffer for boosting signal strength), and a chip designer assembles thousands or millions of them to build complex circuits.

Standard cells in a library all share the same height (so they line up in rows) but vary in width depending on their function. Automated tools place these cells in rows and then route wires between them.

The "density" of standard cells — how many fit per square millimeter — is a key measure of how efficiently a design uses its silicon area. Higher density generally means more logic functionality packed into less chip area, which reduces cost.

## Standard Cell Libraries on This Reticle

| Library | Row Height | Rows per mm | Relative Density | Logic instances | Share |
|---|---|---|---|---|---|
| [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3.92 um | 255 rows | 100% | 147k | 98% |
| [as_sc_mcu7t3v3 (AS 7-track, 3.3V)](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 3.92 um | 255 rows | 100% | 2k | 2% |

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
- **(b) Infrastructure cells** — fillers, taps, antenna diodes, and tie cells make up 65% of cell instances on this reticle
- **(c) Mixed cell types** — designs use a mix of small and large cells
- **(d) Power planning** — power/ground straps consume area
- **(e) Clock distribution** — clock tree buffers and wiring take space

## Achieved Standard Cell Density — Design Averages

The following tables show the average logic standard cell density for each design's "core area" — the interior of the chip excluding the I/O pad ring (a 350um border of large pads around the perimeter used for external connections).

"% of max" compares against the buffer theoretical maximum for the design's primary library. "Cell area" is the share of the core area actually covered by logic cells — the placement utilisation of the die as a whole, including any area left empty or given to SRAM.

### High Density (above 10k logic SC/mm² core average)

| Design | Library | Core SC/mm² | % of max | Cell area | Logic SC | SRAM | Project |
|---|---|---|---|---|---|---|---|
| [067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 34k | 45% | 80% | 2k | 0 | [Car Trip](https://github.com/LukeSilva/tt-gf-car-trip) |
| [195](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/195.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 29k | 39% | 76% | 7k | 0 | [LEA-128](https://github.com/awayzer/ttgf-jct-LEA128) |
| [036](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/036.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 29k | 38% | 72% | 3k | 0 | [Neural Spike Detector](https://github.com/laylaadeli7/tt_neural_spike_detection) |
| [386](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/386.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 60% | 7k | 0 | [Elemental Harmony Game](https://github.com/Aakarshitha/Elemental_Harmony_GF26b) |
| [295](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/295.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 83% | 30k | 0 | [ASCON Integrated Crypto Processor](https://github.com/mealycpp/tt-ascon-full) |
| [551](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/551.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 28k | 37% | 76% | 2k | 0 | [BRISQ](https://github.com/pratyaygopal/BRISQ) |
| [356](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/356.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 27k | 36% | 79% | 3k | 0 | [Arctic0 16-bit CPU](https://github.com/PenguinEino/Arctic0) |
| [071](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/071.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 34% | 77% | 1k | 0 | [4-Neuron LIF Spiking Neural Network](https://github.com/ilim-stankulov/lif-spiking-neural-network) |
| [354](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/354.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 34% | 76% | 3k | 0 | [PWM-Analyser](https://github.com/PaulineKreis/TTGF26b_PWM-Analyser) |
| [390](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/390.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 26k | 34% | 65% | 6k | 0 | [Smerity-Mandelbrot](https://github.com/Smerity/tt_um_smerity_mandelbrot) |
| [612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html) | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) | 25k | 34% | 74% | 1k | 0 | [Detronyx Arithmetic Lab Tile](https://github.com/Zhekar1998/tt_um_arith_lab) |
| [033](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/033.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 25k | 33% | 70% | 3k | 0 | [60 Hz Grid-Forming ASIC with Dump-Load Control](https://github.com/ericpearson1313/tt_grid_tie_load) |
| [610](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/610.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 32% | 61% | 1k | 0 | [PDM Voice Activity Detector](https://github.com/antimatter15/ttgf26-vad) |
| [038](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/038.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 24k | 32% | 69% | 3k | 0 | [Lightscan](https://github.com/EmilioPeJu/ttgf-lightscan) |
| [613](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/613.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 31% | 64% | 1k | 0 | [Simon Says memory game](https://github.com/urish/tt-simon-game) |
| [358](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/358.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 31% | 63% | 3k | 0 | [Pong](https://github.com/ljhahne/ttgf-pong) |
| [101](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/101.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 23k | 30% | 63% | 8k | 0 | [AER Reflex Chip - MCP2515 CAN gateway](https://github.com/khu-haeun/aer_reflex) |
| [453](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/453.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 22k | 29% | 51% | 1k | 0 | [Hardware UTF Encoder/Decoder](https://github.com/RebeccaRGB/ttgf-hardware-utf8) |
| [288](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/288.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 21k | 27% | 63% | 2k | 0 | [100Mbps Ethernet Accelerator Wrapper](https://github.com/Essenceia/Teapot) |
| [581](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/581.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 27% | 53% | 1k | 0 | [Aswarby INT8 MAC](https://github.com/markd666/tt-aswarby-mac) |
| [103](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/103.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 20k | 27% | 53% | 2k | 0 | [Music for ASICs](https://github.com/d5smith/tt_um_d5smith_mfa) |
| [102](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/102.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 2k | 0 | [Wafer.space Logo VGA Screensaver](https://github.com/TinyTapeout/tt-waferspace-vga-screensaver) |
| [135](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/135.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 7k | 0 | [2048 sliding tile puzzle game (VGA)](https://github.com/urish/tt-2048-game) |
| [517](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/517.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 56% | 1k | 0 | [I2C Slave Template with Emulated Sensor](https://github.com/BastiBudde/TTSky26b_I2C-Slave-Sensor) |
| [454](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/454.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 25% | 53% | 4k | 0 | [Spiking Neural Network WTA Inference Engine (GF180)](https://github.com/ragansanthosh/tt_um_santhosh_snn_wta_gf_pub) |
| [547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 19k | 24% | 46% | 1k | 0 | [Tiny RIng Oscillator PUF](https://github.com/mRoales/Programmable_Ring_Oscillator_PUF) |
| [545](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/545.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 18k | 24% | 50% | 1k | 0 | [Quadrature sine generator](https://github.com/fran-retfie/GF26b-qsdss) |
| [100](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/100.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 17k | 22% | 55% | 2k | 0 | [Neuromorphic PUF (distinct-tap LFSR arbiter + memristor XOR, GF180)](https://github.com/santhoshs93/tt_um_santhosh_neuro_puf_gf_pub) |
| [034](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/034.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 16k | 22% | 45% | 2k | 0 | [Neuromorphic Spike Codec (GF180)](https://github.com/SanthoshSivasubramani/tt_um_santhosh_spike_codec_gf_pub) |
| [098](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/098.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 20% | 47% | 2k | 0 | [CIM Controller with BIST and Fault Map (GF180)](https://github.com/santhoshs93/tt_um_santhosh_cim_bist_gf_pub) |
| [450](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/450.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 20% | 48% | 4k | 0 | [Programmable Waveform and PWM Generator](https://github.com/silicon-nomad/tt-programmble-tiny-pattern-gen) |
| [039](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/039.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 15k | 19% | 38% | 12k | 0 | [ChaCha20](https://github.com/egurapha/ttgf-chacha20) |
| [199](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/199.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 14k | 19% | 52% | 3k | 0 | [100Mpbs 3 port Ethernet switch](https://github.com/Essenceia/ethernet_switch) |
| [096](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/096.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 14k | 18% | 49% | 2k | 0 | [Asynchronous-AER Spike Router (4-phase REQ/ACK, 16-entry routing tabl…](https://github.com/SanthoshSivasubramani/tt_um_santhosh_aer_router_gf_pub) |
| [352](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/352.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 14k | 18% | 37% | 2k | 0 | [Procedural ASIC](https://github.com/wiredlab/daehler-procedural_graphics_core) |
| [129](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/129.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 13k | 17% | 34% | 1k | 0 | [CWRU CHIPS Simple Counter with 7-segment Display](https://github.com/john-paul-sm/ASICWRU_SimpleCounter) |

### Minimal (analog, custom or test structures)

These designs contain fewer than 1,000 logic standard cells:

| Design | Logic SC | Transistors | SRAM | Pads | Project |
|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/000.html) | 226 | 12k | 0 | 0 | [Chip ROM](https://github.com/TinyTapeout/tt-chip-rom) |
| [001](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/001.html) | 108 | 12k | 0 | 0 | [Tiny Tapeout Factory Test](https://github.com/TinyTapeout/ttgf26a-factory-test) |
| [003](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/003.html) | 8 | 15k | custom | 0 | [TT-Arrakeen-SPSRAM-direct-sramrules](https://github.com/FibraServiTT/TTGF26b_Arrakeen_SPSRAM_direct_sramrules) |
| [005](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/005.html) | 710 | 14k | 0 | 0 | [spiPWMio](https://github.com/FHW-Appel/TTgf26a-spiPWMio) |
| [007](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/007.html) | 65 | 12k | 0 | 0 | [ECC Scalar Multiplication](https://github.com/CambridgeinstitutetechnologyBLR-Dhanush/ECC_Scalar_Multiplication) |
| [032](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/032.html) | 303 | 12k | 0 | 0 | [8-bit Interactive ALU](https://github.com/matanelk96/ASIC-ALU-MK) |
| [065](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/065.html) | 8 | 12k | 0 | 0 | [TT-Arrakeen-SPSRAM-direct-5V](https://github.com/FibraServiTT/TTGF26b_Arrakeen_SPSRAM_direct_5V) |
| [069](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/069.html) | 402 | 13k | 0 | 0 | [triad01](https://github.com/Alanduan21/ttgf-triad01) |
| [128](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/128.html) | 56 | 12k | 0 | 0 | [UART_SOC](https://github.com/sirijagadeesh4-hub/SIRI_UART_SOC) |
| [130](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/130.html) | 16 | 11k | 0 | 0 | [Raksha](https://github.com/shanthkumars165-commits/secure_packet_authentication) |
| [132](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/132.html) | 23 | 11k | 0 | 0 | [8-bit WNN Pattern Recognizer](https://github.com/cambridgeinstitutetechnology-blr-venkat/cit_project-2) |
| [134](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/134.html) | 16 | 11k | 0 | 0 | [Secure TRNG Entropy Generator](https://github.com/Cambridgeinstituteoftechnology-likitha/likii) |
| [192](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/192.html) | 26 | 11k | 0 | 0 | [ECDSA Verification](https://github.com/santoshism2006-pixel/vtox) |
| [194](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/194.html) | 183 | 12k | 0 | 0 | [ECC Processor](https://github.com/CambridgeinstitutetechnologyBLR-Dhanush/_ECC_Processor) |
| [196](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/196.html) | 252 | 12k | 0 | 0 | [Fast Authentication Accelerator](https://github.com/CambridgeinstitutetechnolgyBLR-Harshini/v2x_accelator) |
| [198](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/198.html) | 27 | 11k | 0 | 0 | [TRNG using Ring Oscillator](https://github.com/cambridgeinstituetechnologyBLR-karthikp/trng_) |
| [353](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/353.html) | 101 | 12k | 0 | 0 | [ttgf jct PoC](https://github.com/awayzer/ttgf-jct-PoC) |
| [355](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/355.html) | 434 | 13k | 0 | 0 | [CORDIC sin/cos generator](https://github.com/JacquesBTe/tt_um_jte_cordic) |
| [357](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/357.html) | 191 | 12k | 0 | 0 | [Three Channel RGB PWM Controller](https://github.com/aidenkoch4/ece430-tt-GF26A) |
| [359](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/359.html) | 356 | 13k | 0 | 0 | [Tremolo guitar pedal ASIC](https://github.com/Pschuetz112/tt-guitar-pedal-tremolo_final) |
| [385](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/385.html) | 118 | 12k | 0 | 0 | [PWM Generator](https://github.com/Omar90551/TTGF-PWM) |
| [387](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/387.html) | 108 | 12k | 0 | 0 | [WashingMachine_FSM](https://github.com/KimLuu02/TTGF26b_WashingMachine-FSM) |
| [389](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/389.html) | 296 | 12k | 0 | 0 | [Traffic Light FSM](https://github.com/Kieckenwama/TTGF26b_Traffic_Ligth_FSM) |
| [391](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/391.html) | 150 | 12k | 0 | 0 | [fibbonaci_tt](https://github.com/wiredlab/sabree-fibonacci_tt) |
| [449](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/449.html) | 159 | 12k | 0 | 0 | [Simple Sprinkler](https://github.com/noahzperez29/Noah_Binary_Hex_Decoder) |
| [451](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/451.html) | 606 | 14k | 0 | 0 | [Universal Binary to Segment Decoder](https://github.com/RebeccaRGB/ttgf-ubcd) |
| [455](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/455.html) | 128 | 12k | 0 | 0 | [SPI Master Slave Communication](https://github.com/nev-1910/SPI) |
| [480](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/480.html) | 57 | 12k | 0 | 0 | [Configurable 8-bit PWM Generator](https://github.com/Cambridge-CIT-ASIC-Tapeouts/PWM) |
| [481](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/481.html) | 31 | 12k | 0 | 0 | [Secure V2X Mini Demonstrator](https://github.com/push-777/Sanpush_ALU) |
| [482](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/482.html) | 9 | 11k | 0 | 0 | [Digital Door Lock](https://github.com/Rameshwar-12/Door_lock_system) |
| [483](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/483.html) | 62 | 12k | 0 | 0 | [AES S-Box Accelerator](https://github.com/cambridgeinstitutetechnologyblr-santosh/sanpush_aes) |
| [484](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/484.html) | 16 | 12k | 0 | 0 | [8-bit LFSR Circuit](https://github.com/CambridgeinstitutetechnologyBLR-satya/lfsrvenkys) |
| [485](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/485.html) | 450 | 13k | 0 | 0 | [Hardware Anomaly Detection](https://github.com/vinayakalk25/Hardware_abnormal_detection) |
| [486](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/486.html) | 115 | 12k | 0 | 0 | [V2X Collision Warning](https://github.com/Cambridge-CIT-ASIC-Tapeouts/V2X_Collision_Warning_system) |
| [487](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/487.html) | 110 | 12k | 0 | 0 | [Multi-Protocol Communication Controller](https://github.com/CambridgeinstituteoftechnologyBLR-chiru/Communication-protocol) |
| [512](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/512.html) | 467 | 14k | 0 | 0 | [SPI Slave with 8-Register File](https://github.com/Ushaop-op/ttgf-spi) |
| [513](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/513.html) | 115 | 12k | 0 | 0 | [Project](https://github.com/DRosen766/ttgf-26b) |
| [514](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/514.html) | 101 | 12k | 0 | 0 | [4 bit Accumulator CPU](https://github.com/Cambridge-CIT-ASIC-Tapeouts/ttgf-4b-accumulator-cpu) |
| [515](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/515.html) | 56 | 12k | 0 | 0 | [Simple SPI configuration for analog designs](https://github.com/agurlask/ttgf26b-spi-config-reg) |
| [516](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/516.html) | 82 | 12k | 0 | 0 | [Programmable Chaotic NLFSR](https://github.com/CambridgeinstitutetechnologyBLR-Aishu/CIT_Programmable-NLFSR) |
| [518](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/518.html) | 279 | 12k | 0 | 0 | [PQC NTT Butterfly Core](https://github.com/bojjireddyrishika12-web/butterfly) |
| [519](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/519.html) | 355 | 13k | 0 | 0 | [BSD Convolution Adder Tree](https://github.com/Vincent2405/BSD-Convolution-Adder-Tree-TinyTapeout) |
| [549](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/549.html) | 978 | 17k | 0 | 0 | [Detronyx UART Trace Exerciser](https://github.com/Zhekar1998/tt_um_detronyx_uart_trace_exerciser) |
| [576](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/576.html) | 21 | 11k | 0 | 0 | [4-bit Maximum-Length LFSR](https://github.com/Geeta-doddamani/ttgf-lfsr) |
| [577](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/577.html) | 843 | 14k | 0 | 0 | [SPI-CPU](https://github.com/cyrilprasannarajp/tt_MS_Engg_Clg_SPI) |
| [578](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/578.html) | 325 | 13k | 0 | 0 | [ECC Scalar Accelerator](https://github.com/pmlikhithkumar55-ship-it/CIT_AMG) |
| [579](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/579.html) | 46 | 12k | 0 | 0 | [I2C Master Controller](https://github.com/abhilash0419/tt_Akshaya_Ins_of_Tech_I2C) |
| [580](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/580.html) | 82 | 12k | 0 | 0 | [Configurable PWM Generator](https://github.com/ShivaranjaniGR/ePWM_Tapeout) |
| [582](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/582.html) | 57 | 11k | 0 | 0 | [8-bit Comparator](https://github.com/Cambridge-CIT-ASIC-Tapeouts/VLSI-project) |
| [583](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/583.html) | 8 | 15k | 0 | 0 | [TT-Arrakeen-SPSRAM-direct](https://github.com/FibraServiTT/TTGF26b_Arrakeen_SPSRAM_direct) |
| [608](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/608.html) | 538 | 13k | 0 | 0 | [7SegmentDice](https://github.com/elvtide01/7SegmentDice) |
| [609](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/609.html) | 837 | 14k | 0 | 0 | [XORing given bits](https://github.com/cherny1001/ttgf-26b) |
| [611](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/611.html) | 601 | 14k | 0 | 0 | [PolyTrig Digital Waveform Synthesis Core](https://github.com/SaeedSeyedfaraji/tt_um_polytrig_core_gf) |
| [614](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/614.html) | 583 | 13k | 0 | 0 | [Nearest Neighbor Interpolation](https://github.com/hasheddan/nni) |

## Achieved Density — Peak 100um x 100um Regions

While the averages above include sparse regions, the densest 100um x 100um square found anywhere on a design shows the highest density it achieved. The square slides over the die in 20um steps and may not touch an SRAM macro.

| Design | Peak Logic SC/mm² | % of buffer max | Library |
|---|---|---|---|
| [547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html) | 47k | 61% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [386](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/386.html) | 44k | 58% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [036](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/036.html) | 41k | 54% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html) | 40k | 52% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [195](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/195.html) | 38k | 50% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [613](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/613.html) | 37k | 49% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [453](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/453.html) | 36k | 48% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [295](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/295.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [356](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/356.html) | 36k | 47% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [039](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/039.html) | 35k | 46% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [451](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/451.html) | 33k | 44% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [354](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/354.html) | 33k | 43% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [551](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/551.html) | 33k | 43% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html) | 32k | 43% of 76k | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [390](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/390.html) | 32k | 42% of 76k | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

The highest achieved density on this reticle is 61% of the buffer theoretical maximum, observed in the densest 100um square region of [547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html). The rest of that area is consumed by larger cells, infrastructure cells and the gaps left for routing.

## Library Comparison

Comparing designs that use one library exclusively:

| Metric | [mcu7t5v0 (7-track, 5V)](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | [as_sc_mcu7t3v3 (AS 7-track, 3.3V)](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
|---|---|---|
| Designs using this library | 88 | 2 |
| Best core density | 34k SC/mm² · 45% of max ([067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html)) | 25k SC/mm² · 34% of max ([612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html)) |
| Best peak grid cell | 47k SC/mm² · 61% of max ([547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html)) | 32k SC/mm² · 43% of max ([612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html)) |
| Median core density | 8k SC/mm² · 10% of max | 21k SC/mm² · 28% of max |

Differences between libraries here reflect which designs chose which library as much as the libraries themselves; the theoretical difference from row height alone is in the table above.

## Most Common Logic Cell Types

The 15 most-used logic cell types across all unique designs on the reticle:

| Cell Type | Library | Instances | What it does |
|---|---|---|---|
| [`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 16k | 2-input NAND gate |
| [`oai21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/oai21/gf180mcu_fd_sc_mcu7t5v0__oai21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 10k | OR-AND-Invert compound gate |
| [`dffq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffq/gf180mcu_fd_sc_mcu7t5v0__dffq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 9k | D flip-flop (1 bit storage) |
| [`nor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nor2/gf180mcu_fd_sc_mcu7t5v0__nor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 9k | 2-input NOR gate |
| [`clkinv_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkinv/gf180mcu_fd_sc_mcu7t5v0__clkinv_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 9k | Clock inverter |
| [`dffrnq_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dffrnq/gf180mcu_fd_sc_mcu7t5v0__dffrnq_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 8k | D flip-flop with reset |
| [`dlyb_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/dlyb/gf180mcu_fd_sc_mcu7t5v0__dlyb_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 8k | Delay buffer |
| [`aoi21_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi21/gf180mcu_fd_sc_mcu7t5v0__aoi21_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 8k | AND-OR-Invert compound gate |
| [`aoi22_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/aoi22/gf180mcu_fd_sc_mcu7t5v0__aoi22_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | AND-OR-Invert (2x2 inputs) |
| [`clkbuf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkbuf/gf180mcu_fd_sc_mcu7t5v0__clkbuf_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | Clock buffer (2x drive) |
| [`buf_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 5k | Buffer (2x drive) |
| [`buf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/buf/gf180mcu_fd_sc_mcu7t5v0__buf_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | Buffer |
| [`xor2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/xor2/gf180mcu_fd_sc_mcu7t5v0__xor2_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 4k | 2-input XOR gate |
| [`mux2_2`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/mux2/gf180mcu_fd_sc_mcu7t5v0__mux2_2.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | 2-input multiplexer (2x drive) |
| [`clkbuf_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/clkbuf/gf180mcu_fd_sc_mcu7t5v0__clkbuf_1.html) | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) | 3k | Clock buffer |

Across the reticle there are 17k 2-input NAND gates and 19k flip-flops — 0.9 NAND2 gates per flip-flop.

## SRAM Block Usage

SRAM (Static Random-Access Memory) blocks are pre-designed memory macros. Unlike standard cells, which are composed by automated tools, SRAM blocks are hand-optimized fixed-size units designed to store data as densely as possible.

1 of the 90 designs include SRAM, holding 0 KiB of memory between them:

| Design | SRAM macros | SRAM bits | SRAM area | Logic SC | Project |
|---|---|---|---|---|---|
| [003](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/003.html) | custom | — | 0.01 mm² (12% of core) | 8 | [TT-Arrakeen-SPSRAM-direct-sramrules](https://github.com/FibraServiTT/TTGF26b_Arrakeen_SPSRAM_direct_sramrules) |

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

### Best Standard Cell Regions

| Design | Peak 1mm² Trans/mm² | % of flip-flop max | Library |
|---|---|---|---|
| [612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html) | 405k/mm² | 92% | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [135](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/135.html) | 348k/mm² | 79% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [096](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/096.html) | 344k/mm² | 78% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [102](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/102.html) | 344k/mm² | 78% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [100](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/100.html) | 344k/mm² | 78% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [295](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/295.html) | 344k/mm² | 78% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |
| [549](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/549.html) | 341k/mm² | 78% | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3) |
| [450](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/450.html) | 338k/mm² | 77% | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html) |

Infrastructure cells are excluded from logic cell counts but their transistors (decoupling capacitors in particular) are included in transistor counts.

## Process Features and Voltages

Which transistor voltages and optional devices of the GF180MCU process the 90 designs use. Voltages count both the libraries a design chose (standard cells and SRAM) and transistors the designer drew. Devices count only what the designer drew: standard cells, SRAM macros, I/O pads and fill are left out, because every die has them. A single test structure counts the same as a large block.

| Transistor voltage | Designs | Which |
|---|---|---|
| 3.3 V | 4 of 90 | [003](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/003.html), [549](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/549.html), [583](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/583.html), [612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html) |
| 5 V | 88 of 90 | [000](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/000.html), [001](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/001.html), [003](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/003.html), [005](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/005.html), [007](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/007.html), [032](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/032.html), [033](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/033.html), [034](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/034.html), [036](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/036.html), [038](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/038.html), [039](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/039.html), [065](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/065.html), [067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html), [069](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/069.html), [071](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/071.html), [096](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/096.html), [098](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/098.html), [100](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/100.html), [101](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/101.html), [102](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/102.html), [103](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/103.html), [128](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/128.html), [129](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/129.html), [130](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/130.html), [132](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/132.html), [134](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/134.html), [135](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/135.html), [192](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/192.html), [194](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/194.html), [195](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/195.html), [196](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/196.html), [198](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/198.html), [199](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/199.html), [288](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/288.html), [295](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/295.html), [352](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/352.html), [353](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/353.html), [354](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/354.html), [355](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/355.html), [356](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/356.html), [357](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/357.html), [358](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/358.html), [359](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/359.html), [385](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/385.html), [386](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/386.html), [387](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/387.html), [389](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/389.html), [390](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/390.html), [391](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/391.html), [449](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/449.html), [450](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/450.html), [451](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/451.html), [453](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/453.html), [454](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/454.html), [455](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/455.html), [480](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/480.html), [481](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/481.html), [482](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/482.html), [483](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/483.html), [484](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/484.html), [485](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/485.html), [486](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/486.html), [487](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/487.html), [512](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/512.html), [513](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/513.html), [514](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/514.html), [515](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/515.html), [516](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/516.html), [517](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/517.html), [518](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/518.html), [519](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/519.html), [545](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/545.html), [547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html), [551](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/551.html), [576](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/576.html), [577](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/577.html), [578](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/578.html), [579](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/579.html), [580](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/580.html), [581](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/581.html), [582](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/582.html), [583](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/583.html), [608](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/608.html), [609](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/609.html), [610](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/610.html), [611](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/611.html), [613](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/613.html), [614](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/614.html) |

| Device | Designs drawing it | Which |
|---|---|---|
| Native transistors | 0 of 90 | — |
| 10 V LDMOS | 0 of 90 | — |
| MIM capacitors | 0 of 90 | — |
| MOS capacitors | 0 of 90 | — |
| High-resistance poly resistors | 0 of 90 | — |
| Unsalicided poly resistors | 0 of 90 | — |
| Salicided poly resistors | 0 of 90 | — |
| Diffusion resistors | 0 of 90 | — |
| N-well resistors | 0 of 90 | — |
| Metal resistors | 0 of 90 | — |
| Diodes (DIODE_MK) | 0 of 90 | — |
| Well diodes | 0 of 90 | — |
| Deep N-well | 0 of 90 | — |
| Bipolar transistors | 0 of 90 | — |
| Schottky diodes | 0 of 90 | — |
| Zener diodes | 0 of 90 | — |
| eFuses | 0 of 90 | — |
| One-time programmable memory | 0 of 90 | — |
| Inductors | 0 of 90 | — |

| Design | Voltages | Custom transistors 3.3 / 5 / 6 V | Devices drawn | I/O library |
|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/000.html) | 5 V | 0 / 0 / 0 | — | — |
| [001](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/001.html) | 5 V | 0 / 0 / 0 | — | — |
| [003](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/003.html) | 3.3 V, 5 V | 7,382 / 0 / 0 | — | — |
| [005](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/005.html) | 5 V | 0 / 0 / 0 | — | — |
| [007](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/007.html) | 5 V | 0 / 0 / 0 | — | — |
| [032](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/032.html) | 5 V | 0 / 0 / 0 | — | — |
| [033](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/033.html) | 5 V | 0 / 0 / 0 | — | — |
| [034](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/034.html) | 5 V | 0 / 0 / 0 | — | — |
| [036](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/036.html) | 5 V | 0 / 0 / 0 | — | — |
| [038](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/038.html) | 5 V | 0 / 0 / 0 | — | — |
| [039](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/039.html) | 5 V | 0 / 0 / 0 | — | — |
| [065](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/065.html) | 5 V | 0 / 7,382 / 0 | — | — |
| [067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html) | 5 V | 0 / 0 / 0 | — | — |
| [069](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/069.html) | 5 V | 0 / 0 / 0 | — | — |
| [071](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/071.html) | 5 V | 0 / 0 / 0 | — | — |
| [096](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/096.html) | 5 V | 0 / 0 / 0 | — | — |
| [098](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/098.html) | 5 V | 0 / 0 / 0 | — | — |
| [100](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/100.html) | 5 V | 0 / 0 / 0 | — | — |
| [101](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/101.html) | 5 V | 0 / 0 / 0 | — | — |
| [102](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/102.html) | 5 V | 0 / 0 / 0 | — | — |
| [103](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/103.html) | 5 V | 0 / 0 / 0 | — | — |
| [128](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/128.html) | 5 V | 0 / 0 / 0 | — | — |
| [129](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/129.html) | 5 V | 0 / 0 / 0 | — | — |
| [130](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/130.html) | 5 V | 0 / 0 / 0 | — | — |
| [132](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/132.html) | 5 V | 0 / 0 / 0 | — | — |
| [134](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/134.html) | 5 V | 0 / 0 / 0 | — | — |
| [135](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/135.html) | 5 V | 0 / 0 / 0 | — | — |
| [192](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/192.html) | 5 V | 0 / 0 / 0 | — | — |
| [194](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/194.html) | 5 V | 0 / 0 / 0 | — | — |
| [195](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/195.html) | 5 V | 0 / 0 / 0 | — | — |
| [196](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/196.html) | 5 V | 0 / 0 / 0 | — | — |
| [198](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/198.html) | 5 V | 0 / 0 / 0 | — | — |
| [199](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/199.html) | 5 V | 0 / 0 / 0 | — | — |
| [288](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/288.html) | 5 V | 0 / 0 / 0 | — | — |
| [295](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/295.html) | 5 V | 0 / 0 / 0 | — | — |
| [352](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/352.html) | 5 V | 0 / 0 / 0 | — | — |
| [353](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/353.html) | 5 V | 0 / 0 / 0 | — | — |
| [354](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/354.html) | 5 V | 0 / 0 / 0 | — | — |
| [355](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/355.html) | 5 V | 0 / 0 / 0 | — | — |
| [356](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/356.html) | 5 V | 0 / 0 / 0 | — | — |
| [357](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/357.html) | 5 V | 0 / 0 / 0 | — | — |
| [358](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/358.html) | 5 V | 0 / 0 / 0 | — | — |
| [359](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/359.html) | 5 V | 0 / 0 / 0 | — | — |
| [385](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/385.html) | 5 V | 0 / 0 / 0 | — | — |
| [386](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/386.html) | 5 V | 0 / 0 / 0 | — | — |
| [387](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/387.html) | 5 V | 0 / 0 / 0 | — | — |
| [389](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/389.html) | 5 V | 0 / 0 / 0 | — | — |
| [390](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/390.html) | 5 V | 0 / 0 / 0 | — | — |
| [391](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/391.html) | 5 V | 0 / 0 / 0 | — | — |
| [449](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/449.html) | 5 V | 0 / 0 / 0 | — | — |
| [450](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/450.html) | 5 V | 0 / 0 / 0 | — | — |
| [451](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/451.html) | 5 V | 0 / 0 / 0 | — | — |
| [453](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/453.html) | 5 V | 0 / 0 / 0 | — | — |
| [454](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/454.html) | 5 V | 0 / 0 / 0 | — | — |
| [455](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/455.html) | 5 V | 0 / 0 / 0 | — | — |
| [480](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/480.html) | 5 V | 0 / 0 / 0 | — | — |
| [481](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/481.html) | 5 V | 0 / 0 / 0 | — | — |
| [482](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/482.html) | 5 V | 0 / 0 / 0 | — | — |
| [483](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/483.html) | 5 V | 0 / 0 / 0 | — | — |
| [484](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/484.html) | 5 V | 0 / 0 / 0 | — | — |
| [485](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/485.html) | 5 V | 0 / 0 / 0 | — | — |
| [486](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/486.html) | 5 V | 0 / 0 / 0 | — | — |
| [487](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/487.html) | 5 V | 0 / 0 / 0 | — | — |
| [512](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/512.html) | 5 V | 0 / 0 / 0 | — | — |
| [513](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/513.html) | 5 V | 0 / 0 / 0 | — | — |
| [514](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/514.html) | 5 V | 0 / 0 / 0 | — | — |
| [515](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/515.html) | 5 V | 0 / 0 / 0 | — | — |
| [516](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/516.html) | 5 V | 0 / 0 / 0 | — | — |
| [517](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/517.html) | 5 V | 0 / 0 / 0 | — | — |
| [518](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/518.html) | 5 V | 0 / 0 / 0 | — | — |
| [519](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/519.html) | 5 V | 0 / 0 / 0 | — | — |
| [545](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/545.html) | 5 V | 0 / 0 / 0 | — | — |
| [547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html) | 5 V | 0 / 0 / 0 | — | — |
| [549](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/549.html) | 3.3 V | 0 / 0 / 0 | — | — |
| [551](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/551.html) | 5 V | 0 / 0 / 0 | — | — |
| [576](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/576.html) | 5 V | 0 / 0 / 0 | — | — |
| [577](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/577.html) | 5 V | 0 / 0 / 0 | — | — |
| [578](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/578.html) | 5 V | 0 / 0 / 0 | — | — |
| [579](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/579.html) | 5 V | 0 / 0 / 0 | — | — |
| [580](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/580.html) | 5 V | 0 / 0 / 0 | — | — |
| [581](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/581.html) | 5 V | 0 / 0 / 0 | — | — |
| [582](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/582.html) | 5 V | 0 / 0 / 0 | — | — |
| [583](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/583.html) | 3.3 V, 5 V | 7,382 / 0 / 0 | — | — |
| [608](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/608.html) | 5 V | 0 / 0 / 0 | — | — |
| [609](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/609.html) | 5 V | 0 / 0 / 0 | — | — |
| [610](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/610.html) | 5 V | 0 / 0 / 0 | — | — |
| [611](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/611.html) | 5 V | 0 / 0 / 0 | — | — |
| [612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html) | 3.3 V | 0 / 0 / 0 | — | — |
| [613](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/613.html) | 5 V | 0 / 0 / 0 | — | — |
| [614](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/614.html) | 5 V | 0 / 0 / 0 | — | — |

Detection uses the open GF180MCU layers: a transistor is gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) over diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), thick oxide inside Dualgate ([55/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), 5 V where V5_XTOR ([112/1](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) also covers it and 6 V where it does not; MIM capacitors are FuseTop ([75/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) shapes; poly resistors are Poly2 under RES_MK ([110/5](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), high resistance under the Resistor layer ([62/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and otherwise unsalicided under SAB ([49/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) or salicided. Other devices are found by their marker layers.

## Key Findings

1. The densest logic standard cell design, [067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html) (Car Trip), achieves **34k logic SC/mm²** averaged over its core (45% of buffer max), with a peak of **40k logic SC/mm²** in its densest 1mm² region.

2. Standard cell libraries in use: **[7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)** (98% of logic cells), **[AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3)** (2% of logic cells).

3. The median digital design achieves **21k logic SC/mm²** over its core. 36 of 36 designs exceed 10k logic SC/mm².

4. Infrastructure cells (fillers, taps, antenna diodes, ties) outnumber logic cells **1.8 to 1** across the reticle (273k vs 149k). Any density analysis must exclude these to avoid dramatically overstating actual logic content.

5. The most common logic cell is **[`nand2_1`](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/nand2/gf180mcu_fd_sc_mcu7t5v0__nand2_1.html)** (16k instances in [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html)).

## Per-Design Details

| Design | Cell | Die (mm) | Core mm² | Placements | Pads | Logic SC | Infra SC | Transistors | SRAM | Libraries |
|---|---|---|---|---|---|---|---|---|---|---|
| [000](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/000.html) | `000_tt_um_chip_rom$2` | 0.35 x 0.16 | 0.1 | 1 | 0 | 226 | 1,655 | 11,854 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 226 |
| [001](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/001.html) | `001_tt_um_factory_test$2` | 0.35 x 0.16 | 0.1 | 1 | 0 | 108 | 1,248 | 11,846 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 108 |
| [003](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/003.html) | `003_tt_um_arrakeen_spsram_direct_sramrules` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,105 | 15,322 | custom | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [005](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/005.html) | `005_tt_um_fhw_appel_spiPWMio$1` | 0.35 x 0.16 | 0.1 | 1 | 0 | 710 | 1,873 | 13,588 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 710 |
| [007](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/007.html) | `007_tt_um_ecc_scalar_mult` | 0.35 x 0.16 | 0.1 | 1 | 0 | 65 | 1,274 | 11,676 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 65 |
| [032](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/032.html) | `032_tt_um_alu` | 0.35 x 0.16 | 0.1 | 1 | 0 | 303 | 1,446 | 12,306 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 303 |
| [033](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/033.html) | `033_tt_um_60hz_load` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,936 | 3,851 | 33,846 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,936 |
| [034](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/034.html) | `034_tt_um_santhosh_spike_codec_gf` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,899 | 3,902 | 30,047 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,899 |
| [036](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/036.html) | `036_tt_um_layla_spike_detector` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,296 | 2,998 | 34,110 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,296 |
| [038](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/038.html) | `038_tt_um_emiliopeju_lightscan` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,796 | 3,939 | 33,377 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,796 |
| [039](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/039.html) | `039_tt_um_egurapha_chacha20` | 1.08 x 0.74 | 0.8 | 1 | 0 | 11,717 | 25,725 | 209,343 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 11,717 |
| [065](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/065.html) | `065_tt_um_arrakeen_spsram_direct_5v` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 890 | 12,220 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [067](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/067.html) | `067_tt_um_LukeSilva_cartrip` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,901 | 1,406 | 17,082 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,901 |
| [069](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/069.html) | `069_tt_um_Alanduan21_triad01_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 402 | 1,518 | 12,911 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 402 |
| [071](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/071.html) | `071_tt_um_lif_snn` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,459 | 1,518 | 17,066 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,459 |
| [096](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/096.html) | `096_tt_um_santhosh_aer_router_gf` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,594 | 3,607 | 31,441 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,594 |
| [098](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/098.html) | `098_tt_um_santhosh_cim_bist_gf` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,759 | 3,674 | 30,834 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,759 |
| [100](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/100.html) | `100_tt_um_santhosh_neuro_puf_gf` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,971 | 4,013 | 31,721 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,971 |
| [101](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/101.html) | `101_tt_um_reflex_s4` | 1.08 x 0.33 | 0.4 | 1 | 0 | 8,164 | 12,481 | 101,576 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8,164 |
| [102](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/102.html) | `102_tt_um_waferspace_vga_screensaver$2` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,228 | 4,301 | 32,311 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,228 |
| [103](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/103.html) | `103_tt_um_d5smith_mfa` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,360 | 4,386 | 31,053 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,360 |
| [128](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/128.html) | `128_tt_um_uart_soc` | 0.35 x 0.16 | 0.1 | 1 | 0 | 56 | 1,298 | 11,692 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 56 |
| [129](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/129.html) | `129_tt_um_cwru_cpu` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,478 | 3,388 | 28,568 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,478 |
| [130](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/130.html) | `130_tt_um_raksha` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,272 | 11,392 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [132](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/132.html) | `132_tt_um_wnn` | 0.35 x 0.16 | 0.1 | 1 | 0 | 23 | 1,268 | 11,404 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 23 |
| [134](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/134.html) | `134_tt_um_likitha_trng` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,266 | 11,436 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [135](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/135.html) | `135_tt_um_2048_vga_game$1` | 1.08 x 0.33 | 0.4 | 1 | 0 | 6,736 | 11,639 | 100,459 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 6,736 |
| [192](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/192.html) | `192_tt_um_ecdsa_verify` | 0.35 x 0.16 | 0.1 | 1 | 0 | 26 | 1,259 | 11,430 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 26 |
| [194](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/194.html) | `194_tt_um_ecc_processor` | 0.35 x 0.16 | 0.1 | 1 | 0 | 183 | 1,381 | 11,984 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 183 |
| [195](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/195.html) | `195_tt_um_jct_lea` | 0.71 x 0.33 | 0.2 | 1 | 0 | 6,850 | 6,764 | 71,771 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 6,850 |
| [196](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/196.html) | `196_tt_um_fast_auth` | 0.35 x 0.16 | 0.1 | 1 | 0 | 252 | 1,407 | 12,382 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 252 |
| [198](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/198.html) | `198_tt_um_karthik_trng` | 0.35 x 0.16 | 0.1 | 1 | 0 | 27 | 1,282 | 11,494 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 27 |
| [199](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/199.html) | `199_tt_um_coffeepot` | 0.71 x 0.33 | 0.2 | 1 | 0 | 3,297 | 5,795 | 66,727 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,297 |
| [288](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/288.html) | `288_tt_um_teapot` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,406 | 4,078 | 33,045 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,406 |
| [295](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/295.html) | `295_tt_um_mealycpp_ascon_sdmc_uart` | 1.44 x 0.74 | 1.1 | 1 | 0 | 30,184 | 27,866 | 342,061 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 30,184 |
| [352](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/352.html) | `352_tt_um_connerdaehler_boop` | 0.35 x 0.33 | 0.1 | 1 | 0 | 1,581 | 3,375 | 29,222 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,581 |
| [353](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/353.html) | `353_tt_um_JCT_PoC` | 0.35 x 0.16 | 0.1 | 1 | 0 | 101 | 1,295 | 11,760 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 101 |
| [354](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/354.html) | `354_tt_um_PaulineKreis_PWM_Analyser` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,960 | 3,100 | 35,050 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,960 |
| [355](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/355.html) | `355_tt_um_jte_cordic` | 0.35 x 0.16 | 0.1 | 1 | 0 | 434 | 1,529 | 12,997 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 434 |
| [356](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/356.html) | `356_tt_um_Arctic0` | 0.35 x 0.33 | 0.1 | 1 | 0 | 3,152 | 2,900 | 35,504 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,152 |
| [357](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/357.html) | `357_tt_um_aidenkoch4` | 0.35 x 0.16 | 0.1 | 1 | 0 | 191 | 1,353 | 12,184 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 191 |
| [358](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/358.html) | `358_tt_um_ljhahne_pong` | 0.35 x 0.33 | 0.1 | 1 | 0 | 2,680 | 4,179 | 32,926 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 2,680 |
| [359](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/359.html) | `359_tt_um_pschuetz_tremolo` | 0.35 x 0.16 | 0.1 | 1 | 0 | 356 | 1,483 | 12,706 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 356 |
| [385](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/385.html) | `385_tt_um_PWM` | 0.35 x 0.16 | 0.1 | 1 | 0 | 118 | 1,338 | 11,766 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 118 |
| [386](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/386.html) | `386_tt_um_elemental_harmony` | 0.71 x 0.33 | 0.2 | 1 | 0 | 6,656 | 7,690 | 64,867 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 6,656 |
| [387](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/387.html) | `387_tt_um_KimLuu02_WashingMachine_FSM` | 0.35 x 0.16 | 0.1 | 1 | 0 | 108 | 1,350 | 11,720 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 108 |
| [389](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/389.html) | `389_tt_um_Kieckenwama_Traffic_LIGHT_FSM` | 0.35 x 0.16 | 0.1 | 1 | 0 | 296 | 1,549 | 12,364 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 296 |
| [390](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/390.html) | `390_tt_um_smerity_mandelbrot` | 0.71 x 0.33 | 0.2 | 1 | 0 | 5,977 | 10,322 | 64,502 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 5,977 |
| [391](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/391.html) | `391_tt_um_jsabree11_fibonacci_checker` | 0.35 x 0.16 | 0.1 | 1 | 0 | 150 | 1,350 | 11,856 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 150 |
| [449](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/449.html) | `449_tt_um_wokwi_466666882406199297` | 0.35 x 0.16 | 0.1 | 1 | 0 | 159 | 1,381 | 11,500 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 159 |
| [450](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/450.html) | `450_tt_um_pattern_gen` | 0.71 x 0.33 | 0.2 | 1 | 0 | 3,560 | 6,743 | 63,487 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 3,560 |
| [451](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/451.html) | `451_tt_um_rebeccargb_universal_decoder$1` | 0.35 x 0.16 | 0.1 | 1 | 0 | 606 | 1,296 | 13,773 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 606 |
| [453](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/453.html) | `453_tt_um_rebeccargb_hardware_utf8$1` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,220 | 1,898 | 15,028 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,220 |
| [454](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/454.html) | `454_tt_um_santhosh_snn_wta_gf` | 0.71 x 0.33 | 0.2 | 1 | 0 | 4,367 | 7,925 | 65,373 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 4,367 |
| [455](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/455.html) | `455_tt_um_spi_master` | 0.35 x 0.16 | 0.1 | 1 | 0 | 128 | 1,339 | 11,916 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 128 |
| [480](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/480.html) | `480_tt_um_pwm_cit` | 0.35 x 0.16 | 0.1 | 1 | 0 | 57 | 1,279 | 11,592 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 57 |
| [481](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/481.html) | `481_tt_um_push` | 0.35 x 0.16 | 0.1 | 1 | 0 | 31 | 1,271 | 11,572 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 31 |
| [482](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/482.html) | `482_tt_um_rameshwar_door_lock` | 0.35 x 0.16 | 0.1 | 1 | 0 | 9 | 1,266 | 11,372 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 9 |
| [483](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/483.html) | `483_tt_um_santosh_aes_sbox` | 0.35 x 0.16 | 0.1 | 1 | 0 | 62 | 1,298 | 11,669 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 62 |
| [484](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/484.html) | `484_tt_um_sandy_venky` | 0.35 x 0.16 | 0.1 | 1 | 0 | 16 | 1,264 | 11,512 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 16 |
| [485](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/485.html) | `485_tt_um_hardware_anomaly_detection` | 0.35 x 0.16 | 0.1 | 1 | 0 | 450 | 1,622 | 13,310 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 450 |
| [486](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/486.html) | `486_tt_um_v2x_warning` | 0.35 x 0.16 | 0.1 | 1 | 0 | 115 | 1,356 | 11,602 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 115 |
| [487](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/487.html) | `487_tt_um_multi_protocol` | 0.35 x 0.16 | 0.1 | 1 | 0 | 110 | 1,303 | 11,840 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 110 |
| [512](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/512.html) | `512_tt_um_spi_slave` | 0.35 x 0.16 | 0.1 | 1 | 0 | 467 | 1,534 | 13,770 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 467 |
| [513](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/513.html) | `513_tt_um_ex_drosen766` | 0.35 x 0.16 | 0.1 | 1 | 0 | 115 | 1,284 | 11,754 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 115 |
| [514](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/514.html) | `514_tt_um_4b_accumulator_cpu` | 0.35 x 0.16 | 0.1 | 1 | 0 | 101 | 1,292 | 11,856 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 101 |
| [515](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/515.html) | `515_tt_um_spi_config_reg` | 0.35 x 0.16 | 0.1 | 1 | 0 | 56 | 1,316 | 11,606 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 56 |
| [516](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/516.html) | `516_tt_um_cambridge_nlfsr` | 0.35 x 0.16 | 0.1 | 1 | 0 | 82 | 1,250 | 11,714 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 82 |
| [517](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/517.html) | `517_tt_um_BastiBudde_i2c_slave_sensor` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,051 | 2,102 | 15,280 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,051 |
| [518](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/518.html) | `518_tt_um_pqc_ntt_butterfly` | 0.35 x 0.16 | 0.1 | 1 | 0 | 279 | 1,380 | 12,309 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 279 |
| [519](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/519.html) | `519_tt_um_Vincent2405_adder_tree` | 0.35 x 0.16 | 0.1 | 1 | 0 | 355 | 1,530 | 12,648 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 355 |
| [545](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/545.html) | `545_tt_um_franretfie_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,017 | 2,023 | 14,740 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,017 |
| [547](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/547.html) | `547_tt_um_ro_puf` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,039 | 1,764 | 14,154 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,039 |
| [549](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/549.html) | `549_tt_um_detronyx_uart_trace_exerciser` | 0.35 x 0.16 | 0.1 | 1 | 0 | 978 | 2,246 | 17,028 | 0 | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3): 978 |
| [551](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/551.html) | `551_tt_um_brisq` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,555 | 1,499 | 17,287 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,555 |
| [576](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/576.html) | `576_tt_um_geeta_doddamani_lfsr` | 0.35 x 0.16 | 0.1 | 1 | 0 | 21 | 1,262 | 11,478 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 21 |
| [577](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/577.html) | `577_tt_um_spi_cpu_top` | 0.35 x 0.16 | 0.1 | 1 | 0 | 843 | 1,852 | 14,430 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 843 |
| [578](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/578.html) | `578_tt_um_ecc_accelerator` | 0.35 x 0.16 | 0.1 | 1 | 0 | 325 | 1,456 | 12,506 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 325 |
| [579](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/579.html) | `579_tt_um_i2c_master` | 0.35 x 0.16 | 0.1 | 1 | 0 | 46 | 1,285 | 11,540 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 46 |
| [580](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/580.html) | `580_tt_um_configurable_pwm` | 0.35 x 0.16 | 0.1 | 1 | 0 | 82 | 1,303 | 11,708 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 82 |
| [581](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/581.html) | `581_tt_um_aswarby_mac` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,146 | 2,060 | 14,944 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,146 |
| [582](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/582.html) | `582_tt_um_comp8` | 0.35 x 0.16 | 0.1 | 1 | 0 | 57 | 1,288 | 11,490 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 57 |
| [583](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/583.html) | `583_tt_um_arrakeen_spsram_direct` | 0.35 x 0.16 | 0.1 | 1 | 0 | 8 | 1,065 | 15,098 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 8 |
| [608](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/608.html) | `608_tt_um_elvtide01_7SegmentDice` | 0.35 x 0.16 | 0.1 | 1 | 0 | 538 | 1,753 | 13,026 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 538 |
| [609](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/609.html) | `609_tt_um_cherny_xor_8bi` | 0.35 x 0.16 | 0.1 | 1 | 0 | 837 | 1,762 | 14,085 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 837 |
| [610](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/610.html) | `610_tt_um_antimatter15_pdm_vad` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,357 | 2,154 | 15,352 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,357 |
| [611](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/611.html) | `611_tt_um_polytrig_core` | 0.35 x 0.16 | 0.1 | 1 | 0 | 601 | 1,252 | 14,067 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 601 |
| [612](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/612.html) | `612_tt_um_detronyx_arith_lab` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,427 | 1,785 | 20,890 | 0 | [AS 7t-3.3V](https://github.com/AvalonSemiconductors/gf180mcu_as_sc_mcu7t3v3): 1,427 |
| [613](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/613.html) | `613_tt_um_urish_simon$2` | 0.35 x 0.16 | 0.1 | 1 | 0 | 1,301 | 1,358 | 13,356 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 1,301 |
| [614](https://wafer.space/tinytapeouts/ttgf26b/ws-run2-t26b/projects/614.html) | `614_tt_um_hasheddan_nni` | 0.35 x 0.16 | 0.1 | 1 | 0 | 583 | 1,788 | 13,298 | 0 | [7t-5V](https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/index.html): 583 |

## Methodology

- **Logic cell counts** come from walking the layout hierarchy and counting instances of every cell whose name contains a standard cell library prefix, excluding types starting with `fill`, `endcap`, `filltie`, `fillcap`, `tap`, `antenna`, `diode`, `tiel`, `tieh`.
- **Transistor counts** are the number of merged polygons in the boolean AND of the diffusion ([22/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) and gate polysilicon ([30/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) layers, leaving out dummy fill cells, whose diffusion and polysilicon squares overlap without forming transistors.
- **Core area** is (die width − 0.70mm) x (die height − 0.70mm), removing a 350um pad ring from each side.
- **Cell dimensions** are the width and height of each standard cell's placement boundary ([GDS 0/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)), measured from the cells present in this layout.
- **Theoretical maximum** = (1000um / cell width) x (1000um / row height).
- **Pads** are openings on the pad layer ([37/0](https://gf180mcu-pdk.readthedocs.io/en/latest/physical_verification/design_manual/drm_04_1.html#drawn-layer-definition-and-abbreviation)) at least 20um across. Those in the pad ring (within 400um of the die edge) or in a second ring of pads inside it are bond pads; the others are probe pads, shown as "+ N probe". Letters and logos on the pad layer are not pads.
- **Peak figures** are the densest 100um x 100um square anywhere inside each die, found by sliding the square in 20um steps over the die and skipping positions that touch an SRAM macro. Logic cells are placed by their origin and transistors by the centre of their gate. They are given per mm².
- **SRAM macros** are counted by cell name. The `sram_block_count` column of the summary CSV is kept for comparison with earlier results; it counts SramCore marker shapes, of which each GF180MCU macro has two.
- Designs placed more than once on the reticle are counted once.

---

*Generated by [ws-run-reports](https://github.com/wafer-space/ws-run-reports) from `T26B.oas` (md5 `a905e364075a3362a8629aee939dd5e6`) in [wafer-space/tinytapeouts/ttgf26b/ws-run2-t26b](https://github.com/wafer-space/tinytapeouts/tree/main/ttgf26b/ws-run2-t26b). Analysis method: [KLayout](https://www.klayout.de/) boolean geometry operations on GDS layers. Grid resolution: 100um x 100um. Density figures are rounded to the nearest 1k.*
