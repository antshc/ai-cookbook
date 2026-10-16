# Recipe: Idempotent Operations, Retry Keys, and Unknown Outcomes

## Problem

Retries after timeouts or partial crashes can duplicate state changes because failure and unknown outcome are treated as the same. Operations must reconcile existing state and bind every retry to the original intent.

## Example

**Task:** Design a retry-safe state-changing operation.

**AI Instructions:**

> 1. Define the intended final state and reconcile existing, partial, stale, and completed state before applying changes.
> 2. Test what happens when the operation runs twice and when it crashes after each state transition. Require every rerun to converge on the same end state.
> 3. Create one idempotency key from the client intent or immutable event identifier. Reuse it for every retry and never generate it inside the retry loop.
> 4. Claim the key atomically with a uniqueness constraint. Store the request hash, state, and replayable result.
> 5. Reject the same key with a different payload. Define a bounded wait, conflict response, or pending response for in-flight duplicates.
> 6. Treat timeout as an unknown outcome. Record intent before the external effect and reconcile it before any retry.
> 7. Retain keys longer than the longest retry, dead-letter replay, and dispute window.

## Best Practices

- Reconcile partial state before reapplying effects.
- Derive retry keys from intent, not attempts.
- Model success, failure, and unknown outcomes separately.

## Related Recipes

- [Safe Pause, Context Recovery, and Verified Resume](safe-pause-context-recovery-and-verified-resume.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [principle-make-operations-idempotent](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-make-operations-idempotent/SKILL.md):** Example 1, adapted from [SKILL.md, lines 9–24](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-make-operations-idempotent/SKILL.md#L9-L24).
- **Addy Osmani — [skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/api-and-interface-design/SKILL.md):** Example 1, adapted from [skills/api-and-interface-design/SKILL.md, lines 156–215](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/api-and-interface-design/SKILL.md#L156-L215).
