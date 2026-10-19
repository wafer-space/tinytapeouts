# Bounding box (um, die coordinates) of each Tiny Tapeout project in a die cut from a ws-run reticle: the
# outermost placement of each macro listed in the release's shuttle_index.json.
#   kl tt_slots.py <die.oas> <shuttle_index.json> <out.json>
import json, re, sys
import klayout.db as db

die, index, out = sys.argv[1:4]
macros = {p["macro"] for p in json.load(open(index))["projects"]}
ly = db.Layout(); ly.read(die)
(top,) = ly.top_cells()
base = lambda name: re.sub(r"\$\d+$", "", name[name.index("tt_um_"):]) if "tt_um_" in name else None
targets = {c.cell_index(): base(c.name) for c in ly.each_cell() if base(c.name) in macros}
it = db.RecursiveInstanceIterator(ly, top)
it.targets = list(targets)
boxes = {}
while not it.at_end():
    m = targets[it.inst_cell().cell_index()]
    bb = ly.cell(it.inst_cell().cell_index()).dbbox().transformed(it.dtrans() * it.inst_dtrans())
    # keep only the outermost placement of a macro (nested copies sit inside it)
    if m not in boxes or not boxes[m].contains(bb.p1):
        assert m not in boxes, (m, boxes[m], bb)
        boxes[m] = bb
    it.next()
missing = macros - set(boxes)
assert not missing, missing
die_bb = top.dbbox()
json.dump({"die": [die_bb.left, die_bb.bottom, die_bb.right, die_bb.top],
           "slots": {m: [b.left, b.bottom, b.right, b.top] for m, b in sorted(boxes.items())}}, open(out, "w"), indent=1)
print(f"{len(boxes)} projects in {die_bb}")
