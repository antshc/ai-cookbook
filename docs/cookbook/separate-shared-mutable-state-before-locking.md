# Recipe: Separate Shared Mutable State before Locking

## Problem

Concurrent agents that write the same file, branch, key, or state object create intermittent races. Adding a lock too early preserves unnecessary coupling and makes independent work wait.

## Example

**Task:** Design state ownership for two concurrent workers.

**AI Instructions:**

> 1. List every file, branch, key, API, and state object that more than one worker can modify.
> 2. Decide whether each worker publishes an independent fact or must update one canonical object.
> 3. Give independent facts separate owned files, keys, branches, or state directories. Merge them only at the read or reporting boundary.
> 4. Keep one shared target only when it is a real invariant.
> 5. For a real shared target, enforce access with a single writer, sequential phases, an atomic compare-and-swap, or a lockfile.
> 6. Do not rely on prompt instructions or naming conventions as concurrency control.

## Best Practices

- Eliminate shared writes before adding coordination.
- Assign one owner to each mutable target.
- Serialize structurally only for genuine shared invariants.

## Related Recipes

- [Scoped Parallel Workers, Bounded Implementation, and Aggregation](scoped-parallel-workers-bounded-implementation-and-aggregation.md)

## Sources & Attribution

Examples adapt the cited workflow. Task details illustrate its use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [principle-separate-before-serializing-shared-state](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md):** Example 1, adapted from [SKILL.md, lines 9–16](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md#L9-L16).
