---
name: audio-cut
description: Use when one named region of one take needs tightening (trim a pause, drop a filler) and the rest kept. Quiet for restitching an episode, naming, or music work.
---
## Trigger
One take file and one region given as start and end times. Quiet when the ask spans the whole episode, reorders takes, or has no region bounds.
## Done-when
check: state-diff
One python3 check script, with the take before and after plus a listen-note file for the region as inputs, exits 0 only if: the same take file is kept (no new take), every sample outside the region bounds is byte-identical (prints "outside-region: N/N samples unchanged"), the region itself is the only part tightened (duration change reported in seconds), and the listen-note file records a person listening to that region (prints "listen: region noted"). The script is not in the repo yet; the desk would run it. A cut that declines to change the region is a valid result.
## Rung
rung: L1
One fast-model pass picks the trim points inside the region; code does the diff (the L1 pass is the judgment, the diff is the only check). Escalate only if the diff shows a changed sample outside the region.
## Forbidden move
Restitching the episode: changing, moving, or re-joining anything outside the named region, or re-rendering the whole take to make the cut.
## Tool
tool: Bash:python3
scope: read
