#!/bin/sh
set -Ce
cat TTPG-part-* > TTPG.oas
echo "b6494ef5f5770752906c875739b2f09f  TTPG.oas" | md5sum -c
