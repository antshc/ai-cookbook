# Recipe: Trusted Triage, Provenance, Deduplication, and Compensating Writes

## Problem

Automated triage can file duplicates, act on an untrusted verdict, or leave an orphan ticket when its source-thread handoff fails. Provenance, ownership, and compensating actions must survive cross-system writes.

## Example

**Task:** Triage a reported bug and hand it to a guarded fix workflow.

**AI Instructions:**

> 1. Freeze the source channel, root-thread coordinates, and permalink. Verify the source parent exists before any tracker write.
> 2. Trace the reported path, separate facts from hypotheses, check ownership, and search existing issues, commits, and PRs for plausible duplicates.
> 3. Create a ticket only for a live, clearly broken bug or performance issue with no plausible live duplicate, resolved target fields, and an available compensation action.
> 4. Keep delegated analysis read-only and credential-free. Only the coordinator may perform the authorized source-thread handoff.
> 5. Recheck the parent immediately before posting the verdict and verify it landed in the same thread. If a newly created ticket cannot be handed off, compensate and verify cancellation, closure, or deletion; report unverified compensation in the run output.
> 6. Start fixing only from a trusted bug or performance verdict with ownership checks. Missing, conflicting, untrusted, or timed-out verdicts stop the workflow; existing fixes switch it to verification, and an authored fix requires a real reproduced symptom.

## Best Practices

- Freeze provenance and deduplicate before writes.
- Gate fixing on trusted verdict and ownership evidence.
- Verify cross-system handoffs and compensation.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/automations/benny/skills/triage-issue-reports/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/triage-issue-reports/SKILL.md, lines 15–28](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L15-L28).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/triage-issue-reports/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/triage-issue-reports/SKILL.md, lines 175–181](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L175-L181).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/triage-issue-reports/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/triage-issue-reports/SKILL.md, lines 226–228](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L226-L228).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md, lines 15–32](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L15-L32).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md, lines 76–76](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L76-L76).
