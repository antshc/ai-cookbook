# Recipe: Live Browser Evidence, Accessibility, and UI State Coverage

## Problem

Static checks cannot prove that a UI works in a real browser. A complete UI review must cover runtime evidence, responsive layouts, accessibility, and non-happy-path states.

## Example

**Task:** Verify a changed interface on its live browser surface.

**AI Instructions:**

> 1. Open the live page and reproduce the changed flow. Capture the initial screenshot and expected state.
> 2. Inspect the rendered DOM, computed styles, console, network requests, and accessibility tree.
> 3. Exercise loading, empty, error, success, and permission states when applicable.
> 4. Test keyboard navigation and screen-reader structure. Run the configured accessibility checker and resolve critical findings.
> 5. Check responsive behavior at 320px, 768px, 1024px, and 1440px or the project's declared breakpoints.
> 6. Reload after the fix, repeat the flow, capture the final screenshot, confirm a clean console, and run the relevant automated tests.
> 7. Report the browser evidence for each required state. Do not infer runtime behavior from source code alone.

## Best Practices

- Inspect the live surface and its runtime signals.
- Cover accessibility and responsive behavior explicitly.
- Verify empty, loading, error, success, and permission states.

## Related Recipes

- [Reference-Grounded UI Contracts and Visual Parity](reference-grounded-ui-contracts-and-visual-parity.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/frontend-ui-engineering/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/frontend-ui-engineering/SKILL.md):** Example 1, adapted from [skills/frontend-ui-engineering/SKILL.md, lines 324–340](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/frontend-ui-engineering/SKILL.md#L324-L340).
- **Addy Osmani — [skills/browser-testing-with-devtools/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/browser-testing-with-devtools/SKILL.md):** Example 1, adapted from [skills/browser-testing-with-devtools/SKILL.md, lines 109–138](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/browser-testing-with-devtools/SKILL.md#L109-L138).
