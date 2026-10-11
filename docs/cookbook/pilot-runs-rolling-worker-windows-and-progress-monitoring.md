# Recipe: Pilot Runs, Rolling Worker Windows, and Progress Monitoring

## Problem

Scaling before one full unit works multiplies failures. Whole-batch waits and narrative status also hide stalled workers.

## Example

**Task:** Scale a multi-agent migration after a complete pilot unit.

**AI Instructions:**

> 1. Run one unit through implementation, verification, and integration before increasing concurrency.
> 2. Use pilot evidence to refine briefs and acceptance checks.
> 3. Keep a bounded rolling worker window. Refill eligible slots as terminal results are drained.
> 4. Monitor commits, pushes, checks, and stored reports as progress rather than assurances.
> 5. Replace workers that exceed their expected runtime without side effects. Preserve their scope and reconcile late results.
> 6. Prefer event wakeups with a heartbeat fallback. Poll only when no useful event exists.

## Best Practices

- Prove the full lifecycle before scaling.
- Refill by readiness rather than waiting for batches.
- Judge progress from observable side effects.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/orchestrate.md, lines 62–63](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/orchestrate.md#L62-L63).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autopilot-stack.md, lines 6–6](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-stack.md#L6-L6).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autonomous-run.md, lines 5–6](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autonomous-run.md#L5-L6).
