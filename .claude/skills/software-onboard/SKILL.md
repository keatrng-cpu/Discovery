---
name: software-onboard
description: Use when a newcomer needs one request flow with one hop matched to a runtime log line. Quiet for repo tours.
---
## Trigger
A named request or endpoint and a runtime log are present. Quiet for "explain the repo" or architecture overviews.
## Done-when
check: quote
Exactly one hop is matched to a runtime log line quoted verbatim with its log line number; `grep -n` of the quote in the log returns that number, and the line names the hop's function or file. No log line matching any hop is a valid result: report "log: unmatched" and stop.
## Rung
rung: L1
Code greps the route and the log; one fast-model pass lists the entry-to-store hops and owning modules as notes, which this directive does not check. Output ends after that one flow. Escalate only if no hop can be quoted.
## Forbidden move
Touring the repo: describing modules that are not on the traced request path.
## Tool
tool: Bash:python3
scope: read
