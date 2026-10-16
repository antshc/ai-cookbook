# Recipe: Approved Specifications, Capability Dependencies, and Living Decisions

## Problem

Implementation drifts when agents plan before requirements are approved, hide module dependencies inside code, or leave changed decisions only in conversation. Gate each phase on an approved, versioned specification that stays current.

## Example

**Task:** Prepare a multi-capability initiative for implementation.

**AI Instructions:**

> 1. Detect independently testable capabilities from consumers, data, acceptance criteria, and replaceable scope.
> 2. Propose a compact capability map with stable module IDs, responsibilities, one-way dependencies, interface ownership, and build order.
> 3. Stop for human approval of module boundaries, dependency direction, and build order before writing module specifications.
> 4. Write one scoped specification per approved module with objectives, boundaries, testable success criteria, and open questions.
> 5. Save and summarize the specification, request approval, and stop. Do not plan or implement in the same turn.
> 6. Start planning only after later approval. Process modules in dependency order and trace every plan and pull request to its specification.
> 7. When a decision or scope changes, update and commit the specification before implementing the change.

## Best Practices

- Approve capability boundaries before module specifications.
- Separate specification approval from planning and coding.
- Update the living specification before changed implementation.

## Related Recipes

- [Clarify Intent, Surface Assumptions, and Challenge Scope](clarify-intent-surface-assumptions-and-challenge-scope.md)

## Sources & Attribution

Examples adapt the cited workflow. Task details illustrate its use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/spec-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/spec-driven-development/SKILL.md):** Example 1, adapted from [skills/spec-driven-development/SKILL.md, lines 38–65](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/spec-driven-development/SKILL.md#L38-L65), [lines 170–190](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/spec-driven-development/SKILL.md#L170-L190), and [lines 216–223](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/spec-driven-development/SKILL.md#L216-L223).
