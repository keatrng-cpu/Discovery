---
name: design-systems-cli
description: Use when off-system output must be rejected by a brand CLI that returns the failed rule. Quiet for markdown guides, style prose, or model-judged review.
---
## Trigger
A brand rejecting CLI is named or present. A markdown guide is not this directive. Quiet when no CLI exists: report "tool absent", do not substitute a model.
## Done-when
check: exit-code
The brand CLI exits 0 on on-system output; on off-system output it exits non-zero and prints the failed rule id. Never "almost" pass. The CLI is absent in this environment: report "tool absent", the check is not runnable, and no script or model stands in for the reject. With the CLI absent, no pass is possible; the result is "tool absent".
## Rung
rung: L0
The tool rejects; no model pass. A model cannot substitute for the reject.
## Forbidden move
Rejecting off-system output in a plea or review comment instead of the tool, or treating a near-pass as a pass.
## Tool
tool: none
scope: none
