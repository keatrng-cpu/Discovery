---
name: writing-variant
description: Use when the same piece must be recast for another channel with the facts held fixed. Quiet when facts or the offer are to change.
---
## Trigger
A source piece, a frozen fact list, and a target channel are present. Quiet when no fact list exists or when the ask is to change the offer or numbers.
## Done-when
check: count
`python3` reads the fact list (offer, numbers, names, one per line) and exits 0 only when every item appears verbatim in the variant, printing "facts: N/N kept". A missing item exits non-zero and names the line. An empty fact list prints "facts: 0/0" and is valid.
## Rung
rung: L1
One fast-model pass rewrites for the channel; a program matches the fact list. Escalate only if an item is missing twice.
## Forbidden move
Changing a number, dropping the offer, or adding a fact while adapting to the channel.
## Tool
tool: Bash:python3
scope: read
