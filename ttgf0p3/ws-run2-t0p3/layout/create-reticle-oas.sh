#!/bin/sh
set -Ce
cat T0P3-part-* > T0P3.oas
echo "bfd37b3547ee338c21a9689a031bbb0c  T0P3.oas" | md5sum -c
