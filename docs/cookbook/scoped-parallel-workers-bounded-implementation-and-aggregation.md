# Recipe: Scoped Parallel Workers, Bounded Implementation, and Aggregation

## Problem

Parallel workers can duplicate effort, collide on files, or return claims the coordinator cannot combine. Each worker needs bounded scope and an evidence contract.

## Example

**Task:** Implement independent feature slices and run specialist reviews in parallel.

**AI Instructions:**

> 1. State the completion predicate and choose partitioned coverage, a race, or best-of selection before spawning.
> 2. Give each worker a standalone brief with bounded files, exact revisions, success checks, and its own writable output.
> 3. Parallelize independent implementation and review scopes. Serialize real shared-write invariants.
> 4. Use report-only subagents for independent findings. Use a communicating team when competing hypotheses require discussion.
> 5. Review each implementation diff and reject reports missing required revision or measurement evidence.
> 6. Aggregate findings and coverage gaps centrally. A missing required slice does not count as a pass.

## Best Practices

- Declare selection rules before seeing results.
- Give writes disjoint ownership.
- Keep evidence reconciliation with the coordinator.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/swarm/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/swarm/SKILL.md):** Example 1, adapted from [pstack/skills/swarm/SKILL.md, lines 22–42](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/swarm/SKILL.md#L22-L42).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/feature.md, lines 5–17](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/feature.md#L5-L17).
- **Addy Osmani — [references/orchestration-patterns.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/references/orchestration-patterns.md):** Example 1, adapted from [references/orchestration-patterns.md, lines 50–74](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/references/orchestration-patterns.md#L50-L74).
- **Addy Osmani — [references/orchestration-patterns.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/references/orchestration-patterns.md):** Example 1, adapted from [references/orchestration-patterns.md, lines 125–135](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/references/orchestration-patterns.md#L125-L135).
