# Recipe: Safe Feature Flags and Post-Rollout Cleanup

## Problem

Incomplete behavior can reach users without a safe default, while completed rollouts leave permanent flag branches that multiply test paths and maintenance work.

## Example

**Task:** Release an incomplete capability behind a temporary flag.

**AI Instructions:**

> 1. Keep the capability disabled by default while incomplete; verify existing behavior with the flag off.
> 2. Assign an owner, cleanup date, and criteria for flag retirement when creating it.
> 3. Enable for testing, then canary, then full rollout while checking user behavior and rollback ability.
> 4. Exercise both flag states until rollout is complete.
> 5. After the completion criteria hold, remove the flag, dead branches, obsolete tests, and configuration; verify the surviving path.

## Best Practices

- Create the flag before incomplete work becomes visible.
- Give every temporary flag a removal plan.
- Delete obsolete branches after rollout.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/ci-cd-and-automation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/ci-cd-and-automation/SKILL.md):** Example 1, adapted from [skills/ci-cd-and-automation/SKILL.md, lines 227–227](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/ci-cd-and-automation/SKILL.md#L227-L227).
- **Addy Osmani — [skills/incremental-implementation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md):** Example 1, adapted from [skills/incremental-implementation/SKILL.md, lines 215–222](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md#L215-L222).
