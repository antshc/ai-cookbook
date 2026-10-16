# Recipe: Architecture Sketches, Structural Red Flags, and Design Rationale

## Problem

An architecture sketch can hide shallow interfaces, leaked internals, or unsupported tradeoffs. Design needs structural screening and a rationale beside the contract.

## Example

**Task:** Sketch a shared search module before implementing it.

**AI Instructions:**

> 1. Write caller usage first, then derive the module map, core types, and signatures.
> 2. Screen the sketch for shallow modules, leaked representation, pass-through layers, split ownership, and duplicate operation paths.
> 3. Revise the shape before implementation when a structural red flag remains.
> 4. Expose one supported operation path and make private internals unimportable from callers.
> 5. Record the chosen shape, encoded invariants, accepted tradeoffs, and open risks.
> 6. Compare concrete alternative shapes by caller complexity and interface depth. State why each lost.

## Best Practices

- Screen structure before coding.
- Keep rationale beside the contract.
- Enforce public boundaries in the module system.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/architect/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md):** Example 1, adapted from [pstack/skills/architect/SKILL.md, lines 79–79](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md#L79-L79).
- **Lauren Tan (poteto) — [pstack/skills/architect/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md):** Example 1, adapted from [pstack/skills/architect/references/design-red-flags.md, lines 35–51](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/references/design-red-flags.md#L35-L51).
- **Lauren Tan (poteto) — [pstack/skills/architect/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md):** Example 1, adapted from [pstack/skills/architect/references/rationale-template.md, lines 9–31](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/references/rationale-template.md#L9-L31).
