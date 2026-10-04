---
name: research-gap
description: Use when a draft's claims must be checked against a corpus and only the first unsupported claim searched. Quiet for broad literature surveys or for drafting new text.
---
## Trigger
A draft with claims and a searchable corpus are both present. Quiet when there is no draft, or when the ask is a broad survey.
## Done-when
check: exit-code
`python3 fixtures/research-gap/check.py --fixture <dir> --out <out.json> --searchlog <log>` exits 0: the claims table validates, every quote is verbatim in the cited document, and the search log holds at most one search. One search is logged when an unsupported claim exists, and it targets the first unsupported claim only, ending resolution "filled" or "open" (declared open is a valid stop). Zero searches is valid when every claim is supported. Runnable today: fixtures/research-gap/check.py is an existing repo program and the search runs through the registered harness desk/tools/localsearch.py; no new program is needed.
## Rung
rung: L1
One fast-model pass lists claims and marks each; the program checks quotes and the search log. Worked example: fixtures/research-gap/tune. Escalate only if the check fails.
## Forbidden move
searching a second claim; a quote that is not verbatim; marking a cited-but-mismatching claim supported
## Tool
tool: Bash:localsearch
scope: read
## Held-out check
`python3 fixtures/research-gap/check.py --fixture heldout --out artifacts/seeds/research-gap.heldout.out.json --searchlog artifacts/seeds/research-gap.heldout.search.log`
`{"claims":[{"id","text","status":"supported"|"unsupported","evidence":null|{"doc","quote"},"searched":bool,"resolution":"filled"|"open"|"not-searched"|"n/a"}]}`
