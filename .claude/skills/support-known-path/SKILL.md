---
name: support-known-path
description: Use when a ticket matches a documented workflow and its steps must run exactly as written. Quiet when any step differs or is missing.
---
## Trigger
A workflow definition with ordered steps and a matching ticket are present. Quiet when no workflow matches; that goes to exception.
## Done-when
check: state-diff
`python3` diff of system state against the workflow's expected end state exits 0 with `state: matches steps N/N`. Any variance from a step exits non-zero and routes to support-exception; the agent does not improvise.
## Rung
rung: L0
A program or workflow engine runs the steps; the agent should not be in this directive. No model pass is needed.
## Forbidden move
Improvising: adding, skipping, or reordering a step, or repairing a variance instead of handing it to exception.
## Tool
tool: Bash:python3
scope: read
