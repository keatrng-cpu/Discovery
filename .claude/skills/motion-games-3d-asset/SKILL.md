---
name: motion-games-3d-asset
description: Use when a 3D asset is built stepwise as mesh, then UV, then rig, with one animation checked before import. Quiet for placing assets in a level.
---
## Trigger
A request to make or fix a mesh, UV, or rig asset. Quiet when the ask is to place the asset in a level or to bundle all stages in one prompt.
## Done-when
check: schema
`jq -e '(.stages==["mesh","uv","rig","animation"]) and (.rig.kind=="default") and (.clips|length)==1 and (.placed_in_level==false)' asset.json` exits 0. A manifest stopped at an earlier stage is valid when it lists only completed stages. The editor-side playback is not checked by a program today; it stays assisted.
## Rung
rung: L1
One fast-model pass produces the manifest for the current stage only; jq validates it. Escalate only if validation fails.
## Forbidden move
Bundling mesh, UV, rig and animation in one prompt, or importing or placing the asset in the level before one animation played on the default rig.
## Tool
tool: Bash:jq
scope: read
