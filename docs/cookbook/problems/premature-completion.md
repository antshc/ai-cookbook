# The agent stops before work is complete

Define observable completion and account for every obligation.

## Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](../verification-exit-criteria-completeness-sweep.md)
- [Checklist-driven workflow](../checklist-driven-workflow.md)
- [Direct Evidence, Safety Assumptions, and Risk-Based Verification](../direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [Live Verification Harness, Feature Maps, and Instance Lifecycle](../live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [Independent Patch Verification and Baseline Comparison](../independent-patch-verification-and-baseline-comparison.md)
- [Functional-Slice Tests, Observable Results, and Test Boundaries](../functional-slice-tests-observable-results-and-test-boundaries.md)
- [Verification Cost, Changed Scope, and Avoiding Redundant Runs](../verification-cost-changed-scope-and-avoiding-redundant-runs.md)
- [Red-Green-Refactor and Failing Regression Tests](../red-green-refactor-and-failing-regression-tests.md)
- [Live Bug Reproduction and Verification of Existing Fixes](../live-bug-reproduction-and-verification-of-existing-fixes.md)
- [Root-Cause Diagnosis, Hypothesis Elimination, and Premise Checks](../root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [Evidence-Based Retrospectives and Approved Guidance Repairs](../evidence-based-retrospectives-and-approved-guidance-repairs.md)
- [Session Ledger, Open Questions, and Restartable Handoffs](../session-ledger-open-questions-and-restartable-handoffs.md)
- [Safe Pause, Context Recovery, and Verified Resume](../safe-pause-context-recovery-and-verified-resume.md)
- [Instruction Loading and Canary Checks](../instruction-loading-and-canary-checks.md)
- [Skill Discovery, Trigger Indexing, and Native Routing](../skill-discovery-trigger-indexing-and-native-routing.md)
- [Positive and Negative Skill Routing Tests](../positive-and-negative-skill-routing-tests.md)
- [Progressive Disclosure, Targeted Context, and Safe Trimming](../progressive-disclosure-targeted-context-and-safe-trimming.md)
- [Scoped Parallel Workers, Bounded Implementation, and Aggregation](../scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [Delegated Worker Permissions and Centralized External Writes](../delegated-worker-permissions-and-centralized-external-writes.md)
- [Fixed Stop Conditions and Immediate Stop Propagation](../fixed-stop-conditions-and-immediate-stop-propagation.md)
- [Clarify Intent, Surface Assumptions, and Challenge Scope](../clarify-intent-surface-assumptions-and-challenge-scope.md)
- [Explore Alternatives and Test MVP Assumptions](../explore-alternatives-and-test-mvp-assumptions.md)
- [Independent Evidence-Based Review, Severity, and Reconciliation](../independent-evidence-based-review-severity-and-reconciliation.md)
- [User-Visible Bottlenecks, Work Elimination, and Regression Monitoring](../user-visible-bottlenecks-work-elimination-and-regression-monitoring.md)
- [Isolated Browser Profiles and Read-Only Inspection](../isolated-browser-profiles-and-read-only-inspection.md)
- [Version-Matched Official Sources and Cache Revalidation](../version-matched-official-sources-and-cache-revalidation.md)
- [Task-Scoped Staging and Atomic Verified Commits](../task-scoped-staging-and-atomic-verified-commits.md)
- [Consumer Migration, Safe Deprecation, and Legacy Retirement](../consumer-migration-safe-deprecation-and-legacy-retirement.md)
- [Additive Schema Migration and Tested Rollback](../additive-schema-migration-and-tested-rollback.md)
- [Safe Feature Flags and Post-Rollout Cleanup](../safe-feature-flags-and-post-rollout-cleanup.md)
- [Semantic Releases, Tags, and Human Changelogs](../semantic-releases-tags-and-human-changelogs.md)

## References

- [Grouped principle checklist](../grouped-index.md)
- [Combined Recipe Checklist](../combined-recipe-checklist.md)

## Templates

- [Delivery skill template](../templates/delivery-template/SKILL.md)
- [Verification skill template](../templates/verification-template/SKILL.md)

## Principles awaiting recipes

- [Investigate the current code path before explaining it](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md)
- [Keep PR summaries short with observable verification evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/opening-a-pr.md)
- [Gate automatic bug fixing on a trusted triage verdict and ownership checks](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [Frame agent delivery for both the user and the future maintainer](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md)
- [Write a specification before implementation and stop for approval before planning](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [Detect attempts to weaken checks, tests, suppressions, or quality thresholds](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [Implement complete vertical slices with test, verification, and commit gates](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md)
- [Verify responsive and accessible UI states including empty, loading, and error flows](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md)
- [Verify browser changes against live DOM, console, network, and before-after screenshots](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md)
- [Refactor incrementally without changing test expectations to force a pass](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [Run non-bypassable CI quality gates and feed failures back into agent correction](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)
- [Propagate correlation and entry-point identity while bounding telemetry label cardinality](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [Make alerts actionable with runbooks and verify telemetry and notification delivery](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [Use prelaunch gates, staged rollout thresholds, and tested rollback triggers](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)
- [Verify critical user flows and health signals after deployment](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)
- [Default launch decisions to NO-GO for unresolved critical findings unless the operator explicitly accepts the risk](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/ship.md)
- [Pressure-test skill compliance against shortcuts justified by urgency, authority, or sunk cost](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
