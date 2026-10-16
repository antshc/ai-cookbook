# Recipe: Behavior-Preserving Refactoring and Protected Source Blocks

## Problem

Refactoring agents can mistake structural cleanup for permission to change behavior, delete intentional complexity, or rewrite protected performance-sensitive code. Pin the contract first, limit edits to proven cleanup, and mask protected blocks.

## Example

**Task:** Simplify a changed subsystem without altering its observable behavior or protected code.

**AI Instructions:**

> 1. Investigate why the current code exists. Identify inputs, outputs, side effects, error behavior, ordering, and integration boundaries.
> 2. Pin existing behavior with a characterization test, snapshot, or equivalence harness before moving structure. Do not treat type checks or lint as a behavior pin.
> 3. Mask annotated protected blocks with content-hashed placeholders and keep project-scoped backups. Restore each block from its verified placeholder or backup after edits.
> 4. Apply only unambiguous cleanup that preserves behavior and follows observed project conventions. Record ambiguous or behavior-changing candidates without applying them.
> 5. Move in small steps and keep the behavior pin green. Do not modify test expectations to force a pass.
> 6. Run focused unit and available functional-slice tests across every touched boundary. Confirm intended tests executed; treat missing proof as unverified.
> 7. Report the changed structure, preserved contract, exact verification, protected-block restoration, and unapplied findings.

## Best Practices

- Pin observable behavior before structural edits.
- Leave uncertain cleanup unapplied.
- Hide and restore protected blocks with verified placeholders.

## Related Recipes

- [Functional-Slice Tests, Observable Results, and Test Boundaries](functional-slice-tests-observable-results-and-test-boundaries.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [refactoring.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/refactoring.md):** Example 1, adapted from [refactoring.md, lines 3–16](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/refactoring.md#L3-L16).
- **Brain — [chorey.agent.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/plugins/crew/agents/chorey.agent.md):** Example 1, adapted from [chorey.agent.md, lines 37–49](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/plugins/crew/agents/chorey.agent.md#L37-L49).
- **Addy Osmani — [skills/code-simplification/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-simplification/SKILL.md):** Example 1, adapted from [skills/code-simplification/SKILL.md, lines 23–42](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-simplification/SKILL.md#L23-L42) and [lines 101–109](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-simplification/SKILL.md#L101-L109).
- **Addy Osmani — [hooks/SIMPLIFY-IGNORE.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/hooks/SIMPLIFY-IGNORE.md):** Example 1, adapted from [hooks/SIMPLIFY-IGNORE.md, lines 45–59](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/hooks/SIMPLIFY-IGNORE.md#L45-L59).
