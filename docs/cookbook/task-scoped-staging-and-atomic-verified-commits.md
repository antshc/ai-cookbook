# Recipe: Task-Scoped Staging and Atomic Verified Commits

## Problem

A broad stage command can absorb unrelated edits into an autonomous task. Commits need an inspected baseline, scoped changes, and verified behavior.

## Example

**Task:** Commit one completed implementation task from an approved plan.

**AI Instructions:**

> 1. Inspect working-tree changes before execution and identify planning artifacts and unrelated edits.
> 2. Stop on unrelated dirty files until their handling is explicitly settled.
> 3. Review the task diff and run required tests, type checks, lint, and secret checks.
> 4. Stage only the task's changed files and its status update. Do not blindly stage the whole tree.
> 5. Create one coherent commit with a message explaining the behavioral change.
> 6. Verify the committed content and recorded checks before advancing to the next task.

## Best Practices

- Inspect before staging.
- Keep unrelated edits out of task commits.
- Make each verified commit a clean rollback boundary.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [.claude/commands/build.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/build.md):** Example 1, adapted from [.claude/commands/build.md, lines 31–39](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/build.md#L31-L39).
- **Addy Osmani — [skills/git-workflow-and-versioning/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/git-workflow-and-versioning/SKILL.md):** Example 1, adapted from [skills/git-workflow-and-versioning/SKILL.md, lines 315–325](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/git-workflow-and-versioning/SKILL.md#L315-L325).
