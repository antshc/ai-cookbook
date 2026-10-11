# Recipe: Instruction Loading and Canary Checks

## Problem

An instruction edit can appear successful even when the runtime never loaded the file. Scope and loading must be observed before trusting behavior.

## Example

**Task:** Verify that a repository instruction file applies to C# implementation workers.

**AI Instructions:**

> 1. Enable the runtime's repository-instruction loading mechanism for the worker.
> 2. Add an artificial harmless marker rule in the exact section and file scope under test.
> 3. Start a fresh worker task that falls inside that scope. Do not mention the marker in its prompt.
> 4. Observe whether the marker appears in the expected output.
> 5. If absent, diagnose discovery, trigger scope, and loading before trusting the real rule.
> 6. Remove the marker immediately after the check. Verify that the final guidance contains only the real instruction.

## Best Practices

- Test the exact loading path and scope.
- Keep the canary harmless and unprimed.
- Remove temporary markers before delivery.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/ops-canary-rule-verification.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-canary-rule-verification.md):** Example 1, adapted from [docs/concepts/ops-canary-rule-verification.md, lines 13–24](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-canary-rule-verification.md#L13-L24).
- **Brain — [docs/adr/crew-agents-uses-instructions.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/crew-agents-uses-instructions.md):** Example 1, adapted from [docs/adr/crew-agents-uses-instructions.md, lines 1–14](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/crew-agents-uses-instructions.md#L1-L14).
