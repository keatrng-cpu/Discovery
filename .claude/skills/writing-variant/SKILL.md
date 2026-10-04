---
name: writing-variant
description: Use when the same piece must be recast for another channel with the facts, numbers, and offer held fixed. Quiet when facts or the offer are to change.
---
## Trigger
A source piece, a frozen fact list with an "offer:" line, and a target channel are present. Quiet when no fact list exists or when the ask is to change the offer or numbers.
## Done-when
check: count
`python3` over the fact list (one item per line, the offer on a line starting "offer:", then numbers and names), the source piece, and the variant exits 0 and prints "violations: 0": one check, frozen facts. violations = fact-list items not verbatim in the variant (the offer text is an item, so a dropped offer counts) + a non-empty fact list with no "offer:" line + digit-bearing tokens in the variant found in neither the source piece nor the fact list (an added number). A missing item exits non-zero and names the line. An empty fact list prints "facts: 0/0" and is valid. An added non-numeric fact is not detectable by program, and the voice file (bans, style) is not measured here: both stay a human read.
## Rung
rung: L1
One fast-model pass rewrites for the channel; a program matches the offer, facts, and numbers. Escalate only if a violation repeats after one repair. Voice and bans get a human read.
## Forbidden move
Changing a number, dropping the offer, or adding a fact while adapting to the channel.
## Tool
tool: Bash:python3
scope: read
