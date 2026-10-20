# Fill tinytapeouts/<ttid>/<run>-<code>/ for a Tiny Tapeout die whose layout is a release asset (Tiny Tapeout
# GF 0.1, made on a GlobalFoundries private MPW run): data/manifest.csv (one row per block), data/projects.csv
# (one row per Tiny Tapeout project, measured from the shared block's netlist), data/shuttle_index.json,
# data/tt_shuttle.json, images/<CODE>.svg, README.md and PROVENANCE.md. build_release_die.sh runs it all.
#   TT_GIT=<clone of the shuttle repository> python3 gen_release_repo.py <code> <slots.json> <index.json> <cells_by_project.csv>
import collections, csv, colorsys, hashlib, json, os, re, shutil, subprocess, sys
import yaml

from dies import DIES

ROOT = os.environ.get("TT_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
code, slots_json, index_json, by_project_csv = sys.argv[1:5]
d = DIES[code]
slug = f"{d['ttid']}/{d['run']}-{code.lower()}"
name = f"tinytapeouts/{slug}"
out = f"{ROOT}/{slug}"
mirror = os.environ["TT_GIT"]
index = json.load(open(index_json))
die_box = json.load(open(slots_json))["die"]
slots = json.load(open(slots_json))["slots"]
tt_repo = f"https://github.com/TinyTapeout/{d['repo']}"
commit = subprocess.run(["git", "-C", mirror, "rev-parse", f"{d['tag']}^{{commit}}"], capture_output=True, text=True,
                        check=True).stdout.strip()

# The blocks, in the order of the pinout (docs/README.md in the shuttle repository).
CELL_TESTS = {
    0: ("GF 7-track 5 V cells", "the foundry's 7-track 5 V library (gf180mcu_fd_sc_mcu7t5v0)"),
    1: ("GF 9-track 5 V cells", "the foundry's 9-track 5 V library (gf180mcu_fd_sc_mcu9t5v0)"),
    2: ("GF 7-track cells as 3.3 V transistors", "the foundry's 7-track 5 V cells with the thick-oxide layers removed, so they are made as 3.3 V transistors"),
    3: ("GF 9-track cells as 3.3 V transistors", "the foundry's 9-track 5 V cells with the thick-oxide layers removed, so they are made as 3.3 V transistors"),
    4: ("OSU 9-track 3.3 V cells", "Oklahoma State University's 9-track 3.3 V library (gf180mcu_osu_sc_gp9t3v3), with its wells and implants redrawn"),
    5: ("OSU 12-track 3.3 V cells", "Oklahoma State University's 12-track 3.3 V library (gf180mcu_osu_sc_gp12t3v3), with its wells and implants redrawn"),
    6: ("AS 7-track 3.3 V cells", "Avalon Semiconductors' 7-track 3.3 V library (gf180mcu_as_sc_mcu7t3v3), with its implants redrawn"),
    7: ("AS 7-track 3.3 V cells, second copy", "Avalon Semiconductors' 7-track 3.3 V library, a second copy of CEL6"),
}
HEARTBEAT = ("A chain of 1,024 inverters delays a Manchester-coded counter, so the speed of the cells can be measured "
             "on the chip from its output pin; each pair of cell tests has a core supply of its own.")
blocks = [dict(CODE="MAIN", PROJECT=f"The {len(index['projects'])} Tiny Tapeout projects", TOP="tt_main_macro",
               PROJECT_DETAILS="Every project, synthesised and placed together as one block behind the multiplexer that "
                               "selects one project at a time")]
for i, (title, what) in CELL_TESTS.items():
    blocks.append(dict(CODE=f"CEL{i}", PROJECT=f"Cell test: {title}", TOP=f"tt_cell_macro_{i}",
                       PROJECT_DETAILS=f"Standard cell test in {what}. {HEARTBEAT}"))
blocks.append(dict(CODE="BUFR", PROJECT="Pad test buffer", TOP="tt_buffer_macro",
                   PROJECT_DETAILS="Connects four of the chip's pins straight to the controls of a test input/output "
                                   "pad, so the pad cell can be driven directly, and ties off the loopback pads"))
assert {b["TOP"] for b in blocks} == set(slots), set(slots) ^ {b["TOP"] for b in blocks}
fields = ["CODE", "PROJECT", "SLOT_SIZE", "VISIBILITY", "PROJECT_DETAILS", "REPOSITORY", "TOP"]
for b in blocks:
    x0, y0, x1, y1 = slots[b["TOP"]]
    b.update(SLOT_SIZE=f"{(x1 - x0) / 1000:g}x{(y1 - y0) / 1000:g}mm", VISIBILITY="Public",
             REPOSITORY=f"{tt_repo}/tree/{commit}/{'main' if b['CODE'] == 'MAIN' else 'buffer' if b['CODE'] == 'BUFR' else 'cells/cell' + b['CODE'][3]}")

def info(macro):
    try:
        text = subprocess.run(["git", "-C", mirror, "show", f"{commit}:main/src/projects/{macro}/info.yaml"],
                              capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return {}
    return yaml.safe_load(text).get("project", {})

def one_line(s):
    return " ".join(str(s or "").split())

def known(s):
    """The index writes N/A for a project with no repository (the pad test)."""
    return "" if str(s or "").strip().upper() == "N/A" else s

# The projects, measured from the shared block's netlist (netlist_projects.py).
FLOP = re.compile(r"^s?d(ff|f[a-z]*t)")  # as ws-run-reports stats.FLIP_FLOP_RE
logic, flops = collections.Counter(), collections.Counter()
for r in csv.DictReader(open(by_project_csv)):
    if r["is_fill"] == "False":
        logic[r["project"]] += int(r["instance_count"])
        flops[r["project"]] += int(r["instance_count"]) if FLOP.match(r["cell_type"]) else 0
total = sum(logic.values())
projects = []
for p in sorted(index["projects"], key=lambda p: p["address"]):
    y, key = info(p["macro"]), f"{p['address']:02d}"
    projects.append(dict(CODE=f"{p['address']:03d}", PROJECT=one_line(y.get("title")) or p["title"], TOP=p["macro"],
                         MACRO_ADDRESS=p["address"], AUTHOR=one_line(y.get("author")) or p.get("author", ""),
                         PROJECT_DETAILS=one_line(y.get("description")), REPOSITORY=known(p.get("repo")), COMMIT=known(p.get("commit")),
                         ORIGINAL_TILES=p.get("tiles", ""), LOGIC_CELLS=logic.get(key, ""), FLIP_FLOPS=flops.get(key, "")))
projects.append(dict(CODE="shared", PROJECT="Multiplexer and controller, with the combinational projects",
                     LOGIC_CELLS=logic["shared"], FLIP_FLOPS=flops["shared"]))
pfields = ["CODE", "PROJECT", "TOP", "MACRO_ADDRESS", "AUTHOR", "PROJECT_DETAILS", "REPOSITORY", "COMMIT",
           "ORIGINAL_TILES", "LOGIC_CELLS", "FLIP_FLOPS"]

os.makedirs(f"{out}/data", exist_ok=True); os.makedirs(f"{out}/images", exist_ok=True)
with open(f"{out}/data/manifest.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore"); w.writeheader(); w.writerows(blocks)
with open(f"{out}/data/projects.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=pfields, lineterminator="\n", extrasaction="ignore"); w.writeheader(); w.writerows(projects)
shutil.copy(by_project_csv, f"{out}/data/main_cells_by_project.csv")
json.dump(index, open(f"{out}/data/shuttle_index.json", "w"), indent=1)
release_url = f"{tt_repo}/releases/tag/{d['tag']}"
release_date = subprocess.run(["gh", "api", f"repos/TinyTapeout/{d['repo']}/releases/tags/{d['tag']}", "--jq", ".published_at"],
                              capture_output=True, text=True, check=True).stdout.strip()[:10]
json.dump({"commit": commit, "id": d["ttid"], "name": index["name"], "repo": tt_repo,
           "release": {"date": release_date, "tag": d["tag"], "url": release_url,
                       "description": f"Tiny Tapeout publishes the die's final layout ({d['tag']}) for {d['run_name']}"}},
          open(f"{out}/data/tt_shuttle.json", "w"), indent=1, sort_keys=True)

# Block map in the style of the ws-run slot diagrams.
W, H = die_box[2] / 1000, die_box[3] / 1000
def colour(s):
    h = int(hashlib.md5(s.encode()).hexdigest()[:4], 16) / 65535
    r, g, b = colorsys.hls_to_rgb(h, 0.45, 0.65)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
font = "font-family:'Adwaita Mono', 'Courier New', 'Lucida Console'"
svg = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
       f'<svg width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" version="1.1" xmlns="http://www.w3.org/2000/svg">', "  <g>",
       f'    <rect style="fill:#d8d8d8;fill-opacity:1;stroke:#808080;stroke-width:0.01" width="{W}" height="{H}" x="0" y="0" />']
for b in blocks:
    x0, y0, x1, y1 = (v / 1000 for v in slots[b["TOP"]])
    x, y, w, h = round(x0, 4), round(H - y1, 4), round(x1 - x0, 4), round(y1 - y0, 4)
    size = round(min(0.09, w / 3.2, h / 1.4), 4)
    svg.append(f'    <rect style="fill:{colour(b["TOP"])};fill-opacity:1;stroke:#FFFFFF;stroke-width:0.004" width="{w}" height="{h}" x="{x}" y="{y}" />')
    svg.append(f'    <text xml:space="preserve" transform="translate({round(x + w / 2, 4)} {round(y + h / 2 + size / 3, 4)}) scale({size})" '
               f'style="font-size:1px;{font};text-anchor:middle;fill:#FFFFFF;fill-opacity:1" x="0" y="0">{b["CODE"]}</text>')
svg += ["  </g>", "</svg>", ""]
open(f"{out}/images/{code}.svg", "w").write("\n".join(svg))

nparts = len([f for f in os.listdir(f"{out}/layout") if f.startswith(f"{code}-part-")]) if os.path.isdir(f"{out}/layout") else 0
md = [f"# {index['name']}", "",
      f"[Tiny Tapeout](https://tinytapeout.com/)'s first GF180MCU chip, made on {d['run_name']}: {len(index['projects'])} "
      f"projects in one shared block, beside eight standard cell tests. From [{d['repo']}]({tt_repo}) release "
      f"[`{d['tag']}`]({release_url}).", "",
      f"- Chip ID: {d['ttid']}", f"- Made on: {d['run_name']}", "- Process: GF180MCU",
      f"- Die: {W:g} x {H:g} mm", f"- Number of projects: {len(index['projects'])}", "",
      '<div align="center">', '<table width="100%">', "  <tr>",
      f'  <td width="50%"><img src="images/{code}.png" width="95%"/></td>',
      f'  <td width="50%"><img src="images/{code}.svg" width="95%"/></td>', "  </tr>", "</table>", "</div>", "",
      "Unlike the later Tiny Tapeout chips, the projects do not have tiles of their own: they were synthesised and placed "
      "together as one block (`MAIN`), so each project's size below is counted from that block's netlist. "
      "See [PROVENANCE.md](PROVENANCE.md) for where everything here comes from.", "",
      "# Blocks", "", "| Code | Block | Size | Details |", "|---|---|---|---|"]
for b in blocks:
    md.append(f"| {b['CODE']} | {b['PROJECT']} | {b['SLOT_SIZE'].replace('x', ' x ').replace('mm', ' mm')} | {b['PROJECT_DETAILS']} |")
md += ["", "# Projects", "", "| Address | Project | Author | Original tiles | Logic cells | Flip-flops | Repository |",
       "|---|---|---|---|---|---|---|"]
for p in projects:
    if p["CODE"] == "shared":
        md.append(f"| | {p['PROJECT']} | | | {p['LOGIC_CELLS']} | {p['FLIP_FLOPS']} | |")
    else:
        md.append(f"| {p['CODE']} | {p['PROJECT'].replace('|', '/')} | {p['AUTHOR'].replace('|', '/')} | {p['ORIGINAL_TILES']} | "
                  f"{p['LOGIC_CELLS']} | {p['FLIP_FLOPS']} | {p['REPOSITORY']} |")
md += ["", "Original tiles is each project's size on the Tiny Tapeout chip it came from. Logic cells and flip-flops are "
       "counted from the shared block's netlist; the purely combinational projects (Chip ROM and the MULDIV unit) keep no "
       "names in it, so they are counted with the multiplexer and controller.", "",
       "# View the Layout", "",
       "1. To view the layout, please install [KLayout](https://www.klayout.de/).",
       f"2. Next, assemble `{code}.oas` from the individual files: `cd layout; cat {code}-part-?? >{code}.oas`",
       f"3. The assembled `{code}.oas` file can then be opened with KLayout.",
       "4. Finally, load the layer properties file in KLayout: \"File → Load Layer Properties\" and choose `lyp/gf180mcu.lyp` at the top of this repository.", "",
       "# License", "",
       "The projects shown here are public. For information on licences, please refer to the individual repositories.", ""]
open(f"{out}/README.md", "w").write("\n".join(md))

prov = [f"# Provenance of {name}", "",
        f"[{index['name']}]({tt_repo}) is an experimental [Tiny Tapeout](https://tinytapeout.com/) chip made on "
        f"{d['run_name']}: {len(index['projects'])} projects from earlier Tiny Tapeout chips in one shared block behind a "
        "multiplexer, eight standard cell tests and a pad test.", "",
        "# How This Repository Was Generated", "",
        f"- `layout/` is the release asset `ttgf0p1_v23.fill.gds` of [`{d['tag']}`]({release_url}) (commit `{commit[:10]}`), "
        "the final layout with fill, written as OASIS. `scripts/xor_check.py` finds no difference between the two on any layer.",
        f"- Its blocks are the same as the block layouts published with the previous release, `v22` (`main.tar.xz`, "
        "`cells.tar.xz`, `buffer.tar.xz`): every layer's shape count matches, block by block. `data/main_cells_by_project.csv` "
        "is counted from `v22`'s `main/runs/test/final/pnl/tt_main_macro.pnl.v`, the powered netlist of the shared block, "
        "by `scripts/netlist_projects.py`: a cell belongs to the project its nets are named after (`mux_inst.p<NN>_I`), or "
        "to the one project of the cells it is connected to. Cells of the multiplexer and controller, and of the purely "
        "combinational projects, which keep no names, are `shared`.",
        f"- `data/manifest.csv` has one row per block, `SLOT_SIZE` its size in mm and `TOP` its cell; the cell tests are "
        f"described from `cells/` in the shuttle repository at `{commit[:10]}`. `data/projects.csv` has one row per project: "
        f"title, author and description from `main/src/projects/<macro>/info.yaml` at `{commit[:10]}`, address, repository, "
        "commit and original tile size from `data/shuttle_index.json`, which is Tiny Tapeout's project index for the chip "
        f"(<https://index.tinytapeout.com/{d['ttid']}.json>) unchanged.",
        f"- `data/tt_shuttle.json` gives the release date for the timeline: when [`{d['tag']}`]({release_url}) was published.",
        f"- `images/{code}.svg` draws each block; `images/{code}.png` is rendered from the layout with `scripts/lay2img.py` "
        "and `reticle.lyp` from [reticle-stitcher](https://github.com/wafer-space/reticle-stitcher) "
        "(`--width 4096 --oversampling 4`), the same way as the other dies.",
        f"- Everything here was made by `scripts/build_release_die.sh {code}` in this repository; see "
        "[scripts/README.md](../../scripts/README.md).", ""]
open(f"{out}/PROVENANCE.md", "w").write("\n".join(prov))
print(f"{name}: {len(blocks)} blocks, {len(projects) - 1} projects, {total} logic cells in MAIN, tag {d['tag']} = "
      f"{commit[:10]}, {nparts} layout parts")
