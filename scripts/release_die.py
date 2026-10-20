# A Tiny Tapeout die whose layout is a release asset rather than a cut from a wafer.space reticle (Tiny Tapeout
# GF 0.1): write it as OASIS, and the bounding box (um) of each block placed in its top cell, the slots of its
# pages. Blocks are the digital macros: the shared project block, the standard cell test macros and the pad
# test buffer.
#   kl release_die.py <release.gds> <out.oas> <slots.json>
import json, re, sys
import klayout.db as db

BLOCK_RE = re.compile(r"^(tt_main_macro|tt_cell_macro_\d+|tt_buffer_macro)$")

src, out, slots_json = sys.argv[1:4]
ly = db.Layout(); ly.read(src)
(top,) = ly.top_cells()
boxes = {}
for inst in top.each_inst():
    name = inst.cell.name
    if BLOCK_RE.match(name):
        assert name not in boxes and inst.size() == 1, name
        bb = inst.dbbox()
        boxes[name] = [round(v, 3) for v in (bb.left, bb.bottom, bb.right, bb.top)]
options = db.SaveLayoutOptions()
options.format = "OASIS"
options.oasis_compression_level = 2
ly.write(out, options)
die = top.dbbox()
json.dump({"die": [die.left, die.bottom, die.right, die.top], "slots": dict(sorted(boxes.items()))},
          open(slots_json, "w"), indent=1)
print(f"{top.name}: {die.width():.0f} x {die.height():.0f} um, {len(boxes)} blocks: {sorted(boxes)}")
