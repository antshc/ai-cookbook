# Recipe: Quality Floors, Measurable Thresholds, and Controlled Exceptions

## Problem

An autonomous agent can ship work against an undefined quality bar, invent arbitrary thresholds, or apply an entire new lifecycle to a fragile legacy system at once. Quality constraints need a working baseline and controlled exceptions.

## Example

**Task:** Establish quality constraints for an existing project before unattended implementation.

**AI Instructions:**

> 1. Read project constraints, stack, test commands, CI, and current measurements before proposing thresholds.
> 2. If no constraints exist during a noninteractive run, apply the minimum floor: no new suppressions, unfinished stubs, unexplained skipped or deleted tests, secrets, or weakened checks. Report that choice and flag additional thresholds for a human.
> 3. Record agreed dimensions, measurable limits, reasons, tools, and execution stages in CONSTRAINTS.md. Use today's measured value as a ratchet when no justified target exists.
> 4. Keep quick checks in the edit loop and expensive checks at task end or CI; verify each declared command runs today.
> 5. Include at least one external quality signal and distinguish measured-only trends from blocking rules.
> 6. Adopt legacy checks incrementally, preserving behavior and adding characterization coverage before refactoring.
> 7. Record each accepted exception with scope, reason, owner, and expiry; link project instructions to the constraints and trial-run them on the current branch.

## Best Practices

- Measure a baseline before choosing thresholds.
- Enforce a minimum floor in unattended work.
- Introduce legacy gates incrementally and time-box exceptions.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/constraint-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md):** Example 1, adapted from [skills/constraint-driven-development/SKILL.md, lines 36–38](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md#L36-L38).
- **Addy Osmani — [skills/constraint-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md):** Example 1, adapted from [skills/constraint-driven-development/SKILL.md, lines 93–120](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md#L93-L120).
- **Addy Osmani — [skills/constraint-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md):** Example 1, adapted from [skills/constraint-driven-development/SKILL.md, lines 294–302](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md#L294-L302).
- **Addy Osmani — [docs/adoption-guide.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/adoption-guide.md):** Example 1, adapted from [docs/adoption-guide.md, lines 81–84](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/adoption-guide.md#L81-L84).
- **Addy Osmani — [docs/adoption-guide.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/adoption-guide.md):** Example 1, adapted from [docs/adoption-guide.md, lines 110–114](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/adoption-guide.md#L110-L114).
