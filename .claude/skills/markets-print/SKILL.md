---
name: markets-print
description: Use when an earnings press release is in hand and the ask is EPS, guidance, and one surprise from it. Quiet for recaps-only input, filings, trading, or sizing.
---
## Trigger
An earnings release file is present (tune example: fixtures/markets-print/tune/release.txt). Quiet when only a news recap exists, or when the ask is to trade or size.
## Done-when
check: exit-code
`python3 fixtures/markets-print/check.py --fixture <dir> --out <out.json>` exits 0: eps, guidance, and surprise each carry a verbatim quote and the line number of the release; every number in the output appears in the release and none comes from the recap only.
A field the release does not hold is reported as absent (null, no quote, no line) and that counts as a pass: unsupported is a valid result.
The check is the existing program fixtures/markets-print/check.py, so checkRunnable is true.
## Rung
rung: L1
One fast-model pass reads the release and writes the JSON; the check program verifies quotes and numbers. Escalate only if the check exits non-zero.
## Forbidden move
Any number taken from a recap; averaging two figures; filling a field the release does not hold.
## Tool
tool: none
scope: none
## Held-out check
`python3 fixtures/markets-print/check.py --fixture heldout --out artifacts/seeds/markets-print.heldout.out.json`
`{"eps":{"value","quote","line"},"guidance":{"quote","line"},"surprise":{"quote","line"}}`
