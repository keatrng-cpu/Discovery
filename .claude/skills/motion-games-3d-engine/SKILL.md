---
name: motion-games-3d-engine
description: Use when a game engine project needs a change in one named system, read first, edited, then the path walked. Quiet without a project on disk.
---
## Trigger
An engine project (Unity, Unreal, Godot) on disk and a request to change one system. Quiet when no project is present or the system is unnamed.
## Done-when
check: state-diff
A program reads systems.json (system name to its file globs), read.json (the pre-edit quote: system path and line, recorded before the first edit) and the output of git diff --name-only, and exits 0 only if the quoted path matches the named system's globs, the quote is non-empty, and every changed path matches the named system's globs; the path walk is reported 'not run' because the connector is absent. One check: read-then-edit scope on the named system.
## Rung
rung: L1
One fast-model pass reads and edits the named system; the program confirms diff scope. Escalate only if the diff touches another system.
## Forbidden move
Writing before reading the project (no quoted system path and line in read.json before the first edit), or editing a system that was not named first.
## Tool
tool: Bash:git
scope: read
