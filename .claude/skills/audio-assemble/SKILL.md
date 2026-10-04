---
name: audio-assemble
description: Use when approved takes must be put in order into an episode sequence. Quiet for regenerating audio, cutting inside a take, or music placement.
---
## Trigger
An approved-takes list and the take files are present. Quiet when a take is unapproved or missing, or when the ask is to regenerate audio.
## Done-when
check: signature
A python3 script hashes each take file and compares against the approved list: it exits 0 only if the sequence holds exactly the approved takes, each hash unchanged, in the listed order, printing "assembled: N/N takes". An unapproved, missing, or altered take makes it exit non-zero and name the take. An empty approved list is a valid result ("assembled: 0/0"). A person listens to the assembly; that listen is the close and the ceiling stays shut.
## Rung
rung: L1
A fast-model pass drafts the sequence from the list; code verifies hashes and order.
## Forbidden move
Regenerating or re-recording audio to fill a gap or smooth a seam, or substituting an unapproved take.
## Tool
tool: Bash:python3
scope: read
