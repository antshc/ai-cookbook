# Recipe: Verification Cost, Changed Scope, and Avoiding Redundant Runs

## Problem

Repeated green checks waste time while slow checks in the edit loop encourage bypasses. Verification must remain complete without rerunning unchanged work for reassurance.

## Example

**Task:** Arrange verification for an incremental implementation that includes slow mutation tests.

**AI Instructions:**

> 1. Run fast focused tests and static checks after each affected edit.
> 2. Place checks that take more than a few seconds outside the edit loop.
> 3. Scope expensive mutation checks to changed files. Run broader required gates at the appropriate commit or CI stage.
> 4. Record command, code revision, relevant inputs, and result.
> 5. Reuse a successful result only while those inputs remain unchanged.
> 6. Rerun after edits, configuration changes, or unresolved failures that could change the result. Do not repeat an identical clean run for reassurance.

## Best Practices

- Place checks by cost rather than deleting them.
- Invalidate saved results when their code or environment changes.
- Preserve required CI gates even when local checks are scoped.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/constraint-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md):** Example 1, adapted from [skills/constraint-driven-development/SKILL.md, lines 200–200](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md#L200-L200).
- **Addy Osmani — [skills/incremental-implementation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md):** Example 1, adapted from [skills/incremental-implementation/SKILL.md, lines 215–235](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md#L215-L235).
