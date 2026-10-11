# Recipe: Secret Protection, Resource Authorization, and Personal Data Minimization

## Problem

Debug artifacts, browser code, or telemetry can expose secrets and unnecessary personal data. Authentication alone also fails to authorize access to a specific resource.

## Example

**Task:** Build a webhook-triggered UI and collect only the diagnostics needed to investigate failures.

**AI Instructions:**

> 1. Keep webhook sender keys on the server, outside browser bundles, chat, and logs.
> 2. Exclude recordings, reproduction logs, tokens, and other sensitive captures from source control.
> 3. Check the principal's permission for each protected resource before any side effect.
> 4. Scan code and diagnostics for secrets and redact sensitive error details.
> 5. Classify personal fields and record their purpose before collection.
> 6. Exclude unnecessary personal data from telemetry. Define retention and a working deletion path for retained copies.

## Best Practices

- Separate authentication from resource authorization.
- Keep secrets out of client code and diagnostics.
- Collect personal data only for a stated purpose.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/make-bot-ui/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/make-bot-ui/SKILL.md):** Example 1, adapted from [pstack/skills/make-bot-ui/SKILL.md, lines 11–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/make-bot-ui/SKILL.md#L11-L11).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md, lines 29–30](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L29-L30).
- **Addy Osmani — [skills/security-and-hardening/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md):** Example 1, adapted from [skills/security-and-hardening/SKILL.md, lines 81–83](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md#L81-L83).
- **Addy Osmani — [skills/security-and-hardening/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md):** Example 1, adapted from [skills/security-and-hardening/SKILL.md, lines 146–150](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md#L146-L150).
