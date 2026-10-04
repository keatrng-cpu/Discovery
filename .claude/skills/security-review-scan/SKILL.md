---
name: security-review-scan
description: Use when a repository needs a secret scan reported as tool output. Quiet for exploit work, for ranking findings, or when no repo is in hand.
---
## Trigger
A repo or branch is present and the ask is to scan for leaked secrets. Defensive only. Quiet for writing exploits, payloads, or bypasses, and for judging code by reading it.
## Done-when
check: exit-code
One result line from one tool run: `mcp__github__run_secret_scanning` stdout quoted verbatim with exit status; each finding a quoted tool line with file and line. Zero findings is valid: "secret scan: 0 findings". A scan that did not run is "secret scan: unscanned". A finding without a quoted scanner line is never reported, and unscanned is never reported as clean.
Dependency scanning is a separate directive with no registered scanner; this skill makes no dependency claim.
## Rung
rung: L0
The tool output is the finding; a program alone clears it. No model pass. Escalate only if the tool errors, and then report the error, not a guess.
## Forbidden move
Reporting a model hunch as a finding: any secret, CVE, or vulnerability that is not a quoted line of scanner output.
## Tool
tool: mcp__github__run_secret_scanning
scope: read
