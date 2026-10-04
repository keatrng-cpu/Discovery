---
name: education-drill
description: Use when a learner wants repeated practice on one skill with each answer marked against a known key. Quiet for explaining or for moving to a new skill.
---
## Trigger
One named skill and an answer key (or a computable answer) exist. Quiet when the key is absent, or when the ask spans more than one skill.
## Done-when
check: count
One command, python3 desk/mark_drill.py key.txt answers.txt reply.txt, gives one exit code and does not exist yet. It asserts key.txt names exactly one 'skill:' and every answer cites it, marks every given answer against key.txt, and prints one 'marked: N/N' line with each mark citing a key item locator. It asserts that line is the last non-empty line of reply.txt, so no second skill, next level, or new item set follows. Exit 0 when N equals the number of answers given and every answer has a key item; with no key it prints 'marked: 0/N unmarked, key absent', which is valid and also exits 0.
## Rung
rung: L0
The marking is a program against the key; no model pass is needed. Escalate only if the key and an answer disagree on a locator.
## Forbidden move
Moving on inside the same directive: introducing a second skill, a next level, or a new item set after marking, or marking an answer with no key.
## Tool
tool: Bash:python3
scope: read
