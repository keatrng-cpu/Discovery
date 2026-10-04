# contract (task)
task: Build an auto-routing layer: a deterministic prompt hook that maps each prompt to the connectors, plugins and skills that fit, injects the exact tool-load call, and respects scope gates
shelf: harness
directive: hook
stakes: med
novelty: high
check: exit-code: python3 .claude/hooks/test_hooks.py exits 0 (git ls-files .claude/hooks/test_hooks.py lists it): the hook exits 2 on a case where the model would have continued, exits 0 on a clean case. A hook that never fired fails.
gate: none
rung: L3
token cap: 40000
verifier: check program + draft-blind verifier on the claims table
skill: none (unverified)
files: plan.md state.json artifacts/harness/hook.out
status: ready
