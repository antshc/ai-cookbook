# Recipe: Delegate Bulk Exploration to Preserve Context

## Problem

Bulk source scans and large outputs consume the coordinator's context before it can judge the work. Exploration needs bounded delegation and compact evidence returns.

## Example

**Task:** Inspect a large trace and repository subsystem without flooding the coordinator.

**AI Instructions:**

> 1. Assign bulk reading to an exploration worker with explicit paths, questions, and scope limits.
> 2. Send pointers to artifacts rather than copying them into the parent conversation.
> 3. Have the worker return concise findings, source locations, unresolved questions, and evidence paths.
> 4. Keep raw traces, large screenshots, and full listings in the worker or artifact store.
> 5. Review the findings before deciding the next action. Delegate follow-up reads when needed.
> 6. Cap files per phase and account for the cost of worker startup and evidence handling.

## Best Practices

- Keep raw payloads outside coordinator context.
- Bound exploration by questions and sources.
- Require evidence pointers with every summary.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-guard-the-context-window/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-guard-the-context-window/SKILL.md):** Example 1, adapted from [pstack/skills/principle-guard-the-context-window/SKILL.md, lines 13–16](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-guard-the-context-window/SKILL.md#L13-L16).
