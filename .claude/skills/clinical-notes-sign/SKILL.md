---
name: clinical-notes-sign
description: Use when a finished clinical note is ready for the clinician to review and sign. Presents the note and stops. Quiet for diagnosis, plan of care, or any request to sign on the clinician's behalf.
---
## Trigger
A note has passed transcribe, gap, and cite and awaits the clinician. Quiet for any ask to sign, attest, or diagnose.
## Done-when
check: state-diff
A program diffs the presented note against the note that passed cite. The only difference allowed is an empty signature block. Any added assessment, impression, plan of care, agent-written signature, attestation, or signed date fails the diff. Presenting the cite-passed note unchanged plus the empty signature block is the valid result. Only the clinician signs, outside this session.
## Rung
rung: L0
A program prints the note with the unsigned block and runs the diff. No model pass is needed.
## Forbidden move
Becoming a diagnosis: adding an assessment, impression, or plan of care to the presented note, or marking it signed, approved, or final on the clinician's behalf.
## Tool
tool: none
scope: none
gate: ABSENT sign, diagnose (present the note, stop; the clinician signs)
