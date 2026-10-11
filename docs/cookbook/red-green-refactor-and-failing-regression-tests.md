# Recipe: Red-Green-Refactor and Failing Regression Tests

## Problem

A test written after a fix may pass without detecting the original bug. Behavior changes need failing-before evidence, a minimal implementation, and preserved checks during cleanup.

## Example

**Task:** Fix a search bug caused by task titles containing special characters.

**AI Instructions:**

> 1. Write a focused search regression test with a literal expected title containing quotes and brackets.
> 2. Run it before editing production code. Confirm failure is caused by the reported search behavior.
> 3. Correct the reproduction if the test passes or fails for setup reasons.
> 4. Make the smallest implementation change that passes the test.
> 5. Refactor with the behavior and assertions unchanged. Rerun the focused test after affected edits.
> 6. Run required regression gates. Report failing-before and passing-after commands and results.

## Best Practices

- Observe the red result rather than assuming the test would fail.
- Keep expectations independent of the implementation.
- State any missing failing-before evidence explicitly.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/tdd/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/tdd/SKILL.md):** Example 1, adapted from [pstack/skills/tdd/SKILL.md, lines 15–20](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/tdd/SKILL.md#L15-L20).
- **Addy Osmani — [skills/test-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md):** Example 1, adapted from [skills/test-driven-development/SKILL.md, lines 40–47](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md#L40-L47).
- **Addy Osmani — [skills/test-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md):** Example 1, adapted from [skills/test-driven-development/SKILL.md, lines 100–117](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md#L100-L117).
