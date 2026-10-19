# Write tinytapeouts/README.md: one row per Tiny Tapeout die on a wafer.space run.
#   python3 gen_tt_index.py
import csv, glob, json, os

from dies import RUNS

T = os.environ.get("TT_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for d in sorted(glob.glob(f"{T}/*/ws-run*-*/data/shuttle_index.json")):
    die = os.path.dirname(os.path.dirname(d))
    ttid, slug = die.split("/")[-2:]
    run, code = slug.split("-")[0] + "-" + slug.split("-")[1], slug.split("-")[2].upper()
    name = json.load(open(d))["name"]
    n = sum(1 for _ in csv.DictReader(open(f"{die}/data/manifest.csv")))
    rows.append((ttid, run, code, name, n, f"{ttid}/{slug}"))
md = ["# Tiny Tapeout on wafer.space", "",
      "[Tiny Tapeout](https://tinytapeout.com/) GF180MCU chips made on [wafer.space](https://wafer.space/) shuttles. "
      "Each directory is one die, laid out like the wafer.space run repositories "
      "([ws-run1](https://github.com/wafer-space/ws-run1), [ws-run2](https://github.com/wafer-space/ws-run2)): "
      "the layout as manufactured, an image of the die, a map of its project slots and one row per Tiny Tapeout project.", "",
      "| Chip | Name | wafer.space run | Slot | Projects | Directory |", "|---|---|---|---|---|---|"]
for ttid, run, code, name, n, path in rows:
    rname, shuttle = RUNS[run]
    md.append(f"| [{ttid}](https://tinytapeout.com/chips/{ttid}) | {name} | [{rname}](https://github.com/wafer-space/{run}) ({shuttle}) | {code} | {n} | [{path}]({path}/) |")
md += ["", "The layer properties file for viewing the layouts in KLayout is `lyp/gf180mcu.lyp`.", "",
       "Each directory is generated from public inputs by the scripts in [scripts/](scripts/); see [scripts/README.md](scripts/README.md).", "",
       "# License", "",
       "The projects shown here are public. For information on licences, please refer to the individual repositories.", ""]
open(f"{T}/README.md", "w").write("\n".join(md))
print(len(rows), "dies")
