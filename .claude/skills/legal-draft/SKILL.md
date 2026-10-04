---
name: legal-draft
description: Use when one flagged clause needs a proposed edit with the original kept visible. Quiet for whole-agreement rewrites or signing.
---
## Trigger
A flag naming one clause (flag id, section) and the original text are present. Quiet when no flag exists.
## Done-when
check: state-diff
A diff of the proposal against the source touches only the flagged section: every changed line falls inside that section's line range. Any changed line outside the flagged section fails. Zero edits is valid when the flag needs none.
## Rung
rung: L1
A fast model proposes the edit, keeps the original text visible beside it, and tags it with the flag id (reviewer aids, not part of the check); a diff program checks the changed lines sit inside the flagged section. Escalate only on an out-of-scope line.
## Forbidden move
Rewriting the deal: editing any clause the flag did not name.
## Tool
tool: none
scope: none
gate: ABSENT sign (prepare the flagged-clause edit and stop; a lawyer signs)
