# Recipe: Safe Pause, Context Recovery, and Verified Resume

## Problem

A resumed agent can repeat finished work or overwrite newer state. Safe interruption needs a durable checkpoint and a verified restart position.

## Example

**Task:** Pause an implementation before context loss, then resume from its checkpoint.

**AI Instructions:**

> 1. Finish or back out of the current atomic step. Start no new work and stop child workers.
> 2. Persist edits in a clear checkpoint commit under the existing authorization. Record broken checks explicitly.
> 3. Save intent, decisions, verified results, pending work, branch, key paths, and gotchas outside conversation context.
> 4. On resume, read the scoped prior trail and current Git state.
> 5. Compare delivered work with the plan. Check for intervening changes before using saved results.
> 6. Name the next pending step. Do not repeat unchanged reproduction or completed checks without a reason.

## Best Practices

- Pause at an atomic boundary.
- Keep recovery scoped to the active workspace.
- Treat the trail as evidence and validate it against current state.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/pause-safely.md, lines 5–8](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/pause-safely.md#L5-L8).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/session-pickup.md, lines 5–9](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/session-pickup.md#L5-L9).
- **Lauren Tan (poteto) — [pstack/skills/recall/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/recall/SKILL.md):** Example 1, adapted from [pstack/skills/recall/SKILL.md, lines 17–22](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/recall/SKILL.md#L17-L22).
