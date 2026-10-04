---
name: support-classify
description: Use when a support ticket needs a policy id and the policy line quoted, or an escalation when no id fits. Quiet for drafting replies or resolving.
---
## Trigger
A ticket text and a policy id list are both present. Quiet when the ask is to reply, resolve, or promise anything.
## Done-when
check: quote
`python3` lookup exits 0 only if the assigned policy id exists in the policy id list and the quoted policy line matches that entry verbatim, reported as `policy-id: <id> line: <file>:<n>`. The result `escalate: no policy id fits` with exit 0 is valid. An id that does not resolve exits non-zero.
## Rung
rung: L1
One fast-model pass proposes an id; code resolves it against the id list. Escalate only when the id fails to resolve, and then the result is escalate, not a new id.
## Forbidden move
Inventing or paraphrasing a policy id or policy line that is not in the id list. If no id fits, escalate.
## Tool
tool: Bash:python3
scope: read
