# Recipe: Improvement Flywheel and Enforced Lessons

## Problem

Repeated failures persist when lessons are stored as reminders that never constrain execution. A durable repair must target the missing fact or the mechanism that caused the failure.

## Example

**Task:** Prevent a recurring agent mistake after reviewing a failed verification run.

**AI Instructions:**

> 1. Classify the observed failure before editing guidance.
> 2. Put a missing reusable fact in memory. Repair wrong routing, missing read-back, or absent guardrails in the responsible harness.
> 3. Choose one owner and one repair tier. Do not duplicate the same fix across memory and instructions.
> 4. Replace repeated reminders with an executable check, metadata rule, or automation where feasible.
> 5. Verify that the mechanism detects the original failure.
> 6. Record the durable repair in this session and sweep for remaining observed failures before exit.

## Best Practices

- Repair the responsible tier.
- Prefer enforced mechanisms for recurring mistakes.
- Require observed evidence rather than speculative lessons.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/ops-improvement-flywheel.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-improvement-flywheel.md):** Example 1, adapted from [docs/concepts/ops-improvement-flywheel.md, lines 12–20](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-improvement-flywheel.md#L12-L20).
- **Lauren Tan (poteto) — [pstack/skills/principle-encode-lessons-in-structure/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-encode-lessons-in-structure/SKILL.md):** Example 1, adapted from [pstack/skills/principle-encode-lessons-in-structure/SKILL.md, lines 9–9](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-encode-lessons-in-structure/SKILL.md#L9-L9).
