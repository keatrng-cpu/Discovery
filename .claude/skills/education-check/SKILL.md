---
name: education-check
description: Use when a learner has just been taught something and must restate it or apply it once, and the answer is marked. Quiet for open drilling or explaining a new concept.
---
## Trigger
A learner answer exists for a restate or one-application prompt, with the key written down first. Quiet when no key exists, or when the ask is many questions on one skill.
## Done-when
check: exit-code
The ask is one restate or one application, marked against a stored key line. After a miss, the old and new example are saved to files and `cmp old_example.txt new_example.txt` exits 1 (they differ). Exit 0 means the paragraph was repeated: fail. A hit needs no new example, so no cmp run is a valid result.
## Rung
rung: L1
One fast-model pass marks and writes the replacement example; cmp is the check. Escalate only if cmp exits 0 after a retry.
## Forbidden move
Repeating the same paragraph or the same example after a miss. Change the example, not the wording.
## Tool
tool: Bash:cmp
scope: read
