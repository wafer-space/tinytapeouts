# Fill tinytapeouts/<ttid>/<run>-<code>/ for one Tiny Tapeout die on a wafer.space run: data/manifest.csv,
# data/shuttle_index.json, images/<CODE>.svg (project slot map), README.md and PROVENANCE.md.
# The layout parts and images/<CODE>.png are made separately (split, lay2img); build_tt.sh runs it all.
#   TT_GIT=<clone of the Tiny Tapeout shuttle repository> python3 gen_tt_repo.py <code> <slots.json> <shuttle_index.json>
import colorsys, csv, hashlib, json, os, re, subprocess, sys
import yaml

from dies import DIES

# The repository root, or TT_OUT to write the die somewhere else (to compare with the committed files).
ROOT = os.environ.get("TT_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS_RUN_REPORTS = os.environ.get("WS_RUN_REPORTS") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ws-run-reports")
code, slots_json, index_json = sys.argv[1:4]
d = DIES[code]
slug = f"{d['ttid']}/{d['run']}-{code.lower()}"
name = f"tinytapeouts/{slug}"
out = f"{ROOT}/{slug}"
mirror = os.environ["TT_GIT"]
index = json.load(open(index_json))
slots = json.load(open(slots_json))["slots"]

def git(*a):
    return subprocess.run(["git", "-C", mirror, *a], capture_output=True, text=True, check=True).stdout

# The project metadata comes from the commit the release was built from (shuttle_index.json). For the power-gated
# 0p2 build that is a commit on the powergate branch on top of the tag commit, with the same projects/.
tag_commit = git("rev-parse", f"{d['tag']}^{{commit}}").strip()
build_commit = index["commit"]
git("cat-file", "-e", f"{build_commit}^{{commit}}")
if build_commit != tag_commit:
    assert not git("diff", "--name-only", tag_commit, build_commit, "--", "projects"), "projects/ differ between tag and build commit"

def info(macro):
    try:
        y = yaml.safe_load(git("show", f"{build_commit}:projects/{macro}/info.yaml")).get("project", {})
    except subprocess.CalledProcessError:
        return {}
    return y

def https_url(u):
    """git@host:owner/repo(.git), http:// or a .git / trailing slash -> https://host/owner/repo"""
    u = (u or "").strip()
    m = re.match(r"^(?:ssh://)?git@([^:/]+)[:/](.+)$", u)
    if m:
        u = f"https://{m.group(1)}/{m.group(2)}"
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://www\.github\.com/", "https://github.com/", u)
    return re.sub(r"(\.git)?/*$", "", u)

def one_line(s):
    return " ".join(str(s or "").split())

rows = []
for p in sorted(index["projects"], key=lambda p: p["address"]):
    y = info(p["macro"])
    rows.append(dict(CODE=f"{p['address']:03d}", PROJECT=one_line(y.get("title")) or p["macro"], SLOT_SIZE=p["tiles"], VISIBILITY="Public",
                     PROJECT_DETAILS=one_line(y.get("description")), REPOSITORY=https_url(p.get("repo")), TOP=p["macro"],
                     MACRO_ADDRESS=p["address"], TILE_X=p["x"], TILE_Y=p["y"], AUTHOR=one_line(y.get("author")),
                     COMMIT=p.get("commit", ""), LANGUAGE=one_line(y.get("language")),
                     CLOCK_HZ="" if y.get("clock_hz") in (None, "") else y.get("clock_hz")))
assert {r["TOP"] for r in rows} == set(slots), set(slots) ^ {r["TOP"] for r in rows}

os.makedirs(f"{out}/data", exist_ok=True); os.makedirs(f"{out}/images", exist_ok=True)
fields = ["CODE", "PROJECT", "SLOT_SIZE", "VISIBILITY", "PROJECT_DETAILS", "REPOSITORY", "TOP",
          "MACRO_ADDRESS", "TILE_X", "TILE_Y", "AUTHOR", "COMMIT", "LANGUAGE", "CLOCK_HZ"]
with open(f"{out}/data/manifest.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n"); w.writeheader(); w.writerows(rows)
json.dump(index, open(f"{out}/data/shuttle_index.json", "w"), indent=1)

# Slot map in the style of the ws-run slot diagrams: die outline, one coloured box per project with its code.
W, H = 3.932, 5.122
def colour(s):
    h = int(hashlib.md5(s.encode()).hexdigest()[:4], 16) / 65535
    r, g, b = colorsys.hls_to_rgb(h, 0.45, 0.65)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
