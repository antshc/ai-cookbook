# Recipe: Architecture Decision Records, Alternatives, and Supersession

## Problem

A significant design choice can lose its constraints and rejected alternatives, forcing later engineers to repeat the debate. Deleting an old decision record erases the context for a changed architecture.

## Example

**Task:** Record a storage architecture decision and later replace it.

**AI Instructions:**

> 1. Inspect existing ADRs and repository instructions; match their location, naming sequence, format, and headings.
> 2. Describe the constraints and context that make the decision necessary.
> 3. State the selected option and compare credible alternatives with their advantages, drawbacks, and rejection reasons.
> 4. Record consequences, costs, risks, date, and current status; separate a proposal from an accepted decision.
> 5. When the architecture changes, create a new ADR linking and superseding the previous record.
> 6. Update the earlier ADR's status to point to its successor while preserving its original reasoning.

## Best Practices

- Match the repository's decision-record convention.
- Record alternatives and consequences.
- Supersede historical decisions instead of deleting them.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/documentation-and-adrs/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/documentation-and-adrs/SKILL.md):** Example 1, adapted from [skills/documentation-and-adrs/SKILL.md, lines 36–44](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/documentation-and-adrs/SKILL.md#L36-L44).
- **Addy Osmani — [skills/documentation-and-adrs/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/documentation-and-adrs/SKILL.md):** Example 1, adapted from [skills/documentation-and-adrs/SKILL.md, lines 50–100](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/documentation-and-adrs/SKILL.md#L50-L100).
