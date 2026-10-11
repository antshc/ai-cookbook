# Recipe: Live Bug Reproduction and Verification of Existing Fixes

## Problem

A tracker claim can lead an agent to accept an unproven fix or create a competing patch. Existing fixes need the same live before-and-after reproduction as new fixes.

## Example

**Task:** Verify an existing PR that claims to fix a reported UI defect.

**AI Instructions:**

> 1. Resolve the concrete PR or commit and record baseline and patched revisions.
> 2. Use an isolated checkout with the same build inputs, data, and environment for both runs.
> 3. Drive the reported UI path on baseline. Observe the discriminating symptom, reset, and reproduce it again.
> 4. Run the patched application. Repeat the same path twice and confirm the expected state replaces the symptom.
> 5. Capture matching before-and-after UI and state evidence.
> 6. Report confirmed, insufficient, or inconclusive. Do not edit the existing fix or open a competing PR. Preserve user changes during cleanup.

## Best Practices

- Require two real UI reproductions rather than injected state.
- Keep baseline and patched inputs comparable.
- Do not claim success when either half cannot be measured.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md, lines 24–28](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L24-L28).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md, lines 19–59](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md#L19-L59).
