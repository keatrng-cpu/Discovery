---
name: legal-risk
description: Use when one party's exposure in a contract needs a written severity score tied to quotes. Quiet for extraction or for relying on the score.
---
## Trigger
A contract, one named party, and a written severity rule are present. The scoring party is the one the ask named, fixed for the whole pass (a second party is a second pass). Quiet when no party or no rule is given.
## Done-when
check: quote
Each score row carries the party it scored, the written rule it applied, a severity from that rule, and a verbatim quote that is a substring of the source with a section locator. Every row's party equals the one party the ask named; a row for any other party fails. A row without a quote is dropped and printed as "unscored: <text>". Zero scored rows is valid.
## Rung
rung: L1
A fast model scores against the rule for the named party only; a program checks every quote is in the source and every row has rule, severity and locator. Escalate only on a failed quote match.
## Forbidden move
Scoring unquoted text, or scoring from both parties' views at once.
## Tool
tool: none
scope: none
gate: ABSENT sign (prepare the scored sheet and stop; a lawyer signs before anyone relies on it)
