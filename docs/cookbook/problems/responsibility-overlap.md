# Skills and agents have overlapping responsibilities

Give each procedure and responsibility one clear owner.

## Recipes

No materials yet.


## References

- [Grouped principle checklist](../grouped-index.md)

## Templates

No materials yet.


## Principles awaiting recipes

- [Template ownership of rendering](https://github.com/antshc/brain/blob/main/.github/instructions/agent-skills.instructions.md)
- [Skill composition and single ownership](https://github.com/antshc/brain/blob/main/docs/concepts/structure-skill-composition.md)
- [Agent-agnostic handoff contracts](https://github.com/antshc/brain/blob/main/docs/adr/ralph-is-agent-agnostic.md)
- [Repository adapter skills](https://github.com/antshc/brain/blob/main/docs/concepts/structure-repository-adapter-skill.md)
- [Choose core data shapes and shared foundations before features](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-foundational-thinking/SKILL.md)
- [Prefer the smallest change and shallowest useful abstraction](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-laziness-protocol/SKILL.md)
- [Redesign new requirements as foundational constraints](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-redesign-from-first-principles/SKILL.md)
- [Separate shared mutable state before using locks](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md)
- [Derive architecture contracts from caller usage before implementing](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md)
- [Write a consumer usage guide before implementing a shared API](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-help/references/prompting.md)
- [Make module internals inaccessible and expose only one supported operation path](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md)
- [Record design alternatives, accepted tradeoffs, and rationale alongside the chosen contract](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/rationale-template.md)
- [Keep orchestration and code-writing responsibilities with separate owners](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [Apply retrospective changes to shared agent instructions only with approval](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/SKILL.md)
- [Keep stack topology updates under one coordinator while PR owners work in parallel](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md)
- [Gate automatic bug fixing on a trusted triage verdict and ownership checks](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [Approve the capability dependency map before specifying a multi-module initiative](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [Define measurable project quality thresholds and record exceptions with owners and expiry](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [Independently doubt nontrivial claims using only the artifact and contract, not the author's conclusion](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md)
- [Define public contracts before implementation and preserve observable consumer behavior](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md)
- [Define a reference-grounded UI design contract before implementation](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md)
- [Include required shared references when distributing an individual skill outside its original pack](https://github.com/addyosmani/agent-skills/blob/main/docs/getting-started.md)
- [Keep vendor runtime settings in per-agent adapters or permitted metadata, not portable skill frontmatter](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md)
- [For negative routing tests, require the intended owner skill to outrank the wrong skill](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)
- [Validate that equivalent host command adapters stay semantically aligned](https://github.com/addyosmani/agent-skills/blob/main/docs/developer-onboarding.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
