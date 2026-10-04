---
name: education-drill
description: Use when a learner wants repeated practice on one skill with each answer marked against a known key. Quiet for explaining or for moving to a new skill.
---
## Trigger
One named skill and an answer key (or a computable answer) exist. Quiet when the key is absent, or when the ask spans more than one skill.
## Done-when
check: count
A python3 script marks every given answer against the stored key file and prints one "marked: N/N" line, each mark citing a key item locator. Exit 0 only when N equals the number of answers given and every answer has a key item. No key prints "marked: 0/N unmarked, key absent" and is a valid result. This is the only check; advancing is forbidden below, not bundled here.
## Rung
rung: L0
The marking is a program against the key; no model pass is needed. Escalate only if the key and an answer disagree on a locator.
## Forbidden move
Moving on inside the same directive: introducing a second skill, a next level, or a new item set after marking, or marking an answer with no key.
## Tool
tool: Bash:python3
scope: read
