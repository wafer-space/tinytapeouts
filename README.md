# Tiny Tapeout on wafer.space

[Tiny Tapeout](https://tinytapeout.com/) GF180MCU chips, most of them made on [wafer.space](https://wafer.space/) shuttles. Each directory is one die, laid out like the wafer.space run repositories ([ws-run1](https://github.com/wafer-space/ws-run1), [ws-run2](https://github.com/wafer-space/ws-run2)): the layout as manufactured, an image of the die, a map of its slots and one row per Tiny Tapeout project.

| Chip | Name | Made on | Slot | Projects | Directory |
|---|---|---|---|---|---|
| ttgf0p1 | Tiny Tapeout GF 0.1 | A GlobalFoundries private MPW run | T0P1 | 24 | [ttgf0p1/gf-mpw-t0p1](ttgf0p1/gf-mpw-t0p1/) |
| [ttgf0p2](https://tinytapeout.com/chips/ttgf0p2) | Tiny Tapeout GF 0.2 | [wafer.space Run 1](https://github.com/wafer-space/ws-run1) (G801) | TTP2 | 52 | [ttgf0p2/ws-run1-ttp2](ttgf0p2/ws-run1-ttp2/) |
| [ttgf0p2](https://tinytapeout.com/chips/ttgf0p2) | Tiny Tapeout GF 0.2 | [wafer.space Run 1](https://github.com/wafer-space/ws-run1) (G801) | TTPG | 52 | [ttgf0p2/ws-run1-ttpg](ttgf0p2/ws-run1-ttpg/) |
| [ttgf0p3](https://tinytapeout.com/chips/ttgf0p3) | Tiny Tapeout GF 0p3 | [wafer.space Run 2](https://github.com/wafer-space/ws-run2) (G802) | T0P3 | 32 | [ttgf0p3/ws-run2-t0p3](ttgf0p3/ws-run2-t0p3/) |
| [ttgf26a](https://tinytapeout.com/chips/ttgf26a) | Tiny Tapeout GF 26a | [wafer.space Run 2](https://github.com/wafer-space/ws-run2) (G802) | T26A | 95 | [ttgf26a/ws-run2-t26a](ttgf26a/ws-run2-t26a/) |
| [ttgf26b](https://tinytapeout.com/chips/ttgf26b) | Tiny Tapeout GF 26b | [wafer.space Run 2](https://github.com/wafer-space/ws-run2) (G802) | T26B | 90 | [ttgf26b/ws-run2-t26b](ttgf26b/ws-run2-t26b/) |

The layer properties file for viewing the layouts in KLayout is `lyp/gf180mcu.lyp`.

Each directory is generated from public inputs by the scripts in [scripts/](scripts/); see [scripts/README.md](scripts/README.md).

# License

The projects shown here are public. For information on licences, please refer to the individual repositories.
