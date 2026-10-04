---
name: legal-draft
description: Use when one flagged clause needs a proposed edit with the original kept visible. Quiet for whole-agreement rewrites or signing.
---
## Trigger
A flag naming one clause (flag id, section) and the original text are present. Quiet when no flag exists.
## Done-when
check: state-diff
The proposal is a tracked edit of the source. Reverting every tracked edit reproduces the source text byte for byte (original stays visible). Every edit hunk carries the flag id from the ask, and every changed line falls inside the flagged section's line range. A changed line outside the range, an untagged hunk, a hunk tagged with another flag id, or a revert that differs from the source fails. Zero edits is valid when the flag needs none.
## Rung
rung: L1
A fast model proposes the edit as a tracked change beside the original, tagged with the flag id; a diff program reverts the edits, compares to the source, and checks hunk tags and line range. Escalate only on a failed check.
## Forbidden move
Rewriting the deal: editing any clause the flag did not name.
## Tool
tool: none
scope: none
gate: ABSENT sign (prepare the flagged-clause edit and stop; a lawyer signs)
