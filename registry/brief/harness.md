# Shelf: harness (harness design; verbatim from the owner's spec)

## Short form
Harness. Skill: one trigger, quiet otherwise, wrong-fire fails. Hook: lifecycle, exit 2 blocks. Memory: stage key analyze, reproduce, edit, verify. Trace: append-only, tamper fails. Evolve: one change, held-out task, token count. Agent does not promote itself.

## Directive definitions
Skill. One trigger. One trick. State when it must stay quiet. Fire-on-wrong-task fails.
Hook. Bind to a lifecycle event. Exit code blocks. Confirm it fires when the model would have continued.
Memory. Store at the stage: analyze, reproduce, edit, or verify. Retrieve by stage, not by similar story. Episode blobs fail.
Trace. Append-only log. A tamper attempt fails. The agent does not get a delete on its own record.
Evolve. Change one harness piece. Run a held-out task. Publish the token count. A gain only on the tuning set does not promote.

## Status and ceiling
This shelf moves faster than the model shelf. Epoch estimates hardware shipped through 2027 could run tens to hundreds of millions of concurrent frontier agents, or on the order of a billion cheaper ones. That is capacity, not correctness. Gartner expects most new applications to be short-lived by 2029, which fits a harness that is rewritten often.
* Skill. Reliable as a file that loads on match. Fire-on-wrong-task is a test you can write. High chance.
* Hook. Reliable. Exit code blocking is already how the strong coding setups work. Stays reliable.
* Memory. Assisted. Subtask-level memory has a measured gain on coding benchmarks. Episode blobs remain the default in the wild. Medium-high chance the stage key wins.
* Trace. Weak in current local agents, which have been shown able to alter their own logs. Append-only is a tool property. Medium chance it is standard. It will not come from the model behaving.
* Evolve. Assisted and dangerous. Held-out gains are smaller than in-sample gains. Low chance self-evolved harnesses promote themselves safely. Medium chance a human-gated held-out check is normal.
