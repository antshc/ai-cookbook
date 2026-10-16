# Recipe: Rerunnable Tools and Automated Mechanical Refactors

## Problem

Large or nontrivial hand edits are inconsistent, hard to review, and expensive to reproduce. A small deterministic tool makes the transformation repeatable and turns the procedure into inspectable evidence.

## Example

**Task:** Apply a repository-wide mechanical refactor safely.

**AI Instructions:**

> 1. Perform one representative change by hand to learn the exact transformation and invariants.
> 2. Build the smallest codemod, script, generator, or checker that applies the same transformation deterministically.
> 3. Rerun the tool on the hand-edited unit and diff the result. Fix the tool until both outputs match.
> 4. Make reruns safe and convergent. Preserve explicit do-not-touch fences and fail on ambiguous inputs.
> 5. Use automation instead of manual edits for wide changes, especially changes spanning more than 500 lines.
> 6. Run focused verification after each logical batch. Revert and correct the tool when behavior changes.
> 7. Commit the tool when the work or verification can outlive the session, and report its command and output.

## Best Practices

- Learn the transformation from one concrete unit.
- Keep the automation deterministic and safe to rerun.
- Ship the lever when future reviewers need to reproduce the work.

## Related Recipes

- [Behavior-Preserving Refactoring and Protected Source Blocks](behavior-preserving-refactoring-and-protected-source-blocks.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [principle-build-the-lever](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-build-the-lever/SKILL.md):** Example 1, adapted from [SKILL.md, lines 8–21](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-build-the-lever/SKILL.md#L8-L21).
- **Addy Osmani — [skills/code-simplification/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-simplification/SKILL.md):** Example 1, adapted from [skills/code-simplification/SKILL.md, lines 162–175](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-simplification/SKILL.md#L162-L175).
