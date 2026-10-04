---
name: support-known-path
description: Use when a ticket matches a documented workflow and its steps must run exactly as written. Quiet when any step differs or is missing.
---
## Trigger
A workflow definition with ordered steps and a matching ticket are present. Quiet when no workflow matches; that goes to exception.
## Done-when
check: state-diff
One command with one exit code: `jq -e --slurpfile e expected_state.json '. == $e[0]' state.json`. Inputs are expected_state.json (the workflow's ordered steps with their end state) and state.json (the observed system-state snapshot). Exit 0 asserts the output state equals the expected end state, so reordering, skipping, or adding a step fails. Any variance exits non-zero and routes to support-exception; the agent does not improvise. state.json is supplied by a person because the state reader is absent, so status is assisted until a reader produces it.
## Rung
rung: L0
A program compares two files; the agent should not be in this directive. No model pass is needed.
## Forbidden move
Improvising: adding, skipping, or reordering a step, or repairing a variance instead of handing it to exception.
## Tool
tool: Bash:jq
scope: read
