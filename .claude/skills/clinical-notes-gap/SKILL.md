---
name: clinical-notes-gap
description: Use when a drafted clinical note has empty or MISSING template fields and the clinician needs to be asked for exactly those fields. Quiet for filling fields, diagnosis, or plan of care.
---
## Trigger
A drafted note with one or more fields marked MISSING or empty. Quiet when every field is filled, or when the ask is to fill a field from inference.
## Done-when
check: count
The number of fields named in the ask equals the number of MISSING or empty fields in the note, and each named field is one of those fields, listed by template field name. Each ask is one question for that field and carries no proposed value. Zero empty fields is a valid result: the output reads "gaps: 0" and asks nothing.
## Rung
rung: L1
A program lists the empty fields; one fast-model pass words one question per field. Escalate only if the counts differ.
## Forbidden move
Inventing the field: filling the empty field with a guessed or typical value, offering a suggested answer, or asking about a field that is already filled.
## Tool
tool: Bash:python3
scope: read
