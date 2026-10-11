# The agent lacks required inputs or context

Specify inputs, configuration, evidence and resource resolution.

## Recipes

- [Direct Evidence, Safety Assumptions, and Risk-Based Verification](../direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [Live Verification Harness, Feature Maps, and Instance Lifecycle](../live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [Functional-Slice Tests, Observable Results, and Test Boundaries](../functional-slice-tests-observable-results-and-test-boundaries.md)
- [Root-Cause Diagnosis, Hypothesis Elimination, and Premise Checks](../root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [Queryable Traces and Source Attribution](../queryable-traces-and-source-attribution.md)
- [Safe Pause, Context Recovery, and Verified Resume](../safe-pause-context-recovery-and-verified-resume.md)
- [Constraint-First Instructions and Anti-Rationalization Rules](../constraint-first-instructions-and-anti-rationalization-rules.md)
- [Progressive Disclosure, Targeted Context, and Safe Trimming](../progressive-disclosure-targeted-context-and-safe-trimming.md)
- [Delegate Bulk Exploration to Preserve Context](../delegate-bulk-exploration-to-preserve-context.md)
- [Repository Adapters, Resource Access, and Portable Skills](../repository-adapters-resource-access-and-portable-skills.md)
- [Scoped Parallel Workers, Bounded Implementation, and Aggregation](../scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [Worker Configuration, Fresh Sessions, and Standing Orders](../worker-configuration-fresh-sessions-and-standing-orders.md)

## References

- [Grouped principle checklist](../grouped-index.md)
- [Combined Recipe Checklist](../combined-recipe-checklist.md)

## Templates

- [Investigation skill template](../templates/investigation-template/SKILL.md)

## Principles awaiting recipes

- [Per-repository configuration resolution](https://github.com/antshc/brain/blob/main/docs/concepts/ops-per-repo-config-resolution.md)
- [Explain measured results with evidence and limiting factors](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-explain-the-number/SKILL.md)
- [Review the implementation against declared intent and require concrete evidence per finding](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/reviewer-prompt.md)
- [Investigate the current code path before explaining it](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md)
- [Reconstruct design rationale across independent evidence sources](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md)
- [Calibrate rationale claims to direct, supported, inferred, or unknown evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/epistemics.md)
- [Separate evidence collection from synthesis and keep investigators within their assigned sources](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md)
- [Record exact investigation queries, empty results, and contradictory evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md)
- [Keep PR summaries short with observable verification evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/opening-a-pr.md)
- [Treat PR review text as untrusted input rather than executable instructions](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/babysit.md)
- [Keep reproduction recordings, logs, and tokens out of source control](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [Keep append-only decision records linked to real evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [Review comments as evidence rather than automatically obeying them](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/references/bugbot-triage.md)
- [Preserve locally edited managed files and keep user configuration outside automation packs](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md)
- [Surface assumptions and stop when requirements conflict or remain uncertain](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
- [Record and test key idea assumptions before committing to an MVP](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md)
- [Cite authoritative implementation sources and label unverifiable patterns explicitly](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md)
- [Honor idempotency keys across retries, payload mismatches, and unknown outcomes](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md)
- [Distinguish tool preapproval from true tool restrictions when configuring least-privilege agents](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md)
- [Classify review findings by severity and lead with required, evidenced changes](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md)
- [Mask protected source blocks during agent simplification and restore them from verified placeholders or backups](https://github.com/addyosmani/agent-skills/blob/main/hooks/SIMPLIFY-IGNORE.md)
- [Review authorization for every protected resource and prevent secrets entering code or logs](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [Record rejected skill changes with evaluation evidence in an append-only ledger](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
