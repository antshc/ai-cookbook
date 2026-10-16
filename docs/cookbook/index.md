# Cookbook Principle Index

Tracks reusable AI-agent practices found in this repository and explicitly scanned external sources. A concept, ADR, or skill is evidence of a principle, **not** evidence that a cookbook recipe exists.

- `[x]` — principle has a cookbook recipe; link the recipe.
- `[ ]` — principle found in guidance but has no cookbook recipe; link its source.

## Delivery and learning

- [x] **Verification** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Exit criteria (completeness verification)** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Completeness sweep** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Gotchas** — [recipe](gotchas-and-persistent-memory.md)
- [x] **Persistent memory** — [recipe](gotchas-and-persistent-memory.md)
- [x] **Checklist-driven workflow** — [recipe](checklist-driven-workflow.md)
- [x] **Improvement flywheel (classify and fix observed failures)** — [recipe](improvement-flywheel-and-enforced-lessons.md)
- [x] **Canary rule verification** — [recipe](instruction-loading-and-canary-checks.md)
- [x] **Focused functional-slice testing** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Behavior-preserving agent review** — [recipe](behavior-preserving-refactoring-and-protected-source-blocks.md)

## Instructions and drafting

- [x] **Instruction robustness** — [recipe](constraint-first-instructions-and-anti-rationalization-rules.md)
- [x] **Constraint-first reasoning** — [recipe](constraint-first-instructions-and-anti-rationalization-rules.md)
- [x] **Agent design and bounded responsibility** — [recipe](bounded-agent-roles-single-ownership-and-composition.md)
- [x] **Open-question markers** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md)
- [x] **Repository instruction loading** — [recipe](instruction-loading-and-canary-checks.md)
- [x] **Skill discovery and trigger descriptions** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md)
- [x] **Progressive disclosure of agent guidance** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md)
- [x] **Template ownership of rendering** — [recipe](template-ownership-of-rendering.md)

## Composition and state

- [x] **Skill composition and single ownership** — [recipe](bounded-agent-roles-single-ownership-and-composition.md)
- [x] **Cross-scope specialist discovery** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md)
- [x] **Delegation engine isolation** — [recipe](bounded-agent-roles-single-ownership-and-composition.md)
- [x] **Agent-agnostic handoff contracts** — [recipe](agent-agnostic-contracts-and-structured-cli-handoffs.md)
- [x] **Session ledger** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md)
- [x] **Trigger indexing** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md)
- [x] **Per-repository configuration resolution** — [recipe](repository-configuration-local-edits-and-committed-automation-files.md)
- [x] **Repository adapter skills** — [recipe](repository-adapters-resource-access-and-portable-skills.md)
- [x] **Resource access skills** — [recipe](repository-adapters-resource-access-and-portable-skills.md)
- [x] **Skill-owned code** — [recipe](skill-owned-code-and-supporting-files.md)
- [x] **CLI JSON handoff** — [recipe](agent-agnostic-contracts-and-structured-cli-handoffs.md)

## External scan: cursor/plugins/pstack

Source: [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack), scanned three times on 2026-10-11. These principles link to guidance in another repository. Existing brain entries remain unchanged.

### Design and code principles

