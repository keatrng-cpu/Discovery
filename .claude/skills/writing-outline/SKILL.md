---
name: writing-outline
description: Use when a piece needs its claims listed and ordered before any prose. Quiet when an outline already exists and the ask is to write it.
---
## Trigger
A topic or source notes are present and no outline exists. Quiet when an outline file is given and the ask is prose, or when the ask is to shorten or fact-check.
## Done-when
check: count
`python3` over the outline file exits 0 and prints "claims: N/N slotted": N claim lines, each with a unique order slot, and zero prose lines (a line that is neither a numbered claim nor blank). A claim with no slot is cut, not kept. An empty outline ("claims: 0/0") is a valid result when the source holds no claim.
## Rung
rung: L0
A program counts claims and slots; no model is needed to list them from a short source. Escalate only if the count tool exits non-zero for a reason other than a missing slot.
## Forbidden move
Writing prose or a transition sentence in the outline, or keeping a claim that has no slot.
## Tool
tool: Bash:python3
scope: read
