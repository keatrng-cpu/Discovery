---
name: strategy-analogy
description: Use when a borrowed analogy must name the part that does not transfer before any use. Quiet for metaphors in prose or for decisions without a source domain.
---
## Trigger
A proposed analogy or a request to reason by analogy. Quiet when no source domain is named or the ask is a rank or a what-if.
## Done-when
check: count
`python3` over the output prints "analogy: 3/3" only if exactly three labelled non-empty lines exist: "Source:", "Transfers:", "Does not transfer:", and no later line (any reasoning after the three) contains a content word that appears in the Does not transfer line but not in the Transfers line; a hit prints "analogy: leak <word>" and exits 1. A line reading "Does not transfer: none found" prints "analogy: 2/3 (none stated)" and exits 1: the skipped half is flagged, not smoothed. Whether the Does not transfer line is true stays a person review.
## Rung
rung: L1
A fast model fills the three lines; code checks presence and scans later reasoning for words from the Does not transfer line. Whether that line is true stays a person review.
## Forbidden move
Skipping or softening the Does not transfer line, or using a property from it afterwards.
## Tool
tool: Bash:python3
scope: read
