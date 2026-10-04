---
name: software-verify
description: Use when a code change must be proven done by running the named test, the build, and the screenshot compare. Quiet for fixing the failure, writing new tests, or review.
---
## Trigger
A project directory holds verify_gate.sh and a change claims to be finished. Also fires when the Stop hook asks whether work is done. Quiet when no gate script exists: report "gate: absent" and stop.
## Done-when
check: exit-code
`bash verify_gate.sh` in the project directory exits 0 (unit test, then build, then render-compare against the fixture; the first failure stops it). The Stop hook blocks 'done' until it does.
A non-zero exit is a valid result: report RED with the exit code and the first failing line quoted verbatim. Never report GREEN without exit 0.
Worked example: run it inside fixtures/sw-verify/tune.
## Rung
rung: L0
A program alone: run the script, read the exit code, copy one line. No model pass. Escalation is not warranted by a failing gate; a red gate goes back to the edit directive, not to a stronger verifier.
## Forbidden move
declaring done, or editing any file, on a model read of the output; verify never fixes.
## Tool
tool: Bash:unittest
scope: read
## Held-out check
`python3 fixtures/sw-verify/check.py --fixture heldout --out artifacts/seeds/software-verify.heldout.out.json`
Output shape:
`{"status":"RED"|"GREEN","gate_exit":<int>,"failing_line":<verbatim line from the gate output or null>,"declared_done":false}`
