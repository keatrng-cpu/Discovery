---
name: design-systems-ban-list
description: Use when output must be failed for containing named banned patterns (a short ban list tested in code). Quiet for taste judgments, token lookups, or component selection.
---
## Trigger
A named ban list exists, shorter than the design system, and output must pass it. Quiet when asked to ban taste or style opinions; those are not testable.
## Done-when
check: exit-code
One pytest command over the ban-list test file and the system's token or component list exits 0 only when every assertion holds: one test per banned pattern passes on the output (a hit names the pattern), a banned pattern with no test is not on the list, and the count of banned patterns is below the count of entries in the system. An empty ban list is a valid result: report "no bans", exit 0.
## Rung
rung: L0
A program alone: pytest runs the per-pattern tests. No model pass.
## Forbidden move
Enforcing the ban list by instruction in the prompt, or banning taste, so the fail is a plea rather than a test.
## Tool
tool: Bash:pytest
scope: read
