#!/bin/sh
set -Ce
cat T0P1-part-* > T0P1.oas
echo "1064ed9cfa033b91c1a45309a916fa83  T0P1.oas" | md5sum -c
