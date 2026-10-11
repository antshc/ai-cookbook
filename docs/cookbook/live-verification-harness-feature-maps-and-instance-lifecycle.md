# Recipe: Live Verification Harness, Feature Maps, and Instance Lifecycle

## Problem

A verification procedure drifts when routes change or failed runs leave stale instances. Agents need a repository-specific harness, maintained feature paths, and evidence that survives cleanup.

## Example

**Task:** Create and maintain a live verification harness for a CLI or web application.

**AI Instructions:**

> 1. Record the repository's exact launch command, readiness signal, health check, drive commands, evidence path, and teardown.
> 2. Map each feature's entry routes, prerequisites, user actions, and observable success state.
> 3. Compare feature maps with current source. Exercise every mapped feature live when maintaining the harness.
> 4. Health-check before the first drive and after unexpected failures. Reset wedged state or relaunch before retrying.
> 5. Use a fresh isolated session per short-lived CLI drive. Serialize drives that share one server instance.
> 6. Remove only processes and scratch state created by the run. Confirm saved proof still exists after every cleanup.

## Best Practices

- Use real selectors and repository commands.
- Treat clean source inspection as insufficient without a live pass.
- Track ownership of instances and preserve evidence outside their scratch state.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/create-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/create-verification-skill/SKILL.md):** Example 1, adapted from [pstack/skills/create-verification-skill/SKILL.md, lines 15–40](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/create-verification-skill/SKILL.md#L15-L40).
- **Lauren Tan (poteto) — [pstack/skills/maintain-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/maintain-verification-skill/SKILL.md):** Example 1, adapted from [pstack/skills/maintain-verification-skill/SKILL.md, lines 29–33](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/maintain-verification-skill/SKILL.md#L29-L33).
