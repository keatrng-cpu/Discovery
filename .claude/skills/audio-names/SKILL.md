---
name: audio-names
description: Use when a script or transcript needs its proper nouns checked against a pronunciation list. Quiet for cutting, music, or ordering takes, and when no list file is supplied.
---
## Trigger
A script or transcript and a pronunciation list file are both present. Quiet when the list is missing: report "no list" and stop, never substitute a guess.
## Done-when
check: exit-code
A python3 script reads the list file and the script's proper nouns and exits 0 only if every noun is on the list; otherwise it exits non-zero and prints each unlisted name as "missing: <name> line <n>". An empty script, or one with no proper nouns, passes with "names: 0/0". The list wins over any model reading.
## Rung
rung: L0
A program does the lookup against the list; no model pass is needed. A model may only propose candidate nouns to look up, never a pronunciation.
## Forbidden move
Guessing a pronunciation or spelling for a proper noun that is not on the list, instead of flagging it as missing.
## Tool
tool: Bash:python3
scope: read
