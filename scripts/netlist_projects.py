# Which Tiny Tapeout project each standard cell of a shared block belongs to, from the block's powered netlist
# (.pnl.v). On Tiny Tapeout GF 0.1 all projects were synthesised and placed together in tt_main_macro, so the
# layout has no per-project cells; the netlist keeps the hierarchy in its net names (mux_inst.p<NN>_I...).
#
#   python3 netlist_projects.py <block.pnl.v> <out.csv>
#
# A cell belongs to the project named by most of its nets. A cell with only anonymous nets (net123, _0456_)
# takes the project of the cells it shares nets with when they all belong to one project, repeated until
# nothing changes; power, constant and
# high-fanout nets (clock and reset trees, more than FANOUT cells) do not link cells. What is left is the
# block's own logic, the multiplexer and controller, as "shared", together with any project that is purely
# combinational: synthesis keeps no names for those (on GF 0.1, Chip ROM and the MULDIV unit). Writes one row per project, cell type and fill
# flag with the instance count, and prints how each cell was assigned.
import collections, csv, re, sys

FANOUT = 32
PROJECT_RE = re.compile(r"mux_inst\.p(\d\d)_I\.")
INST_RE = re.compile(r"^\s*(gf180mcu_\w+)\s+(\\\S+ |\S+)\s*\((.*?)\);", re.M | re.S)
NET_RE = re.compile(r"\.\w+\(\s*(\\\S+ |[^()\s,]+)\s*\)")
POWER = {"VDD", "VSS", "1'b0", "1'b1"}
FILL = ("fill", "endcap", "filltie", "fillcap", "tap", "antenna", "diode", "tiel", "tieh")  # as in ws-run-reports analyze.py

pnl, out = sys.argv[1:3]
cells = []  # (type, nets)
for m in INST_RE.finditer(open(pnl).read()):
    nets = [n.strip() for n in NET_RE.findall(m.group(3))]
    cells.append((m.group(1), [n for n in nets if n not in POWER]))

owner, how = [None] * len(cells), [""] * len(cells)
members = collections.defaultdict(list)
for i, (_, nets) in enumerate(cells):
    named = collections.Counter(p for n in nets for p in PROJECT_RE.findall(n))
    if named:
        owner[i], how[i] = named.most_common(1)[0][0], "named"
    for n in nets:
        members[n].append(i)
links = {n: c for n, c in members.items() if 1 < len(c) <= FANOUT}

changed = True
rounds = 0
while changed:
    changed, rounds = False, rounds + 1
    votes = collections.defaultdict(collections.Counter)
    for c in links.values():
        labels = collections.Counter(owner[i] for i in c if owner[i])
        if labels:
            for i in c:
                if owner[i] is None:
                    votes[i].update(labels)
    for i, v in votes.items():
        # Only when every labelled neighbour agrees: the multiplexer touches many projects and stays shared.
        if len(v) == 1:
            owner[i], how[i] = next(iter(v)), "neighbours"
            changed = True

rows = collections.Counter()
for i, (ctype, _) in enumerate(cells):
    lib, _, short = ctype.partition("__")
    rows[(owner[i] or "shared", lib, short, short.startswith(FILL))] += 1
with open(out, "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["project", "library", "cell_type", "is_fill", "instance_count"])
    for (p, lib, short, fill), n in sorted(rows.items()):
        w.writerow([p, lib, short, fill, n])
print(f"{len(cells)} cells in {rounds} rounds:", dict(collections.Counter(how[i] or "shared" for i in range(len(cells)))))
