# Check that two layouts of the same die are the same geometry, layer by layer: the XOR of each layer's
# merged shapes (deep mode, so the hierarchy is kept) must be empty. Shape counts alone can differ when one
# file stores repeated shapes as OASIS arrays.
#   kl xor_check.py <a> <b>
import sys
import klayout.db as db

a, b = db.Layout(), db.Layout()
a.read(sys.argv[1]); b.read(sys.argv[2])
ta, tb = a.top_cells()[0], b.top_cells()[0]
dss = db.DeepShapeStore()
layers = {(a.get_info(i).layer, a.get_info(i).datatype) for i in a.layer_indexes()}
layers |= {(b.get_info(i).layer, b.get_info(i).datatype) for i in b.layer_indexes()}
bad = 0
for ld in sorted(layers):
    ia, ib = a.find_layer(*ld), b.find_layer(*ld)
    ra = db.Region(ta.begin_shapes_rec(ia), dss) if ia is not None else db.Region()
    rb = db.Region(tb.begin_shapes_rec(ib), dss) if ib is not None else db.Region()
    x = ra ^ rb
    n = x.count()
    if n:
        bad += 1
        print(f"{ld[0]}/{ld[1]}: XOR {n} shapes, area {x.area() * a.dbu ** 2:.3f} um2", flush=True)
print(f"{len(layers)} layers, {bad} differ")
