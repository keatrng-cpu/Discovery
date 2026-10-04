# plan.md

## Stage
scaffold -> shelves -> merge -> seeds -> invention -> report. Current: scaffold.

## Files to change (named)
CLAUDE.md, contract.md, plan.md, state.json, .claude/{settings.json,agents/*,hooks/*,skills/router,skills/invention}, desk/*, registry/*, fixtures/*, artifacts/*

## Files not to touch
trace/trace.jsonl (appended by the PostToolUse hook only). Workers may touch only .claude/skills/<their shelf>-*/ and registry/shelf/<their shelf>.json; desk.py merge-shelves rejects any branch that touches anything else.

## Tokens
Measured after the run from transcripts; written to artifacts/tokens.json.

## Report
Filled after the run.
