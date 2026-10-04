---
name: design-systems-ban-list
description: Use when output must be failed for containing named banned patterns (a short ban list tested in code). Quiet for taste judgments, token lookups, or component selection.
---
## Trigger
A named ban list exists, shorter than the design system, and output must pass it. Quiet when asked to ban taste or style opinions; those are not testable.
## Done-when
check: exit-code
`pytest` over one test per banned pattern exits 0 on the output; any hit exits non-zero and names the pattern. A banned pattern with no test is not on the list. An empty ban list is a valid result: report "no bans", exit 0.
## Rung
rung: L0
A program alone matches the patterns. No model pass. Escalate only if a test itself errors, not when output fails it.
## Forbidden move
Enforcing the ban list by instruction in the prompt, or banning taste, so the fail is a plea rather than a test.
## Tool
tool: Bash:pytest
scope: read
