# Recipe: Independent Evidence-Based Review, Severity, and Reconciliation

## Problem

Reviewers can repeat the author's conclusion, file unsupported concerns, or turn a cohesive change into scattered edits. Review needs independent evidence, severity, and bounded reconciliation.

## Example

**Task:** Review a nontrivial caching patch against its thread-safety contract.

**AI Instructions:**

> 1. Read the tests and declared behavior before reviewing the implementation.
> 2. Give a fresh reviewer the artifact and contract without the author's conclusion or reasoning.
> 3. Inspect correctness, readability, architecture, security, and performance. Keep the change cohesive and inspect total file size as well as diff size.
> 4. Require a concrete code location, violated behavior, and evidence for each finding.
> 5. Label critical, required, optional, and nit findings. Lead with required changes.
> 6. Merge duplicate findings and record disagreements. Re-read the artifact before accepting or dismissing any result.
> 7. Classify contract misreads, actionable defects, accepted tradeoffs, and noise with reasons.
> 8. Fix actionable defects and re-review changed artifacts. Stop at the defined limit rather than repeating unchanged reviews.

## Best Practices

- Keep review independent of author confidence.
- Require evidence and severity for findings.
- Reconcile with judgment and bound the correction loop.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/interrogate/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate/SKILL.md):** Example 1, adapted from [pstack/skills/interrogate/references/reviewer-prompt.md, lines 43–43](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate/references/reviewer-prompt.md#L43-L43).
- **Lauren Tan (poteto) — [pstack/skills/interrogate/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate/SKILL.md):** Example 1, adapted from [pstack/skills/interrogate/SKILL.md, lines 42–51](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate/SKILL.md#L42-L51).
- **Addy Osmani — [skills/doubt-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/doubt-driven-development/SKILL.md):** Example 1, adapted from [skills/doubt-driven-development/SKILL.md, lines 53–59](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/doubt-driven-development/SKILL.md#L53-L59).
- **Addy Osmani — [skills/doubt-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/doubt-driven-development/SKILL.md):** Example 1, adapted from [skills/doubt-driven-development/SKILL.md, lines 75–106](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/doubt-driven-development/SKILL.md#L75-L106).
- **Addy Osmani — [skills/code-review-and-quality/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-review-and-quality/SKILL.md):** Example 1, adapted from [skills/code-review-and-quality/SKILL.md, lines 148–194](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-review-and-quality/SKILL.md#L148-L194).
- **Addy Osmani — [skills/code-review-and-quality/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-review-and-quality/SKILL.md):** Example 1, adapted from [skills/code-review-and-quality/SKILL.md, lines 109–113](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-review-and-quality/SKILL.md#L109-L113).
