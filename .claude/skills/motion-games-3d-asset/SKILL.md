---
name: motion-games-3d-asset
description: Use when a 3D asset is built stepwise as mesh, then UV, then rig, with one animation checked before import. Quiet for placing assets in a level.
---
## Trigger
A request to make or fix a mesh, UV, or rig asset. Quiet when the ask is to place the asset in a level or to bundle all stages in one prompt.
## Done-when
check: schema
`jq -e '(["mesh","uv","rig","animation"] as $o | .stages==$o[:(.stages|length)]) and (.imported==false) and (.placed_in_level==false) and (if (.stages|index("animation")) then (.rig.kind=="default") and (.animation.count==1) and (.animation.played_on=="default") else true end)' asset.json` exits 0. One schema over one manifest: stages must be an ordered prefix, so a manifest of only completed earlier stages is valid; the animation fields are required only once "animation" is listed; `imported` false means no import before the animation played. Editor playback is not program-checked; it stays assisted.
## Rung
rung: L1
One fast-model pass produces the manifest for the current stage only; jq validates it. Escalate only if validation fails.
## Forbidden move
Bundling mesh, UV, rig and animation in one prompt, or importing or placing the asset in the level before one animation played on the default rig.
## Tool
tool: Bash:jq
scope: read
