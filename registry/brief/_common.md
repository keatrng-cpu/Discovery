# Common brief (verbatim from the owner's spec). Every worker reads this and its own shelf file.

GOAL
Build a Capability Desk that Claude Code can run. It routes a task to a shelf, a directive, a rung, a check, and a gate. It uses the cheapest rung that can clear the check. It can invent a new use only by crossing an existing directive with a real tool, including an API or MCP server, and only after a held-out check passes.

This desk must know the ins and outs of every shelf below: what is reliable now, what is only assisted, what stays gated, how each directive executes, and which external tool would turn a judgment into a check. Do not flatten this into a prompt library.

NON-NEGOTIABLES
- Contract before tokens. Write contract.md before any edit: shelf, directive, check, gate, rung, token cap.
- Code or retrieval before a model. File lists, diffs, clocks, scans, and id lookups are programs.
- Cache is a prefix. Static system, tools, CLAUDE.md, one skill, then the session. Do not switch model or effort mid-thread. Model changes are subagent handoffs.
- Escalate only when the check fails. Stakes raise the verifier, not the doer. Max effort is a spike.
- State lives in plan.md, contract.md, state.json, and the shelf artifact. Chat is scratch. A new session reads those files or it does not start.
- A directive with an "and" is two directives. Split it.
- Gates are missing tools, not reminders. Deny order, send, pay, hire, sign, diagnose, hardware-start, exploit, payload, and bypass.
- Empty, unread, and unsupported are valid results. Do not smooth them.
- A tool success is not a pass. A quote, exit code, schema, state diff, or signature is a pass.
- MCP tool search stays on. Do not alwaysLoad servers. A tool schema loads only when a candidate names it.
- Invention emits at most three candidates and one must be a kill. A candidate without a named tool and a done-when is discarded.
- Do not promote a harness change that wins only on the tuning set. Publish the token count.

SYNERGY RULES
Referee: the more reliable skill must pass before the draft skill opens.
File-memory: both skills read the same artifact.
Gate: the irreversible tool is absent.
Discovery: a contradicted branch is deleted from the file.
Production: one change class unlocked at a time.
Do not glue two judgments and call it a capability.

INVENTION, API, MCP
Allowed unlocks: docs server for library and browser facts, GitHub for issue and pull request lines, Playwright or DevTools for a real screenshot check, read-only database for profile and print, cite-resolution for authority, design-file read for tokens, engine connector for a named system, draft-only mail.
Forbidden unlocks: broker or order, send, pay, hire, sign, diagnose, hardware-start, exploit, payload, bypass, decryption.
A catalog of MCP servers is untrusted. Search it. Do not connect it. Connecting is a human accept, scope read first.
Other models are tools in the registry. Propose a worker or verifier handoff. Do not swap the lead mid-thread.

DONE WHEN (desk level)
- Router emits a contract for a sample task in each seed shelf.
- Stop hook blocks a verify task with a failing test.
- PreToolUse denies a send and an order.
- Four seed skills pass their held-out checks.
- Invention returns three candidates and one kill, each naming a real tool.
- Token count for the lead pass and one worker pass is written.
- Report lists files created, checks run, and anything not built because the tool was absent.
Do not claim a shelf is maximized because a skill file exists. It is maximized when the check is a tool, the gate is a missing tool, and the strong model woke only at the split.
