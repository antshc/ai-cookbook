# Delegated work loses scope or results

Define bounded assignments and verifiable handoff contracts.

## Recipes

- [Session Ledger, Open Questions, and Restartable Handoffs](../session-ledger-open-questions-and-restartable-handoffs.md)
- [Delegate Bulk Exploration to Preserve Context](../delegate-bulk-exploration-to-preserve-context.md)
- [Bounded Agent Roles, Single Ownership, and Composition](../bounded-agent-roles-single-ownership-and-composition.md)

## References

- [Grouped principle checklist](../grouped-index.md)
- [Combined Recipe Checklist](../combined-recipe-checklist.md)

## Templates

- [Orchestration skill template](../templates/orchestration-template/SKILL.md)

## Principles awaiting recipes

- [Agent-agnostic handoff contracts](https://github.com/antshc/brain/blob/main/docs/adr/ralph-is-agent-agnostic.md)
- [CLI JSON handoff](https://github.com/antshc/brain/blob/main/docs/concepts/str-cli-json-handoff.md)
- [Decompose parallel work into scoped workers and aggregate results](https://github.com/cursor/plugins/blob/main/pstack/skills/swarm/SKILL.md)
- [Audit live sessions and uncommitted changes before removing worktrees](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md)
- [Pilot a full work unit before scaling a multi-agent program](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [Delegate implementation with bounded files and success criteria, then review the diff](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/feature.md)
- [Carry immutable standing orders into every worker spawn and resume](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [Refill a rolling worker window instead of waiting for whole batches](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [Judge agent progress by actual side effects and replace stalled workers](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md)
- [Validate multi-phase plans with an executable checker before handoff](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md)
- [Keep stack topology updates under one coordinator while PR owners work in parallel](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md)
- [Keep external writes and credentials out of delegated workers](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [Compensate cross-system ticket writes when the final handoff fails](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md)
- [Parallelize independent specialist reviews, but keep aggregation with the orchestrator](https://github.com/addyosmani/agent-skills/blob/main/references/orchestration-patterns.md)
- [Use isolated worktrees when parallel agents would otherwise share a working tree](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
