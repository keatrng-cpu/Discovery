---
name: audio-names
description: Use when a script or transcript needs its proper nouns checked against a pronunciation list. Quiet for cutting, music, or ordering takes, and when no list file is supplied.
---
## Trigger
A script or transcript and a pronunciation list file are both present. Quiet when the list is missing: report "no list" and stop, never substitute a guess.
## Done-when
check: exit-code
A python3 script loads the list file itself (the list is read by the program, not recalled by a model) and compares the script's proper nouns against it. It exits 0 on every completed run, printing each unlisted name as "missing: <name> line <n>" and a final "names: K/N listed"; a flagged name is a valid result, not a failure. An empty script, or one with no proper nouns, passes with "names: 0/0". An unreadable or absent list file prints "no list" and exits 0 as a reported result, never a guess. The list wins over any model reading.
## Rung
rung: L1
No program alone can pick out every proper noun: one fast-model pass proposes candidate nouns, and the program does the lookup against the list. The model never supplies a pronunciation.
## Forbidden move
Guessing a pronunciation or spelling for a proper noun that is not on the list, instead of flagging it as missing.
## Tool
tool: Bash:python3
scope: read
absent: pronunciation list service (not registered; the list file is read by a script, so the status stays assisted)
