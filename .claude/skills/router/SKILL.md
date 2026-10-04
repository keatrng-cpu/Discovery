---
name: router
description: Use at the start of any substantive task to classify shelf, directive, stakes, novelty and emit a contract before any edit. Quiet for chat and one-line questions.
---
## Trigger
A task that edits, researches, analyzes, drafts, or acts. Quiet for conversation. Run before the first edit, never after.
## Done-when
check: schema
`python3 desk/desk.py route "<task>" --out artifacts/router/<id>.contract.md` exits 0 and `python3 desk/desk.py contract-lint artifacts/router/<id>.contract.md` exits 0.
## Rung
rung: L0
Classification is a program over registry/shelf/*.json keywords. Empty, ambiguous, and unsupported are valid results and are never smoothed into a guess.
## Forbidden move
Choosing a shelf or directive by feel when the router says ambiguous or unsupported. Starting work with no contract. Switching model or effort mid-thread.
## Tool
tool: Bash:python3
scope: read

Procedure
1. Read plan.md, contract.md, state.json (missing any: write them, do not start). Then run the route command above.
2. status ready: read the named SKILL.md (one skill only). status split: one contract per directive, run in order, stop at the first red check. status ambiguous: choose among the listed candidates only by quoting task words; if none fits, ask. status unsupported: say so; do not improvise a shelf.
3. Add one Done-when row to contract.md whose check command is the task contract's check program. Stop blocks done until it exits 0.
4. Cascade, cheapest first, escalate only when the check fails: L0 tool only. L1 this skill plus a fast model. L2 isolated swarm only if one transform repeats across files (worker per file, verifier rejects unchecked files). L3 planner agent writes plan.md. L4 only when novelty and stakes are both high: three planner agents get the same cached prefix, each writes a plan under 40 lines, a verifier that has not seen them ranks by the check, implement the winner only.
5. Stakes raise the verifier, never the doer. Max effort is a spike on one directive, not a setting.
6. Gate verbs are absent tools. Prepare the details with the gate agent and stop.
