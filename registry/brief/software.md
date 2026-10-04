# Shelf: software (verbatim from the owner's spec)

## Short form
Software. Analyze: entry file from the failing path, invariant, files not to touch, log line. Reproduce: smallest failing command, pinned input, actual next to expected, red before any edit. Edit: named files only, signature stable unless the plan says otherwise, one-line note on non-obvious hunks, diff matches plan. Verify: named test, build, screenshot fixture, Stop hook. Migrate: tool enumerates files, one shape, isolated copies, reject unchecked. Review: quote line for logic, reach, and performance, drop unquoted comments. Onboard: one request entry to store, module per hop, one hop matched to a log, no tour.
Now: verify reliable. Reproduce reliable if a harness exists. Edit reliable once the plan is frozen. Review and onboard assisted.

## Directive definitions
Analyze. Locate the entry file from the failing path. Name the invariant the bug breaks. List files the change must not touch. Attach the log line that proves the map.
Reproduce. Write the smallest failing command. Pin the input that triggers it. Record the actual output next to the expected. Confirm the failure exists before any edit.
Edit. Change only the files named in the plan. Keep the public signature stable unless the plan says otherwise. Leave a one-line note on each non-obvious hunk. Stop when the diff matches the plan and nothing else.
Verify. Run the named test. Run the build. Compare the screenshot to the fixture. Block "done" until those three exit clean.
Migrate. Enumerate target files with a tool, not a guess. Transform one file shape only. Isolate each worker on its own copy. Reject a file whose result was not rechecked.
Review. Quote the line for a logic miss. Quote the line for a security reach. Quote the line for a performance path. Drop any comment that cannot point at a line.
Onboard. Trace one request from entry to store. Name the module that owns each hop. Match one hop to a runtime log. Stop after that flow. Do not tour the repo.

## Status and ceiling
Frontier agents now resolve a large majority of SWE-bench Verified issues. Public snapshots are not stable: a June 2026 table put the leader near 78%, later aggregators claim the mid-90s. Treat that as "in-benchmark issue fixing is mostly working," not as a precise rate. The mechanism is search, reproduce, edit, test, not a single completion.
* Analyze. Reliable. It greps the stack and the path, then names files. Fails when the log is noisy and the model guesses a file. By 2027 this stays reliable and gets cheaper, because it is a retrieval job.
* Reproduce. Reliable if a test harness exists. It writes the smallest command and keeps the red output. Weak in repos with no harness. High chance the missing-harness case is still the blocker in 2027.
* Edit. Assisted to reliable once the plan is frozen. It applies a constrained diff and stops when the diff matches. Drift is the failure. High chance a frozen plan plus a diff check is routine by 2027.
* Verify. Reliable. It runs the command and reads the exit code. This is already the highest-leverage directive. Stays reliable. The gain is making the hook mandatory, not a smarter model.
* Migrate. Assisted, ceiling on repeated transforms. Workers get isolated copies, a verifier rejects unchecked files. The Bun-scale port is real and rare. Medium chance ordinary migrations are routine by 2027. Low chance untested migrations become safe.
* Review. Assisted. It can quote a line. It still misses cross-file logic and over-comments. Medium chance quote-or-drop is reliable by 2027. The judgment of "is this a bug" stays assisted.
* Onboard. Assisted. It traces one path well and tours the repo if you let it. High chance a one-flow trace with a log match is reliable by 2027.
