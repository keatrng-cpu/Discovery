---
name: design-systems-tokens
description: Use when output must use design tokens read from a source file (Figma variables, tokens JSON, CSS custom properties). Quiet for ban lists, component lists, page templates, or style prose.
---
## Trigger
A token source file or design-file link is present and the ask is to style output with the system's values. Quiet when no source file exists: report "unsupported", do not guess values.
## Done-when
check: quote
A program reads the source file and, for each token name used in the output, prints the name, its source locator (file path and line, or Figma variable name from get_variable_defs) and the value the source states. It exits non-zero and lists by name any token absent from the source, any token whose value in the output differs from the source value, and any raw hex or literal spacing value in the output where a token name belongs. An empty token set is a valid result: report "absent", never invent.
## Rung
rung: L0
A program alone: id lookup of each token name against the source locator and value, plus a scan for raw hex. No model pass.
## Forbidden move
Sampling a hex or spacing value from a screenshot instead of reading the source file, or writing the hex where the token name belongs.
## Tool
tool: mcp__Figma__get_variable_defs
scope: read
