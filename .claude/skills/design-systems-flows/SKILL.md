---
name: design-systems-flows
description: Use when one page type must be built from a template and checked by a visual diff. Quiet for single tokens, component lists, or multi-page-type requests.
---
## Trigger
One page type and its one template screenshot exist. A request naming two page types is two directives: pick one and diff against that template only. Quiet when no template exists.
## Done-when
check: state-diff
One program runs a real screenshot of the output (npx playwright screenshot) and exits 0 only when every assertion holds: the pixel diff against the one named template screenshot reports "off-template regions: 0" (any region fails, listed by locator), and the rendered spacing and type values read from the page each equal a token value in the token source file. No rendered page is a valid result: "unread", not a pass.
## Rung
rung: L0
A program alone: screenshot plus pixel diff. The diff, not a model, judges regions.
## Forbidden move
Judging a region on-template by looking at it instead of the diff, or waving through an off-template region.
## Tool
tool: Bash:playwright
scope: read
