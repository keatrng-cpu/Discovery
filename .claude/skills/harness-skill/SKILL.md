---
name: harness-skill
description: Use when writing or fixing a Claude Code skill file so it has one trigger and one trick and stays quiet otherwise. Quiet for hooks, memory, logs, or harness promotion.
---
## Trigger
A SKILL.md is being authored or its description is being tuned. One trigger, one trick. Quiet when the ask is a hook, a memory store, a trace, or an evolve run, and quiet when no skill file is in scope.
## Done-when
check: exit-code
`python3 lint_skill.py <SKILL.md> --wrong-task <prompts.txt>` exits 0 only if: the description has exactly one "Use when" clause (one trigger); Done-when holds exactly one "check:" line and one backticked command and Tool holds exactly one "tool:" line (one trick); the description and the Trigger section each contain "Quiet" followed by a stated quiet case; no sibling-task prompt in the prompts file matches the "Use when" clause and every positive prompt does (firing on the wrong task fails). A missing or empty file is unsupported, not a pass. The lint script is not written yet, so the check is not runnable today.
## Rung
rung: L0
A program alone: clause counts, line counts and a keyword match of each prompt against the "Use when" clause. No model reads the file.
## Forbidden move
Firing on the wrong task: a skill with two triggers, a broad description, or no stated quiet case. Writing a second trick (a second check command or tool) into the same file instead of a second skill.
## Tool
tool: Bash:python3
scope: read
