# Recipe: Additive Schema Migration and Tested Rollback

## Problem

A schema rename or drop can break older application instances during rollout. Unbounded backfills can lock production tables, and an untested down migration leaves recovery uncertain.

## Example

**Task:** Plan a database column replacement that remains compatible during deployment.

**AI Instructions:**

> 1. Add the new nullable column in its own migration; keep the old shape available to running consumers.
> 2. Backfill in bounded, throttled batches off the hot path; build large indexes without blocking writes using the database's supported mechanism.
> 3. Deploy compatible code and use a feature flag for a risky cutover.
> 4. Write and run the down migration before merging; record data-loss constraints and demonstrate the supported rollback.
> 5. Verify no deployed code references the old shape.
> 6. Drop the old column in a separate later deploy after compatibility and recovery checks pass.

## Best Practices

- Expand first; contract only after consumer migration.
- Test rollback before deployment.
- Bound backfills and index impact.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/deprecation-and-migration/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/deprecation-and-migration/SKILL.md):** Example 1, adapted from [skills/deprecation-and-migration/SKILL.md, lines 185–190](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/deprecation-and-migration/SKILL.md#L185-L190).
