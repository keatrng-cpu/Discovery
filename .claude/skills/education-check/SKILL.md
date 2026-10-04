---
name: education-check
description: Use when a learner has just been taught something, missed the restate or application, and the next example must differ. Quiet for open drilling or explaining a new concept.
---
## Trigger
A learner answer exists for a restate or one-application prompt, with the key written down first, and the last answer was a miss. Quiet when no key exists, or when the ask is many questions on one skill.
## Done-when
check: exit-code
One command, python3 desk/check_example.py key.txt answer.txt old_example.txt new_example.txt, gives one exit code (0 pass, 1 fail) and does not exist yet. It asserts the answer file is a restate or one application and prints one 'mark: hit' or 'mark: miss' line from comparing it to key.txt. On a miss it asserts the new example differs: each file starts with a 'scenario:' line, the two scenario lines share under half their lowercase words (Jaccard below 0.5) and no paragraph is identical, and the new scenario introduces at least one noun absent from the old one so a rewording fails. A hit needs no new example and exit 0 with no comparison is valid; no key or no answer prints 'mark: unsupported' and is valid.
## Rung
rung: L1
One fast-model pass writes the replacement example; the python3 comparison is the check. Escalate only if it exits 1 after a retry.
## Forbidden move
Repeating the same paragraph or the same scenario after a miss. Rewording or a one-byte edit does not count; the scenario must change.
## Tool
tool: Bash:python3
scope: read
