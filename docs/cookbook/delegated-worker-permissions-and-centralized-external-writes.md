# Recipe: Delegated Worker Permissions and Centralized External Writes

## Problem

A delegated worker can publish to the wrong external thread or leak credentials if analysis and external writes share authority. The coordinator must retain write capability.

## Example

**Task:** Delegate investigation of a reported bug while the coordinator owns external status updates.

**AI Instructions:**

> 1. Freeze the authorized external target and verify it before each write.
> 2. Give analysis workers read-only access and require findings or media notes as their only output.
> 3. Explicitly forbid external posting in every worker brief.
> 4. Do not provide posting tokens, write instructions, or target coordinates for posting.
> 5. Allow code edits only when the worker environment provably excludes external write credentials and actions. Otherwise keep edits with the coordinator.
> 6. Have the coordinator validate findings and perform authorized external writes.

## Best Practices

- Enforce capability isolation as well as prompt rules.
- Keep external target verification centralized.
- Do not launch a worker that requires forbidden write access.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md, lines 15–23](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L15-L23).
