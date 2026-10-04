# contract (task)
task: I have an unknown executable binary. Identify the file format and the architecture from the ELF header with the file tools and name the entry point
shelf: reverse-engineering
directive: triage
stakes: med
novelty: low
check: exit-code: `python3 fixtures/re-triage/check.py --fixture <dir> --out <out.json>` exits 0: for each file the output fields format, class, endian, arch, and entry (the entry point address) equal what the checker parses from `file` and `readelf -h` itself, or is {"stop":"tools disagree"} when the tools error or disagree, or {"unsupported":"not ELF"}.
gate: none
rung: L0
token cap: 0
verifier: check program + draft-blind verifier on the claims table
skill: .claude/skills/reverse-engineering-triage/SKILL.md
files: plan.md state.json artifacts/reverse-engineering/triage.out
status: ready
