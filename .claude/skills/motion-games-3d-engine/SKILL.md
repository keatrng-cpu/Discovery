---
name: motion-games-3d-engine
description: Use when a game engine project needs a change in one named system, read first, edited, then the path walked. Quiet without a project on disk.
---
## Trigger
An engine project (Unity, Unreal, Godot) on disk and a request to change one system. Quiet when no project is present or the system is unnamed.
## Done-when
check: state-diff
One program over systems.json (system name to file globs), read.json (the quote: system path, line number and line text) and git exits 0 only if: the quote is non-empty and its path matches the named system's globs; the quoted line text equals that line of the file at the pre-edit HEAD (git show HEAD:path), proving the read came before the write; and every path in git diff --name-only matches the named system's globs. The path walk is reported 'not run' because the connector is absent; no project or an unnamed system is unsupported, a valid result.
## Rung
rung: L1
One fast-model pass reads and edits the named system; the program confirms diff scope. Escalate only if the diff touches another system.
## Forbidden move
Writing before reading the project (no quoted system path and line in read.json before the first edit), or editing a system that was not named first.
## Tool
tool: Bash:git
scope: read
