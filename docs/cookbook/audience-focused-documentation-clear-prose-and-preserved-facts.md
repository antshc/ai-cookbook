# Recipe: Audience-Focused Documentation, Clear Prose, and Preserved Facts

## Problem

Documentation can mix learning and reference needs, bury behavior under function lists, or simplify prose by dropping important facts and uncertainty. Readers need an appropriate structure and faithful explanations.

## Example

**Task:** Rewrite a subsystem guide for engineers preparing to change it.

**AI Instructions:**

> 1. Infer what readers need to do and already know from the task; choose tutorial, how-to, reference, or explanation and split mixed modes into linked documents.
> 2. Read the implementation and decision evidence before explaining behavior and rationale; preserve the source's confidence language.
> 3. Mark facts that must survive: names, units, commands, paths, links, conditions, trade-offs, and uncertainty.
> 4. Start with a plain definition tied to the subsystem. Explain the behavior incrementally with a concrete user flow and a diagram when relationships need it.
> 5. Replace promotional wording, repeated summaries, and generic AI phrasing with concrete information; preserve established technical terms.
> 6. Compare the revision with sources, restore lost caveats, verify examples and commands, and flag unsupported facts rather than strengthening claims.

## Best Practices

- Match structure and depth to the reader's purpose.
- Teach behavior and rationale through concrete steps.
- Preserve facts, trade-offs, and uncertainty.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/teach/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/teach/SKILL.md):** Example 1, adapted from [pstack/skills/teach/SKILL.md, lines 11–17](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/teach/SKILL.md#L11-L17).
- **Lauren Tan (poteto) — [pstack/skills/technical-writing/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md):** Example 1, adapted from [pstack/skills/technical-writing/SKILL.md, lines 34–37](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md#L34-L37).
- **Lauren Tan (poteto) — [pstack/skills/technical-writing/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md):** Example 1, adapted from [pstack/skills/technical-writing/SKILL.md, lines 49–49](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md#L49-L49).
- **Lauren Tan (poteto) — [pstack/skills/unslop/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/unslop/SKILL.md):** Example 1, adapted from [pstack/skills/unslop/SKILL.md, lines 22–27](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/unslop/SKILL.md#L22-L27).
- **Addy Osmani — [skills/documentation-and-adrs/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/documentation-and-adrs/SKILL.md):** Example 1, adapted from [skills/documentation-and-adrs/SKILL.md, lines 263–265](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/documentation-and-adrs/SKILL.md#L263-L265).
