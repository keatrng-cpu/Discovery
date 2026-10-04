---
name: reverse-engineering-lift
description: Use when a spec must be recovered from code, scored on a known architecture before the target. Quiet for plain disassembly, naming, or unknown-ISA reliability claims.
---
## Trigger
A known-architecture sample with ground truth exists, and a target needs a recovered spec. Quiet when no scored sample exists, or when the ask is decrypting or bypassing.
## Done-when
check: count
A scoring program run on the known-architecture sample prints the line "lift: M/N matched" and exits 0, and its log shows the sample scored before the target file is opened. M=N, or an unknown architecture reported as "unsupported", is a valid result.
## Rung
rung: L1
Deterministic ISA recovery does the matching first. One fast-model pass touches only the target items left unmatched by the deterministic recovery; the whole target is never sent. Escalate only if the score on the known sample falls below what the router set.
## Forbidden move
Sending the whole target to a model before the known-architecture score exists; calling an unknown-ISA lift reliable.
## Tool
tool: Bash:python3
scope: read
