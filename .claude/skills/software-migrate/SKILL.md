---
name: software-migrate
description: Use when one repeated code transform must be applied across many files, each on an isolated copy and rechecked. Quiet for a single-file edit.
---
## Trigger
One transform of one file shape applies to many files. Quiet for a single file, or when two different shapes are mixed.
## Done-when
check: count
`git ls-files` filtered by the one file shape prints N target paths, and the worker manifest lists exactly those N paths (sorted set comparison). N of 0 is a valid result: report "targets: 0".

## Rung
rung: L2
Workers run in parallel on isolated copies because the transform repeats; a separate verifier rechecks each transformed file and rejects any unchecked one. That recheck is a distinct step, not part of this count check. Escalate only for a file whose recheck fails twice.

## Forbidden move
Guessing the file list instead of enumerating it, or accepting a file whose result was not rechecked.
## Tool
tool: Bash:git
scope: read
