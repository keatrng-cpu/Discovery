---
name: education-check
description: Use when a learner has just been taught something, missed the restate or application, and the next example must differ. Quiet for open drilling or explaining a new concept.
---
## Trigger
A learner answer exists for a restate or one-application prompt, with the key written down first, and the last answer was a miss. Quiet when no key exists, or when the ask is many questions on one skill.
## Done-when
check: exit-code
After a miss, the old and new example are saved to old_example.txt and new_example.txt, each starting with a "scenario:" line. python3 compares their lowercase word sets: Jaccard similarity must be below 0.5 (exit 0 pass; exit 1 means the paragraph or scenario was repeated or reworded: fail). A hit needs no new example, so no comparison run is a valid result. This is the only check; marking is not bundled here.
## Rung
rung: L1
One fast-model pass writes the replacement example; the python3 comparison is the check. Escalate only if it exits 1 after a retry.
## Forbidden move
Repeating the same paragraph or the same scenario after a miss. Rewording or a one-byte edit does not count; the scenario must change.
## Tool
tool: Bash:python3
scope: read
