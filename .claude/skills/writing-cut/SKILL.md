---
name: writing-cut
description: Use when an existing piece must be shortened without changing what it says. Quiet for rewriting into a new style or adding material.
---
## Trigger
A finished piece is present with a length target. Quiet when the ask is new material, a restyle, or a channel change.
## Done-when
check: count
`python3` over the original and the cut exits 0 only when words fell and nothing was inserted: cut words < original words, and the cut's tokens are an ordered subsequence of the original's (a diff shows only deletions), so no new claim can be swapped in at equal count and no restyle passes. It prints "claims: A -> B; words: X -> Y; inserted: 0" with B <= A. Equal claim counts are a valid result. A cut that rewords to shorten fails and goes to a person.
## Rung
rung: L1
One fast-model pass deletes; a program diffs the token sequence. Escalate only if inserted tokens appear or words did not fall.
## Forbidden move
Adding a claim while shortening, or restyling the piece into a new one.
## Tool
tool: Bash:python3
scope: read
