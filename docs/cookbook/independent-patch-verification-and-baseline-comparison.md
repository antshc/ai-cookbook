# Recipe: Independent Patch Verification and Baseline Comparison

## Problem

CI can pass for a patch that nobody independently exercised. Rebases can also make an old verification verdict describe different code.

## Example

**Task:** Verify a repaired feature on the exact PR patch and compare its user path with current trunk.

**AI Instructions:**

> 1. Record the reviewed base SHA, head SHA, and patch ID.
> 2. Assign verification to an agent who did not write the patch.
> 3. Run the same user-visible scenario on current trunk and the patched build with matching inputs.
> 4. Record absent baseline capability explicitly. Verify the new end state instead of inventing baseline parity.
> 5. Run focused regression tests, required regression gates, and runtime checks.
> 6. Before merge, compare the current patch with the reviewed patch. Repeat affected checks when code changes and refresh CI and mergeability at the current head.

## Best Practices

- Bind evidence to the actual patch.
- Keep independent verification separate from author self-proof.
- Compare the same path and inputs across baseline and patch.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/shipping.md, lines 7–9](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/shipping.md#L7-L9).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autopilot-full.md, lines 8–9](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-full.md#L8-L9).
- **Addy Osmani — [skills/debugging-and-error-recovery/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md):** Example 1, adapted from [skills/debugging-and-error-recovery/SKILL.md, lines 154–174](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md#L154-L174).
