---
name: design-systems-tokens
description: Use when output must use design tokens read from a source file (Figma variables, tokens JSON, CSS custom properties). Quiet for ban lists, component lists, page templates, or style prose.
---
## Trigger
A token source file or design-file link is present and the ask is to style output with the system's values. Quiet when no source file exists: report "unsupported", do not guess values.
## Done-when
check: quote
Each token name used in the output is quoted with its source-file locator (file path and line, or Figma variable name from get_variable_defs) and the value that source states. A token name absent from the source fails, listed by name. An empty token set is a valid result: report "absent", never invent.
## Rung
rung: L1
One fast-model pass maps the output's styles to token names; the design-file read supplies the quoted source line. Escalate only if a quoted value disagrees with the source.
## Forbidden move
Sampling a hex or spacing value from a screenshot instead of reading the source file, or writing the hex where the token name belongs.
## Tool
tool: mcp__Figma__get_variable_defs
scope: read
