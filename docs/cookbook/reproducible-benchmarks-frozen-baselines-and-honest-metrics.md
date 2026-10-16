# Recipe: Reproducible Benchmarks, Frozen Baselines, and Honest Metrics

## Problem

A speedup can measure skipped work, cached inputs, errors, or a saturated load generator. Benchmarks need fixed conditions and evidence that explains the number.

## Example

**Task:** Evaluate one optimization against a frozen baseline workload.

**AI Instructions:**

> 1. Freeze the workload, harness, metric, acceptance threshold, and baseline before iterating.
> 2. Use production-equivalent builds, flags, data, and tuning on both sides.
> 3. Run repeated alternating baseline and candidate measurements. Report variance as well as the central result.
> 4. Profile separately from reported timing runs. Identify the limiting resource and map it to source.
> 5. Rule out errors, skipped work, caching differences, generator saturation, and unequal scenarios.
> 6. Keep only improvements that exceed noise and preserve behavior. Revert unsupported iterations and record every attempt.
> 7. Label lab, field, and static-analysis findings accurately. Never invent performance scores without artifacts.

## Best Practices

- Compare equivalent workloads under fixed conditions.
- Explain the measured limiter.
- Keep evidence for retained and rejected optimizations.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-explain-the-number/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-explain-the-number/SKILL.md):** Example 1, adapted from [pstack/skills/principle-explain-the-number/SKILL.md, lines 9–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-explain-the-number/SKILL.md#L9-L11).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/hillclimb.md, lines 7–19](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/hillclimb.md#L7-L19).
- **Lauren Tan (poteto) — [pstack/skills/benchmark-checklist/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/benchmark-checklist/SKILL.md):** Example 1, adapted from [pstack/skills/benchmark-checklist/SKILL.md, lines 21–27](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/benchmark-checklist/SKILL.md#L21-L27).
- **Addy Osmani — [skills/performance-optimization/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/performance-optimization/SKILL.md):** Example 1, adapted from [skills/performance-optimization/SKILL.md, lines 255–259](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/performance-optimization/SKILL.md#L255-L259).
- **Addy Osmani — [agents/web-performance-auditor.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/agents/web-performance-auditor.md):** Example 1, adapted from [agents/web-performance-auditor.md, lines 168–178](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/agents/web-performance-auditor.md#L168-L178).
