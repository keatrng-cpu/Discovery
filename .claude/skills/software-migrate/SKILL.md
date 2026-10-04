---
name: software-migrate
description: Use when one repeated code transform must be applied across many files, each on an isolated copy and rechecked. Quiet for a single-file edit.
---
## Trigger
One transform of one file shape applies to many files. Quiet for a single file, or when two different shapes are mixed.
## Done-when
check: count
One command, `python3 migrate_check.py manifest.json --shape '*.ext'`, with one exit code. It does not exist in the repo yet: it is the program the desk would run. Inputs: the worker manifest and the one file shape. It exits 0 only if the manifest paths equal `git ls-files` filtered by that shape (sorted set comparison, N targets); every path has exactly one transform and that transform is of the one shape; each worker has its own distinct isolated copy; every path has a passing recheck record, and any path without one is rejected. N of 0 is a valid result: it prints "targets: 0" and exits 0.

## Rung
rung: L2
Workers run in parallel on isolated copies because the transform repeats; a separate verifier rechecks each transformed file and rejects any unchecked one. That recheck is a distinct step, not part of this count check. Escalate only for a file whose recheck fails twice.

## Forbidden move
Guessing the file list instead of enumerating it, or accepting a file whose result was not rechecked.
## Tool
tool: Bash:git
scope: read