- [x] **Question a repeatedly failed premise with an actor census** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Validate and handle errors at system boundaries** — [recipe](boundary-validation-threat-models-and-abuse-cases.md)
- [x] **Build a rerunnable tool for nontrivial work** — [recipe](rerunnable-tools-and-automated-mechanical-refactors.md)
- [x] **Turn recurring corrections into enforced mechanisms** — [recipe](improvement-flywheel-and-enforced-lessons.md)
- [x] **Compare competing prototypes for novel designs** — [recipe](competing-designs-prototype-experiments-and-cross-judging.md)
- [x] **Prioritize consumer experience over implementation convenience** — [recipe](consumer-first-design-public-contracts-and-usage-guides.md)
- [x] **Explain measured results with evidence and limiting factors** — [recipe](reproducible-benchmarks-frozen-baselines-and-honest-metrics.md)
- [x] **Reproduce failures and fix root causes rather than symptoms** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Choose core data shapes and shared foundations before features** — [recipe](domain-models-foundational-constraints-and-invalid-states.md)
- [x] **Preserve agent context by delegating bulk exploration** — [recipe](delegate-bulk-exploration-to-preserve-context.md)
- [x] **Prefer the smallest change and shallowest useful abstraction** — [recipe](subtract-complexity-reduce-reader-load-and-fix-suppressions.md)
- [x] **Make state-changing operations converge across retries** — [recipe](idempotent-operations-retry-keys-and-unknown-outcomes.md)
- [x] **Migrate callers and delete obsolete internal APIs together** — [recipe](consumer-migration-safe-deprecation-and-legacy-retirement.md)
- [x] **Minimize reader load from indirection and mutable state** — [recipe](subtract-complexity-reduce-reader-load-and-fix-suppressions.md)
- [x] **Represent domain invariants in explicit data structures** — [recipe](domain-models-foundational-constraints-and-invalid-states.md)
- [x] **Proceed on reversible work without human blocking** — [recipe](reversible-autonomy-approval-gates-and-uncertain-targets.md)
- [x] **Optimize planned migrations for a verified final state** — [recipe](consumer-migration-safe-deprecation-and-legacy-retirement.md)
- [x] **Prove the real artifact rather than trusting proxies or reports** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Redesign new requirements as foundational constraints** — [recipe](domain-models-foundational-constraints-and-invalid-states.md)
- [x] **Separate shared mutable state before using locks** — [recipe](separate-shared-mutable-state-before-locking.md)
- [ ] **Sequence changes as independently verifiable units** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-sequence-verifiable-units/SKILL.md)
- [x] **Remove dead or redundant complexity before additions** — [recipe](subtract-complexity-reduce-reader-load-and-fix-suppressions.md)
- [x] **Test observable behavior with exact expected results** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Use types to exclude invalid states and exhaust variants** — [recipe](domain-models-foundational-constraints-and-invalid-states.md)

- [x] **Derive architecture contracts from caller usage before implementing** — [recipe](consumer-first-design-public-contracts-and-usage-guides.md)
- [x] **Write a consumer usage guide before implementing a shared API** — [recipe](consumer-first-design-public-contracts-and-usage-guides.md)
- [x] **Reject unnecessary scope instead of reflexively agreeing** — [recipe](clarify-intent-surface-assumptions-and-challenge-scope.md)
- [x] **Replace redundant comments and unsafe suppressions with code fixes** — [recipe](subtract-complexity-reduce-reader-load-and-fix-suppressions.md)
- [ ] **Validate authored skills, referenced files, and structural examples** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md)
- [x] **Repair broken workflow skills in a separate PR from feature work** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md)

- [x] **Make module internals inaccessible and expose only one supported operation path** — [recipe](architecture-sketches-structural-red-flags-and-design-rationale.md)
- [x] **Record design alternatives, accepted tradeoffs, and rationale alongside the chosen contract** — [recipe](architecture-sketches-structural-red-flags-and-design-rationale.md)
- [x] **Review the implementation against declared intent and require concrete evidence per finding** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)

### Understanding and design workflows

- [x] **Investigate the current code path before explaining it** — [recipe](code-path-investigation-and-evidence-calibrated-rationale.md)
- [x] **Reconstruct design rationale across independent evidence sources** — [recipe](code-path-investigation-and-evidence-calibrated-rationale.md)
- [x] **Sketch architecture first and redo it when structural red flags appear** — [recipe](architecture-sketches-structural-red-flags-and-design-rationale.md)
- [x] **Compare independent design candidates with cross-judging** — [recipe](competing-designs-prototype-experiments-and-cross-judging.md)
- [x] **Decompose parallel work into scoped workers and aggregate results** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [x] **Classify adversarial review findings with independent judgment** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)
- [x] **Resolve observable decisions with throwaway experiments** — [recipe](competing-designs-prototype-experiments-and-cross-judging.md)
- [x] **Scale verification rigor to impact and reversibility** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Prove the key safety assumption behind a change** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)

