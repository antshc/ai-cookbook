# Recipe: Verification, Exit Criteria, Completeness Sweep, and Definition of Done

## Problem

An agent can pass tests and still omit requested work. Multi-part changes need four separate checks: verification proves behavior; exit criteria prove task completion; a completeness sweep finds missing obligations; definition of done applies the standing project quality bar.

## Example

**Task:** Complete an autonomous bug fix and prepare its handoff. Prove the reported failure is gone and the change meets the project's standing quality bar.

**AI Instructions:**

> 1. Define the finish condition before editing: the original reproduction fails on baseline and succeeds after the fix.
> 2. Verify the real runtime behavior and save the command, revision, expected result, and actual result.
> 3. Check every task acceptance criterion against that evidence.
> 4. Apply the standing definition of done separately: regressions, lint, integration, documentation, security, and rollback where required.
> 5. Run the completeness sweep last. Reconstruct every obligation from the request and account for each result or blocker.
> 6. Stop only when the finish condition and standing checks pass. Do not relax the predicate to declare completion.

## Best Practices

- Define falsifiable finish conditions before the first iteration.
- Keep task acceptance criteria separate from the standing definition of done.
- Use the final sweep to find omitted obligations; passing tests alone cannot prove full completion.

## Related Recipes

- [Checklist-driven Workflow](checklist-driven-workflow.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autonomous-run.md, lines 3–12](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autonomous-run.md#L3-L12).
- **Addy Osmani — [skills/planning-and-task-breakdown/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md):** Example 1, adapted from [references/definition-of-done.md, lines 3–61](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/references/definition-of-done.md#L3-L61).
