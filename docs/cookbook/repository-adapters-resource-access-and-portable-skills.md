# Recipe: Repository Adapters, Resource Access, and Portable Skills

## Problem

Repository bindings and vendor controls can leak into portable skills. Installation can also lose shared references or let equivalent command adapters drift.

## Example

**Task:** Install a reusable ticket workflow in a repository with project-specific tracker fields.

**AI Instructions:**

> 1. Discover tracker variants and required fields from the live target.
> 2. Generate a repository-local adapter that resolves bound data and invokes the shared owner's action. Do not copy the workflow.
> 3. Access the tracker through the owning resource-access boundary.
> 4. Install reusable skills and project-specific instructions without copying the source repository's contributor AGENTS file.
> 5. Include required shared checklists inside the distributed skill or use a whole-repository integration. Verify all references resolve.
> 6. Keep vendor runtime controls in per-agent adapters or permitted metadata.
> 7. Validate equivalent host command adapters for semantic parity after edits.

## Best Practices

- Keep repository data at the adapter edge.
- Package required supporting references.
- Separate portable procedures from vendor runtime controls.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/structure-repository-adapter-skill.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-repository-adapter-skill.md):** Example 1, adapted from [docs/concepts/structure-repository-adapter-skill.md, lines 14–21](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-repository-adapter-skill.md#L14-L21).
- **Brain — [docs/concepts/structure-resource-access-skill.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-resource-access-skill.md):** Example 1, adapted from [docs/concepts/structure-resource-access-skill.md, lines 5–8](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-resource-access-skill.md#L5-L8).
- **Addy Osmani — [AGENTS.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/AGENTS.md):** Example 1, adapted from [AGENTS.md, lines 5–5](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/AGENTS.md#L5-L5).
- **Addy Osmani — [docs/getting-started.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/getting-started.md):** Example 1, adapted from [docs/getting-started.md, lines 163–169](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/getting-started.md#L163-L169).
- **Addy Osmani — [docs/advanced-per-agent-configuration.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/advanced-per-agent-configuration.md):** Example 1, adapted from [docs/advanced-per-agent-configuration.md, lines 11–14](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/advanced-per-agent-configuration.md#L11-L14).
- **Addy Osmani — [docs/developer-onboarding.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/developer-onboarding.md):** Example 1, adapted from [docs/developer-onboarding.md, lines 100–107](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/developer-onboarding.md#L100-L107).
