# Write tinytapeouts/README.md: one row per Tiny Tapeout GF180MCU die here.
#   python3 gen_tt_index.py
import csv, glob, json, os

from dies import RUNS

T = os.environ.get("TT_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for d in sorted(glob.glob(f"{T}/tt*/*-*/data/shuttle_index.json")):
    die = os.path.dirname(os.path.dirname(d))
    ttid, slug = die.split("/")[-2:]
    run, code = slug.split("-")[0] + "-" + slug.split("-")[1], slug.split("-")[2].upper()
    name = json.load(open(d))["name"]
    # A die measured from its netlist (GF 0.1) lists its projects in projects.csv; the manifest holds its blocks.
    listed = f"{die}/data/projects.csv" if os.path.exists(f"{die}/data/projects.csv") else f"{die}/data/manifest.csv"
    n = sum(1 for r in csv.DictReader(open(listed)) if r["CODE"] != "shared")
    rows.append((ttid, run, code, name, n, f"{ttid}/{slug}"))
md = ["# Tiny Tapeout on wafer.space", "",
      "[Tiny Tapeout](https://tinytapeout.com/) GF180MCU chips, most of them made on [wafer.space](https://wafer.space/) shuttles. "
      "Each directory is one die, laid out like the wafer.space run repositories "
      "([ws-run1](https://github.com/wafer-space/ws-run1), [ws-run2](https://github.com/wafer-space/ws-run2)): "
      "the layout as manufactured, an image of the die, a map of its slots and one row per Tiny Tapeout project.", "",
      "| Chip | Name | Made on | Slot | Projects | Directory |", "|---|---|---|---|---|---|"]
for ttid, run, code, name, n, path in rows:
    rname, shuttle = RUNS[run]
    wafer_space = run.startswith("ws-")
    made = f"[wafer.space {rname}](https://github.com/wafer-space/{run}) ({shuttle})" if wafer_space else rname[0].upper() + rname[1:]
    chip = f"[{ttid}](https://tinytapeout.com/chips/{ttid})" if wafer_space else ttid
    md.append(f"| {chip} | {name} | {made} | {code} | {n} | [{path}]({path}/) |")
md += ["", "The layer properties file for viewing the layouts in KLayout is `lyp/gf180mcu.lyp`.", "",
       "Each directory is generated from public inputs by the scripts in [scripts/](scripts/); see [scripts/README.md](scripts/README.md).", "",
       "# License", "",
       "The projects shown here are public. For information on licences, please refer to the individual repositories.", ""]
open(f"{T}/README.md", "w").write("\n".join(md))
print(len(rows), "dies")
