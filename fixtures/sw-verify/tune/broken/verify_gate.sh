#!/usr/bin/env bash
# One exit code over three checks: unit tests, build, render-compare. The first failure stops it.
set -e
cd "$(dirname "$0")"
python3 -m unittest discover -s tests -q
python3 -m py_compile src/mod.py
python3 render.py | cmp -s - fixture.txt
