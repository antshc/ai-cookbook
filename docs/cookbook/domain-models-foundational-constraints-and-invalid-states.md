# Recipe: Domain Models, Foundational Constraints, and Invalid States

## Problem

Scattered conditionals allow invalid combinations and make new requirements expensive to retrofit. Core data shapes must encode the domain before feature logic expands.

## Example

**Task:** Model a task lifecycle in which completed tasks always carry a completion time.

**AI Instructions:**

> 1. List domain states, invariants, and dominant read/write paths before coding.
> 2. Represent open and completed tasks as explicit variants; require a timestamp in the completed variant.
> 3. Derive completion status from the variant rather than combining a boolean with an optional timestamp.
> 4. Use exhaustive handling and boundary parsing to prevent unsupported states.
> 5. Choose shared data structures and foundational constraints before dependent features.
> 6. When a new requirement changes the foundation, redesign the target shape and propagate it through callers, types, documentation, and examples incrementally.

## Best Practices

- Encode invariants in structures and types.
- Exclude illegal combinations by construction.
- Treat new foundational constraints as design inputs.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-foundational-thinking/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-foundational-thinking/SKILL.md):** Example 1, adapted from [pstack/skills/principle-foundational-thinking/SKILL.md, lines 11–11](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-foundational-thinking/SKILL.md#L11-L11).
- **Lauren Tan (poteto) — [pstack/skills/principle-model-the-domain/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-model-the-domain/SKILL.md):** Example 1, adapted from [pstack/skills/principle-model-the-domain/SKILL.md, lines 9–9](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-model-the-domain/SKILL.md#L9-L9).
- **Lauren Tan (poteto) — [pstack/skills/principle-redesign-from-first-principles/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-redesign-from-first-principles/SKILL.md):** Example 1, adapted from [pstack/skills/principle-redesign-from-first-principles/SKILL.md, lines 11–14](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-redesign-from-first-principles/SKILL.md#L11-L14).
- **Lauren Tan (poteto) — [pstack/skills/principle-type-system-discipline/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-type-system-discipline/SKILL.md):** Example 1, adapted from [pstack/skills/principle-type-system-discipline/SKILL.md, lines 11–18](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-type-system-discipline/SKILL.md#L11-L18).
