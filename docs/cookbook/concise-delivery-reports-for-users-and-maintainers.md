# Recipe: Concise Delivery Reports for Users and Maintainers

## Problem

Delivery reports can list implementation trivia without saying what users gain or what maintainers inherit. Long PR descriptions can still omit scope, risk, and actual verification.

## Example

**Task:** Write the PR description and final handoff for a completed behavior change.

**AI Instructions:**

> 1. Lead with who the change serves, the previous problem, and the observable resulting behavior.
> 2. Explain what the next maintainer inherits, including ownership and any material operational constraint.
> 3. Keep the PR's why concise and group the meaningful changes; name paths or symbols only when they explain the result.
> 4. State scope, known gaps, blast radius, and real trade-offs without recounting abandoned work.
> 5. Report a few actual verification runs and outcomes. Link only artifacts produced or read, and label inference or uncertainty beside its claim.
> 6. Use short declarative sentences while retaining the details needed to review and maintain the change.

## Best Practices

- Lead with consumer and maintainer impact.
- Keep scope and material risks explicit.
- Support delivery claims with observed evidence.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/opening-a-pr.md, lines 15–20](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/opening-a-pr.md#L15-L20).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/SKILL.md, lines 105–111](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md#L105-L111).
