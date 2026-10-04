---
name: software-onboard
description: Use when a newcomer needs one request flow with one hop matched to a runtime log line. Quiet for repo tours.
---
## Trigger
A named request or endpoint and a runtime log are present. Quiet for "explain the repo" or architecture overviews.
## Done-when
check: quote
One command, `python3 onboard_check.py record.json --repo . --log app.log`, with one exit code. It does not exist in the repo yet: it is the program the desk would run. Inputs: the flow record, the repo, the log. It exits 0 only if each hop is a file:line whose line exists and contains the hop function name, with an owning module; the first hop is the route entry and the last is the store call; exactly one hop carries a log line quoted verbatim at its stated log line number, naming that hop's function or file. No log line matching any hop is a valid result: it prints "log: unmatched" and exits 0.

## Rung
rung: L1
Code greps the route and the log; one fast-model pass lists the entry-to-store hops and owning modules, then the program above checks every hop locator. Output ends after that one flow. Escalate only if no hop can be quoted.

## Forbidden move
Touring the repo: describing modules that are not on the traced request path.
## Tool
tool: Bash:python3
scope: read
