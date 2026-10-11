# Recipe: Gotchas and Persistent Memory

## Problem

AI agents repeat avoidable mistakes when lessons from prior runs are lost. **Gotchas** are reusable directives grounded in observed friction. **Memory** stores those directives across sessions and makes them available to later runs.

## Example 1

**Task:** Start a Crew implementation or review run. Repository memory supplies the gotcha rules that apply to the work.

**Source:** Adapted from the actual [Crew gotcha read workflow, lines 8–16](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/plugins/crew/skills/crew-gotchas/SKILL.md#L8-L16).

**AI Instructions:**

> 1. Load relevant repository rules through the memory owner.
> 2. Read every supplied gotcha. Apply its directive during the work.
> 3. Report conflicts with current requirements. Do not ignore them silently.
> 4. If no rules exist, report that no gotchas are recorded. Continue with repository conventions.

## Example 2

**Task:** Review friction from a Crew run before returning its result. A required CLI was unavailable during verification; record a reusable rule that helps future runs detect the blocker earlier.

**Source:** Adapted from the [tool-access candidate and rule-update workflow, lines 18–50](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/plugins/crew/skills/crew-gotchas/SKILL.md#L18-L50). This task illustrates a failure class named in the skill; it is not a claim about an observed incident.

**AI Instructions:**

> 1. Review changed files, failures, and corrections for reusable lessons.
> 2. Discard one-off errors, routine steps, and transient failures resolved on the first retry.
> 3. Turn the observed missing CLI into a directive: check required tool availability before verification; report blocked when unavailable.
> 4. Refine a matching gotcha or return a new one. Preserve unrelated rules.
> 5. Return exact updates to the memory owner. Have that owner save them before exit, including blocked or partial results.
> 6. If persistence fails, report that the update was not saved.

## Best Practices

- Read memory before work. Save new gotchas before every exit, including blocked or partial results.
- Record concise, actionable directives from actual repeatable friction. Do not save speculation, secrets, or routine steps.
- Put missing facts in memory; fix broken agent routing or guardrails in the responsible instructions.

## Sources & Attribution

- **[Brain: Crew Gotchas read workflow, lines 8–16](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/plugins/crew/skills/crew-gotchas/SKILL.md#L8-L16)**: Load supplied rules, handle absent memory, and report conflicts.
- **[Brain: Crew Gotchas write workflow, lines 18–50](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/plugins/crew/skills/crew-gotchas/SKILL.md#L18-L50)**: Classify real friction, discard one-off failures, and refine rules without duplication.
- **[Brain: Crew Memory skill template, lines 8–20](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/plugins/crew/skills/init-crew/templates/crew-memory.SKILL.template.md#L8-L20)**: The repository memory owner loads and persists updates. This is a template used to generate repository-local skills, not an installed memory skill in the source repository.

## Related Recipes

- [Verification, Exit Criteria, and Completeness Sweep](verification-exit-criteria-completeness-sweep.md)
