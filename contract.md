# contract.md: Capability Desk build
STATUS: GREEN

shelf: harness
directive: evolve (one change class per run: scaffold, then shelves, then seeds, then invention)
check: every Done-when row below exits 0; the Stop hook re-runs them
gate: act-scope tools ABSENT (order, send, pay, hire, sign, diagnose, hardware-start, exploit, payload, bypass, decrypt)
rung: L3 lead plan (this thread) -> L2 isolated swarm (worker sonnet medium, one shelf each) -> verifier opus high, draft-blind
token cap: lead pass and one worker pass measured from transcripts and written to artifacts/tokens.json; per-shelf soft cap 60000

## Done-when
| id | row | check |
|---|---|---|
| d1 | Router emits a valid contract for a held-out task in each seed shelf | `python3 desk/desk.py route-eval fixtures/router/heldout/tasks.json` |
| d2 | Stop hook blocks a verify task with a failing test | `python3 .claude/hooks/test_hooks.py stop` |
| d3 | PreToolUse denies a send and an order | `python3 .claude/hooks/test_hooks.py deny` |
| d4a | Seed software-verify passes its held-out check | `python3 fixtures/sw-verify/check.py --fixture heldout --out artifacts/seeds/software-verify.heldout.out.json` |
| d4b | Seed research-gap passes its held-out check | `python3 fixtures/research-gap/check.py --fixture heldout --out artifacts/seeds/research-gap.heldout.out.json --searchlog artifacts/seeds/research-gap.heldout.search.log` |
| d4c | Seed markets-print passes its held-out check | `python3 fixtures/markets-print/check.py --fixture heldout --out artifacts/seeds/markets-print.heldout.out.json` |
| d4d | Seed reverse-engineering-triage passes its held-out check | `python3 fixtures/re-triage/check.py --fixture heldout --out artifacts/seeds/reverse-engineering-triage.heldout.out.json` |
| d5 | Invention returns three candidates and one kill, each naming a real tool | `python3 desk/desk.py invent-check registry/invention-last.json` |
| d6 | Token count for the lead pass and one worker pass is written | `python3 desk/desk.py tokens-check artifacts/tokens.json` |
| d7 | Registry, skills, tools, and gates lint clean | `python3 desk/desk.py lint` |
| d8a | Trace chain is intact | `python3 desk/desk.py verify-trace` |
| d8b | Trace tamper (edit, delete, reorder) fails verification | `python3 .claude/hooks/test_hooks.py trace` |
| d9 | Unit tests pass | `python3 -m unittest discover -s desk/tests -q` |
| d10 | Report lists files created, checks run, and what was not built because a tool was absent | `python3 desk/desk.py report-check plan.md` |
| d11 | Capability map lints clean: only read or draft tools auto-load, no gate verb, no act tool, index fresh | `python3 desk/desk.py caps-lint` |
| d12 | Prompt and session-start hooks name the exact tool-load call, stay silent on chit-chat, fail open, and never name an act tool | `python3 .claude/hooks/test_hooks.py route` |
| d13 | Recorded index-proxy answers plus the matcher meet the pre-registered thresholds on the held-out prompts (arithmetic re-run; the model answers are a recorded file) | `python3 desk/desk.py caps-score fixtures/caps/heldout.json artifacts/caps/index_eval_answers.json` |

## Per-task contract template (the router emits this; no contract, no start)
shelf: | directive: | stakes: low/med/high | novelty: low/high
check: exit code | quote with locator | schema | state diff | signature | count
gate: the absent tool, or none
rung: L0 to L4, the cheapest that clears the check; escalate only on a failed check
token cap: integer (L0 0, L1 20000, L2 60000, L3 40000, L4 90000)
