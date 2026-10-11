# Recipe: Progressive Disclosure, Targeted Context, and Safe Trimming

## Problem

Loading every reference floods context, while trimming the active task can remove essential constraints. Disclosure and compression must preserve the information needed for the current branch.

## Example

**Task:** Keep context focused during a long debugging session.

**AI Instructions:**

> 1. Load the workflow entry point, applicable rules, affected source, and one neighboring example.
> 2. Keep instructions required on every path inline. Load branch-specific references only when that branch is reached.
> 3. Link supporting files directly and sharpen pointers that fail to trigger.
> 4. Trim replaced drafts, resolved attempts, and verbose outputs after preserving their conclusions.
> 5. Protect the original task, hard constraints, current failing output, and current file until completion.
> 6. Checkpoint verified progress and refresh context at a safe task boundary.

## Best Practices

- Disclose references by task relevance.
- Compress conclusions before discarding exploration.
- Preserve live errors and constraints while trimming stale material.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [skills/engineering/writing-great-skills/GLOSSARY.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/skills/engineering/writing-great-skills/GLOSSARY.md):** Example 1, adapted from [skills/engineering/writing-great-skills/GLOSSARY.md, lines 101–105](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/skills/engineering/writing-great-skills/GLOSSARY.md#L101-L105).
- **Addy Osmani — [skills/context-engineering/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/context-engineering/SKILL.md):** Example 1, adapted from [skills/context-engineering/SKILL.md, lines 198–230](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/context-engineering/SKILL.md#L198-L230).
- **Addy Osmani — [docs/skill-anatomy.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/skill-anatomy.md):** Example 1, adapted from [docs/skill-anatomy.md, lines 132–136](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/skill-anatomy.md#L132-L136).