font = "font-family:'Adwaita Mono', 'Courier New', 'Lucida Console'"
svg = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
       f'<svg width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" version="1.1" xmlns="http://www.w3.org/2000/svg">', "  <g>",
       f'    <rect style="fill:#FFFFFF;fill-opacity:1" width="{W}" height="{H}" x="0" y="0" />',
       f'    <rect style="fill:#d8d8d8;fill-opacity:1;stroke:#808080;stroke-width:0.01" width="{W - 0.052}" height="{H - 0.052}" x="0.026" y="0.026" />']
for r in rows:
    x0, y0, x1, y1 = (v / 1000 for v in slots[r["TOP"]])
    x, y, w, h = round(x0, 4), round(H - y1, 4), round(x1 - x0, 4), round(y1 - y0, 4)
    size = round(min(0.09, w / 3.2, h / 1.4), 4)
    svg.append(f'    <rect style="fill:{colour(r["TOP"])};fill-opacity:1;stroke:#FFFFFF;stroke-width:0.004" width="{w}" height="{h}" x="{x}" y="{y}" />')
    # 1px text scaled down: some renderers clamp font sizes far below 1px
    svg.append(f'    <text xml:space="preserve" transform="translate({round(x + w / 2, 4)} {round(y + h / 2 + size / 3, 4)}) scale({size})" '
               f'style="font-size:1px;{font};text-anchor:middle;fill:#FFFFFF;fill-opacity:1" x="0" y="0">{r["CODE"]}</text>')
svg += ["  </g>", "</svg>", ""]
open(f"{out}/images/{code}.svg", "w").write("\n".join(svg))

nparts = len([f for f in os.listdir(f"{out}/layout") if f.startswith(f"{code}-part-")]) if os.path.isdir(f"{out}/layout") else 0
tt_chip = f"https://tinytapeout.com/chips/{d['ttid']}"
tt_repo = f"https://github.com/TinyTapeout/{d['repo']}"
md = [f"# {index['name']} on wafer.space {d['run_name']}", "",
      f"[Tiny Tapeout](https://tinytapeout.com/) chip [{d['ttid']}]({tt_chip}), slot {code} of the "
      f"[wafer.space GF180MCU {d['run_name']}](https://github.com/wafer-space/{d['run']}) reticle ({d['shuttle']})", "",
      f"- Chip ID: {d['ttid']}", f"- wafer.space run: {d['run']} ({d['shuttle']}), slot {code}", "- Process: GF180MCU",
      f"- Number of projects: {len(rows)}", "",
      '<div align="center">', '<table width="100%">', "  <tr>",
      f'  <td width="50%"><img src="images/{code}.png" width="95%"/></td>',
      f'  <td width="50%"><img src="images/{code}.svg" width="95%"/></td>', "  </tr>", "</table>", "</div>", "",
      f"This is one Tiny Tapeout die on a wafer.space shuttle; each project slot is a Tiny Tapeout project. "
      f"See [PROVENANCE.md](PROVENANCE.md) for where the layout and project information come from.", "",
      "# Projects", "", "| Code | Project | Tiles | Author | Project Details | Repository |", "|---|---|---|---|---|---|"]
for r in rows:
    link = f"[{r['PROJECT'].replace('|', '/')}]({tt_chip}/{r['TOP']})"
    md.append(f"| {r['CODE']} | {link} | {r['SLOT_SIZE']} | {r['AUTHOR'].replace('|', '/')} | {r['PROJECT_DETAILS'].replace('|', '/')} | {r['REPOSITORY']} |")
md += ["", "The code is the project's Tiny Tapeout multiplexer address.", "",
       "# View the Layout", "",
       "1. To view the layout, please install [KLayout](https://www.klayout.de/).",
       f"2. Next, assemble `{code}.oas` from the individual files: `cd layout; cat {code}-part-?? >{code}.oas`",
       f"3. The assembled `{code}.oas` file can then be opened with KLayout.",
       "4. Finally, load the layer properties file in KLayout: \"File → Load Layer Properties\" and choose `lyp/gf180mcu.lyp` at the top of this repository.", "",
       f"Note: The `{code}.oas` file was split with `split -b 90M {code}.oas {code}-part-`", "",
       "# License", "",
       "The projects shown here are public. For information on licences, please refer to the individual repositories.", ""]
open(f"{out}/README.md", "w").write("\n".join(md))

