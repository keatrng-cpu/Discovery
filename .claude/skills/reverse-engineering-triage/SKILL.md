---
name: reverse-engineering-triage
description: Use when a binary or firmware file needs format, architecture, and entry identified from file tools. Quiet for disassembly, naming, decrypting, or bypassing.
---
## Trigger
One or more files are in hand and the ask is "what is this": format, class, endianness, architecture, entry. Quiet when the ask is function lists, call graphs, naming, lifting, or decrypting or bypassing anything.
## Done-when
check: exit-code
`python3 fixtures/re-triage/check.py --fixture <dir> --out <out.json>` exits 0: for each file the output equals what the checker parses from `file` and `readelf -h` itself, or is {"stop":"tools disagree"} when the tools error or disagree, or {"unsupported":"not ELF"}.
Worked example: run it on the tune fixture, `python3 fixtures/re-triage/check.py --fixture fixtures/re-triage/tune --out artifacts/triage.tune.json`. Not ELF and disagreement are valid results; report them as they are.
## Rung
rung: L0
A program alone. Run `file` and `readelf -h`, copy the fields they print, write the JSON. No model pass is needed; escalate only if the check exits non-zero for a reason other than a tool disagreement.
## Forbidden move
Any field the tools did not emit; continuing past a disagreement; anything beyond identification (no decryption, no bypass).
## Tool
tool: Bash:file
scope: read
## Held-out check
`python3 fixtures/re-triage/check.py --fixture heldout --out artifacts/seeds/reverse-engineering-triage.heldout.out.json`
Output shape: {"<filename>":{"format","class","endian","arch","entry"} | {"stop":"tools disagree"} | {"unsupported":"not ELF"}}
