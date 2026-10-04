---
name: strategy-analogy
description: Use when a borrowed analogy must name the part that does not transfer before any use. Quiet for metaphors in prose or for decisions without a source domain.
---
## Trigger
A proposed analogy or a request to reason by analogy. Quiet when no source domain is named or the ask is a rank or a what-if.
## Done-when
check: count
`python3` over the output prints "analogy: 3/3" only if exactly three labelled non-empty lines exist: "Source:", "Transfers:", "Does not transfer:". Only the Transfers line may feed later reasoning. A line reading "Does not transfer: none found" prints "analogy: 2/3 (none stated)" and exits 1: the skipped half is flagged, not smoothed.
## Rung
rung: L1
A fast model fills the three lines; code checks presence. The program cannot judge whether the does-not-transfer line is true; that half is the weak part and stays a person review.
## Forbidden move
Skipping or softening the Does not transfer line, or using a property from it afterwards.
## Tool
tool: Bash:python3
scope: read
