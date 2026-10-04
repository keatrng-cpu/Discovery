---
name: clinical-notes-transcribe
description: Use when a visit transcript and a note template are both present and the template fields need filling from what was said. Quiet for diagnosis, plan of care, or any task without a transcript.
---
## Trigger
A transcript and a template (SOAP or similar) are both in hand. Quiet when only one exists, or when asked what the patient has or what to do next. Documentation only.
## Done-when
check: schema
Every template field in the output holds either a value quoted verbatim from the transcript with its turn or line locator, or the literal "MISSING". The output validates against the template field list: no extra fields, no field left blank, no field without one of the two forms. A transcript that fills zero fields is a valid result: all fields read "MISSING". An unread or unsupported transcript is also valid and is reported as such.
## Rung
rung: L1
One fast-model pass fills the fields; a program validates field names and the MISSING-or-quote rule. Escalate only if validation fails.
## Forbidden move
Smoothing a gap into a finding: writing a plausible value, a normal exam, or an inferred symptom into a field the transcript does not state. A silent field is MISSING, never "unremarkable" or "denies".
## Tool
tool: Bash:python3
scope: read
