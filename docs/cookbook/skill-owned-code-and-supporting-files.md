# Recipe: Skill-Owned Code and Supporting Files

## Problem

Supporting code drifts when skills share copied helpers or edit generated module copies. Code ownership must match the scope of reuse.

## Example

**Task:** Add a parser helper for one skill and decide whether it belongs in shared infrastructure.

**AI Instructions:**

> 1. Keep skill-specific Python code inside the owning skill folder.
> 2. Place its tests in the repository's designated root test hierarchy.
> 3. Give logic shared within one plugin exactly one skill owner. Invoke that owner's contract instead of importing its private code.
> 4. Move code to the shared modules source only when more than one plugin consumes it.
> 5. Map every shared-module destination in the synchronization hook.
> 6. Edit authoritative source and regenerate destination copies. Do not patch synchronized copies directly.

## Best Practices

- Locate code by its actual consumers.
- Keep one authoritative implementation.
- Use repository test and synchronization conventions.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/structure-skill-owned-code.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-skill-owned-code.md):** Example 1, adapted from [docs/concepts/structure-skill-owned-code.md, lines 11–20](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-skill-owned-code.md#L11-L20).
