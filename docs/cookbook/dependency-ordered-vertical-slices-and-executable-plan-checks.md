# Recipe: Dependency-Ordered Vertical Slices and Executable Plan Checks

## Problem

Large plans fail when tasks are ordered by technical layer, omit proof, or depend on prose review alone. Sequence independently verifiable vertical slices by dependency and validate the plan mechanically before execution.

## Example

**Task:** Turn an approved specification into an executable multi-phase delivery plan.

**AI Instructions:**

> 1. Stay read-only during planning. Inspect the approved specification, relevant code, conventions, dependencies, risks, and unknowns; do not implement.
> 2. Map the dependency graph and order foundational work before dependents.
> 3. Slice work into the smallest end-to-end user-visible capabilities instead of database, API, and UI layers.
> 4. Make every slice independently landable. State its files or boundaries, acceptance criteria, test, live verification, and commit gate.
> 5. Order commits and pull requests so each state proves the next: baseline before change, failing test before fix, or subtraction before reshape.
> 6. Run the repository's executable plan checker and fix every reported defect before handoff.
> 7. During execution, implement one slice, test it, verify the real behavior, commit it, and only then start the next slice.
> 8. Report the plan path, dependency order, checker output, and evidence required for each slice.

## Best Practices

- Order work by real dependencies.
- Deliver complete vertical behavior in each slice.
- Validate plan structure mechanically before handoff.

## Related Recipes

- [Approved Specifications, Capability Dependencies, and Living Decisions](approved-specifications-capability-dependencies-and-living-decisions.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [principle-sequence-verifiable-units](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-sequence-verifiable-units/SKILL.md):** Example 1, adapted from [SKILL.md, lines 7–15](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L7-L15).
- **Lauren Tan (poteto) — [multi-phase-plan.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md):** Example 1, adapted from [multi-phase-plan.md, lines 3–13](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L3-L13).
- **Addy Osmani — [skills/planning-and-task-breakdown/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md):** Example 1, adapted from [skills/planning-and-task-breakdown/SKILL.md, lines 24–77](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md#L24-L77).
- **Addy Osmani — [skills/incremental-implementation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md):** Example 1, adapted from [skills/incremental-implementation/SKILL.md, lines 36–64](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md#L36-L64).
