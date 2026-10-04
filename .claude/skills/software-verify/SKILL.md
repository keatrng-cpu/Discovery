---
name: software-verify
description: Use when a code change must be proven done by running the project's verify gate script. Quiet for fixing the failure, writing new tests, or review.
---
## Trigger
A project directory holds verify_gate.sh and a change claims to be finished. Quiet when no gate script exists: report "gate: absent" and stop.
## Done-when
check: exit-code
`bash verify_gate.sh` in the project directory exits 0: unit test, then build, then a real Playwright (chromium) screenshot of the rendered page compared byte for byte to fixture.png; the first failure stops it. The Stop hook blocks 'done' until it does. The script runs `python3 -m unittest discover -s tests` (tune fixture tests test_simple and test_zero_numerator in tests/test_mod.py), then py_compile, then the Playwright screenshot and cmp against fixture.png, under one exit code. A non-zero exit is a valid result: report RED with the exit code and the first failing line quoted verbatim, declared_done false. No verify_gate.sh in the directory is also a valid result: report "gate: absent" and stop. Never report GREEN without exit 0.
Worked example: run it inside fixtures/sw-verify/tune/broken (RED) and fixtures/sw-verify/tune/fixed (GREEN).

## Rung
rung: L0
A program alone: run the script, read the exit code, copy one line. No model pass. A red gate goes back to the edit directive, not to a stronger verifier.
## Forbidden move
declaring done, or editing any file, on a model read of the output; verify never fixes.
## Tool
tool: Bash:unittest
scope: read
The script verify_gate.sh exists today under fixtures/sw-verify/tune; its first step is `python3 -m unittest` (the registered tool), its build step is py_compile and its render step is a Playwright chromium screenshot cmp'd to fixture.png, both run inside the same script and covered by its single exit code. No new program is needed.
## Held-out check
`python3 fixtures/sw-verify/check.py --fixture heldout --out artifacts/seeds/software-verify.heldout.out.json`
Output shape:
`{"status":"RED"|"GREEN","gate_exit":<int>,"failing_line":<verbatim line from the gate output or null>,"declared_done":false}`
