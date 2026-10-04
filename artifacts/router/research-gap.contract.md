# contract (task)
task: My draft has six claims and some citations. List the claims, mark which ones are unsupported, and search for a source only for the first unsupported claim
shelf: research
directive: gap
stakes: med
novelty: low
check: exit-code: `python3 fixtures/research-gap/check.py --fixture <dir> --out <out.json> --searchlog <log>` exits 0: the claims table validates, every quote is verbatim in the cited document, and the search log holds at most one search. One search is logged when an unsupported claim exists, and it targets the first unsupported claim only, ending resolution "filled" or "open" (declared open is a valid stop). Zero searches is valid when every claim is supported. Runnable today: fixtures/research-gap/check.py is an existing repo program and the search runs through the registered harness desk/tools/localsearch.py; no new program is needed.
gate: none
rung: L1
token cap: 20000
verifier: check program + draft-blind verifier on the claims table
skill: .claude/skills/research-gap/SKILL.md
files: plan.md state.json artifacts/research/gap.out
status: ready
