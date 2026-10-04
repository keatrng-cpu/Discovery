#!/usr/bin/env python3
"""Held-out check for markets-print. Document-locked: every number must be in the release, none from the recap only."""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NUM = re.compile(r"\$?\d[\d,]*(?:\.\d+)?%?")


def nums(s):
    return {m.rstrip(".,") for m in NUM.findall(s)}


def norm(s):
    return " ".join(s.split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    base = os.path.join(HERE, a.fixture)
    rel = open(os.path.join(base, "release.txt"), encoding="utf-8").read().splitlines()
    recap = open(os.path.join(base, "recap.txt"), encoding="utf-8").read()
    rel_nums = nums("\n".join(rel))
    recap_only = nums(recap) - rel_nums
    errs = []
    try:
        out = json.load(open(a.out))
    except Exception as e:
        print(f"FAIL: cannot read {a.out}: {e}")
        return 1
    if set(out) != {"eps", "guidance", "surprise"}:
        print(f"FAIL: keys must be eps, guidance, surprise; got {sorted(out)}")
        return 1
    strings = []
    for key in ("eps", "guidance", "surprise"):
        f = out[key]
        need = {"value", "quote", "line"} if key == "eps" else {"quote", "line"}
        if not isinstance(f, dict) or set(f) != need:
            errs.append(f"{key}: keys must be {sorted(need)}")
            continue
        ln, q = f["line"], f["quote"]
        if not isinstance(ln, int) or not (1 <= ln <= len(rel)):
            errs.append(f"{key}: line {ln!r} out of range 1..{len(rel)}")
            continue
        if not isinstance(q, str) or not q.strip() or norm(q) not in norm(rel[ln - 1]):
            errs.append(f"{key}: quote is not verbatim on release line {ln}")
        strings += [q] + ([f["value"]] if key == "eps" else [])
        if key == "eps":
            if not isinstance(f["value"], str) or f["value"] not in q:
                errs.append("eps: value must appear inside the quote")
            if not re.search(r"per\s+(diluted\s+)?share|\beps\b", q, re.I):
                errs.append("eps: quote must be an earnings-per-share line")
        if key == "guidance" and not re.search(r"expect|outlook|guid|forecast|range|between", q, re.I):
            errs.append("guidance: quote is not a guidance line")
    got = set()
    for s in strings:
        got |= nums(str(s))
    for n in sorted(got - rel_nums):
        errs.append(f"number {n} is not in the release")
    for n in sorted(got & recap_only):
        errs.append(f"number {n} appears only in the recap")
    for e in errs:
        print("FAIL:", e)
    print("OK" if not errs else f"{len(errs)} assertion(s) failed")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
