---
name: writing-variant
description: Use when the same piece must be recast for another channel with the facts held fixed. Quiet when facts or the offer are to change.
---
## Trigger
A source piece, a frozen fact list, and a target channel are present. Quiet when no fact list exists or when the ask is to change the offer or numbers.
## Done-when
check: count
`python3` over the fact list (offer, numbers, names, one per line), the source piece, the variant, and the voice file exits 0 and prints "violations: 0": violations = fact-list items not verbatim in the variant + digit-bearing tokens in the variant found in neither the source piece nor the fact list (an added number) + hits of any phrase under the voice file's "Bans" heading. A missing item exits non-zero and names the line. An empty fact list prints "facts: 0/0" and is valid. An added non-numeric fact is not detectable by program; it stays a human read.
## Rung
rung: L1
One fast-model pass rewrites for the channel; a program matches facts, numbers, and bans. Escalate only if a violation repeats after one repair.
## Forbidden move
Changing a number, dropping the offer, or adding a fact while adapting to the channel.
## Tool
tool: Bash:python3
scope: read
