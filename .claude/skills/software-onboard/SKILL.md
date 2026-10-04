---
name: software-onboard
description: Use when a newcomer needs one request flow with one hop matched to a runtime log line. Quiet for repo tours.
---
## Trigger
A named request or endpoint and a runtime log are present. Quiet for "explain the repo" or architecture overviews.
## Done-when
check: quote
One record, read by a program: the hops of one request from entry to store, each as file:line of the hop function (the line exists in the file and contains the function name) plus the owning module; the first hop is the route entry and the last hop is the store call. Exactly one hop is also matched to a runtime log line quoted verbatim with its log line number; python3 reading that log line number returns the quote, and the line names the hop's function or file. No log line matching any hop is a valid result: report "log: unmatched" and stop.

## Rung
rung: L1
Code greps the route and the log; one fast-model pass lists the entry-to-store hops and owning modules, then the program above checks every hop locator. Output ends after that one flow. Escalate only if no hop can be quoted.

## Forbidden move
Touring the repo: describing modules that are not on the traced request path.
## Tool
tool: Bash:python3
scope: read
