# Recipe: Version-Matched Official Sources and Cache Revalidation

## Problem

An agent can apply an outdated API pattern or trust a stale documentation cache. Framework decisions need current, version-matched official evidence.

## Example

**Task:** Implement a framework-specific integration from official documentation.

**AI Instructions:**

> 1. Read dependency files to identify the installed framework and library versions.
> 2. Fetch official documentation for those versions before choosing framework-specific APIs.
> 3. Before reusing cached content across sessions, validate it with the origin's ETag or Last-Modified response.
> 4. Refetch when validation fails or the cached prompt-shaped interpretation does not fit the task. Do not cache origins without usable validators.
> 5. Cite the authoritative source beside nontrivial implementation decisions.
> 6. Surface documentation/code conflicts and label every unverifiable pattern explicitly.

## Best Practices

- Match sources to installed versions.
- Revalidate caches across sessions.
- Keep unverified decisions visibly labeled.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/source-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/source-driven-development/SKILL.md):** Example 1, adapted from [skills/source-driven-development/SKILL.md, lines 208–216](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/source-driven-development/SKILL.md#L208-L216).
- **Addy Osmani — [hooks/SDD-CACHE.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/hooks/SDD-CACHE.md):** Example 1, adapted from [hooks/SDD-CACHE.md, lines 156–160](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/hooks/SDD-CACHE.md#L156-L160).
