# Recipe: Skill Validation, Proposal Checks, and Rejected-Change Ledgers

## Problem

Skill changes can introduce broken references, duplicate active work, or repeat ideas already rejected by evaluations. Validate structure and search durable proposal history before creating or changing a skill.

## Example

**Task:** Propose and validate a new or revised agent skill.

**AI Instructions:**

> 1. Search the skill catalog and skill directories for existing coverage. Prefer a focused extension when the responsibility already has an owner.
> 2. Search active proposals for overlapping work and the rejection ledger for earlier attempts and evaluation evidence.
> 3. State the uncovered gap and why an existing skill, open proposal, or rejected approach does not satisfy it.
> 4. Write an actionable workflow with verification. Remove model-specific workarounds and prose that does not change a decision.
> 5. Validate required frontmatter, referenced files, supporting assets, structural examples, and cross-skill links.
> 6. Run structural tests when behavior can be checked objectively and report skipped subjective checks.
> 7. When evaluation rejects a change, append the date, skill, attempted change, before-and-after score, proposal link, and outcome to the durable ledger in a separate default-branch update.

## Best Practices

- Search existing, active, and rejected work first.
- Validate every referenced artifact and structural contract.
- Preserve rejected evaluation evidence outside disposable branches.

## Related Recipes

- [Controlled Skill Evaluations, Observable Traces, and Repeated Trials](controlled-skill-evaluations-observable-traces-and-repeated-trials.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [authoring-a-skill.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md):** Example 1, adapted from [authoring-a-skill.md, lines 3–12](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md#L3-L12).
- **Addy Osmani — [CONTRIBUTING.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/CONTRIBUTING.md):** Example 1, adapted from [CONTRIBUTING.md, lines 9–20](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/CONTRIBUTING.md#L9-L20) and [lines 65–73](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/CONTRIBUTING.md#L65-L73).
