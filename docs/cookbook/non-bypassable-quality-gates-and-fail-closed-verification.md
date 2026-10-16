# Recipe: Non-Bypassable Quality Gates and Fail-Closed Verification

## Problem

An agent can reach green by weakening a threshold, skipping a test, or treating a guard failure as success. Quality gates must detect bypasses, fail closed, and return failures to the agent for correction.

## Example

**Task:** Protect an autonomous change with a quality-floor guard and blocking CI feedback.

**AI Instructions:**

> 1. Compare the working diff with the merge base, including staged, unstaged, deleted, and untracked files.
> 2. Block threshold reductions, removed assertions, skipped or deleted tests, new suppressions, unfinished stubs, and unapproved exceptions.
> 3. Return exit code 1 for a violation and exit code 2 when the guard cannot run. Never interpret either result as clean.
> 4. Run lint, type, test, build, security, and floor checks as non-bypassable CI gates.
> 5. Fix the implementation when a gate fails. Do not disable rules, skip tests, lower thresholds, or edit the guard to obtain green.
> 6. Feed the exact failure output back into the correction loop. Verify locally, push the fix, and rerun every failed gate.

## Best Practices

- Detect weakened checks and weakened evidence.
- Fail closed when verification cannot execute.
- Correct the change instead of silencing the gate.

## Related Recipes

- [Quality Floors, Measurable Thresholds, and Controlled Exceptions](quality-floors-measurable-thresholds-and-controlled-exceptions.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/constraint-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md):** Example 1, adapted from [skills/constraint-driven-development/SKILL.md, lines 202–216](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md#L202-L216).
- **Addy Osmani — [references/floor-guard.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/references/floor-guard.md):** Example 1, adapted from [references/floor-guard.md, lines 3–13](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/references/floor-guard.md#L3-L13).
- **Addy Osmani — [skills/ci-cd-and-automation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/ci-cd-and-automation/SKILL.md):** Example 1, adapted from [skills/ci-cd-and-automation/SKILL.md, line 54](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/ci-cd-and-automation/SKILL.md#L54) and [lines 164–190](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/ci-cd-and-automation/SKILL.md#L164-L190).
