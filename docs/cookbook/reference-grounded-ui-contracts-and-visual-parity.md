# Recipe: Reference-Grounded UI Contracts and Visual Parity

## Problem

UI work drifts when implementation starts before visual decisions are explicit or when parity is judged by eye. Define the design contract from trusted references and verify the result against an immutable baseline.

## Example

**Task:** Migrate a UI component while preserving its visual contract.

**AI Instructions:**

> 1. Study two or three trusted reference screens and record hierarchy, density, navigation, controls, responsive behavior, and interaction states.
> 2. Write a short design contract before implementation. State the screen job, primary action, required states, responsive rules, and rejected patterns.
> 3. Capture screenshots of the current component in every required state before changing it. Keep the baseline immutable.
> 4. Change one component at a time. Do not edit the harness, baseline, or component structure merely to make the comparison pass.
> 5. Run image diffs on the matching surface. Treat every nonzero diff as a failure and investigate the pixel delta.
> 6. Report the contract, baseline location, diff result for each state, and remaining components.

## Best Practices

- Convert visual references into an explicit contract.
- Capture and freeze the baseline before implementation.
- Use image diffs, not visual memory, to prove parity.

## Related Recipes

- [Direct Evidence, Safety Assumptions, and Risk-Based Verification](direct-evidence-safety-assumptions-and-risk-based-verification.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [visual-parity.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/visual-parity.md):** Example 1, adapted from [visual-parity.md, lines 3–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/visual-parity.md#L3-L11).
- **Addy Osmani — [skills/frontend-ui-engineering/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/frontend-ui-engineering/SKILL.md):** Example 1, adapted from [skills/frontend-ui-engineering/SKILL.md, lines 120–127](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/frontend-ui-engineering/SKILL.md#L120-L127).
