# contract (task)
task: CI is red on the checkout service: a failing unit test after the refactor. Run the test suite and the build and the screenshot compare, and block done until verify exits clean
shelf: software
directive: verify
stakes: low
novelty: high
check: exit-code: `bash verify_gate.sh` in the project directory exits 0: unit test, then build, then a real Playwright (chromium) screenshot of the rendered page compared byte for byte to fixture.png; the first failure stops it. The Stop hook blocks 'done' until it does. The script runs `python3 -m unittest discover -s tests` (tune fixture tests test_simple and test_zero_numerator in tests/test_mod.py), then py_compile, then the Playwright screenshot and cmp against fixture.png, under one exit code. A non-zero exit is a valid result: report RED with the exit code and the first failing line quoted verbatim, declared_done false. No verify_gate.sh in the directory is also a valid result: report "gate: absent" and stop. Never report GREEN without exit 0.
gate: none
rung: L3
token cap: 40000
verifier: check program only
skill: none (unverified)
files: plan.md state.json artifacts/software/verify.out
status: ready
