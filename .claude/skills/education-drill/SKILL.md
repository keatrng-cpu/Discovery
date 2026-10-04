---
name: education-drill
description: Use when a learner wants repeated practice on one skill with each answer marked against a known key. Quiet for explaining or for moving to a new skill.
---
## Trigger
One named skill and an answer key (or a computable answer) exist. Quiet when the key is absent, or when the ask spans more than one skill.
## Done-when
check: count
A marking line "marked: N/N" appears, where N equals the number of answers given and each mark cites a key line locator (item number). Every item carries the same skill tag. No key present prints "marked: 0/N unmarked, key absent" and is a valid result. Advancing to another skill in this directive fails.
## Rung
rung: L1
One fast-model pass writes items; the marking is done against the key by code or by line. Escalate only if the key and an answer disagree on a locator.
## Forbidden move
Moving on inside the same directive: introducing a second skill or a next level after the marks, or marking an answer with no key.
## Tool
tool: Bash:python3
scope: read
