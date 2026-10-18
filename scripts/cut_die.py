# Cut one die out of a wafer.space reticle: the reticle's top-level cell for the die (<CODE>_...) and everything
# below it, in the cell's own coordinates, written as OASIS.
#   kl cut_die.py <reticle.oas> <CODE> <out.oas>
import sys
import klayout.db as db

reticle, code, out = sys.argv[1:4]
ly = db.Layout(); ly.read(reticle)
top = ly.top_cells()[0]
cells = {i.cell.cell_index(): i.cell for i in top.each_inst() if i.cell.name.startswith(code + "_")}
assert len(cells) == 1, f"{len(cells)} top-level cells for {code}: {[c.name for c in cells.values()]}"
(cell,) = cells.values()
options = db.SaveLayoutOptions()
options.format = "OASIS"
options.oasis_compression_level = 2
cell.write(out, options)
print(f"{code}: {cell.name}, {cell.dbbox().width():.0f} x {cell.dbbox().height():.0f} um")
