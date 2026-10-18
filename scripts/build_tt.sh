#!/bin/bash
# Build <ttid>/<run>-<code>/ in this repository for one Tiny Tapeout die on a wafer.space run: the die cut from
# the run's reticle, split into parts, a render, the project slot map, manifest, README and PROVENANCE.
#   scripts/build_tt.sh <CODE>          (the die must be listed in scripts/dies.py)
#
# Inputs, all public, by default checkouts next to this repository (override with the variable):
#   RUN_REPO        wafer-space/<run>: layout/<shuttle>.oas, or the layout/<shuttle>-part-* it is assembled from
#   RS              wafer-space/reticle-stitcher: scripts/lay2img.py and reticle.lyp, for the render
#   WS_RUN_REPORTS  wafer-space/ws-run-reports: `ws-run-reports tt-manifest` writes data/manifest.csv
#   TT_GIT          a clone of TinyTapeout/<shuttle repository> holding the release commit (default: cloned into TT_WORK)
#   KL              the command that runs a Python script with the klayout module (default: python3)
#   TT_WORK         scratch files (default: scripts/work, not committed)
#   TT_OUT          write the die (and README) under this directory instead of the repository, to compare
set -e
code=$1
D=$(cd "$(dirname "$0")" && pwd)
T=$(dirname "$D")
eval "$(python3 "$D/dies.py" "$code")"
W=${TT_WORK:-$D/work}
RUN_REPO=${RUN_REPO:-$T/../$run}
RS=${RS:-$T/../reticle-stitcher}
export WS_RUN_REPORTS=${WS_RUN_REPORTS:-$T/../ws-run-reports}
KL=${KL:-python3}
export TT_OUT
N=${TT_OUT:-$T}/$ttid/$run-${code,,}
test -f "$RS/scripts/lay2img.py" || { echo "no reticle-stitcher at $RS (set RS)"; exit 1; }
test ! -e "$N" || { echo "$N already exists"; exit 1; }
mkdir -p "$W/$code"
cd "$W/$code"

# The Tiny Tapeout release: its shuttle index, and the shuttle repository for the projects' info.yaml.
curl -sSfL -o shuttle_index.zip "https://github.com/TinyTapeout/$repo/releases/download/$tag/shuttle_index.zip"
unzip -o -q shuttle_index.zip
if [ -z "$TT_GIT" ]; then
  TT_GIT=$W/$repo.git
  test -d "$TT_GIT" || git clone -q --bare "https://github.com/TinyTapeout/$repo" "$TT_GIT"
fi
export TT_GIT

# The die exactly as it is on the reticle.
R=$RUN_REPO/layout/$shuttle.oas
if [ ! -f "$R" ]; then
  R=$W/$shuttle.oas
  test -f "$R" || cat "$RUN_REPO/layout/$shuttle"-part-* > "$R"
fi
$KL "$D/cut_die.py" "$R" "$code" "$code.oas"
L=$W/$code/$code.oas

mkdir -p "$N/layout" "$N/images"
(cd "$N/layout" && split -b 90M "$L" "$code-part-")
M=$(md5sum < "$L" | cut -d' ' -f1)
printf '#!/bin/sh\nset -Ce\ncat %s-part-* > %s.oas\necho "%s  %s.oas" | md5sum -c\n' $code $code $M $code > "$N/layout/create-reticle-oas.sh"
chmod +x "$N/layout/create-reticle-oas.sh"
$KL "$D/tt_slots.py" "$L" shuttle_index.json "$code-slots.json"
$KL "$RS/scripts/lay2img.py" "$L" "$N/images/$code.png" --lyp "$RS/reticle.lyp" --width 4096 --oversampling 4 > "$code-lay2img.log" 2>&1
python3 "$D/gen_tt_repo.py" "$code" "$code-slots.json" shuttle_index.json
python3 "$D/gen_tt_index.py"
echo "$code md5=$M repo=$N"
