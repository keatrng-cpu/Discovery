# contract
STATUS: RED
shelf: software
directive: verify
check: bash verify_gate.sh exits 0
gate: none
rung: L0
token cap: 0

## Done-when
| id | row | check |
|---|---|---|
| v1 | verify gate is clean (unit test, build, render-compare) | `bash verify_gate.sh` |
