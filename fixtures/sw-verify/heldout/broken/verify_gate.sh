#!/usr/bin/env bash
# One exit code over three checks: unit tests, build, screenshot compare. The first failure stops it.
set -e
cd "$(dirname "$0")"
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT
python3 -m unittest discover -s tests -q
python3 -m py_compile src/mod.py
python3 render.py > "$T/page.html"
npx --no-install playwright screenshot --browser chromium --viewport-size=320,80 "file://$T/page.html" "$T/shot.png" > /dev/null
cmp -s "$T/shot.png" fixture.png
