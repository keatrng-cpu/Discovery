---
name: harness-skill
description: Use when writing or fixing a Claude Code skill file so it has one trigger and one trick and stays quiet otherwise. Quiet for hooks, memory, logs, or harness promotion.
---
## Trigger
A SKILL.md is being authored or its description is being tuned. One trigger, one trick. Quiet when the ask is a hook, a memory store, a trace, or an evolve run, and quiet when no skill file is in scope.
## Done-when
check: exit-code
A fire test exits 0: every positive prompt matches this skill's description and every wrong-task prompt (at least one per sibling directive) does not. The skill states in its text when it must stay quiet. A skill that fires on a wrong-task prompt exits non-zero. An empty positive set is not a pass: report "unsupported".
## Rung
rung: L0
A program alone runs the fire test. No model pass is needed to count matches. Escalate only if the test cannot be written.
## Forbidden move
Firing on the wrong task: a skill with two triggers, a broad description, or no stated quiet case. Writing a second trick into the same file instead of a second skill.
## Tool
tool: Bash:python3
scope: read
