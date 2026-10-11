# Recipe: Bounded Agent Roles, Single Ownership, and Composition

## Problem

Generic agents and overlapping skills create unclear ownership and conflicting edits. Each role needs one deliverable, bounded authority, and explicit composition.

## Example

**Task:** Define a feature implementer and a behavior-preserving reviewer.

**AI Instructions:**

> 1. Give each agent a concrete deliverable, file scope, expertise, autonomy level, forbidden actions, and output format.
> 2. Assign one owner for each patch, branch, and shared procedure.
> 3. Keep role orchestration and judgment in the agent. Invoke the owning skill for specialized work.
> 4. Keep one-use behavior local and shared behavior under exactly one owner.
> 5. Keep the exploration engine independent of passenger skills. Do not nest it inside its own delegated workflow.
> 6. Record delegation boundaries and review returned work before aggregation.

## Best Practices

- Describe deliverables rather than vague personas.
- Invoke owners instead of copying procedures.
- Separate responsibilities and shared-write authority.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/structure-agents-style.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-agents-style.md):** Example 1, adapted from [docs/concepts/structure-agents-style.md, lines 11–23](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-agents-style.md#L11-L23).
- **Brain — [docs/concepts/structure-skill-composition.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-skill-composition.md):** Example 1, adapted from [docs/concepts/structure-skill-composition.md, lines 12–55](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-skill-composition.md#L12-L55).
- **Brain — [docs/adr/explore-codebase-is-skill-agnostic.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/explore-codebase-is-skill-agnostic.md):** Example 1, adapted from [docs/adr/explore-codebase-is-skill-agnostic.md, lines 7–10](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/explore-codebase-is-skill-agnostic.md#L7-L10).
- **Addy Osmani — [docs/agents.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/agents.md):** Example 1, adapted from [docs/agents.md, lines 119–123](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/agents.md#L119-L123).
