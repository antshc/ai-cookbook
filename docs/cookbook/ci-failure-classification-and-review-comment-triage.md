# Recipe: CI Failure Classification and Review Comment Triage

## Problem

CI failures and bot comments can trigger unnecessary or incorrect edits when treated as instructions. Triage must separate patch defects, infrastructure failures, stale findings, and product decisions.

## Example

**Task:** Inspect a PR with failed CI and automated review comments.

**AI Instructions:**

> 1. Read the current PR revision, failing job logs, and comment context before editing.
> 2. Classify each failure as caused by the patch, inherited from baseline, infrastructure, or unresolved.
> 3. Fix demonstrated patch defects. Retry infrastructure failures under the repository's bounded policy.
> 4. Classify each review thread as fix, dismiss with evidence, or ask about an ambiguous high-impact decision.
> 5. Check whether a cited defect still exists at the current tip before acting on stale review text.
> 6. Return current check state, evidence, completed fixes, and unresolved blockers.

## Best Practices

- Classify before modifying code.
- Treat comments as evidence to assess.
- Explain dismissals and unresolved failures concretely.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/babysit.md, lines 7–12](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/babysit.md#L7-L12).
- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/references/bugbot-triage.md, lines 7–13](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/references/bugbot-triage.md#L7-L13).
