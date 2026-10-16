# Recipe: Subtract Complexity, Reduce Reader Load, and Fix Suppressions

## Problem

Agents often add abstractions, guards, and comments while trying to improve code. The result can increase indirection, mutable state, and maintenance cost while leaving the underlying problem or suppression intact.

## Example

**Task:** Simplify a changed code path with the smallest maintainable patch.

**AI Instructions:**

> 1. Remove dead code, redundant validators, unused references, and speculative guards before adding structure.
> 2. Prefer the smallest change that meets the requirement. Reject abstractions with one caller, pass-through layers, and signal threading that do not compress decisions.
> 3. Reduce layers a reader must trace and hidden state a reader must retain. Prefer local immutable values and pure returns over wider mutable state.
> 4. Keep an abstraction only when it hides meaningful complexity or represents an observed second implementation.
> 5. Inspect comments and suppressions in the changed scope. Replace redundant explanations, workaround comments, and unsafe suppressions with the smallest root-cause code, type, test, or lint fix.
> 6. Preserve only comments about constraints outside the code's control and record proof for each exception.
> 7. Report deletions, remaining indirection, state-scope reductions, fixed suppressions, and unresolved constraints.

## Best Practices

- Subtract before introducing new structure.
- Measure simplicity by reader load, not line count.
- Replace suppressions with root-cause fixes.

## Related Recipes

- [Behavior-Preserving Refactoring and Protected Source Blocks](behavior-preserving-refactoring-and-protected-source-blocks.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [principle-laziness-protocol](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-laziness-protocol/SKILL.md):** Example 1, adapted from [SKILL.md, lines 9–18](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-laziness-protocol/SKILL.md#L9-L18).
- **Lauren Tan (poteto) — [principle-minimize-reader-load](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-minimize-reader-load/SKILL.md):** Example 1, adapted from [SKILL.md, lines 9–18](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-minimize-reader-load/SKILL.md#L9-L18).
- **Lauren Tan (poteto) — [principle-subtract-before-you-add](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-subtract-before-you-add/SKILL.md):** Example 1, adapted from [SKILL.md, lines 9–18](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-subtract-before-you-add/SKILL.md#L9-L18).
- **Lauren Tan (poteto) — [no-comments](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/no-comments/SKILL.md):** Example 1, adapted from [SKILL.md, lines 15–24](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/no-comments/SKILL.md#L15-L24).
