---
name: invention
description: Use only when no verified skill fits or a directive keeps failing its check; crosses a weak directive with a real tool whose output is the check. Quiet otherwise.
---
## Trigger
The router says unsupported or novelty high with no verified skill, or artifacts/verdicts shows the same directive voted down twice. Quiet for any task a verified skill already clears.
## Done-when
check: exit-code
`python3 desk/desk.py invent-check registry/invention-last.json` exits 0: exactly 3 candidates, exactly 1 kill, each naming a tool in registry/tools.json (or a proposed tool with needsHumanAdd true), a done-when, and a shadow-run plan. A candidate without a named tool and a done-when is discarded, not emitted.
## Rung
rung: L3
Rare and novelty-high by definition. One planner pass; the verifier and invent-check decide, not the planner.
## Forbidden move
Inventing an act-scope tool. Connecting an MCP catalog entry (search it; connecting is a human accept, scope read first). Promoting on the tuning set. Crossing a directive already marked reliable. Swapping the lead model mid-thread: a worker or verifier handoff is the only model change.
## Tool
tool: Bash:python3
scope: read

Procedure
1. Read registry/shelf/*.json (status), registry/tools.json, registry/gaps.json, and the last failures in artifacts/verdicts/.
2. Cross ONE weak or assisted directive with ONE real tool whose output becomes a check (quote, exit code, schema, state diff, count). Allowed unlocks: docs server, GitHub issue and PR lines, Playwright or DevTools screenshot, read-only database, cite-resolution, design-file read, engine connector, draft-only mail. Forbidden: broker or order, send, pay, hire, sign, diagnose, hardware-start, exploit, payload, bypass, decryption.
3. Emit registry/invention-last.json: {"candidates":[{"shelf","directive","tool","toolScope":"read|draft","doneWhen","shadowRun","reason","kill":bool,"needsHumanAdd":bool}]}. One candidate is a kill: an attractive crossing you reject, with the reason.
4. Shadow-run the surviving candidate beside the current skill on the same held-out task. Write {"baseline":{"tokens","seconds","heldout_pass"},"candidate":{"tune_pass","heldout_pass","tokens","seconds"}} and run `python3 desk/desk.py promote-gate <file>`. Promote only on exit 0: held-out passes and tokens or seconds drop. The agent does not promote itself; a person merges.
