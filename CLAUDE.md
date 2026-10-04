# Capability Desk

A router, a registry, and a set of gates. It sends a task to a shelf, a directive, a rung, a check, and a gate, and uses the cheapest rung that can clear the check. Shelf lore lives in `registry/` and `.claude/skills/`, never here.

## Resume rule
A new session reads `plan.md`, then `contract.md`, then `state.json`, then the shelf artifact, in that order. If any is missing, write it before doing anything else. Chat is scratch; these files are the state.

## Router (every substantive task)
1. Run `python3 desk/desk.py route "<task>" --out artifacts/router/<id>.contract.md`. It classifies shelf, directive, stakes, novelty from `registry/shelf/*.json` and emits a contract: shelf, directive, check, gate, rung, token cap.
2. `ready`: load that one skill (`.claude/skills/<shelf>-<directive>/SKILL.md`). `split`: one contract per directive, in order. `ambiguous` or `unsupported`: say so; do not guess a shelf.
3. Add a Done-when row to `contract.md` whose check command is the contract's check program. The Stop hook re-runs every row and blocks "done" until all exit 0.
4. Cascade, cheapest first. Escalate only when the check fails.
   - L0 tool only (file lists, diffs, clocks, scans, id lookups are programs, never a model)
   - L1 one skill plus a fast model
   - L2 isolated swarm, only if one transform repeats across files
   - L3 `planner` agent writes `plan.md`
   - L4 three short plans from one cached prefix, only if novelty and stakes are both high; implement the winner only
5. Stakes raise the verifier, not the doer. Max effort is a spike on one directive, not a setting.

## Gate list: these are missing tools, not reminders
order, send, pay, hire, sign, diagnose, hardware-start, exploit, payload, bypass (and decrypt).
Prepare the details with the `gate` agent, write them to the shelf artifact, and stop. A tool whose scope is `act` needs a human add in `registry/tools.json` (`human_added: true`). The deny list wins over the registry. Unregistered MCP tools are denied; a catalog of MCP servers is untrusted: search it, never connect it. MCP tool search stays on; nothing is `alwaysLoad`.

## Split rule
One directive, one check. A directive with an "and" is two directives: write two skills and two contract rows. Do not glue two judgments and call it a capability.

## Results
Empty, unread, and unsupported are valid results; do not smooth them. A tool success is not a pass. A quote with a locator, an exit code, a schema validation, a state diff, or a signature is a pass.

## Cache is a prefix
Static system, tools, this file, one skill, then the session. Do not switch model or effort mid-thread. A model change is a subagent handoff (`.claude/agents/`): planner (opus, high), worker (sonnet, medium, isolated copy), verifier (opus, high, never sees the draft), gate (sonnet, prepares only).

## Hooks (`.claude/settings.json`)
- Stop: re-runs `contract.md` Done-when checks; exit 2 blocks. Capped at 3 blocks per red streak, then a STOP-FORCED record goes to the trace.
- PreToolUse: denies gate verbs, send-class commands, unregistered and un-added act tools, and any write to the trace.
- PostToolUse: appends a hash-chained record to `trace/trace.jsonl`. Nothing deletes it. `python3 desk/desk.py verify-trace` must exit 0.

## Invention
Only `.claude/skills/invention/SKILL.md`. Exactly three candidates and one kill, each naming a real tool and a done-when, shadow-run beside the current skill, promoted only if the held-out check holds and tokens or time drop. The agent does not promote itself.

## Commands
- `python3 desk/desk.py lint` registry, skills, tools, gates
- `python3 desk/desk.py contract-check` run every Done-when row (add `--write` to update STATUS)
- `python3 -m unittest discover -s desk/tests -q` unit tests
- `python3 .claude/hooks/test_hooks.py all` hook tests
