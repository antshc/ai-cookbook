# Recipe: Question-Driven Telemetry, Correlation, and Actionable Alerts

## Problem

Indiscriminate logs and noisy alerts do not answer incident questions. Missing correlation or entry-point identity obstructs diagnosis, and unbounded metric labels overload telemetry systems.

## Example

**Task:** Instrument a scheduled job also callable through an API and CLI.

**AI Instructions:**

> 1. Write the on-call questions: whether runs succeed, where latency accumulates, and which entry point started a failed run.
> 2. Map each signal to a question; use structured stable events and propagate correlation ID and entry-point identity from the start through every hop.
> 3. Measure request rate, errors, and duration with bounded labels and latency histograms; keep high-cardinality identifiers in logs or traces.
> 4. Spot-check actual outputs for secrets and unredacted personal data; redact sensitive fields.
> 5. Create symptom-based alerts with runbook links and actionable thresholds. Test-fire each alert and verify notification delivery.
> 6. Induce a staging failure and locate it through telemetry alone; verify an unbroken trace and the responsible entry point.

## Best Practices

- Start from on-call questions.
- Propagate identity without unbounded metric labels.
- Test diagnosis and alert delivery.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/observability-and-instrumentation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/observability-and-instrumentation/SKILL.md):** Example 1, adapted from [skills/observability-and-instrumentation/SKILL.md, lines 91–91](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/observability-and-instrumentation/SKILL.md#L91-L91).
- **Addy Osmani — [skills/observability-and-instrumentation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/observability-and-instrumentation/SKILL.md):** Example 1, adapted from [skills/observability-and-instrumentation/SKILL.md, lines 228–236](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/observability-and-instrumentation/SKILL.md#L228-L236).
