#!/bin/sh
set -Ce
cat TTP2-part-* > TTP2.oas
echo "b5f1b08305411c44c4bb3f1f5ddbbeab  TTP2.oas" | md5sum -c
