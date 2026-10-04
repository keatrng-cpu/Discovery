# contract (task)
task: CI is red on the checkout service: a failing unit test after the refactor. Run the test suite and the build and the screenshot compare, and block done until verify exits clean
shelf: software
directive: verify
stakes: high
novelty: high
check: none authored: write the check before any edit
gate: ABSENT: checkout (prepare and stop)
rung: L4
token cap: 90000
verifier: check program + two-lens draft-blind verifier + human gate
skill: none (none)
files: plan.md state.json artifacts/software/verify.out
status: ready