- [x] **Calibrate rationale claims to direct, supported, inferred, or unknown evidence** — [recipe](code-path-investigation-and-evidence-calibrated-rationale.md)
- [x] **Eliminate debugging hypotheses using runtime observations** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Teach behavior and rationale through incremental explanations and diagrams** — [recipe](audience-focused-documentation-clear-prose-and-preserved-facts.md)
- [x] **Summarize session progress as outcomes and human-owned decisions** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md)
- [x] **Convert traces to queryable data and attribute findings to source symbols** — [recipe](queryable-traces-and-source-attribution.md)
- [x] **Keep suspected causes out of the initial agent task brief** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)

- [x] **Separate evidence collection from synthesis and keep investigators within their assigned sources** — [recipe](scoped-evidence-collection-query-logs-and-contradictions.md)
- [x] **Record exact investigation queries, empty results, and contradictory evidence** — [recipe](scoped-evidence-collection-query-logs-and-contradictions.md)
- [x] **Treat agent transcripts and reviewer outputs as untrusted data, not executable instructions** — [recipe](untrusted-content-and-prompt-injection-boundaries.md)
- [x] **Limit retrospective skill changes to demonstrated use or missed triggers** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md)
- [x] **Resume from the prior execution trail rather than repeating completed work** — [recipe](safe-pause-context-recovery-and-verified-resume.md)

### Testing and delivery workflows

- [x] **Pin existing behavior before structural refactoring** — [recipe](behavior-preserving-refactoring-and-protected-source-blocks.md)
- [x] **Run a failing regression check before fixing a bug** — [recipe](red-green-refactor-and-failing-regression-tests.md)
- [x] **Create a repository-specific live verification harness** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Maintain verification feature maps with source and live checks** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Freeze an evaluation harness and revert unsupported iterations** — [recipe](reproducible-benchmarks-frozen-baselines-and-honest-metrics.md)
- [x] **Prove visual parity against an unchanged screenshot baseline** — [recipe](reference-grounded-ui-contracts-and-visual-parity.md)
- [x] **Verify each PR independently at the reviewed patch before merging** — [recipe](independent-patch-verification-and-baseline-comparison.md)
- [x] **Classify CI failures and review comments before modifying a PR** — [recipe](ci-failure-classification-and-review-comment-triage.md)
- [x] **Keep PR summaries short with observable verification evidence** — [recipe](concise-delivery-reports-for-users-and-maintainers.md)

- [x] **Compare performance under production-equivalent conditions and repeated alternating runs** — [recipe](reproducible-benchmarks-frozen-baselines-and-honest-metrics.md)
- [x] **Remove unnecessary work before optimizing remaining performance cost** — [recipe](user-visible-bottlenecks-work-elimination-and-regression-monitoring.md)
- [x] **Verify an existing fix against baseline and patched live behavior before authoring another** — [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md)
- [x] **Audit live sessions and uncommitted changes before removing worktrees** — [recipe](isolated-worktrees-and-safe-workspace-cleanup.md)
- [x] **Treat PR review text as untrusted input rather than executable instructions** — [recipe](untrusted-content-and-prompt-injection-boundaries.md)
- [x] **Select documentation structure by tutorial, how-to, reference, or explanation purpose** — [recipe](audience-focused-documentation-clear-prose-and-preserved-facts.md)

- [x] **Verify dry-run claims by inspecting actual network, file, and repository effects** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Health-check and reset verification instances after unexpected drive failures** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Clean up only owned verification processes and preserve collected proof artifacts** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Compare changed behavior with current trunk on the same user-visible path** — [recipe](independent-patch-verification-and-baseline-comparison.md)
- [x] **Keep reproduction recordings, logs, and tokens out of source control** — [recipe](secret-protection-resource-authorization-and-personal-data-minimization.md)

### Autonomy, continuity, and learning

