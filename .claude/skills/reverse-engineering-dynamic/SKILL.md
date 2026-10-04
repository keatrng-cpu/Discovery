---
name: reverse-engineering-dynamic
description: Use when a static claim about a binary must be compared to an emulation trace and contradicted claims dropped. Quiet when no trace exists or the ask is to run code on real hardware.
---
## Trigger
A static claim list and a saved trace from emulation are both in hand. Quiet when only one exists, when the ask is to start hardware, or to decrypt or bypass anything.
## Done-when
check: count
A comparison program prints "claims: K kept, D dropped of N" with K+D=N. Each dropped claim cites the contradicting trace line by line number; no kept claim has a contradicting trace line. With no trace the result is "unsupported: no trace", exit 0, claims unchanged and marked untested.
## Rung
rung: L1
One fast-model pass pairs each claim with the trace lines; code does the count and the line lookup. Escalate only if a dropped claim has no cited line.
## Forbidden move
Keeping a claim the trace contradicts, or dropping one without a cited trace line; inventing a trace when no emulator is registered.
## Tool
tool: Bash:python3
scope: read
