# Recipe: Gotchas, Persistent Memory, and Evidence-Based Preferences

## Problem

Agents repeat mistakes when prior lessons are lost, and can turn one isolated correction into a false lasting preference. Memory needs evidence, scoped loading, and one owner for persistence.

## Example

**Task:** Prepare an implementation run from recorded gotchas and update its memory after verification is blocked by a missing CLI.

**AI Instructions:**

> 1. Load supplied repository gotchas before work. Report missing rules and conflicts explicitly.
> 2. Apply the relevant directives during implementation and verification.
> 3. Review actual friction before exit, including partial and blocked results. Discard one-off mistakes and transient first-retry failures.
> 4. Return a rule to check required CLI availability before verification. Refine a matching rule rather than duplicating it.
> 5. Cross-check preference signals across separate history slices. Treat repeated signals as stronger evidence and confirm new intent with the user.
> 6. Preserve unrelated rules and preferences. Return exact replacements or additions to the memory owner.
> 7. Have the owner persist updates before exit. Report persistence failures without claiming the rule was saved.

## Best Practices

- Record actionable directives from observed repeatable friction.
- Use repeated evidence and explicit confirmation for lasting preferences.
- Keep storage ownership centralized and preserve unrelated memory.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [plugins/crew/skills/crew-gotchas/SKILL.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/plugins/crew/skills/crew-gotchas/SKILL.md):** Example 1, adapted from [plugins/crew/skills/crew-gotchas/SKILL.md, lines 8–50](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/plugins/crew/skills/crew-gotchas/SKILL.md#L8-L50).
- **Lauren Tan (poteto) — [pstack/skills/automate-me/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/automate-me/SKILL.md):** Example 1, adapted from [pstack/skills/automate-me/SKILL.md, lines 22–46](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/automate-me/SKILL.md#L22-L46).
