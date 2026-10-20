#!/bin/bash
# Build <ttid>/<run>-<code>/ in this repository for a Tiny Tapeout die whose layout is a release asset rather than a
# cut from a wafer.space reticle (Tiny Tapeout GF 0.1): the layout as OASIS, split into parts, a render, the block
# map, the manifest of blocks, the projects measured from the shared block's netlist, README and PROVENANCE.
#   scripts/build_release_die.sh <CODE>          (the die must be listed in scripts/dies.py, with `asset`)
#
# Inputs, all public (override with the variable):
#   RS              wafer-space/reticle-stitcher: scripts/lay2img.py and reticle.lyp, for the render
#   TT_GIT          a clone of TinyTapeout/<shuttle repository> (default: cloned into TT_WORK)
#   KL              the command that runs a Python script with the klayout module (default: python3)
#   TT_WORK         scratch files (default: scripts/work, not committed)
#   TT_OUT          write the die (and README) under this directory instead of the repository, to compare
set -e
code=$1
D=$(cd "$(dirname "$0")" && pwd)
T=$(dirname "$D")
eval "$(python3 "$D/dies.py" "$code")"
test -n "$asset" || { echo "$code has no release asset in dies.py; use build_tt.sh"; exit 1; }
W=${TT_WORK:-$D/work}
RS=${RS:-$T/../reticle-stitcher}
KL=${KL:-python3}
export TT_OUT
N=${TT_OUT:-$T}/$ttid/$run-${code,,}
test -f "$RS/scripts/lay2img.py" || { echo "no reticle-stitcher at $RS (set RS)"; exit 1; }
test ! -e "$N" || { echo "$N already exists"; exit 1; }
mkdir -p "$W/$code"
cd "$W/$code"

# The release's final layout, the earlier release's block outputs (their netlists), the project index.
R=https://github.com/TinyTapeout/$repo/releases/download
test -f "$asset" || curl -sSfL -o "$asset" "$R/$tag/$asset"
test -f main.tar.xz || curl -sSfL -o main.tar.xz "$R/$blocks_tag/main.tar.xz"
mkdir -p blocks && tar -xJf main.tar.xz -C blocks --no-same-owner --no-same-permissions
curl -sSfL -o index.json "https://index.tinytapeout.com/$ttid.json"
if [ -z "$TT_GIT" ]; then
  TT_GIT=$W/$repo.git
  test -d "$TT_GIT" || git clone -q --bare "https://github.com/TinyTapeout/$repo" "$TT_GIT"
fi
export TT_GIT

$KL "$D/release_die.py" "$asset" "$code.oas" "$code-slots.json"
$KL "$D/xor_check.py" "$asset" "$code.oas" | tee "$code-xor.log"
grep -q ' 0 differ$' "$code-xor.log"
python3 "$D/netlist_projects.py" blocks/main/runs/test/final/pnl/tt_main_macro.pnl.v main_cells_by_project.csv
L=$W/$code/$code.oas

mkdir -p "$N/layout" "$N/images"
(cd "$N/layout" && split -b 90M "$L" "$code-part-")
M=$(md5sum < "$L" | cut -d' ' -f1)
printf '#!/bin/sh\nset -Ce\ncat %s-part-* > %s.oas\necho "%s  %s.oas" | md5sum -c\n' $code $code $M $code > "$N/layout/create-reticle-oas.sh"
chmod +x "$N/layout/create-reticle-oas.sh"
$KL "$RS/scripts/lay2img.py" "$L" "$N/images/$code.png" --lyp "$RS/reticle.lyp" --width 4096 --oversampling 4 > "$code-lay2img.log" 2>&1
python3 "$D/gen_release_repo.py" "$code" "$code-slots.json" index.json main_cells_by_project.csv
python3 "$D/gen_tt_index.py"
echo "$code md5=$M repo=$N"
