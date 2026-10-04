---
name: design-systems-flows
description: Use when one page type must be built from a template and checked by a visual diff. Quiet for single tokens, component lists, or multi-page-type requests.
---
## Trigger
One page type and its template exist. A request naming two page types is two directives: pick one. Quiet when no template exists.
## Done-when
check: state-diff
A real screenshot of the output (npx playwright screenshot) is diffed against the template screenshot; the diff reports 0 off-template regions, spacing and type taken from tokens. Any off-template region fails, listed by locator. No rendered page is a valid result: "unread", not a pass.
## Rung
rung: L1
One fast-model pass fills the template; the diff, not the model, decides off-template regions. Escalate only if the diff fails.
## Forbidden move
Judging a region on-template by looking at it instead of the diff, or waving through an off-template region.
## Tool
tool: Bash:playwright
scope: read
