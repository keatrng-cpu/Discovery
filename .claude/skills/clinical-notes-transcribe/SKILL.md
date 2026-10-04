---
name: clinical-notes-transcribe
description: Use when a visit transcript and a note template are both present and the template fields need filling from what was said. Quiet for diagnosis, plan of care, or any task without a transcript.
---
## Trigger
A transcript and a template (SOAP or similar) are both in hand. Quiet when only one exists, or when asked what the patient has or what to do next. Documentation only.
## Done-when
check: quote
Every field value that is not the literal "MISSING" is a verbatim substring of the transcript, reported with its turn or line locator, and a program confirms the substring match. A field the transcript does not state reads "MISSING". A transcript that fills zero fields is a valid result: all fields read "MISSING". An unread or unsupported transcript is also valid and is reported as such.
## Rung
rung: L1
One fast-model pass fills the fields; a program checks each quoted value against the transcript. Escalate only if a quote fails to match.
## Forbidden move
Smoothing a gap into a finding: writing a plausible value, a normal exam, or an inferred symptom into a field the transcript does not state. A silent field is MISSING, never "unremarkable" or "denies".
## Tool
tool: Bash:python3
scope: read
