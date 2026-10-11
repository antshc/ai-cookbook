# Recipe: Code-Path Investigation and Evidence-Calibrated Rationale

## Problem

A plausible explanation can describe stale code or invent author intent from implementation mechanics. Current behavior and historical rationale require different evidence and confidence labels.

## Example

**Task:** Explain how a retry path works and why its limits were chosen.

**AI Instructions:**

> 1. Identify the exact subsystem and question, then inspect the current entry point, call path, dependencies, tests, and runtime boundaries.
> 2. Trace inputs, state changes, failure branches, and observable outputs before drafting the explanation.
> 3. Search relevant independent evidence categories: source history and reviews, tickets, design documents, team discussion, runtime signals, and analytics; record unavailable or skipped categories.
> 4. Separate current mechanics from stated motivation. Code behavior alone does not establish why its author chose it.
> 5. Label rationale as direct, supported, inferred, speculative, or unknown. Cite direct statements and converging evidence next to each claim.
> 6. Present a compact behavior model, the supported rationale, competing hypotheses, and the unresolved questions without removing uncertainty.

## Best Practices

- Inspect the current path before explaining it.
- Use independent records for motivation.
- Match every rationale claim to its evidence tier.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/how/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/how/SKILL.md):** Example 1, adapted from [pstack/skills/how/SKILL.md, lines 13–28](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/how/SKILL.md#L13-L28).
- **Lauren Tan (poteto) — [pstack/skills/why/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/SKILL.md):** Example 1, adapted from [pstack/skills/why/SKILL.md, lines 60–66](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/SKILL.md#L60-L66).
- **Lauren Tan (poteto) — [pstack/skills/why/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/SKILL.md):** Example 1, adapted from [pstack/skills/why/references/epistemics.md, lines 5–37](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/references/epistemics.md#L5-L37).
- **Lauren Tan (poteto) — [pstack/skills/why/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/SKILL.md):** Example 1, adapted from [pstack/skills/why/references/epistemics.md, lines 71–71](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/references/epistemics.md#L71-L71).
