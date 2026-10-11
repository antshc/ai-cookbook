# Recipe: Isolated Worktrees and Safe Workspace Cleanup

## Problem

Parallel agents can overwrite a shared working tree, and cleanup can delete a live session's uncommitted work. Workspaces need isolation and an evidence-based removal decision.

## Example

**Task:** Create isolated workspaces for two agents and later clean up unused worktrees.

**AI Instructions:**

> 1. Give each writer its own branch and worktree.
> 2. Enumerate cleanup candidates from Git's actual worktree list rather than guessed paths.
> 3. Audit uncommitted changes, merge state, PR status, and active sessions for every candidate.
> 4. Treat automated cleanup buckets as advice. Independently verify that no live worker owns the worktree.
> 5. Preserve dirty, active, or uncertain worktrees and report the unresolved ownership.
> 6. Remove only verified unused owned worktrees under the applicable authorization and recheck the remaining inventory.

## Best Practices

- Isolate parallel writers.
- Protect active sessions and uncommitted work.
- Base cleanup on current ownership evidence.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/git-workflow-and-versioning/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/git-workflow-and-versioning/SKILL.md):** Example 1, adapted from [skills/git-workflow-and-versioning/SKILL.md, lines 151–154](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/git-workflow-and-versioning/SKILL.md#L151-L154).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/worktree-cleanup.md, lines 5–10](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md#L5-L10).
