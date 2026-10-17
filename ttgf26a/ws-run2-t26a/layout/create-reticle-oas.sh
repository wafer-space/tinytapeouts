#!/bin/sh
set -Ce
cat T26A-part-* > T26A.oas
echo "8fdfc77220918a548aa0b9707aa0e5ff  T26A.oas" | md5sum -c
