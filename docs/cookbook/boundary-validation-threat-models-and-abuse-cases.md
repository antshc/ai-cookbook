# Recipe: Boundary Validation, Threat Models, and Abuse Cases

## Problem

A feature can trust external or model-generated values without considering abuse paths. Validation and security policy belong at explicit system boundaries.

## Example

**Task:** Harden an API endpoint that accepts external requests and model-generated structured data.

**AI Instructions:**

> 1. Map assets, trust boundaries, actors, and external entry points before hardening.
> 2. Write abuse cases for authorization bypass, malformed data, injection, and excessive resource use.
> 3. Validate external and generated data against explicit schemas before it drives code or decisions.
> 4. Parse boundary representations into domain types and return safe errors.
> 5. Keep validated internal logic typed. Propagate errors without duplicating boundary validation everywhere.
> 6. Test allowed requests and abuse cases through the real protected boundary.

## Best Practices

- Threat-model before adding guards.
- Validate untrusted data at entry points.
- Keep domain internals separate from external representation.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-boundary-discipline/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-boundary-discipline/SKILL.md):** Example 1, adapted from [pstack/skills/principle-boundary-discipline/SKILL.md, lines 13–16](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-boundary-discipline/SKILL.md#L13-L16).
- **Addy Osmani — [skills/security-and-hardening/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md):** Example 1, adapted from [skills/security-and-hardening/SKILL.md, lines 205–216](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md#L205-L216).
