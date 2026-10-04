# Shelf: motion-games-3d (motion, games, 3D; verbatim from the owner's spec)

## Short form
Motion, games, 3D. Still: one frame, one subject, score, no animate. Time: seek t, that frame only. Score: fix worst frame, rescore, full render waits. Asset: mesh, UV, rig, default rig first, one animation before import. Level: one change class, editor check, revert if path breaks. Engine: read project, name system, edit it, walk path.
Now: assisted. Tool success is not scene success. Max effort only on opening seconds.

## Directive definitions
Still. One frame. One subject. Score it. Do not animate yet.
Time. Seek a frame at a given t. Draw only that frame. Match the brief at that t. No full render in this directive.
Score. Score the contact sheet. Fix the worst frame only. Rescore. Full render waits for the threshold.
Asset. Build mesh, then UV, then rig. Play on the default rig before a custom one. Check one animation before import. Do not place it in the level yet.
Level. Change terrain or light or character or interaction, one of those. Validate in the editor. Revert if the path breaks. Tool success is not a pass.
Engine. Read the project before writing. Name the system you will touch. Edit that system. Walk the path after.

## Status and ceiling
* Still. Assisted. One frame, one subject is controllable. Scoring is still mostly human. Medium chance an automatic score is good enough for a first gate.
* Time. Assisted where the renderer is a function of t. That is a harness property. High chance inside that harness. Low chance inside a generic video generator.
* Score. Assisted. Fix-the-worst-frame works if the score is external. Medium chance.
* Asset. Assisted, stepwise. Mesh then rig then one animation is the working order. Bundled prompts break it. Medium chance.
* Level. Assisted and fragile. One change class per pass is necessary. Tool success still gets mistaken for scene success. Medium chance the editor check holds. Low chance unattended level building is reliable.
* Engine. Assisted via a connector. Read-then-edit works on a named system. Medium chance.
