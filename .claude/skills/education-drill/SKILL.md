---
name: education-drill
description: Use when a learner wants repeated practice on one skill with each answer marked against a known key. Quiet for explaining or for moving to a new skill.
---
## Trigger
One named skill and an answer key (or a computable answer) exist. Quiet when the key is absent, or when the ask spans more than one skill.
## Done-when
check: count
A line "marked: N/N" appears with N equal to the number of answers given, each mark citing a key item locator, and it is the last non-empty line of the reply: nothing follows the marks, so no next level, new item set, or new skill. No key prints "marked: 0/N unmarked, key absent" as the last line and is a valid result.
## Rung
rung: L1
One fast-model pass writes items; the marking is done against the key by code or by line. Escalate only if the key and an answer disagree on a locator.
## Forbidden move
Moving on inside the same directive: any text after the marked line that introduces a second skill, a next level, or a new item set, or marking an answer with no key.
## Tool
tool: Bash:python3
scope: read
