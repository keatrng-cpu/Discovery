---
name: software-onboard
description: Use when a newcomer needs one request traced from entry to store, with the owning module per hop and one hop matched to a runtime log. Quiet for repo tours.
---
## Trigger
A named request or endpoint and a runtime log are present. Quiet for "explain the repo" or architecture overviews.
## Done-when
check: quote
The trace lists one entry, each hop to the store with the owning module and a quoted file:line, and exactly one hop matched to a verbatim runtime log line with its log line number. No log line matching any hop is a valid result: report "log: unmatched" and stop. Output ends after that one flow.
## Rung
rung: L1
Code greps the route and log; one fast-model pass names the owner of each hop. Escalate only if no hop can be quoted.
## Forbidden move
Touring the repo: describing modules that are not on the traced request path.
## Tool
tool: Bash:python3
scope: read
