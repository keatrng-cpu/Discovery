# contract (task)
task: Here is the quarterly earnings press release for the stock. Give me the EPS and the guidance from the release and one surprise, with quotes and line numbers
shelf: markets
directive: print
stakes: med
novelty: high
check: exit-code: `python3 fixtures/markets-print/check.py --fixture <dir> --out <out.json>` exits 0: eps, guidance, and surprise each carry a verbatim quote and the line number of the release; every number in the output appears in the release and none comes from the recap only. A field the release does not hold is reported as absent (null, no quote, no line) and that counts as a pass: unsupported is a valid result. The check program fixtures/markets-print/check.py already exists in the repo and runs under the registered Bash:python3 with no new program.
gate: none
rung: L3
token cap: 40000
verifier: check program + draft-blind verifier on the claims table
skill: none (unverified)
files: plan.md state.json artifacts/markets/print.out
status: ready
