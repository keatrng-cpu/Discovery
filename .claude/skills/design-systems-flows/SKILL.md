---
name: design-systems-flows
description: Use when one page type must be built from a template and checked by a visual diff. Quiet for single tokens, component lists, or multi-page-type requests.
---
## Trigger
One page type and its one template screenshot exist. A request naming two page types is two directives: pick one and diff against that template only. Quiet when no template exists.
## Done-when
check: state-diff
A real screenshot of the output (npx playwright screenshot) is diffed against the one named template screenshot; the diff reports "off-template regions: 0". Any off-template region fails, listed by locator. Token provenance of spacing and type is the tokens directive, not checked here. No rendered page is a valid result: "unread", not a pass.
## Rung
rung: L1
One fast-model pass fills the template; the diff, not the model, decides off-template regions. Escalate only if the diff fails.
## Forbidden move
Judging a region on-template by looking at it instead of the diff, or waving through an off-template region.
## Tool
tool: Bash:playwright
scope: read
