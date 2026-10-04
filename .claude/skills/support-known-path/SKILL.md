---
name: support-known-path
description: Use when a ticket matches a documented workflow and its steps must run exactly as written. Quiet when any step differs or is missing.
---
## Trigger
A workflow definition with ordered steps and a matching ticket are present. Quiet when no workflow matches; that goes to exception.
## Done-when
check: state-diff
`jq -e --slurpfile e expected_state.json '. == $e[0]' state.json` exits 0 and prints `true`. Both files are supplied as input: expected_state.json lists the workflow's ordered steps with their end state, state.json is the observed snapshot, so reordering, skipping, or adding a step makes the arrays unequal. Any variance exits non-zero and routes to support-exception; the agent does not improvise. No model is in the loop, so reliable holds. Fetching a live snapshot needs an absent state reader.
## Rung
rung: L0
A program compares two files; the agent should not be in this directive. No model pass is needed.
## Forbidden move
Improvising: adding, skipping, or reordering a step, or repairing a variance instead of handing it to exception.
## Tool
tool: Bash:jq
scope: read
