# Recipe: Clarify Intent, Surface Assumptions, and Challenge Scope

## Problem

An agent can confidently solve an unstated problem or add complexity the user never wanted. Unclear intent needs a confirmed restatement before downstream work.

## Example

**Task:** Clarify a request for a more sophisticated dashboard before designing it.

**AI Instructions:**

> 1. State one explicit guess about the desired outcome and explain uncertainty.
> 2. Ask one intent question at a time with that guess attached.
> 3. Identify the user, desired outcome, why now, success measure, constraints, and exclusions.
> 4. Challenge scope or complexity that does not serve the outcome. Explain the tradeoff candidly.
> 5. Surface conflicting requirements and unresolved assumptions.
> 6. Restate the intent concretely and obtain explicit confirmation. Stop before planning or implementation until it is confirmed.

## Best Practices

- Clarify the actual outcome.
- Challenge unnecessary complexity without taking over product decisions.
- Keep unknowns visible and require a confirmed restatement.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/SKILL.md, lines 89–89](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md#L89-L89).
- **Addy Osmani — [skills/interview-me/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/interview-me/SKILL.md):** Example 1, adapted from [skills/interview-me/SKILL.md, lines 227–235](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/interview-me/SKILL.md#L227-L235).
