---
name: writing-cut
description: Use when an existing piece must be shortened without changing what it says. Quiet for rewriting into a new style or adding material.
---
## Trigger
A finished piece is present with a length target. Quiet when the ask is new material, a restyle, or a channel change.
## Done-when
check: count
`python3` counts claims in the original and the cut and exits 0 only when cut_claims <= original_claims, printing "claims: A -> B" with B <= A. A diff of claim lines shows only deletions. Equal counts are a valid result.
## Rung
rung: L1
One fast-model pass deletes and tightens; a program diffs the claim list. Escalate only if the count rises.
## Forbidden move
Adding a claim while shortening, or restyling the piece into a new one.
## Tool
tool: Bash:python3
scope: read
