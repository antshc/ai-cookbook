# Recipe: Root-Cause Diagnosis, Hypothesis Elimination, and Premise Checks

## Problem

Repeated symptom fixes can preserve the false premise causing a failure. Diagnosis needs runtime evidence, reduced reproductions, and explicit elimination of competing causes.

## Example

**Task:** Investigate a recurring imbalance that remains after two attempted fixes.

**AI Instructions:**

> 1. State the observed symptom and reproduction steps without presenting a guessed cause as fact.
> 2. Pause feature work while the build or tests are broken. Preserve logs and failing inputs.
> 3. Reduce the failing case. Use history bisection when a known-good revision exists.
> 4. List competing hypotheses. Instrument the running path and eliminate each contradicted hypothesis.
> 5. Write the premise shared by prior failed fixes. Count imbalance per actor with a rerunnable census.
> 6. Find what assigns the skewed role. Remove that asymmetry instead of adding compensation.
> 7. Fix the root cause across matching instances. Add a regression check and resume only after verification passes.

## Best Practices

- Separate symptoms from cause theories.
- Use observations to eliminate hypotheses.
- Question a shared premise after repeated failure.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/principle-attack-the-premise/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-attack-the-premise/SKILL.md):** Example 1, adapted from [pstack/skills/principle-attack-the-premise/SKILL.md, lines 13–17](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-attack-the-premise/SKILL.md#L13-L17).
- **Lauren Tan (poteto) — [pstack/skills/principle-fix-root-causes/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-fix-root-causes/SKILL.md):** Example 1, adapted from [pstack/skills/principle-fix-root-causes/SKILL.md, lines 13–19](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-fix-root-causes/SKILL.md#L13-L19).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/bug-fix.md, lines 7–13](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/bug-fix.md#L7-L13).
- **Lauren Tan (poteto) — [pstack/skills/poteto-help/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-help/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-help/references/prompting.md, lines 15–17](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-help/references/prompting.md#L15-L17).
- **Addy Osmani — [skills/debugging-and-error-recovery/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md):** Example 1, adapted from [skills/debugging-and-error-recovery/SKILL.md, lines 21–34](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md#L21-L34).
- **Addy Osmani — [skills/debugging-and-error-recovery/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md):** Example 1, adapted from [skills/debugging-and-error-recovery/SKILL.md, lines 101–119](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md#L101-L119).
