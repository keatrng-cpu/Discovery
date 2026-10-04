---
name: harness-skill
description: Use when writing or fixing a Claude Code skill file so it has one trigger and one trick and stays quiet otherwise. Quiet for hooks, memory, logs, or harness promotion.
---
## Trigger
A SKILL.md is being authored or its description is being tuned. One trigger, one trick. Quiet when the ask is a hook, a memory store, a trace, or an evolve run, and quiet when no skill file is in scope.
## Done-when
check: exit-code
A fire test exits 0 only if all hold: the description has exactly one "Use when" clause (one trigger); the description and the Trigger section each contain "Quiet" followed by a stated quiet case; every positive prompt matches this description and every wrong-task prompt (at least one per sibling directive) does not. An empty positive set is not a pass: report "unsupported".
## Rung
rung: L1
One fast-model pass judges whether each prompt matches the description; a program counts the clauses and the matches. Not L0: matching is a judgment and no fire-test harness is registered.
## Forbidden move
Firing on the wrong task: a skill with two triggers, a broad description, or no stated quiet case. Writing a second trick into the same file instead of a second skill.
## Tool
tool: Bash:python3
scope: read
