# Recipe: Session Ledger, Open Questions, and Restartable Handoffs

## Problem

Long sessions lose open decisions, source-reading history, and exact verification state. A restartable handoff needs a durable task ledger and visible unresolved questions.

## Example

**Task:** Checkpoint a multi-step implementation so a fresh agent can continue safely.

**AI Instructions:**

> 1. Record accepted scope, decisions, completed work, and the next pending task in the project-designated plan or tracker.
> 2. Record each opened architecture document and its topic in a lazily created session ledger. Consult it before rescanning modules.
> 3. Mark unresolved facts and choices inline. Explain options, costs, recommendation, and the effect of no answer.
> 4. Save changed paths, branch and working-tree state, exact checks and results, risks, and required approvals.
> 5. Link the authoritative artifacts instead of copying large content.
> 6. Write a concrete resume point and verify the handoff is accessible outside the current conversation.

## Best Practices

- Use the designated task store.
- Distinguish unresolved questions from settled decisions.
- Keep evidence and resume steps durable.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/str-open-question-marker.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/str-open-question-marker.md):** Example 1, adapted from [docs/concepts/str-open-question-marker.md, lines 20–20](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/str-open-question-marker.md#L20-L20).
- **Brain — [docs/concepts/structure-ledger.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-ledger.md):** Example 1, adapted from [docs/concepts/structure-ledger.md, lines 12–17](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-ledger.md#L12-L17).
- **Lauren Tan (poteto) — [pstack/skills/ketchup/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/ketchup/SKILL.md):** Example 1, adapted from [pstack/skills/ketchup/SKILL.md, lines 23–23](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/ketchup/SKILL.md#L23-L23).
- **Addy Osmani — [skills/planning-and-task-breakdown/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md):** Example 1, adapted from [skills/planning-and-task-breakdown/SKILL.md, lines 161–162](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md#L161-L162).
- **Addy Osmani — [skills/context-engineering/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/context-engineering/SKILL.md):** Example 1, adapted from [skills/context-engineering/SKILL.md, lines 127–131](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/context-engineering/SKILL.md#L127-L131).
