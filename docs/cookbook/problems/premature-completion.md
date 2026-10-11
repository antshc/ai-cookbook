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

## References

- [Grouped principle checklist](../grouped-index.md)
- [Combined Recipe Checklist](../combined-recipe-checklist.md)

## Templates

- [Delivery skill template](../templates/delivery-template/SKILL.md)
- [Verification skill template](../templates/verification-template/SKILL.md)

## Principles awaiting recipes

- [Optimize planned migrations for a verified final state](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-outcome-oriented-execution/SKILL.md)
- [Investigate the current code path before explaining it](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md)
- [Keep PR summaries short with observable verification evidence](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/opening-a-pr.md)
- [Gate automatic bug fixing on a trusted triage verdict and ownership checks](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [Frame agent delivery for both the user and the future maintainer](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md)
- [Surface assumptions and stop when requirements conflict or remain uncertain](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
- [Require explicit confirmation of the restated intent and stop before downstream work](https://github.com/addyosmani/agent-skills/blob/main/skills/interview-me/SKILL.md)
- [Record and test key idea assumptions before committing to an MVP](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md)
- [Write a specification before implementation and stop for approval before planning](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [Detect attempts to weaken checks, tests, suppressions, or quality thresholds](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [Inspect working-tree changes before autonomous execution and stop on unrelated dirty files](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md)
- [Implement complete vertical slices with test, verification, and commit gates](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md)
- [Keep incomplete capabilities behind safe defaults or feature flags](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md)
- [Verify framework-specific decisions against version-matched official documentation](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md)
- [Verify responsive and accessible UI states including empty, loading, and error flows](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md)
- [Verify browser changes against live DOM, console, network, and before-after screenshots](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md)
- [Isolate automated browser tests from personal signed-in browser profiles](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md)
- [Review correctness, readability, architecture, security, and performance, reading tests first](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md)
- [Refactor incrementally without changing test expectations to force a pass](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [Record rejected optimizations and install regression monitors for measured gains](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md)
- [Create atomic, reviewed commits and verify tests, types, lint, and secrets before commit](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)
- [Version consumer-facing releases with tags, semantic versions, and human changelogs](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)
- [Run non-bypassable CI quality gates and feed failures back into agent correction](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)
- [Remove feature flags and dead branches after their rollout finishes](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)
- [Prefer advisory deprecation and provide a production-proven replacement plus migration guidance](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)
- [Migrate schemas additively before destructive changes and test the rollback path](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)
- [Verify old consumers are inactive before deleting a deprecated interface or system](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)
- [Propagate correlation and entry-point identity while bounding telemetry label cardinality](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [Make alerts actionable with runbooks and verify telemetry and notification delivery](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [Use prelaunch gates, staged rollout thresholds, and tested rollback triggers](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)
- [Verify critical user flows and health signals after deployment](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)
- [Default launch decisions to NO-GO for unresolved critical findings unless the operator explicitly accepts the risk](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/ship.md)
- [Pressure-test skill compliance against shortcuts justified by urgency, authority, or sunk cost](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
