---
name: writing-fact
description: Use when claims in a piece must each carry a source or an unsupported label. Quiet for style edits or when no claims exist.
---
## Trigger
A piece with factual claims is present. Quiet when the piece holds no checkable claim or the ask is style.
## Done-when
check: quote
`python3` over the piece and the source corpus exits 0 and prints "claims: N = S sourced + U unsupported" with N equal to the claim count. A claim line ends with exactly one of: the label "unsupported", or a quote plus locator (doc, line) whose quote appears verbatim at that line of that source (localsearch finds it; the program compares the text). A quote absent from the cited line, a missing locator, or any other label ("likely", "reportedly") exits non-zero naming the claim line. Zero sourced is a valid result.
## Rung
rung: L1
One fast-model pass searches and proposes quotes; a program matches each quote against its cited line. Escalate only if a quote does not match its source.
## Forbidden move
Upgrading a label by tone: a hedged or confident claim passed off as sourced without a matching quote, or a third state such as "likely".
## Tool
tool: Bash:localsearch
scope: read
