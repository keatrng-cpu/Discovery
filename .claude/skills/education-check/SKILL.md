---
name: education-check
description: Use when a learner has just been taught something and must restate it or apply it once, and the answer is marked. Quiet for open drilling or explaining a new concept.
---
## Trigger
A learner answer exists for a restate or one-application prompt, with the key written down first. Quiet when no key exists, or when the ask is many questions on one skill.
## Done-when
check: exit-code
The answer is marked by exactly one line "marked: hit" or "marked: miss" citing the stored key line locator (count 1); no mark line fails. After a miss, old and new example are saved to old_example.txt and new_example.txt, each starting with a "scenario:" line. The scenario lines go to old_scenario.txt and new_scenario.txt, and `cmp old_scenario.txt new_scenario.txt` exits 1 (a new scenario, not rewording) and `cmp old_example.txt new_example.txt` exits 1. Exit 0 on either means the paragraph or example was repeated: fail. A hit needs no new example, so no cmp run is a valid result.
## Rung
rung: L1
One fast-model pass marks and writes the replacement example; cmp is the check. Escalate only if cmp exits 0 after a retry.
## Forbidden move
Repeating the same paragraph or the same scenario after a miss. Rewording or a one-byte edit does not count; the scenario must change.
## Tool
tool: Bash:cmp
scope: read
