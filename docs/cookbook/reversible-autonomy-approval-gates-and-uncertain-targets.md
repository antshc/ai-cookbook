# Recipe: Reversible Autonomy, Approval Gates, and Uncertain Targets

## Problem

Autonomy can either stall reversible work or cross an authorization boundary. Planning, risky changes, uncertain external targets, and external review need distinct gates.

## Example

**Task:** Execute an approved feature plan while preparing a verified PR and optional external review.

**AI Instructions:**

> 1. Proceed with authorized reversible edits and present concrete results.
> 2. If the request is for a plan only, deliver it and stop until an explicit execution go.
> 3. Keep verified stacked PRs unmerged when landing authority is withheld.
> 4. Before an irreversible or high-risk action, check its authorization and obtain fresh approval when the run's policy requires it.
> 5. Fail closed for external writes whose parent, target, or required fields cannot be verified.
> 6. Obtain explicit authorization for each external cross-model review invocation. Confirm tool availability and use read-only execution.
> 7. Record unresolved gates and continue independent authorized work.

## Best Practices

- Distinguish planning, execution, and landing authority.
- Prepare reviewable results before requesting gated actions.
- Do not guess uncertain external targets.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-never-block-on-the-human/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-never-block-on-the-human/SKILL.md):** Example 1, adapted from [pstack/skills/principle-never-block-on-the-human/SKILL.md, lines 11–15](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-never-block-on-the-human/SKILL.md#L11-L15).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/multi-phase-plan.md, lines 11–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L11-L11).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autopilot-stack.md, lines 7–12](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-stack.md#L7-L12).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/triage-issue-reports/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/triage-issue-reports/SKILL.md, lines 15–19](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L15-L19).
- **Addy Osmani — [skills/doubt-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/doubt-driven-development/SKILL.md):** Example 1, adapted from [skills/doubt-driven-development/SKILL.md, lines 120–166](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/doubt-driven-development/SKILL.md#L120-L166).
- **Addy Osmani — [.claude/commands/build.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/build.md):** Example 1, adapted from [.claude/commands/build.md, lines 31–39](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/build.md#L31-L39).