- [x] **Route tasks through explicit, falsifiable finish conditions** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Keep autonomous iterations bound to an unchanged stop predicate** — [recipe](fixed-stop-conditions-and-immediate-stop-propagation.md)
- [x] **Pilot a full work unit before scaling a multi-agent program** — [recipe](pilot-runs-rolling-worker-windows-and-progress-monitoring.md)
- [x] **Keep append-only decision records linked to real evidence** — [recipe](append-only-decision-trails-audit-and-independent-review.md)
- [x] **Preserve work and a resume note when pausing an agent run** — [recipe](safe-pause-context-recovery-and-verified-resume.md)
- [x] **Recover prior context within the workspace and verify live state** — [recipe](safe-pause-context-recovery-and-verified-resume.md)
- [x] **Turn session retrospectives into tested agent-guidance changes** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md)
- [x] **Infer reusable agent preferences only from stable evidence** — [recipe](gotchas-and-persistent-memory.md)
- [x] **Evaluate agent instructions with blinded candidates and judges** — [recipe](controlled-skill-evaluations-observable-traces-and-repeated-trials.md)
- [x] **Configure model selection per agent responsibility** — [recipe](worker-configuration-fresh-sessions-and-standing-orders.md)

- [x] **Delegate implementation with bounded files and success criteria, then review the diff** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [x] **Start fresh subagents with consolidated instructions unless local state requires a resume** — [recipe](worker-configuration-fresh-sessions-and-standing-orders.md)
- [x] **Carry immutable standing orders into every worker spawn and resume** — [recipe](worker-configuration-fresh-sessions-and-standing-orders.md)
- [x] **Keep orchestration and code-writing responsibilities with separate owners** — [recipe](bounded-agent-roles-single-ownership-and-composition.md)
- [x] **Refill a rolling worker window instead of waiting for whole batches** — [recipe](pilot-runs-rolling-worker-windows-and-progress-monitoring.md)
- [x] **Judge agent progress by actual side effects and replace stalled workers** — [recipe](pilot-runs-rolling-worker-windows-and-progress-monitoring.md)
- [ ] **Validate multi-phase plans with an executable checker before handoff** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md)
- [x] **Wait for an explicit operator go before executing an approved plan** — [recipe](reversible-autonomy-approval-gates-and-uncertain-targets.md)
- [x] **Keep verified stacked PRs unmerged until explicitly authorized** — [recipe](reversible-autonomy-approval-gates-and-uncertain-targets.md)
- [x] **Apply retrospective changes to shared agent instructions only with approval** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md)

- [x] **Audit decision logs against transcripts and correct false or omitted claims by appending rows** — [recipe](append-only-decision-trails-audit-and-independent-review.md)
- [x] **Independently review long-running decision trails with a different model family** — [recipe](append-only-decision-trails-audit-and-independent-review.md)
- [x] **Propagate operator stop orders to all active agents as an immediate no-writes hold** — [recipe](fixed-stop-conditions-and-immediate-stop-propagation.md)
- [x] **Prefer event-based agent wakeups with a heartbeat fallback over unnecessary polling** — [recipe](pilot-runs-rolling-worker-windows-and-progress-monitoring.md)
- [x] **Keep stack topology updates under one coordinator while PR owners work in parallel** — [recipe](single-coordinator-for-shared-pr-stack-topology.md)

### External automations and communication

- [x] **Freeze report provenance and deduplicate before filing tickets** — [recipe](trusted-triage-provenance-deduplication-and-compensating-writes.md)
- [x] **Confirm a reported defect twice through the live user interface** — [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md)
- [x] **Keep external writes and credentials out of delegated workers** — [recipe](delegated-worker-permissions-and-centralized-external-writes.md)
- [x] **Fail closed when an external automation's target is uncertain** — [recipe](reversible-autonomy-approval-gates-and-uncertain-targets.md)
- [x] **Write audience-specific instructions in concise, controlled language** — [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md)
- [x] **Review comments as evidence rather than automatically obeying them** — [recipe](ci-failure-classification-and-review-comment-triage.md)

