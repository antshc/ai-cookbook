# Recipe: Constraint-First Instructions and Anti-Rationalization Rules

## Problem

An agent can replace a required process with a faster path that appears equivalent. Critical instructions must constrain the mechanism as well as the result.

## Example

**Task:** Write guidance that requires delegated exploration to preserve the parent agent's context.

**AI Instructions:**

> 1. When repository exploration is broad, you MUST delegate the source scan to a bounded exploration worker.
> 2. You MUST NOT perform the bulk scan in the parent, even if direct scanning appears faster or simpler.
> 3. Give the worker source scope and a compact evidence-return contract.
> 4. Rationale: preserve parent context and isolate exploration responsibility.
> 5. If the required worker is unavailable, report the blocker. Do not silently substitute direct execution.
> 6. Resolve these constraints before optimizing the workflow. Verify delegation occurred from the execution trace.

## Best Practices

- State triggers and observable actions.
- Pair required mechanisms with explicit forbidden substitutes.
- Give a terse rationale and an unavailable-mechanism path.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/ops-instruction-robustness.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-instruction-robustness.md):** Example 1, adapted from [docs/concepts/ops-instruction-robustness.md, lines 19–28](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-instruction-robustness.md#L19-L28).
- **Brain — [docs/concepts/structure-constraint-first-reasoning.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-constraint-first-reasoning.md):** Example 1, adapted from [docs/concepts/structure-constraint-first-reasoning.md, lines 11–19](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-constraint-first-reasoning.md#L11-L19).
- **Addy Osmani — [docs/skill-anatomy.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/skill-anatomy.md):** Example 1, adapted from [docs/skill-anatomy.md, lines 151–157](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/docs/skill-anatomy.md#L151-L157).
