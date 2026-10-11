# Recipe: Concise Instructions, Explicit Goals, and Model-Neutral Procedures

## Problem

Vague goals and verbose, model-specific hints make procedures hard to execute and verify. Instructions need clear intent, evidence, and short commands.

## Example

**Task:** Write a bug-fix task brief and reusable procedure for different agent runtimes.

**AI Instructions:**

> 1. State the observed bug, reproduction steps, and desired user-visible result.
> 2. Define a pass-or-fail completion check and the proof to return.
> 3. Name constraints such as reproduction before edits and zero unrelated behavior changes.
> 4. Write each action as a short imperative sentence. Put its condition first.
> 5. Describe the required procedure without model-specific workarounds or repeated reminders.
> 6. Remove words that do not change execution. Preserve facts, constraints, and evidence.

## Best Practices

- Make goals and completion checks explicit.
- Use one action per command.
- Keep procedures model-neutral and operational.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-help/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-help/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-help/references/prompting.md, lines 7–17](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-help/references/prompting.md#L7-L17).
- **Lauren Tan (poteto) — [pstack/skills/technical-writing/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md):** Example 1, adapted from [pstack/skills/technical-writing/SKILL.md, lines 53–63](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md#L53-L63).
- **Addy Osmani — [docs/skill-anatomy.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/skill-anatomy.md):** Example 1, adapted from [docs/skill-anatomy.md, lines 151–157](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/skill-anatomy.md#L151-L157).
