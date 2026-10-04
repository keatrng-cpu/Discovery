---
name: motion-games-3d-engine
description: Use when a game engine project needs a change in one named system, read first, edited, then the path walked. Quiet without a project on disk.
---
## Trigger
An engine project (Unity, Unreal, Godot) on disk and a request to change one system. Quiet when no project is present or the system is unnamed.
## Done-when
check: state-diff
A program reads `systems.json` (system name to file globs) and `git diff --name-only`, and exits 0 only if every changed path matches the named system's globs. One check: diff scope. Reading first is enforced by the Forbidden move (quote the system path and line before the first edit). The path walk needs an engine connector, which is absent; report "walk not run".
## Rung
rung: L1
One fast-model pass reads and edits the named system; the program confirms diff scope. Escalate only if the diff touches another system.
## Forbidden move
Writing before reading the project (no quoted system path and line before the first edit), or editing a system that was not named first.
## Tool
tool: Bash:git
scope: read
