---
name: motion-games-3d-engine
description: Use when a game engine project needs a change in one named system, read first, edited, then the path walked. Quiet without a project on disk.
---
## Trigger
An engine project (Unity, Unreal, Godot) on disk and a request to change one system. Quiet when no project is present or the system is unnamed.
## Done-when
check: state-diff
Before any edit, the named system is quoted with file path and line. Afterward `git diff --name-only` lists only files of that system. The path walk needs an engine connector, which is absent; report "walk not run" rather than pass.
## Rung
rung: L1
One fast-model pass reads and edits the named system; git confirms the diff scope. Escalate only if the diff touches another system.
## Forbidden move
Writing before reading the project, or editing a system that was not named first.
## Tool
tool: Bash:git
scope: read
