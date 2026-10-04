---
name: audio-assemble
description: Use when approved takes must be put in order into an episode sequence. Quiet for regenerating audio, cutting inside a take, or music placement.
---
## Trigger
An approved-takes list and the take files are present. Quiet when a take is unapproved or missing, or when the ask is to regenerate audio.
## Done-when
check: signature
A python3 script hashes each take file and compares against the approved list: it exits 0 only if the sequence holds exactly the approved takes, each hash unchanged, in the listed order, printing "assembled: N/N takes". An unapproved, missing, or altered take makes it exit non-zero and name the take. An empty approved list is a valid result ("assembled: 0/0"). This directive prepares the ordered list and hash report, then stops; the listen and accept belong to the gate.
## Rung
rung: L0
The approved list fixes the order, so a program alone builds the ordered take list and hash report; no model pass is needed. The hash script is run by hand, not as a registered tool.
## Forbidden move
Regenerating or re-recording audio to fill a gap or smooth a seam, or substituting an unapproved take.
## Tool
tool: none
scope: none
gate: ABSENT accept (prepare the ordered take list and hash report, stop; a person listens and accepts the assembly)
