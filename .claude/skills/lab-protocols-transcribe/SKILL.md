---
name: lab-protocols-transcribe
description: Use when steps of a named lab method in a text or PDF source must be copied with quantities and units, gaps marked. Quiet for building a graph, repairing one, or running anything.
---
## Trigger
A named method and its source text are both present, and the ask is to copy the steps. Quiet when the source is absent, or when the ask is a graph, a repair, a campaign, or a run.
## Done-when
check: quote
Every transcribed step carries a quote of the source line with a locator (page and line, or step number) and the quote appears verbatim in the source (`pdftotext` output or the text file, matched by program). Every quantity and unit in a step appears in its quote. Each place the source skips a step is written as "GAP: <what is missing> after <locator>". A source with no steps is a valid result: output "steps: 0" and stop. An unread or unsupported source is reported as such, never filled.
## Rung
rung: L1
One fast-model pass copies the steps; a program matches each quote against the source. Escalate only if a quote fails to match.
## Forbidden move
Inventing a step the source skips (a wash, a spin time, a temperature) instead of marking a GAP; also rewriting units or rounding a quantity.
## Tool
tool: Bash:python3
scope: read