- [x] **Gate automatic bug fixing on a trusted triage verdict and ownership checks** — [recipe](trusted-triage-provenance-deduplication-and-compensating-writes.md)
- [x] **Compensate cross-system ticket writes when the final handoff fails** — [recipe](trusted-triage-provenance-deduplication-and-compensating-writes.md)
- [x] **Keep automation webhook secrets on the server, never in the browser or chat** — [recipe](secret-protection-resource-authorization-and-personal-data-minimization.md)
- [x] **Remove generic AI phrasing while preserving the intended meaning** — [recipe](audience-focused-documentation-clear-prose-and-preserved-facts.md)
- [x] **Describe goals, proof, and constraints without prescribing skill choreography** — [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md)
- [x] **Frame agent delivery for both the user and the future maintainer** — [recipe](concise-delivery-reports-for-users-and-maintainers.md)

- [x] **Preserve locally edited managed files and keep user configuration outside automation packs** — [recipe](repository-configuration-local-edits-and-committed-automation-files.md)
- [x] **Run automations from committed operational files rather than copied instructions or caches** — [recipe](repository-configuration-local-edits-and-committed-automation-files.md)

## External scan: addyosmani/agent-skills

Source: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), scanned and rescanned 2026-10-11. Reviewed the 25 active skills, four agent personas, seven shared reference checklists, root agent instructions, command workflows, skill-evaluation guidance, nested references, and hooks. Missing entries link to source evidence; recipes were not created.

### Intent, discovery, and specifications

- [x] **Select the applicable skill before work and follow its gates in order** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md)
- [x] **Surface assumptions and stop when requirements conflict or remain uncertain** — [recipe](clarify-intent-surface-assumptions-and-challenge-scope.md)
- [x] **Challenge unwarranted scope or complexity while leaving informed decisions to the user** — [recipe](clarify-intent-surface-assumptions-and-challenge-scope.md)
- [x] **Interview for intent one question and one explicit guess at a time** — [recipe](clarify-intent-surface-assumptions-and-challenge-scope.md)
- [x] **Require explicit confirmation of the restated intent and stop before downstream work** — [recipe](clarify-intent-surface-assumptions-and-challenge-scope.md)
- [x] **Diverge into alternatives before converging on an evaluated idea** — [recipe](explore-alternatives-and-test-mvp-assumptions.md)
- [x] **Record and test key idea assumptions before committing to an MVP** — [recipe](explore-alternatives-and-test-mvp-assumptions.md)
- [ ] **Approve the capability dependency map before specifying a multi-module initiative** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [ ] **Write a specification before implementation and stop for approval before planning** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [ ] **Update the living specification before implementing changed decisions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [x] **Define measurable project quality thresholds and record exceptions with owners and expiry** — [recipe](quality-floors-measurable-thresholds-and-controlled-exceptions.md)
- [x] **Apply a minimum quality floor in noninteractive runs when project thresholds are absent** — [recipe](quality-floors-measurable-thresholds-and-controlled-exceptions.md)
- [x] **Detect attempts to weaken checks, tests, suppressions, or quality thresholds** — [recipe](non-bypassable-quality-gates-and-fail-closed-verification.md)
- [x] **Place verification checks according to execution cost and scope expensive checks to changed code** — [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md)
- [ ] **Build dependency-ordered, verifiable task slices without implementing during planning** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md)
- [x] **Preserve incomplete plans and use the project's designated task tracker** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md)

- [x] **Inspect working-tree changes before autonomous execution and stop on unrelated dirty files** — [recipe](task-scoped-staging-and-atomic-verified-commits.md)
- [x] **Escalate irreversible or high-risk work for fresh human approval even during an approved autonomous run** — [recipe](reversible-autonomy-approval-gates-and-uncertain-targets.md)

### Implementation, context, and independent judgment

