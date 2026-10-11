# Recipe: Direct Evidence, Safety Assumptions, and Risk-Based Verification

## Problem

Agents can mistake a green build or a dry-run label for proof of safe behavior. Risky changes need direct evidence of the artifact and the assumption that limits harm.

## Example

**Task:** Verify a cache-cleanup change before delivery. Check that the dry-run mode leaves cache entries and repository refs unchanged.

**AI Instructions:**

> 1. Identify the safety fact: cleanup can delete only expired cache entries.
> 2. Trace the pinned library and downstream callers that could invalidate that fact.
> 3. Run the real cleanup path against expired and live entries. Compare exact resulting state.
> 4. Observe file writes, network calls, and Git refs during dry-run. Record every effect it still performs.
> 5. Set verification depth from impact and reversibility. Add rollback and independent checks for wide or irreversible changes.
> 6. Save rerunnable proof. Mark the safety fact unproven if the evidence cannot establish it.

## Best Practices

- Observe actual effects rather than accepting tool labels.
- Prove the central safety assumption before enumerating speculative risks.
- Increase gates and evidence with impact and irreversibility.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-prove-it-works/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-prove-it-works/SKILL.md):** Example 1, adapted from [pstack/skills/principle-prove-it-works/SKILL.md, lines 9–22](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-prove-it-works/SKILL.md#L9-L22).
- **Lauren Tan (poteto) — [pstack/skills/figure-it-out/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/figure-it-out/SKILL.md):** Example 1, adapted from [pstack/skills/figure-it-out/SKILL.md, lines 19–21](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/figure-it-out/SKILL.md#L19-L21).
- **Lauren Tan (poteto) — [pstack/skills/blast-radius/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/blast-radius/SKILL.md):** Example 1, adapted from [pstack/skills/blast-radius/SKILL.md, lines 33–38](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/blast-radius/SKILL.md#L33-L38).
- **Lauren Tan (poteto) — [pstack/skills/create-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/create-verification-skill/SKILL.md):** Example 1, adapted from [pstack/skills/create-verification-skill/SKILL.md, lines 27–32](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/create-verification-skill/SKILL.md#L27-L32).
