---
name: legal-risk
description: Use when one party's exposure in a contract needs a written severity score tied to quotes. Quiet for extraction or for relying on the score.
---
## Trigger
A contract, one named party, and a written severity rule are present. Quiet when no party or no rule is given.
## Done-when
check: quote
Every score row carries one named party, and that party is identical on every row and equal to the party the ask named; a row naming a different or a second party fails. Each row also carries the written rule it applied, a severity from that rule, and a verbatim quote that is a substring of the source with a section locator. A row without a quote is dropped and printed as "unscored: <text>". Zero scored rows is valid.
## Rung
rung: L1
A fast model scores against the rule; a program checks every quote is in the source and every row has party and rule. Escalate only on a failed quote match.
## Forbidden move
Scoring unquoted text, or scoring from both parties' views at once.
## Tool
tool: none
scope: none
gate: ABSENT sign (prepare the scored sheet and stop; a lawyer signs before anyone relies on it)