- [ ] **Implement complete vertical slices with test, verification, and commit gates** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md)
- [x] **Keep incomplete capabilities behind safe defaults or feature flags** — [recipe](safe-feature-flags-and-post-rollout-cleanup.md)
- [x] **Do not repeat unchanged verification commands without intervening changes** — [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md)
- [x] **Load relevant implementation, tests, types, and precedent instead of entire context dumps** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md)
- [x] **Trim context proactively while preserving active constraints, errors, and decisions** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md)
- [x] **Persist restartable session handoffs with decisions, changed files, verification, and next work** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md)
- [x] **Verify framework-specific decisions against version-matched official documentation** — [recipe](version-matched-official-sources-and-cache-revalidation.md)
- [x] **Cite authoritative implementation sources and label unverifiable patterns explicitly** — [recipe](version-matched-official-sources-and-cache-revalidation.md)
- [x] **Independently doubt nontrivial claims using only the artifact and contract, not the author's conclusion** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)
- [x] **Reconcile reviewer findings rather than accepting them verbatim, with a bounded review loop** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)
- [x] **Require explicit authorization for each external cross-model review invocation** — [recipe](reversible-autonomy-approval-gates-and-uncertain-targets.md)
- [x] **Define public contracts before implementation and preserve observable consumer behavior** — [recipe](consumer-first-design-public-contracts-and-usage-guides.md)
- [x] **Honor idempotency keys across retries, payload mismatches, and unknown outcomes** — [recipe](idempotent-operations-retry-keys-and-unknown-outcomes.md)
- [x] **Define a reference-grounded UI design contract before implementation** — [recipe](reference-grounded-ui-contracts-and-visual-parity.md)
- [x] **Verify responsive and accessible UI states including empty, loading, and error flows** — [recipe](live-browser-evidence-accessibility-and-ui-state-coverage.md)

- [x] **Stage only files belonging to the current autonomous task rather than blindly staging every change** — [recipe](task-scoped-staging-and-atomic-verified-commits.md)
- [x] **Avoid installing a second always-on skill router when the agent host already routes skills natively** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md)
- [x] **Keep reusable skills separate from repository-specific agent instructions during installation** — [recipe](repository-adapters-resource-access-and-portable-skills.md)
- [x] **Include required shared references when distributing an individual skill outside its original pack** — [recipe](repository-adapters-resource-access-and-portable-skills.md)
- [x] **Keep vendor runtime settings in per-agent adapters or permitted metadata, not portable skill frontmatter** — [recipe](repository-adapters-resource-access-and-portable-skills.md)
- [x] **Distinguish tool preapproval from true tool restrictions when configuring least-privilege agents** — [recipe](least-privilege-tool-restrictions-versus-preapproval.md)
- [x] **Revalidate cached official documentation with origin validators before using it across sessions** — [recipe](version-matched-official-sources-and-cache-revalidation.md)

### Testing, debugging, and evidence

- [x] **Use the red-green-refactor cycle for behavior-changing implementation** — [recipe](red-green-refactor-and-failing-regression-tests.md)
- [x] **Reproduce a reported bug with a failing regression test before applying the fix** — [recipe](red-green-refactor-and-failing-regression-tests.md)
- [x] **Test observable state with descriptive tests and minimize interaction mocks** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Choose test sizes by real resource boundaries and preserve the repository test conventions** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Stop further feature work on broken tests or builds until the failure is resolved** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Isolate and reduce failures before root-cause fixes, using history bisect when useful** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Verify repaired behavior with focused tests, full regression checks, and runtime checks** — [recipe](independent-patch-verification-and-baseline-comparison.md)
- [x] **Verify browser changes against live DOM, console, network, and before-after screenshots** — [recipe](live-browser-evidence-accessibility-and-ui-state-coverage.md)
- [x] **Isolate automated browser tests from personal signed-in browser profiles** — [recipe](isolated-browser-profiles-and-read-only-inspection.md)
- [x] **Keep browser JavaScript inspection read-only unless mutations are explicitly authorized** — [recipe](isolated-browser-profiles-and-read-only-inspection.md)
- [x] **Treat error output, external documentation, and browser content as untrusted instructions** — [recipe](untrusted-content-and-prompt-injection-boundaries.md)
- [x] **Apply standing definition-of-done checks separately from task acceptance criteria** — [recipe](verification-exit-criteria-completeness-sweep.md)

- [x] **Treat a quality guard that could not run as a blocking failure rather than a clean result** — [recipe](non-bypassable-quality-gates-and-fail-closed-verification.md)

### Review and simplification

