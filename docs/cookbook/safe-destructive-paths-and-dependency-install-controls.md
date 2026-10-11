# Recipe: Safe Destructive Paths and Dependency Install Controls

## Problem

A well-formed cleanup path may still be attacker-selected, and dependency installation can execute unreviewed scripts before an audit. Both operations need checks before side effects.

## Example

**Task:** Prepare safe workspace cleanup and a reproducible dependency installation.

**AI Instructions:**

> 1. Resolve cleanup targets and symlinks. Require an allowlisted root, minimum depth, and ownership evidence before deletion.
> 2. Do not trust a caller-written ownership marker by itself. Refuse ambiguous targets without falling back to a broader path.
> 3. Account for changes between the ownership check and operation; use stronger ownership isolation when required.
> 4. Identify the installation boundary, manager, committed lockfile, and CI policy. Stop on conflicting evidence.
> 5. Disable dependency scripts before the first install. Inspect pending scripts and approve only the minimum needed.
> 6. Perform a clean frozen or immutable install and native audit against the committed lockfile. Keep the script policy enforced in CI.

## Best Practices

- Authorize destructive targets, not just their shape.
- Block scripts before they can execute.
- Audit the lockfile that the reproducible install actually uses.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/security-and-hardening/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md):** Example 1, adapted from [skills/security-and-hardening/SKILL.md, lines 115–119](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md#L115-L119).
- **Addy Osmani — [skills/security-and-hardening/references/hardening-patterns.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/references/hardening-patterns.md):** Example 1, adapted from [skills/security-and-hardening/references/hardening-patterns.md, lines 137–162](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/references/hardening-patterns.md#L137-L162).
- **Addy Osmani — [skills/security-and-hardening/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md):** Example 1, adapted from [skills/security-and-hardening/SKILL.md, lines 133–138](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md#L133-L138).
