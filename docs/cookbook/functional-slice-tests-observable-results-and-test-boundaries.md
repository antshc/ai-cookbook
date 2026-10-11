# Recipe: Functional-Slice Tests, Observable Results, and Test Boundaries

## Problem

Tests can confirm internal calls while the user-visible result is wrong. A change that crosses storage or service boundaries needs a focused functional slice at a real observable seam.

## Example

**Task:** Test a search fix that must return task titles containing quotes and brackets.

**AI Instructions:**

> 1. Trace the request through search logic, storage access, and response formatting.
> 2. Select the highest existing observable test seam that exercises the affected slice.
> 3. Create a task titled Fix quotes and brackets. Search for quotes and assert the exact returned title and result count.
> 4. Assert resulting state and output. Mock only external boundaries that the repository already isolates.
> 5. Classify test size by resources: pure in-process logic, localhost integration, or external end-to-end flow.
> 6. Follow neighboring test names, setup, wrappers, and commands. Run the smallest checks that prove the slice and required repository gates.

## Best Practices

- Assert literal expected results rather than truthiness or internal calls.
- Use integration checks when the changed slice crosses a real boundary.
- Preserve repository test conventions and state isolation.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/adr/crew-is-agnostic.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/crew-is-agnostic.md):** Example 1, adapted from [docs/adr/crew-is-agnostic.md, lines 13–19](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/crew-is-agnostic.md#L13-L19).
- **Lauren Tan (poteto) — [pstack/skills/principle-test-behavior-not-implementation/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-test-behavior-not-implementation/SKILL.md):** Example 1, adapted from [pstack/skills/principle-test-behavior-not-implementation/SKILL.md, lines 9–17](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L9-L17).
- **Addy Osmani — [skills/test-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md):** Example 1, adapted from [skills/test-driven-development/SKILL.md, lines 26–34](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md#L26-L34).
- **Addy Osmani — [skills/test-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md):** Example 1, adapted from [skills/test-driven-development/SKILL.md, lines 163–173](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md#L163-L173).
- **Addy Osmani — [skills/test-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md):** Example 1, adapted from [skills/test-driven-development/SKILL.md, lines 190–209](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md#L190-L209).
