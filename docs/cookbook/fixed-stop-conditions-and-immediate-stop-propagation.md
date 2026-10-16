# Recipe: Fixed Stop Conditions and Immediate Stop Propagation

## Problem

An autonomous loop can lower its completion bar or continue writing after an operator stop. Finish conditions and stop propagation must remain explicit.

## Example

**Task:** Run a task to a fixed verification predicate while retaining an immediate operator hold.

**AI Instructions:**

> 1. Define a checkable stop predicate before the first iteration.
> 2. Verify each iteration against that predicate and checkpoint progress.
> 3. Do not weaken the predicate after a plateau. Pivot the approach or report a real dead end.
> 4. On an operator stop, immediately issue a zero-writes hold to every active owner and child.
> 5. Confirm workers are held and start no replacement work.
> 6. Resume only after the operator releases the hold. Recheck current state before continuing.

## Best Practices

- Keep the completion predicate unchanged.
- Propagate stops immediately.
- Verify the hold across every active worker.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autonomous-run.md, lines 5–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autonomous-run.md#L5-L11).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autopilot-full.md, lines 11–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-full.md#L11-L11).
