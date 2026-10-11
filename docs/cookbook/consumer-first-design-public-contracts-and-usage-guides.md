# Recipe: Consumer-First Design, Public Contracts, and Usage Guides

## Problem

An implementation can be convenient internally but painful for callers. Public contracts need to start from actual usage and preserve observable behavior.

## Example

**Task:** Design a shared search API from the consumer's intended workflow.

**AI Instructions:**

> 1. Write the consumer usage guide and example call before implementation.
> 2. Name expected inputs, outputs, errors, and observable side effects.
> 3. Derive types and signatures from the usage sketch.
> 4. Compare API choices by caller effort and the experience they enable.
> 5. Treat existing observable behavior as a consumer dependency, including undocumented behavior.
> 6. Verify contract examples against the implementation and update the guide when the contract changes.

## Best Practices

- Start with the consumer path.
- Define public contracts before code.
- Preserve observable behavior or provide an explicit migration.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-experience-first/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-experience-first/SKILL.md):** Example 1, adapted from [pstack/skills/principle-experience-first/SKILL.md, lines 9–19](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-experience-first/SKILL.md#L9-L19).
- **Lauren Tan (poteto) — [pstack/skills/architect/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md):** Example 1, adapted from [pstack/skills/architect/SKILL.md, lines 79–79](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md#L79-L79).
- **Lauren Tan (poteto) — [pstack/skills/poteto-help/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-help/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-help/references/prompting.md, lines 30–30](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-help/references/prompting.md#L30-L30).
- **Addy Osmani — [skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/api-and-interface-design/SKILL.md):** Example 1, adapted from [skills/api-and-interface-design/SKILL.md, lines 325–336](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/api-and-interface-design/SKILL.md#L325-L336).
