# Recipe: Consumer Migration, Safe Deprecation, and Legacy Retirement

## Problem

A migration can leave duplicate APIs and adapters indefinitely, or delete an interface while consumers still depend on it. Internal rewrites and public retirement need explicit consumer evidence.

## Example

**Task:** Migrate an internal API and retire the externally consumed predecessor.

**AI Instructions:**

> 1. Define the target contract and inventory internal and external consumers.
> 2. For a planned internal rewrite, migrate callers and remove obsolete APIs and tests together; time-box any necessary adapter.
> 3. Declare acceptable intermediate breakage and keep high-signal checks on touched areas. Require full static and runtime checks at completion.
> 4. Provide external consumers a production-proven replacement and concrete migration guide. Start with advisory deprecation and measure remaining usage.
> 5. Migrate downstream consumers and verify their new behavior; do not add features to the deprecated system.
> 6. Delete the externally consumed interface only after metrics and logs show no active consumers; remove old tests, configuration, references, and notices.

## Best Practices

- Distinguish controlled internal migration from public retirement.
- Verify the final state, including consumer behavior.
- Require usage evidence before external deletion.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md):** Example 1, adapted from [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md, lines 11–15](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md#L11-L15).
- **Lauren Tan (poteto) — [pstack/skills/principle-outcome-oriented-execution/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-outcome-oriented-execution/SKILL.md):** Example 1, adapted from [pstack/skills/principle-outcome-oriented-execution/SKILL.md, lines 17–21](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L17-L21).
- **Addy Osmani — [skills/deprecation-and-migration/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/deprecation-and-migration/SKILL.md):** Example 1, adapted from [skills/deprecation-and-migration/SKILL.md, lines 235–240](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/deprecation-and-migration/SKILL.md#L235-L240).