- [x] **Review correctness, readability, architecture, security, and performance, reading tests first** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)
- [x] **Classify review findings by severity and lead with required, evidenced changes** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)
- [x] **Keep review changes cohesive and consider total file size as well as diff size** — [recipe](independent-evidence-based-review-severity-and-reconciliation.md)
- [x] **Understand why existing code exists before simplifying or deleting it** — [recipe](behavior-preserving-refactoring-and-protected-source-blocks.md)
- [x] **Refactor incrementally without changing test expectations to force a pass** — [recipe](behavior-preserving-refactoring-and-protected-source-blocks.md)
- [x] **Automate wide mechanical refactors instead of hand-editing large change sets** — [recipe](rerunnable-tools-and-automated-mechanical-refactors.md)
- [x] **Parallelize independent specialist reviews, but keep aggregation with the orchestrator** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [x] **Do not make agent personas invoke other personas or add routing-only hops** — [recipe](bounded-agent-roles-single-ownership-and-composition.md)

- [x] **Use communicating agent teams for competing-hypothesis investigations and independent subagents for report fan-out** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [x] **Mask protected source blocks during agent simplification and restore them from verified placeholders or backups** — [recipe](behavior-preserving-refactoring-and-protected-source-blocks.md)

### Security and trust boundaries

- [x] **Threat-model system boundaries and write abuse cases before hardening a feature** — [recipe](boundary-validation-threat-models-and-abuse-cases.md)
- [x] **Validate external and model-generated data at the boundary before using it as code or decisions** — [recipe](boundary-validation-threat-models-and-abuse-cases.md)
- [x] **Guard destructive operations against paths controlled by untrusted upstream processes** — [recipe](safe-destructive-paths-and-dependency-install-controls.md)
- [x] **Block unreviewed dependency install scripts and audit the committed lockfile** — [recipe](safe-destructive-paths-and-dependency-install-controls.md)
- [x] **Review authorization for every protected resource and prevent secrets entering code or logs** — [recipe](secret-protection-resource-authorization-and-personal-data-minimization.md)
- [x] **Classify personal data by purpose and exclude unnecessary personal information from telemetry** — [recipe](secret-protection-resource-authorization-and-personal-data-minimization.md)

### Performance, delivery, and operation

- [x] **Measure user-visible performance and identify its bottleneck before optimizing** — [recipe](user-visible-bottlenecks-work-elimination-and-regression-monitoring.md)
- [x] **Compare one optimization against an equivalent baseline and revert unproven changes** — [recipe](reproducible-benchmarks-frozen-baselines-and-honest-metrics.md)
- [x] **Record rejected optimizations and install regression monitors for measured gains** — [recipe](user-visible-bottlenecks-work-elimination-and-regression-monitoring.md)
- [x] **Never invent web performance scores without actual measurement artifacts** — [recipe](reproducible-benchmarks-frozen-baselines-and-honest-metrics.md)
- [x] **Create atomic, reviewed commits and verify tests, types, lint, and secrets before commit** — [recipe](task-scoped-staging-and-atomic-verified-commits.md)
- [x] **Use isolated worktrees when parallel agents would otherwise share a working tree** — [recipe](isolated-worktrees-and-safe-workspace-cleanup.md)
- [x] **Version consumer-facing releases with tags, semantic versions, and human changelogs** — [recipe](semantic-releases-tags-and-human-changelogs.md)
- [x] **Run non-bypassable CI quality gates and feed failures back into agent correction** — [recipe](non-bypassable-quality-gates-and-fail-closed-verification.md)
- [x] **Remove feature flags and dead branches after their rollout finishes** — [recipe](safe-feature-flags-and-post-rollout-cleanup.md)
- [x] **Prefer advisory deprecation and provide a production-proven replacement plus migration guidance** — [recipe](consumer-migration-safe-deprecation-and-legacy-retirement.md)
- [x] **Migrate schemas additively before destructive changes and test the rollback path** — [recipe](additive-schema-migration-and-tested-rollback.md)
- [x] **Verify old consumers are inactive before deleting a deprecated interface or system** — [recipe](consumer-migration-safe-deprecation-and-legacy-retirement.md)
- [x] **Record architecture decisions with alternatives and supersede rather than erase old ADRs** — [recipe](architecture-decision-records-alternatives-and-supersession.md)
- [x] **Preserve factual details and uncertainty when simplifying documentation prose** — [recipe](audience-focused-documentation-clear-prose-and-preserved-facts.md)
- [x] **Choose telemetry from explicit on-call questions instead of instrumenting indiscriminately** — [recipe](question-driven-telemetry-correlation-and-actionable-alerts.md)
- [x] **Propagate correlation and entry-point identity while bounding telemetry label cardinality** — [recipe](question-driven-telemetry-correlation-and-actionable-alerts.md)
- [x] **Make alerts actionable with runbooks and verify telemetry and notification delivery** — [recipe](question-driven-telemetry-correlation-and-actionable-alerts.md)
- [x] **Use prelaunch gates, staged rollout thresholds, and tested rollback triggers** — [recipe](launch-gates-staged-rollout-health-checks-and-rollback.md)
- [x] **Verify critical user flows and health signals after deployment** — [recipe](launch-gates-staged-rollout-health-checks-and-rollback.md)
- [x] **Introduce quality checks incrementally in legacy projects rather than enabling the entire lifecycle at once** — [recipe](quality-floors-measurable-thresholds-and-controlled-exceptions.md)
- [x] **Keep skill entrypoints concise with trigger descriptions and load long references on demand** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md)

