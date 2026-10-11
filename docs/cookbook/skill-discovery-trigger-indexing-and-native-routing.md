# Recipe: Skill Discovery, Trigger Indexing, and Native Routing

## Problem

Hardcoded skill lists and duplicated routers miss new capabilities or select the wrong procedure. Discovery must use declared triggers across the full available roster.

## Example

**Task:** Route a documentation task through a discoverable skill family.

**AI Instructions:**

> 1. Write descriptions with when, responsibility, result, and distinctive user trigger words.
> 2. Discover family members across plugin, user, and repository scopes. Select by description and compatibility rather than a hardcoded list.
> 3. Report a missing required tool for the best match instead of silently skipping it.
> 4. For trigger indexes, match the supplied clauses semantically. Treat blank trigger cells as no match; do not infer triggers from titles.
> 5. Update index rows in the same change as their records and preserve unrelated columns.
> 6. Use the host's native skill activation when available. Do not install a second always-on router for the same task.

## Best Practices

- Keep one routing owner.
- Make discovery depend on declared capabilities.
- Keep indexes synchronized with their source records.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [.github/instructions/agent-skills.instructions.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/.github/instructions/agent-skills.instructions.md):** Example 1, adapted from [.github/instructions/agent-skills.instructions.md, lines 24–34](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/.github/instructions/agent-skills.instructions.md#L24-L34).
- **Brain — [docs/concepts/structure-cross-scope-skill-family.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-cross-scope-skill-family.md):** Example 1, adapted from [docs/concepts/structure-cross-scope-skill-family.md, lines 12–19](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-cross-scope-skill-family.md#L12-L19).
- **Brain — [docs/concepts/structure-trigger-indexer.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-trigger-indexer.md):** Example 1, adapted from [docs/concepts/structure-trigger-indexer.md, lines 12–20](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-trigger-indexer.md#L12-L20).
- **Addy Osmani — [docs/getting-started.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/getting-started.md):** Example 1, adapted from [docs/getting-started.md, lines 47–47](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/getting-started.md#L47-L47).
