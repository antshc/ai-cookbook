# Recipe: Least-Privilege Tool Restrictions versus Preapproval

## Problem

A preapproved tool can still be available to an agent that should never use it. Reduced prompting is not least privilege.

## Example

**Task:** Configure a review worker that must inspect code without write access.

**AI Instructions:**

> 1. List the operations required for review and the operations that must be unavailable.
> 2. Check the host's actual capability controls rather than relying on a field's name.
> 3. Use runtime tool restrictions to remove forbidden capabilities. Treat preapproval only as permission-prompt behavior.
> 4. Keep vendor-specific controls in the host adapter or local agent definition.
> 5. Verify the worker can read the artifact and cannot perform forbidden writes.
> 6. Recheck restriction lifetime across new messages or sessions.

## Best Practices

- Distinguish prompt suppression from capability removal.
- Verify restrictions in the runtime.
- Keep vendor controls outside portable skill frontmatter.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [docs/advanced-per-agent-configuration.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/advanced-per-agent-configuration.md):** Example 1, adapted from [docs/advanced-per-agent-configuration.md, lines 24–32](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/advanced-per-agent-configuration.md#L24-L32).
- **Addy Osmani — [docs/advanced-per-agent-configuration.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/advanced-per-agent-configuration.md):** Example 1, adapted from [docs/advanced-per-agent-configuration.md, lines 38–41](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/advanced-per-agent-configuration.md#L38-L41).
