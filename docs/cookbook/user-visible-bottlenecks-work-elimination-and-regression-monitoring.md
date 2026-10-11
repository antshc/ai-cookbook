# Recipe: User-Visible Bottlenecks, Work Elimination, and Regression Monitoring

## Problem

An agent can optimize a helper while users still wait on another bottleneck. Performance work must reduce the actual critical path and retain proof of gains.

## Example

**Task:** Improve a slow user-visible request path and prevent regression.

**AI Instructions:**

> 1. Measure the end-to-end path on representative data, hardware, and concurrency.
> 2. Profile the run and identify the actual limiting work before editing.
> 3. Try work elimination first, then reuse, reduction, deferral, concurrency, and cheaper execution.
> 4. Compare one change with the same baseline conditions and variance.
> 5. Record retained and rejected attempts. Revert changes without a measurable gain.
> 6. Install a synthetic budget or field monitor for the improved user-facing metric and preserve behavior checks.

## Best Practices

- Optimize what users wait for.
- Remove unnecessary work before making it cheaper.
- Monitor measured gains and record rejected ideas.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/perf-issue.md, lines 5–14](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/perf-issue.md#L5-L14).
- **Addy Osmani — [skills/performance-optimization/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/performance-optimization/SKILL.md):** Example 1, adapted from [skills/performance-optimization/SKILL.md, lines 255–267](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/performance-optimization/SKILL.md#L255-L267).
