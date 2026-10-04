#!/usr/bin/env python3
"""Held-out check for reverse-engineering triage. Identification only. The CHECKER runs `file` and
`readelf -h` itself and derives the expected answer; the model's JSON must equal it exactly."""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def arch_norm(s):
    s = s.lower()
    if "x86-64" in s or "x86_64" in s:
        return "x86-64"
    if "aarch64" in s:
        return "aarch64"
    if "80386" in s or "i386" in s:
        return "x86"
    if "risc-v" in s or "riscv" in s:
        return "riscv"
    if "mips" in s:
        return "mips"
    if "powerpc" in s or "ppc" in s:
        return "powerpc"
    if "arm" in s:
        return "arm"
    return "other:" + s.strip()


def expected(path):
    f = subprocess.run(["file", "-b", path], capture_output=True, text=True)
    ftxt = f.stdout.strip()
    if f.returncode != 0 or not ftxt.startswith("ELF"):
        return {"unsupported": "not ELF"}
    r = subprocess.run(["readelf", "-h", path], capture_output=True, text=True)
    if r.returncode != 0:
        return {"stop": "tools disagree"}
    rt = r.stdout
    def field(name):
        m = re.search(rf"^\s*{name}:\s*(.+)$", rt, re.M)
        return m.group(1).strip() if m else None
    cls, data, mach, entry = field("Class"), field("Data"), field("Machine"), field("Entry point address")
    if not all((cls, data, mach, entry)):
        return {"stop": "tools disagree"}
    f_cls = "ELF64" if "64-bit" in ftxt else "ELF32" if "32-bit" in ftxt else None
    f_end = "little" if "LSB" in ftxt else "big" if "MSB" in ftxt else None
    parts = [p.strip() for p in ftxt.split(",")]
    f_arch = arch_norm(parts[1]) if len(parts) > 1 else None
    r_end = "little" if "little" in data else "big" if "big" in data else None
    if (f_cls, f_end, f_arch) != (cls, r_end, arch_norm(mach)):
        return {"stop": "tools disagree"}
    return {"format": "ELF", "class": cls, "endian": r_end, "arch": arch_norm(mach), "entry": entry}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    inputs = os.path.join(HERE, a.fixture, "inputs")
    files = sorted(os.listdir(inputs))
    try:
        out = json.load(open(a.out))
    except Exception as e:
        print(f"FAIL: cannot read {a.out}: {e}")
        return 1
    errs = []
    if sorted(out) != files:
        errs.append(f"keys {sorted(out)} != files {files}")
    for fn in files:
        want = expected(os.path.join(inputs, fn))
        if out.get(fn) != want:
            errs.append(f"{fn}: got {out.get(fn)!r}, tools say {want!r}")
    for e in errs:
        print("FAIL:", e)
    print("OK" if not errs else f"{len(errs)} assertion(s) failed")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