- [x] **Default launch decisions to NO-GO for unresolved critical findings unless the operator explicitly accepts the risk** — [recipe](launch-gates-staged-rollout-health-checks-and-rollback.md)

### Skill authoring and evaluation (second pass)

- [ ] **Check existing skills, active proposals, and rejected changes before introducing a new skill** — [source](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)
- [ ] **Record rejected skill changes with evaluation evidence in an append-only ledger** — [source](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)
- [x] **Write skill procedures in model-neutral capabilities instead of model-specific workarounds** — [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md)
- [x] **Include concrete anti-rationalization rebuttals, misuse red flags, and evidence-based exit checks in skills** — [recipe](constraint-first-instructions-and-anti-rationalization-rules.md)
- [x] **Test skill routing with realistic positive triggers and neighboring negative triggers** — [recipe](positive-and-negative-skill-routing-tests.md)
- [x] **For negative routing tests, require the intended owner skill to outrank the wrong skill** — [recipe](positive-and-negative-skill-routing-tests.md)
- [x] **Evaluate skill behavior using isolated executable fixtures and full tool traces rather than claimed intentions** — [recipe](controlled-skill-evaluations-observable-traces-and-repeated-trials.md)
- [x] **Use dialogue-only evaluations only when conversation itself is the skill's deliverable** — [recipe](controlled-skill-evaluations-observable-traces-and-repeated-trials.md)
- [x] **Pressure-test skill compliance against shortcuts justified by urgency, authority, or sunk cost** — [recipe](pressure-tests-for-instruction-compliance.md)
- [x] **Run skill-on versus skill-off evaluations and score observable output rather than invocation alone** — [recipe](controlled-skill-evaluations-observable-traces-and-repeated-trials.md)
- [x] **Pin model and runtime versions and repeat trials before drawing conclusions from stochastic skill routing** — [recipe](controlled-skill-evaluations-observable-traces-and-repeated-trials.md)
- [x] **Validate that equivalent host command adapters stay semantically aligned** — [recipe](repository-adapters-resource-access-and-portable-skills.md)

## Scan and update

1. Scan current `ARCHITECTURE.md`, `docs/concepts/`, `docs/adr/`, `.github/instructions/`, and active agents and skills in `plugins/` and `skills/`. Ignore `_backup/` and `_in-progress/`.
2. Extract reusable **AI-agent behavior principles** supported by an explicit source rule. Merge synonyms and duplicate occurrences into one checklist entry.
3. Compare each principle with the recipes in `docs/cookbook/` (excluding this index). Check the box **only** when a recipe actually covers the principle with actionable AI instructions, and link that recipe. Otherwise leave it unchecked and link the source.
4. Add newly found principles; recheck existing entries and links. Do not mark a principle covered merely because its source document exists.
5. For external repositories, retain links to the original source. Check coverage only against local cookbook recipes.

