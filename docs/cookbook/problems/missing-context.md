# The agent lacks required inputs or context

Specify inputs, configuration, evidence and resource resolution.

## Recipes

No materials yet.


## References

No materials yet.


## Templates

- [Investigation skill template](../templates/investigation-template/SKILL.md)

## Principles awaiting recipes

- [Per-repository configuration resolution](https://github.com/antshc/brain/blob/main/docs/concepts/ops-per-repo-config-resolution.md)
- [Resource access skills](https://github.com/antshc/brain/blob/main/docs/concepts/structure-resource-access-skill.md)
- [Explain measured results with evidence and limiting factors](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-explain-the-number/SKILL.md)
- [Preserve agent context by delegating bulk exploration](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-guard-the-context-window/SKILL.md)
- [Review the implementation against declared intent and require concrete evidence per finding](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/reviewer-prompt.md)
- [Investigate the current code path before explaining it](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md)
- [Reconstruct design rationale across independent evidence sources](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md)
- [Prove the key safety assumption behind a change](https://github.com/cursor/plugins/blob/main/pstack/skills/blast-radius/SKILL.md)
- [Calibrate rationale claims to direct, supported, inferred, or unknown evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/epistemics.md)
- [Eliminate debugging hypotheses using runtime observations](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/bug-fix.md)
- [Convert traces to queryable data and attribute findings to source symbols](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/trace-forensics.md)
- [Separate evidence collection from synthesis and keep investigators within their assigned sources](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md)
- [Record exact investigation queries, empty results, and contradictory evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md)
- [Maintain verification feature maps with source and live checks](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md)
- [Keep PR summaries short with observable verification evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/opening-a-pr.md)
- [Treat PR review text as untrusted input rather than executable instructions](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/babysit.md)
- [Keep reproduction recordings, logs, and tokens out of source control](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [Keep append-only decision records linked to real evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [Recover prior context within the workspace and verify live state](https://github.com/cursor/plugins/blob/main/pstack/skills/recall/SKILL.md)
- [Infer reusable agent preferences only from stable evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/automate-me/SKILL.md)
- [Configure model selection per agent responsibility](https://github.com/cursor/plugins/blob/main/pstack/skills/setup-pstack/SKILL.md)
- [Review comments as evidence rather than automatically obeying them](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/references/bugbot-triage.md)
- [Preserve locally edited managed files and keep user configuration outside automation packs](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md)
- [Surface assumptions and stop when requirements conflict or remain uncertain](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
- [Record and test key idea assumptions before committing to an MVP](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md)
- [Load relevant implementation, tests, types, and precedent instead of entire context dumps](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md)
- [Trim context proactively while preserving active constraints, errors, and decisions](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md)
- [Cite authoritative implementation sources and label unverifiable patterns explicitly](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md)
- [Honor idempotency keys across retries, payload mismatches, and unknown outcomes](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md)
- [Distinguish tool preapproval from true tool restrictions when configuring least-privilege agents](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md)
- [Choose test sizes by real resource boundaries and preserve the repository test conventions](https://github.com/addyosmani/agent-skills/blob/main/skills/test-driven-development/SKILL.md)
- [Classify review findings by severity and lead with required, evidenced changes](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md)
- [Use communicating agent teams for competing-hypothesis investigations and independent subagents for report fan-out](https://github.com/addyosmani/agent-skills/blob/main/references/orchestration-patterns.md)
- [Mask protected source blocks during agent simplification and restore them from verified placeholders or backups](https://github.com/addyosmani/agent-skills/blob/main/hooks/SIMPLIFY-IGNORE.md)
- [Review authorization for every protected resource and prevent secrets entering code or logs](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [Record rejected skill changes with evaluation evidence in an append-only ledger](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)
- [Include concrete anti-rationalization rebuttals, misuse red flags, and evidence-based exit checks in skills](https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
