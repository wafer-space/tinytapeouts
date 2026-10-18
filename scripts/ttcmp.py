# Fingerprint a Tiny Tapeout GF die so different copies can be compared: per-layer flat shape counts
# (via instance multiplicities, no flattening), die bbox, and every tt_um_* placement relative to the
# die's lower-left corner.   kl ttcmp.py <layout> <out.json>
import collections, json, sys
import klayout.db as db

path, out = sys.argv[1:3]
ly = db.Layout(); ly.read(path)
tops = ly.top_cells()
top = max(tops, key=lambda c: c.bbox().area())
mult = collections.Counter({top.cell_index(): 1})
for ci in ly.each_cell_top_down():
    cell = ly.cell(ci)
    n = mult[ci]
    if not n:
        continue
    for inst in cell.each_inst():
        mult[inst.cell_index] += n * inst.size()
layers = {}
for li in ly.layer_indexes():
    info = ly.get_info(li)
    n = sum(ly.cell(ci).shapes(li).size() * k for ci, k in mult.items())
    if n:
        layers[f"{info.layer}/{info.datatype}"] = n
bb = top.dbbox()
places = []
it = db.RecursiveInstanceIterator(ly, top)
it.targets = [c.cell_index() for c in ly.each_cell() if "tt_um_" in c.name]
while not it.at_end():
    t = it.dtrans() * it.inst_dtrans()
    name = ly.cell(it.inst_cell().cell_index()).name
    places.append([name[name.index("tt_um_"):], round(t.disp.x - bb.left, 3), round(t.disp.y - bb.bottom, 3), t.rot()])
    it.next()
json.dump({"file": path, "top": top.name, "tops": [c.name for c in tops], "bbox": [bb.left, bb.bottom, bb.width(), bb.height()],
           "cells": ly.cells(), "layers": layers, "tt_um": sorted(places)}, open(out, "w"), indent=0)
print(path, top.name, bb, len(layers), "layers", len(places), "tt_um placements", flush=True)
