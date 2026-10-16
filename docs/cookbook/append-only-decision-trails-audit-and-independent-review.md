# Recipe: Append-Only Decision Trails, Audit, and Independent Review

## Problem

A long-running agent can rewrite history, omit failed choices, or cite evidence that never existed. A decision trail needs append-only correction and independent scrutiny.

## Example

**Task:** Maintain and review the decision trail for a multi-stage implementation.

**AI Instructions:**

> 1. Append timestamped rows for meaningful decisions and actions, their reason, evidence pointer, and actual result.
> 2. Link only real commits, commands, artifacts, or transcript moments and mark uncertain outcomes explicitly.
> 3. Audit this run's rows against its transcript in the active workspace; do not search unrelated private conversations.
> 4. Append missing decisions and superseding corrections for false claims or bad evidence. Preserve the original rows.
> 5. Have an independent reviewer from a different model family read the trail and relevant transcript and flag risky or suboptimal choices.
> 6. Include the reviewer identity and attention flags with pointers to specific rows or moments in the handoff; report no flags only if that review actually occurred.

## Best Practices

- Append corrections instead of rewriting history.
- Audit claims against actual run evidence.
- Use independent review for long-running trails.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/show-me-your-work/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md):** Example 1, adapted from [pstack/skills/show-me-your-work/SKILL.md, lines 26–32](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md#L26-L32).
- **Lauren Tan (poteto) — [pstack/skills/show-me-your-work/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md):** Example 1, adapted from [pstack/skills/show-me-your-work/SKILL.md, lines 57–67](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md#L57-L67).
- **Lauren Tan (poteto) — [pstack/skills/show-me-your-work/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md):** Example 1, adapted from [pstack/skills/show-me-your-work/SKILL.md, lines 74–74](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md#L74-L74).
