---
name: writing-fact
description: Use when claims in a piece must each carry a source or an unsupported label. Quiet for style edits or when no claims exist.
---
## Trigger
A piece with factual claims is present. Quiet when the piece holds no checkable claim or the ask is style.
## Done-when
check: quote
Every claim line ends with either a source quote plus locator (page, line, or item) or the label "unsupported", and a program prints "claims: N = S sourced + U unsupported" with N equal to the claim count. Zero sourced is a valid result. A claim left with neither is cut or labelled; there is no third option.
## Rung
rung: L1
One fast-model pass searches and proposes quotes; a program matches each quote against the source text. Escalate only if a quote does not match its source.
## Forbidden move
Upgrading a label by tone: a hedged or confident claim passed off as sourced without a matching quote, or a third state such as "likely".
## Tool
tool: Bash:localsearch
scope: read
