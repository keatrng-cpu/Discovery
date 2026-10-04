---
name: security-review-scan
description: Use when a repository needs a secret scan reported as tool output. Quiet for exploit work, for ranking findings, or when no repo is in hand.
---
## Trigger
A repo or branch is present and the ask is to scan for leaked secrets. Defensive only. Quiet for writing exploits, payloads, or bypasses, and for judging code by reading it.
## Done-when
check: exit-code
`mcp__github__run_secret_scanning` is run on the target and its stdout is quoted verbatim with the exit status. Each finding is reported as a quoted tool line with file path and line. Zero findings is a valid result: report "scan: 0 findings" with the tool's exit status. A tool that did not run is reported as "unscanned", never as clean.
The dependency scan is a separate check and is not bundled here; no dependency scanner is registered, so report "dependency scan: absent".
## Rung
rung: L0
The tool output is the finding; a program alone clears it. No model pass. Escalate only if the tool errors, and then report the error, not a guess.
## Forbidden move
Reporting a model hunch as a finding: any secret, CVE, or vulnerability that is not a quoted line of scanner output.
## Tool
tool: mcp__github__run_secret_scanning
scope: read
