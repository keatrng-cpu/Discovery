---
name: design-systems-cli
description: Use when off-system output must be rejected by a brand CLI that returns the failed rule. Quiet for markdown guides, style prose, or model-judged review.
---
## Trigger
A brand rejecting CLI is named or present. A markdown guide is not this directive. Quiet when no CLI exists: report "tool absent", do not substitute a model.
## Done-when
check: exit-code
The CLI exits 0 on on-system output; on off-system output it exits non-zero and prints the failed rule id. Never "almost" pass. No CLI in this environment is a valid result: the check is not runnable and must say so.
## Rung
rung: L0
The tool rejects; no model pass. A model cannot substitute for the reject. Escalate only to report the printed rule.
## Forbidden move
Rejecting off-system output in a plea or review comment instead of the tool, or treating a near-pass as a pass.
## Tool
tool: Bash:python3
scope: read
