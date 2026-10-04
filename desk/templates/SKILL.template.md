# SKILL.md format (the linter enforces it; the verifier checks it from the claims table only)

Path: .claude/skills/<shelf>-<directive>/SKILL.md   Name in frontmatter must equal <shelf>-<directive>.
At most 60 lines. Exactly these H2 sections in this order. Seed skills add one more at the end: "## Held-out check".
`check:` `rung:` `tool:` `scope:` (and `gate:` when gated) are parsed by code and must equal the registry entry.

--- worked example (a fake shelf "example"; copy the shape, not the words) ---

---
name: example-measure
description: Use when a part list needs its widths counted against a drawing. Quiet for ordering parts or for any task without the drawing in hand.
---
## Trigger
A drawing file and a part list are both present. Quiet when only one exists, or when the ask is to buy or ship.
## Done-when
check: count
`python3 tools/width_count.py parts.csv drawing.dxf` exits 0 and prints "widths: N/N matched". An empty part list is a valid result: it prints "widths: 0/0" and exits 0.
## Rung
rung: L1
A fast model reads the list; code does the count. Escalate only if the count tool exits non-zero for a reason other than a missing field.
## Forbidden move
Estimating a width the drawing does not state. Write "absent" instead.
## Tool
tool: Bash:python3
scope: read

--- worked example of a gated directive ---

## Tool
tool: none
scope: none
gate: ABSENT order, pay (prepare the purchase sheet, stop; a person places it)

--- registry entry shape (registry/shelf/<shelf>.json, under directives.<name>) ---
{"trigger": "...", "doneWhen": "...", "checkKind": "exit-code|quote|schema|state-diff|signature|count|human-only",
 "rung": "L0|L1|L2|L3|L4", "forbidden": "...", "tool": "<name in registry/tools.json or none>",
 "toolScope": "read|draft|act|none", "gated": false, "gate": "", "status": "reliable|assisted|weak|gated",
 "checkRunnable": false,   (true ONLY if a registered tool or an existing repo program under desk/ or fixtures/ can produce the check today; otherwise false)
 "keywords": ["3 or more lowercase task words that would appear when someone asks for exactly this directive"],
 "absentTools": ["names of tools that would turn this judgment into a check but are not connected"]}
