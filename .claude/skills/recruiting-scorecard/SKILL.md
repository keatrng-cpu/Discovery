---
name: recruiting-scorecard
description: Use when a job req needs scorecard lines drafted for a hiring manager to accept. Quiet for resumes, candidates, or offers.
---
## Trigger
A job requisition text is present and the ask is to turn it into scorecard lines. Quiet when no req exists, or when the ask concerns a candidate.
## Done-when
check: quote
Every scorecard line carries a verbatim quote from the req with its line number, and a program confirms each quote is a substring of the req at that line (python3 exits 0, prints "lines: N/N quoted"). A line with no req quote fails. The status stays "awaiting manager accept" until a person marks each line accepted; a req with zero usable lines is a valid result and prints "lines: 0/0".
## Rung
rung: L1
One fast-model pass drafts lines from the req; code checks the quotes. Escalate only if a quote fails to resolve after one repair pass.
## Forbidden move
Adding a trait the req does not state (culture fit, energy, leadership presence). The req wins; drop the line.
## Tool
tool: none
scope: none
gate: ABSENT accept (the hiring manager accepts each scorecard line; the draft is prepared with req quotes and stops at status "awaiting manager accept")
