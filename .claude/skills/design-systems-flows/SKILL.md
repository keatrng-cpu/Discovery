---
name: design-systems-flows
description: Use when one page type must be built from a template and checked by a visual diff. Quiet for single tokens, component lists, or multi-page-type requests.
---
## Trigger
One page type and its one template screenshot exist. A request naming two page types is two directives: pick one and diff against that template only. Quiet when no template exists.
## Done-when
check: state-diff
A real screenshot of the output (npx playwright screenshot) is diffed against the one named template screenshot; the diff reports "off-template regions: 0". Spacing and type are held to the template: the template renders token spacing and type, so any deviation in either appears as an off-template region. Any off-template region fails, listed by locator. No rendered page is a valid result: "unread", not a pass.
## Rung
rung: L0
A program alone: screenshot plus pixel diff. The diff, not a model, judges regions.
## Forbidden move
Judging a region on-template by looking at it instead of the diff, or waving through an off-template region.
## Tool
tool: Bash:playwright
scope: read
