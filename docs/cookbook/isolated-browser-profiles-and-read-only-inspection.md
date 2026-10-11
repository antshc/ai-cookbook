# Recipe: Isolated Browser Profiles and Read-Only Inspection

## Problem

Browser automation can expose unrelated signed-in sessions or mutate application state while supposedly inspecting it. Verification needs profile isolation and read-only inspection.

## Example

**Task:** Inspect a localhost UI's DOM, console, and layout in an isolated browser profile.

**AI Instructions:**

> 1. Use a dedicated or temporary testing profile by default.
> 2. If authentication is required, use a separate test profile signed into only the target account.
> 3. Attach to a personal profile only when necessary and authorized; close unrelated windows and detach afterward.
> 4. Use JavaScript only to read relevant DOM state and computed values unless mutation is explicitly authorized.
> 5. Do not read credentials, make external requests, load remote scripts, or inspect unrelated pages.
> 6. Report unexpected access to unrelated tabs and remove the exposure.

## Best Practices

- Isolate sessions before testing.
- Keep inspection read-only by default.
- Limit browser access to the task's account and pages.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/browser-testing-with-devtools/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/browser-testing-with-devtools/SKILL.md):** Example 1, adapted from [skills/browser-testing-with-devtools/SKILL.md, lines 62–70](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/browser-testing-with-devtools/SKILL.md#L62-L70).
- **Addy Osmani — [skills/browser-testing-with-devtools/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/browser-testing-with-devtools/SKILL.md):** Example 1, adapted from [skills/browser-testing-with-devtools/SKILL.md, lines 86–90](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/browser-testing-with-devtools/SKILL.md#L86-L90).
