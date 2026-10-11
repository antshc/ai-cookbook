# The agent ignores or reinterprets instructions

Write instructions that survive ambiguity, shortcuts and pressure.

## Recipes

- [Checklist-driven workflow](../checklist-driven-workflow.md)
- [Direct Evidence, Safety Assumptions, and Risk-Based Verification](../direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [Independent Patch Verification and Baseline Comparison](../independent-patch-verification-and-baseline-comparison.md)
- [Functional-Slice Tests, Observable Results, and Test Boundaries](../functional-slice-tests-observable-results-and-test-boundaries.md)
- [Verification Cost, Changed Scope, and Avoiding Redundant Runs](../verification-cost-changed-scope-and-avoiding-redundant-runs.md)
- [Red-Green-Refactor and Failing Regression Tests](../red-green-refactor-and-failing-regression-tests.md)
- [Root-Cause Diagnosis, Hypothesis Elimination, and Premise Checks](../root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [Improvement Flywheel and Enforced Lessons](../improvement-flywheel-and-enforced-lessons.md)
- [Evidence-Based Retrospectives and Approved Guidance Repairs](../evidence-based-retrospectives-and-approved-guidance-repairs.md)
- [Session Ledger, Open Questions, and Restartable Handoffs](../session-ledger-open-questions-and-restartable-handoffs.md)
- [Constraint-First Instructions and Anti-Rationalization Rules](../constraint-first-instructions-and-anti-rationalization-rules.md)
- [Concise Instructions, Explicit Goals, and Model-Neutral Procedures](../concise-instructions-explicit-goals-and-model-neutral-procedures.md)
- [Instruction Loading and Canary Checks](../instruction-loading-and-canary-checks.md)
- [Skill Discovery, Trigger Indexing, and Native Routing](../skill-discovery-trigger-indexing-and-native-routing.md)
- [Progressive Disclosure, Targeted Context, and Safe Trimming](../progressive-disclosure-targeted-context-and-safe-trimming.md)
- [Bounded Agent Roles, Single Ownership, and Composition](../bounded-agent-roles-single-ownership-and-composition.md)
- [Skill-Owned Code and Supporting Files](../skill-owned-code-and-supporting-files.md)
- [Repository Adapters, Resource Access, and Portable Skills](../repository-adapters-resource-access-and-portable-skills.md)
- [Scoped Parallel Workers, Bounded Implementation, and Aggregation](../scoped-parallel-workers-bounded-implementation-and-aggregation.md)
- [Pilot Runs, Rolling Worker Windows, and Progress Monitoring](../pilot-runs-rolling-worker-windows-and-progress-monitoring.md)
- [Reversible Autonomy, Approval Gates, and Uncertain Targets](../reversible-autonomy-approval-gates-and-uncertain-targets.md)
- [Clarify Intent, Surface Assumptions, and Challenge Scope](../clarify-intent-surface-assumptions-and-challenge-scope.md)
- [Consumer-First Design, Public Contracts, and Usage Guides](../consumer-first-design-public-contracts-and-usage-guides.md)
- [Domain Models, Foundational Constraints, and Invalid States](../domain-models-foundational-constraints-and-invalid-states.md)
- [Competing Designs, Prototype Experiments, and Cross-Judging](../competing-designs-prototype-experiments-and-cross-judging.md)
- [Architecture Sketches, Structural Red Flags, and Design Rationale](../architecture-sketches-structural-red-flags-and-design-rationale.md)
- [Independent Evidence-Based Review, Severity, and Reconciliation](../independent-evidence-based-review-severity-and-reconciliation.md)
- [CI Failure Classification and Review Comment Triage](../ci-failure-classification-and-review-comment-triage.md)
- [Reproducible Benchmarks, Frozen Baselines, and Honest Metrics](../reproducible-benchmarks-frozen-baselines-and-honest-metrics.md)
- [User-Visible Bottlenecks, Work Elimination, and Regression Monitoring](../user-visible-bottlenecks-work-elimination-and-regression-monitoring.md)
- [Untrusted Content and Prompt Injection Boundaries](../untrusted-content-and-prompt-injection-boundaries.md)
- [Boundary Validation, Threat Models, and Abuse Cases](../boundary-validation-threat-models-and-abuse-cases.md)
- [Secret Protection, Resource Authorization, and Personal Data Minimization](../secret-protection-resource-authorization-and-personal-data-minimization.md)
- [Isolated Browser Profiles and Read-Only Inspection](../isolated-browser-profiles-and-read-only-inspection.md)
- [Safe Destructive Paths and Dependency Install Controls](../safe-destructive-paths-and-dependency-install-controls.md)

## References

- [Writing agent-facing documents](../agent-skills.instructions.md)
- [Authors & Sources](../authors-and-sources.md)
- [Grouped principle checklist](../grouped-index.md)
- [Combined Recipe Checklist](../combined-recipe-checklist.md)

## Templates

No materials yet.


## Principles awaiting recipes

- [Behavior-preserving agent review](https://github.com/antshc/brain/blob/main/plugins/crew/agents/chorey.agent.md)
- [Build a rerunnable tool for nontrivial work](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-build-the-lever/SKILL.md)
- [Make state-changing operations converge across retries](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-make-operations-idempotent/SKILL.md)
- [Migrate callers and delete obsolete internal APIs together](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md)
- [Sequence changes as independently verifiable units](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-sequence-verifiable-units/SKILL.md)
- [Validate authored skills, referenced files, and structural examples](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md)
- [Pin existing behavior before structural refactoring](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/refactoring.md)
- [Audit decision logs against transcripts and correct false or omitted claims by appending rows](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [Independently review long-running decision trails with a different model family](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [Remove generic AI phrasing while preserving the intended meaning](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md)
- [Run automations from committed operational files rather than copied instructions or caches](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md)
- [Write a specification before implementation and stop for approval before planning](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [Update the living specification before implementing changed decisions](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [Apply a minimum quality floor in noninteractive runs when project thresholds are absent](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [Build dependency-ordered, verifiable task slices without implementing during planning](https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md)
- [Stage only files belonging to the current autonomous task rather than blindly staging every change](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md)
- [Distinguish tool preapproval from true tool restrictions when configuring least-privilege agents](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md)
- [Treat a quality guard that could not run as a blocking failure rather than a clean result](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/references/floor-guard.md)
- [Understand why existing code exists before simplifying or deleting it](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [Automate wide mechanical refactors instead of hand-editing large change sets](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [Create atomic, reviewed commits and verify tests, types, lint, and secrets before commit](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)
- [Migrate schemas additively before destructive changes and test the rollback path](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)
- [Choose telemetry from explicit on-call questions instead of instrumenting indiscriminately](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [Introduce quality checks incrementally in legacy projects rather than enabling the entire lifecycle at once](https://github.com/addyosmani/agent-skills/blob/main/docs/adoption-guide.md)
- [Check existing skills, active proposals, and rejected changes before introducing a new skill](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)

[All problems](../README.md) · [Agent index](../agent-index.json)
