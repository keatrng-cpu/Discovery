---
name: software-migrate
description: Use when one repeated code transform must be applied across many files, each on an isolated copy and rechecked. Quiet for a single-file edit.
---
## Trigger
One transform of one file shape applies to many files. Quiet for a single file, or when two different shapes are mixed.
## Done-when
check: count
`git ls-files` filtered by the shape lists N target files, and the verifier report shows "rechecked: N/N" with every transformed file rechecked on its own isolated copy. Any file without a recheck is rejected and counted out. N of 0 is a valid result: report "targets: 0".
## Rung
rung: L2
Workers run in parallel on isolated copies because the transform repeats; a verifier rejects unchecked files. Escalate only for a file whose recheck fails twice.
## Forbidden move
Guessing the file list instead of enumerating it, or accepting a file whose result was not rechecked.
## Tool
tool: Bash:git
scope: read
