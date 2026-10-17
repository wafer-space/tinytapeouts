#!/bin/sh
set -Ce
cat T26B-part-* > T26B.oas
echo "a905e364075a3362a8629aee939dd5e6  T26B.oas" | md5sum -c