prov = [f"# Provenance of {name}", "",
        f"[{index['name']}]({tt_chip}) is a [Tiny Tapeout](https://tinytapeout.com/) chip: {len(rows)} projects, each in one or more tiles, "
        "behind a multiplexer that selects one project at a time, with the multiplexer, controller and pads around them. "
        f"It was made as slot {code} of the wafer.space GF180MCU {d['run_name']} shuttle ({d['shuttle']}, "
        f"[{d['run']}](https://github.com/wafer-space/{d['run']})){', ' + d['note'] if d['note'] else ''}.", "",
        "# How This Repository Was Generated", "",
        f"- `layout/` is the die exactly as it is on the {d['shuttle']} reticle: the `{code}_tt_gf_wrapper_<column>_<row>` cell cut from "
        f"the reticle in [{d['run']}](https://github.com/wafer-space/{d['run']}) with its seal ring and fill, moved to the origin. "
        f"Cell names keep the reticle's `$N` suffixes.",
        f"- It matches the precheck output of the Tiny Tapeout release [`{d['tag']}`]({tt_repo}/releases/tag/{d['tag']}) "
        "(`tt_gf_wrapper.oas.tt_gf_wrapper.precheck.*.output.*`) on every layer and in every project placement. The one difference is "
        "that on the reticle the dummy COMP layer (22/4) is merged into COMP (22/0); the shape counts match exactly.",
        f"- `data/shuttle_index.json` is the release's `shuttle_index.json` unchanged. It lists each project's multiplexer address, "
        "tile position and size, source repository and commit. In `data/manifest.csv` and the README the repository URLs are normalised to `https://` (no `git@` form, `.git` suffix or trailing slash).",
        f"- `data/tt_shuttle.json` gives the dates shown in the shuttle status: when submissions closed (`end_date` in the shuttle repository's `config.yaml`) "
        f"and when the release [`{d['tag']}`]({tt_repo}/releases/tag/{d['tag']}) was published. It is written by `ws-run-reports tt-manifest`.",
        f"- `data/manifest.csv` has one row per project: `CODE` is the multiplexer address, zero-padded to three digits, `TOP` the "
        "project's `tt_um_*` macro, `SLOT_SIZE` its size in tiles. It is written by `ws-run-reports tt-manifest` ([ws-run-reports](https://github.com/wafer-space/ws-run-reports)); `FLOW_VERSION` (LibreLane) and `PDK_VERSION` (open_pdks commit) come from each project's `pdk.json` and are empty where it does not record them. `LICENSE_FILE` and `DOCS_FILE` give the project's `LICENSE` and `docs/info.md` in the shuttle repository, and are empty where the project has none. Title, author, description, language and clock come from "
        f"`projects/<macro>/info.yaml` in [{d['repo']}]({tt_repo}/tree/{build_commit}) at `{build_commit[:10]}`, the commit the release was built from"
        + (f" (the release tag points at `{tag_commit[:10]}`; `{build_commit[:10]}` is the {d['note'].split(',')[0].replace('the ', '')} on top of it, with the same `projects/`)" if build_commit != tag_commit else "") + ".",
        f"- `images/{code}.svg` draws each project's outermost placement in the layout; `images/{code}.png` is rendered from the layout "
        "with `scripts/lay2img.py` and `reticle.lyp` from [reticle-stitcher](https://github.com/wafer-space/reticle-stitcher) "
        "(`--width 4096 --oversampling 4`), the same way as the ws-run images.",
        f"- Everything here was made by `scripts/build_tt.sh {code}` in this repository; see [scripts/README.md](../../scripts/README.md).", ""]
open(f"{out}/PROVENANCE.md", "w").write("\n".join(prov))
# The committed manifest is ws-run-reports' own (adds FLOW_VERSION / PDK_VERSION from pdk.json); ours must agree with it.
subprocess.run(["uv", "run", "ws-run-reports", "tt-manifest", "--index", os.path.abspath(index_json), "--tt-repo", mirror, "--release-tag", d["tag"], "--output", f"{out}/data/manifest.csv"],
               cwd=WS_RUN_REPORTS, check=True)
ours = {r["CODE"]: {k: str(v) for k, v in r.items()} for r in rows}
for r in csv.DictReader(open(f"{out}/data/manifest.csv")):
    assert {k: r[k] for k in fields} == ours[r["CODE"]], r["CODE"]
print(f"{name}: {len(rows)} projects, tag {d['tag']} = {tag_commit[:10]}, built from {build_commit[:10]}, {nparts} layout parts")
