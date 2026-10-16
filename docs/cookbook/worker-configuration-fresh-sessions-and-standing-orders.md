# Recipe: Worker Configuration, Fresh Sessions, and Standing Orders

## Problem

Worker behavior drifts when models are chosen ad hoc or follow-ups omit later instructions. Fresh work needs consolidated scope and unchanged standing orders.

## Example

**Task:** Dispatch a new implementation round after a worker's first report.

**AI Instructions:**

> 1. Resolve the model from the role's configuration. Use the documented default or parent inheritance policy.
> 2. Give a fresh worker the original brief, later directives, prior report, and current branch.
> 3. Carry standing orders verbatim into every spawn and resume.
> 4. Resume an existing worker only when costly local state, uncommitted work, or a running process is required.
> 5. Record worker identity, responsibility, model, and state.
> 6. Treat a stop message as control of the current worker, not a reason to reuse it for new work.

## Best Practices

- Choose models by responsibility.
- Consolidate all directives for fresh rounds.
- Preserve standing orders across lifecycle boundaries.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/setup-pstack/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/setup-pstack/SKILL.md):** Example 1, adapted from [pstack/skills/setup-pstack/SKILL.md, lines 41–66](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/setup-pstack/SKILL.md#L41-L66).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/SKILL.md, lines 95–99](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md#L95-L99).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/orchestrate.md, lines 9–10](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/orchestrate.md#L9-L10).
