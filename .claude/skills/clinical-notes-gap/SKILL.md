---
name: clinical-notes-gap
description: Use when a drafted clinical note has empty or MISSING template fields and the clinician needs to be asked for exactly those fields. Quiet for filling fields, diagnosis, or plan of care.
---
## Trigger
A drafted note with one or more fields marked MISSING or empty. Quiet when every field is filled, or when the ask is to fill a field from inference.
## Done-when
check: count
A program lists the MISSING or empty template fields by name and counts them. The set of field names in the ask equals the program's list of MISSING or empty fields (set equality by template field name): the counts match, every empty field is named, and no filled field is named in place of an empty one. A missing or substituted name fails. The ask carries no proposed value. Zero empty fields is a valid result: the output reads "gaps: 0" and asks nothing.
## Rung
rung: L0
Listing and counting empty fields is a pure program over the drafted note; the ask is the field names, with no model pass.
## Forbidden move
Inventing the field: filling the empty field with a guessed or typical value, offering a suggested answer, or asking about a field that is already filled.
## Tool
tool: Bash:python3
scope: read
