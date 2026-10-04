---
name: clinical-notes-sign
description: Use when a finished clinical note is ready for the clinician to review and sign. Presents the note and stops. Quiet for diagnosis, plan of care, or any request to sign on the clinician's behalf.
---
## Trigger
A note has passed transcribe, gap, and cite and awaits the clinician. Quiet for any ask to sign, attest, or diagnose.
## Done-when
check: signature
The presented note carries an empty signature block and no signature, attestation, or date-signed value written by the agent. Only the clinician's own signature, added outside this session, counts as signed. A program reads the signature field and passes only when it is empty at presentation.
## Rung
rung: L0
A program prints the note with the unsigned block. No model pass is needed.
## Forbidden move
Becoming a diagnosis: adding an assessment, impression, or plan of care to the presented note, or marking it signed, approved, or final on the clinician's behalf.
## Tool
tool: none
scope: none
gate: ABSENT sign, diagnose (present the note, stop; the clinician signs)
