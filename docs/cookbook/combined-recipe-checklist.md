# Combined Recipe Checklist

**Progress: 2/82 recipes complete; 8/244 principles covered.**

This backlog maps all 244 original principles exactly once. Coverage is checked only after the assigned recipe contains actionable instructions.

## Grouping rule

Combine principles when they address the same agent failure and can be taught as one practical workflow. Preserve distinct checks, responsibilities, and gates within that recipe, as in [Verification, Exit Criteria, and Completeness Sweep](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/verification-exit-criteria-completeness-sweep.md). Broad topic categories organize navigation; they do not automatically become one recipe.

A recipe must remain usable with one or two examples under the [draft-recipe skill](https://github.com/antshc/brain/blob/main/.github/skills/draft-recipe/SKILL.md). Source inspection during drafting may show that a proposed recipe needs splitting; report that change before increasing the approved count.

## Checklist legend

- `[ ] NEW`: write a new recipe.
- `[ ] EXTEND`: expand an existing recipe; existing coverage stays checked in the principle index.
- `[x] KEEP`: retain an existing recipe.
- The number in parentheses is the assigned original principle count, not the number of examples.

## Recipe checklist

### Completion

- [x] **R01. Verification, Exit Criteria, Completeness Sweep, and Definition of Done** — EXTEND (5 principles); [existing recipe](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/verification-exit-criteria-completeness-sweep.md). [recipe](verification-exit-criteria-completeness-sweep.md).
### Verification and testing

- [x] **R02. Direct Evidence, Safety Assumptions, and Risk-Based Verification** — NEW (4 principles). [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md).
- [x] **R03. Live Verification Harness, Feature Maps, and Instance Lifecycle** — NEW (4 principles). [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md).
- [x] **R04. Independent Patch Verification and Baseline Comparison** — NEW (3 principles). [recipe](independent-patch-verification-and-baseline-comparison.md).
- [x] **R05. Functional-Slice Tests, Observable Results, and Test Boundaries** — NEW (4 principles). [recipe](functional-slice-tests-observable-results-and-test-boundaries.md).
- [x] **R06. Verification Cost, Changed Scope, and Avoiding Redundant Runs** — NEW (2 principles). [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md).
- [x] **R07. Red-Green-Refactor and Failing Regression Tests** — NEW (3 principles). [recipe](red-green-refactor-and-failing-regression-tests.md).
- [x] **R08. Live Bug Reproduction and Verification of Existing Fixes** — NEW (2 principles). [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md).
### Diagnosis

- [x] **R09. Root-Cause Diagnosis, Hypothesis Elimination, and Premise Checks** — NEW (6 principles). [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).
- [x] **R10. Queryable Traces and Source Attribution** — NEW (1 principles). [recipe](queryable-traces-and-source-attribution.md).
### Learning and continuity

- [x] **R11. Gotchas, Persistent Memory, and Evidence-Based Preferences** — EXTEND (3 principles); [existing recipe](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/gotchas-and-persistent-memory.md). [recipe](gotchas-and-persistent-memory.md).
- [x] **R12. Improvement Flywheel and Enforced Lessons** — NEW (2 principles). [recipe](improvement-flywheel-and-enforced-lessons.md).
- [x] **R13. Evidence-Based Retrospectives and Approved Guidance Repairs** — NEW (4 principles). [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md).
- [x] **R14. Checklist-Driven Workflow** — KEEP (1 principles); [existing recipe](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/checklist-driven-workflow.md).
- [x] **R15. Session Ledger, Open Questions, and Restartable Handoffs** — NEW (5 principles). [recipe](session-ledger-open-questions-and-restartable-handoffs.md).
- [x] **R16. Safe Pause, Context Recovery, and Verified Resume** — NEW (3 principles). [recipe](safe-pause-context-recovery-and-verified-resume.md).
### Instructions and routing

- [x] **R17. Constraint-First Instructions and Anti-Rationalization Rules** — NEW (3 principles). [recipe](constraint-first-instructions-and-anti-rationalization-rules.md).
- [x] **R18. Concise Instructions, Explicit Goals, and Model-Neutral Procedures** — NEW (3 principles). [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md).
- [x] **R19. Instruction Loading and Canary Checks** — NEW (2 principles). [recipe](instruction-loading-and-canary-checks.md).
- [x] **R20. Skill Discovery, Trigger Indexing, and Native Routing** — NEW (5 principles). [recipe](skill-discovery-trigger-indexing-and-native-routing.md).
- [x] **R21. Positive and Negative Skill Routing Tests** — NEW (2 principles). [recipe](positive-and-negative-skill-routing-tests.md).
- [x] **R22. Progressive Disclosure, Targeted Context, and Safe Trimming** — NEW (4 principles). [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md).
- [x] **R23. Delegate Bulk Exploration to Preserve Context** — NEW (1 principles). [recipe](delegate-bulk-exploration-to-preserve-context.md).
### Ownership and delegation

- [x] **R24. Bounded Agent Roles, Single Ownership, and Composition** — NEW (5 principles). [recipe](bounded-agent-roles-single-ownership-and-composition.md).
- [x] **R25. Template Ownership of Rendering** — NEW (1 principles). [recipe](template-ownership-of-rendering.md).
- [x] **R26. Skill-Owned Code and Supporting Files** — NEW (1 principles). [recipe](skill-owned-code-and-supporting-files.md).
- [x] **R27. Repository Adapters, Resource Access, and Portable Skills** — NEW (6 principles). [recipe](repository-adapters-resource-access-and-portable-skills.md).
- [x] **R28. Agent-Agnostic Contracts and Structured CLI Handoffs** — NEW (2 principles). [recipe](agent-agnostic-contracts-and-structured-cli-handoffs.md).
- [x] **R29. Scoped Parallel Workers, Bounded Implementation, and Aggregation** — NEW (4 principles). [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md).
- [x] **R30. Delegated Worker Permissions and Centralized External Writes** — NEW (1 principles). [recipe](delegated-worker-permissions-and-centralized-external-writes.md).
### Worker lifecycle and autonomy

- [x] **R31. Worker Configuration, Fresh Sessions, and Standing Orders** — NEW (3 principles). [recipe](worker-configuration-fresh-sessions-and-standing-orders.md).
- [ ] **R32. Pilot Runs, Rolling Worker Windows, and Progress Monitoring** — NEW (4 principles).
- [ ] **R33. Single Coordinator for Shared PR Stack Topology** — NEW (1 principles).
- [ ] **R34. Fixed Stop Conditions and Immediate Stop Propagation** — NEW (2 principles).
- [ ] **R35. Reversible Autonomy, Approval Gates, and Uncertain Targets** — NEW (6 principles).
### Intent and design

- [ ] **R36. Clarify Intent, Surface Assumptions, and Challenge Scope** — NEW (5 principles).
- [ ] **R37. Explore Alternatives and Test MVP Assumptions** — NEW (2 principles).
- [ ] **R38. Consumer-First Design, Public Contracts, and Usage Guides** — NEW (4 principles).
- [ ] **R39. Domain Models, Foundational Constraints, and Invalid States** — NEW (4 principles).
- [ ] **R40. Competing Designs, Prototype Experiments, and Cross-Judging** — NEW (3 principles).
- [ ] **R41. Architecture Sketches, Structural Red Flags, and Design Rationale** — NEW (3 principles).
### Review

- [ ] **R42. Independent Evidence-Based Review, Severity, and Reconciliation** — NEW (7 principles).
- [ ] **R43. CI Failure Classification and Review Comment Triage** — NEW (2 principles).
### Performance

- [ ] **R44. Reproducible Benchmarks, Frozen Baselines, and Honest Metrics** — NEW (5 principles).
- [ ] **R45. User-Visible Bottlenecks, Work Elimination, and Regression Monitoring** — NEW (3 principles).
### Trust and security

- [ ] **R46. Untrusted Content and Prompt Injection Boundaries** — NEW (3 principles).
- [ ] **R47. Boundary Validation, Threat Models, and Abuse Cases** — NEW (3 principles).
- [ ] **R48. Secret Protection, Resource Authorization, and Personal Data Minimization** — NEW (4 principles).
- [ ] **R49. Isolated Browser Profiles and Read-Only Inspection** — NEW (2 principles).
- [ ] **R50. Safe Destructive Paths and Dependency Install Controls** — NEW (2 principles).
### Configuration and Git

- [ ] **R51. Repository Configuration, Local Edits, and Committed Automation Files** — NEW (3 principles).
- [ ] **R52. Least-Privilege Tool Restrictions versus Preapproval** — NEW (1 principles).
- [ ] **R53. Version-Matched Official Sources and Cache Revalidation** — NEW (3 principles).
- [ ] **R54. Task-Scoped Staging and Atomic Verified Commits** — NEW (3 principles).
- [ ] **R55. Isolated Worktrees and Safe Workspace Cleanup** — NEW (2 principles).
### Migration and release

- [ ] **R56. Consumer Migration, Safe Deprecation, and Legacy Retirement** — NEW (4 principles).
- [ ] **R57. Additive Schema Migration and Tested Rollback** — NEW (1 principles).
- [ ] **R58. Safe Feature Flags and Post-Rollout Cleanup** — NEW (2 principles).
- [ ] **R59. Semantic Releases, Tags, and Human Changelogs** — NEW (1 principles).
- [ ] **R60. Launch Gates, Staged Rollout, Health Checks, and Rollback** — NEW (3 principles).
### Operations and evaluation

- [ ] **R61. Question-Driven Telemetry, Correlation, and Actionable Alerts** — NEW (3 principles).
- [ ] **R62. Controlled Skill Evaluations, Observable Traces, and Repeated Trials** — NEW (5 principles).
- [ ] **R63. Pressure Tests for Instruction Compliance** — NEW (1 principles).
### Documentation and evidence

- [ ] **R64. Audience-Focused Documentation, Clear Prose, and Preserved Facts** — NEW (4 principles).
- [ ] **R65. Concise Delivery Reports for Users and Maintainers** — NEW (2 principles).
- [ ] **R66. Append-Only Decision Trails, Audit, and Independent Review** — NEW (3 principles).
- [ ] **R67. Architecture Decision Records, Alternatives, and Supersession** — NEW (1 principles).
- [ ] **R68. Code-Path Investigation and Evidence-Calibrated Rationale** — NEW (3 principles).
- [ ] **R69. Scoped Evidence Collection, Query Logs, and Contradictions** — NEW (2 principles).
### External writes and quality

- [ ] **R70. Trusted Triage, Provenance, Deduplication, and Compensating Writes** — NEW (3 principles).
- [ ] **R71. Quality Floors, Measurable Thresholds, and Controlled Exceptions** — NEW (3 principles).
- [ ] **R72. Non-Bypassable Quality Gates and Fail-Closed Verification** — NEW (3 principles).
### UI verification

- [ ] **R73. Reference-Grounded UI Contracts and Visual Parity** — NEW (2 principles).
- [ ] **R74. Live Browser Evidence, Accessibility, and UI State Coverage** — NEW (2 principles).
### Simplification and repeatability

- [ ] **R75. Behavior-Preserving Refactoring and Protected Source Blocks** — NEW (5 principles).
- [ ] **R76. Subtract Complexity, Reduce Reader Load, and Fix Suppressions** — NEW (4 principles).
- [ ] **R77. Idempotent Operations, Retry Keys, and Unknown Outcomes** — NEW (2 principles).
- [ ] **R78. Separate Shared Mutable State before Locking** — NEW (1 principles).
- [ ] **R79. Rerunnable Tools and Automated Mechanical Refactors** — NEW (2 principles).
### Skill maintenance and delivery slices

- [ ] **R80. Skill Validation, Proposal Checks, and Rejected-Change Ledgers** — NEW (3 principles).
- [ ] **R81. Approved Specifications, Capability Dependencies, and Living Decisions** — NEW (3 principles).
- [ ] **R82. Dependency-Ordered Vertical Slices and Executable Plan Checks** — NEW (4 principles).

## Exact principle-to-recipe mapping

Every original principle appears below once. Links retain the original recipe or source evidence. The mapping proposes future coverage; it does not assert that unwritten recipes exist.

### R01. Verification, Exit Criteria, Completeness Sweep, and Definition of Done

**Action:** Extend existing recipe.

- [x] **Verification** — [recipe](verification-exit-criteria-completeness-sweep.md).
- [x] **Exit criteria (completeness verification)** — [recipe](verification-exit-criteria-completeness-sweep.md).
- [x] **Completeness sweep** — [recipe](verification-exit-criteria-completeness-sweep.md).
- [x] **Route tasks through explicit, falsifiable finish conditions** — [recipe](verification-exit-criteria-completeness-sweep.md).
- [x] **Apply standing definition-of-done checks separately from task acceptance criteria** — [recipe](verification-exit-criteria-completeness-sweep.md).

### R02. Direct Evidence, Safety Assumptions, and Risk-Based Verification

**Action:** Write new recipe.

- [x] **Prove the real artifact rather than trusting proxies or reports** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md).
- [x] **Scale verification rigor to impact and reversibility** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md).
- [x] **Prove the key safety assumption behind a change** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md).
- [x] **Verify dry-run claims by inspecting actual network, file, and repository effects** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md).

### R03. Live Verification Harness, Feature Maps, and Instance Lifecycle

**Action:** Write new recipe.

- [x] **Create a repository-specific live verification harness** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md).
- [x] **Maintain verification feature maps with source and live checks** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md).
- [x] **Health-check and reset verification instances after unexpected drive failures** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md).
- [x] **Clean up only owned verification processes and preserve collected proof artifacts** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md).

### R04. Independent Patch Verification and Baseline Comparison

**Action:** Write new recipe.

- [x] **Verify each PR independently at the reviewed patch before merging** — [recipe](independent-patch-verification-and-baseline-comparison.md).
- [x] **Compare changed behavior with current trunk on the same user-visible path** — [recipe](independent-patch-verification-and-baseline-comparison.md).
- [x] **Verify repaired behavior with focused tests, full regression checks, and runtime checks** — [recipe](independent-patch-verification-and-baseline-comparison.md).

### R05. Functional-Slice Tests, Observable Results, and Test Boundaries

**Action:** Write new recipe.

- [x] **Focused functional-slice testing** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md).
- [x] **Test observable behavior with exact expected results** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md).
- [x] **Test observable state with descriptive tests and minimize interaction mocks** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md).
- [x] **Choose test sizes by real resource boundaries and preserve the repository test conventions** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md).

### R06. Verification Cost, Changed Scope, and Avoiding Redundant Runs

**Action:** Write new recipe.

- [x] **Place verification checks according to execution cost and scope expensive checks to changed code** — [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md).
- [x] **Do not repeat unchanged verification commands without intervening changes** — [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md).

### R07. Red-Green-Refactor and Failing Regression Tests

**Action:** Write new recipe.

- [x] **Run a failing regression check before fixing a bug** — [recipe](red-green-refactor-and-failing-regression-tests.md).
- [x] **Use the red-green-refactor cycle for behavior-changing implementation** — [recipe](red-green-refactor-and-failing-regression-tests.md).
- [x] **Reproduce a reported bug with a failing regression test before applying the fix** — [recipe](red-green-refactor-and-failing-regression-tests.md).

### R08. Live Bug Reproduction and Verification of Existing Fixes

**Action:** Write new recipe.

- [x] **Verify an existing fix against baseline and patched live behavior before authoring another** — [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md).
- [x] **Confirm a reported defect twice through the live user interface** — [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md).

### R09. Root-Cause Diagnosis, Hypothesis Elimination, and Premise Checks

**Action:** Write new recipe.

- [x] **Question a repeatedly failed premise with an actor census** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).
- [x] **Reproduce failures and fix root causes rather than symptoms** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).
- [x] **Eliminate debugging hypotheses using runtime observations** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).
- [x] **Keep suspected causes out of the initial agent task brief** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).
- [x] **Stop further feature work on broken tests or builds until the failure is resolved** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).
- [x] **Isolate and reduce failures before root-cause fixes, using history bisect when useful** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md).

### R10. Queryable Traces and Source Attribution

**Action:** Write new recipe.

- [x] **Convert traces to queryable data and attribute findings to source symbols** — [recipe](queryable-traces-and-source-attribution.md).

### R11. Gotchas, Persistent Memory, and Evidence-Based Preferences

**Action:** Extend existing recipe.

- [x] **Gotchas** — [recipe](gotchas-and-persistent-memory.md).
- [x] **Persistent memory** — [recipe](gotchas-and-persistent-memory.md).
- [x] **Infer reusable agent preferences only from stable evidence** — [recipe](gotchas-and-persistent-memory.md).

### R12. Improvement Flywheel and Enforced Lessons

**Action:** Write new recipe.

- [x] **Improvement flywheel (classify and fix observed failures)** — [recipe](improvement-flywheel-and-enforced-lessons.md).
- [x] **Turn recurring corrections into enforced mechanisms** — [recipe](improvement-flywheel-and-enforced-lessons.md).

### R13. Evidence-Based Retrospectives and Approved Guidance Repairs

**Action:** Write new recipe.

- [x] **Repair broken workflow skills in a separate PR from feature work** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md).
- [x] **Limit retrospective skill changes to demonstrated use or missed triggers** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md).
- [x] **Turn session retrospectives into tested agent-guidance changes** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md).
- [x] **Apply retrospective changes to shared agent instructions only with approval** — [recipe](evidence-based-retrospectives-and-approved-guidance-repairs.md).

### R14. Checklist-Driven Workflow

**Action:** Retain existing recipe.

- [x] **Checklist-driven workflow** — [existing recipe](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/checklist-driven-workflow.md).

### R15. Session Ledger, Open Questions, and Restartable Handoffs

**Action:** Write new recipe.

- [x] **Open-question markers** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md).
- [x] **Session ledger** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md).
- [x] **Summarize session progress as outcomes and human-owned decisions** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md).
- [x] **Preserve incomplete plans and use the project's designated task tracker** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md).
- [x] **Persist restartable session handoffs with decisions, changed files, verification, and next work** — [recipe](session-ledger-open-questions-and-restartable-handoffs.md).

### R16. Safe Pause, Context Recovery, and Verified Resume

**Action:** Write new recipe.

- [x] **Resume from the prior execution trail rather than repeating completed work** — [recipe](safe-pause-context-recovery-and-verified-resume.md).
- [x] **Preserve work and a resume note when pausing an agent run** — [recipe](safe-pause-context-recovery-and-verified-resume.md).
- [x] **Recover prior context within the workspace and verify live state** — [recipe](safe-pause-context-recovery-and-verified-resume.md).

### R17. Constraint-First Instructions and Anti-Rationalization Rules

**Action:** Write new recipe.

- [x] **Instruction robustness** — [recipe](constraint-first-instructions-and-anti-rationalization-rules.md).
- [x] **Constraint-first reasoning** — [recipe](constraint-first-instructions-and-anti-rationalization-rules.md).
- [x] **Include concrete anti-rationalization rebuttals, misuse red flags, and evidence-based exit checks in skills** — [recipe](constraint-first-instructions-and-anti-rationalization-rules.md).

### R18. Concise Instructions, Explicit Goals, and Model-Neutral Procedures

**Action:** Write new recipe.

- [x] **Write audience-specific instructions in concise, controlled language** — [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md).
- [x] **Describe goals, proof, and constraints without prescribing skill choreography** — [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md).
- [x] **Write skill procedures in model-neutral capabilities instead of model-specific workarounds** — [recipe](concise-instructions-explicit-goals-and-model-neutral-procedures.md).

### R19. Instruction Loading and Canary Checks

**Action:** Write new recipe.

- [x] **Canary rule verification** — [recipe](instruction-loading-and-canary-checks.md).
- [x] **Repository instruction loading** — [recipe](instruction-loading-and-canary-checks.md).

### R20. Skill Discovery, Trigger Indexing, and Native Routing

**Action:** Write new recipe.

- [x] **Skill discovery and trigger descriptions** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md).
- [x] **Cross-scope specialist discovery** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md).
- [x] **Trigger indexing** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md).
- [x] **Select the applicable skill before work and follow its gates in order** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md).
- [x] **Avoid installing a second always-on skill router when the agent host already routes skills natively** — [recipe](skill-discovery-trigger-indexing-and-native-routing.md).

### R21. Positive and Negative Skill Routing Tests

**Action:** Write new recipe.

- [x] **Test skill routing with realistic positive triggers and neighboring negative triggers** — [recipe](positive-and-negative-skill-routing-tests.md).
- [x] **For negative routing tests, require the intended owner skill to outrank the wrong skill** — [recipe](positive-and-negative-skill-routing-tests.md).

### R22. Progressive Disclosure, Targeted Context, and Safe Trimming

**Action:** Write new recipe.

- [x] **Progressive disclosure of agent guidance** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md).
- [x] **Load relevant implementation, tests, types, and precedent instead of entire context dumps** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md).
- [x] **Trim context proactively while preserving active constraints, errors, and decisions** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md).
- [x] **Keep skill entrypoints concise with trigger descriptions and load long references on demand** — [recipe](progressive-disclosure-targeted-context-and-safe-trimming.md).

### R23. Delegate Bulk Exploration to Preserve Context

**Action:** Write new recipe.

- [x] **Preserve agent context by delegating bulk exploration** — [recipe](delegate-bulk-exploration-to-preserve-context.md).

### R24. Bounded Agent Roles, Single Ownership, and Composition

**Action:** Write new recipe.

- [x] **Agent design and bounded responsibility** — [recipe](bounded-agent-roles-single-ownership-and-composition.md).
- [x] **Skill composition and single ownership** — [recipe](bounded-agent-roles-single-ownership-and-composition.md).
- [x] **Delegation engine isolation** — [recipe](bounded-agent-roles-single-ownership-and-composition.md).
- [x] **Keep orchestration and code-writing responsibilities with separate owners** — [recipe](bounded-agent-roles-single-ownership-and-composition.md).
- [x] **Do not make agent personas invoke other personas or add routing-only hops** — [recipe](bounded-agent-roles-single-ownership-and-composition.md).

### R25. Template Ownership of Rendering

**Action:** Write new recipe.

- [x] **Template ownership of rendering** — [recipe](template-ownership-of-rendering.md).

### R26. Skill-Owned Code and Supporting Files

**Action:** Write new recipe.

- [x] **Skill-owned code** — [recipe](skill-owned-code-and-supporting-files.md).

### R27. Repository Adapters, Resource Access, and Portable Skills

**Action:** Write new recipe.

- [x] **Repository adapter skills** — [recipe](repository-adapters-resource-access-and-portable-skills.md).
- [x] **Resource access skills** — [recipe](repository-adapters-resource-access-and-portable-skills.md).
- [x] **Keep reusable skills separate from repository-specific agent instructions during installation** — [recipe](repository-adapters-resource-access-and-portable-skills.md).
- [x] **Include required shared references when distributing an individual skill outside its original pack** — [recipe](repository-adapters-resource-access-and-portable-skills.md).
- [x] **Keep vendor runtime settings in per-agent adapters or permitted metadata, not portable skill frontmatter** — [recipe](repository-adapters-resource-access-and-portable-skills.md).
- [x] **Validate that equivalent host command adapters stay semantically aligned** — [recipe](repository-adapters-resource-access-and-portable-skills.md).

### R28. Agent-Agnostic Contracts and Structured CLI Handoffs

**Action:** Write new recipe.

- [x] **Agent-agnostic handoff contracts** — [recipe](agent-agnostic-contracts-and-structured-cli-handoffs.md).
- [x] **CLI JSON handoff** — [recipe](agent-agnostic-contracts-and-structured-cli-handoffs.md).

### R29. Scoped Parallel Workers, Bounded Implementation, and Aggregation

**Action:** Write new recipe.

- [x] **Decompose parallel work into scoped workers and aggregate results** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md).
- [x] **Delegate implementation with bounded files and success criteria, then review the diff** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md).
- [x] **Parallelize independent specialist reviews, but keep aggregation with the orchestrator** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md).
- [x] **Use communicating agent teams for competing-hypothesis investigations and independent subagents for report fan-out** — [recipe](scoped-parallel-workers-bounded-implementation-and-aggregation.md).

### R30. Delegated Worker Permissions and Centralized External Writes

**Action:** Write new recipe.

- [x] **Keep external writes and credentials out of delegated workers** — [recipe](delegated-worker-permissions-and-centralized-external-writes.md).

### R31. Worker Configuration, Fresh Sessions, and Standing Orders

**Action:** Write new recipe.

- [x] **Configure model selection per agent responsibility** — [recipe](worker-configuration-fresh-sessions-and-standing-orders.md).
- [x] **Start fresh subagents with consolidated instructions unless local state requires a resume** — [recipe](worker-configuration-fresh-sessions-and-standing-orders.md).
- [x] **Carry immutable standing orders into every worker spawn and resume** — [recipe](worker-configuration-fresh-sessions-and-standing-orders.md).

### R32. Pilot Runs, Rolling Worker Windows, and Progress Monitoring

**Action:** Write new recipe.

- [ ] **Pilot a full work unit before scaling a multi-agent program** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md).
- [ ] **Refill a rolling worker window instead of waiting for whole batches** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md).
- [ ] **Judge agent progress by actual side effects and replace stalled workers** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md).
- [ ] **Prefer event-based agent wakeups with a heartbeat fallback over unnecessary polling** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autonomous-run.md).

### R33. Single Coordinator for Shared PR Stack Topology

**Action:** Write new recipe.

- [ ] **Keep stack topology updates under one coordinator while PR owners work in parallel** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md).

### R34. Fixed Stop Conditions and Immediate Stop Propagation

**Action:** Write new recipe.

- [ ] **Propagate operator stop orders to all active agents as an immediate no-writes hold** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-full.md).
- [ ] **Keep autonomous iterations bound to an unchanged stop predicate** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autonomous-run.md).

### R35. Reversible Autonomy, Approval Gates, and Uncertain Targets

**Action:** Write new recipe.

- [ ] **Proceed on reversible work without human blocking** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-never-block-on-the-human/SKILL.md).
- [ ] **Wait for an explicit operator go before executing an approved plan** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md).
- [ ] **Keep verified stacked PRs unmerged until explicitly authorized** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md).
- [ ] **Fail closed when an external automation's target is uncertain** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md).
- [ ] **Escalate irreversible or high-risk work for fresh human approval even during an approved autonomous run** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md).
- [ ] **Require explicit authorization for each external cross-model review invocation** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md).

### R36. Clarify Intent, Surface Assumptions, and Challenge Scope

**Action:** Write new recipe.

- [ ] **Reject unnecessary scope instead of reflexively agreeing** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md).
- [ ] **Surface assumptions and stop when requirements conflict or remain uncertain** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md).
- [ ] **Challenge unwarranted scope or complexity while leaving informed decisions to the user** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md).
- [ ] **Interview for intent one question and one explicit guess at a time** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/interview-me/SKILL.md).
- [ ] **Require explicit confirmation of the restated intent and stop before downstream work** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/interview-me/SKILL.md).

### R37. Explore Alternatives and Test MVP Assumptions

**Action:** Write new recipe.

- [ ] **Diverge into alternatives before converging on an evaluated idea** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md).
- [ ] **Record and test key idea assumptions before committing to an MVP** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md).

### R38. Consumer-First Design, Public Contracts, and Usage Guides

**Action:** Write new recipe.

- [ ] **Prioritize consumer experience over implementation convenience** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-experience-first/SKILL.md).
- [ ] **Derive architecture contracts from caller usage before implementing** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md).
- [ ] **Write a consumer usage guide before implementing a shared API** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-help/references/prompting.md).
- [ ] **Define public contracts before implementation and preserve observable consumer behavior** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md).

### R39. Domain Models, Foundational Constraints, and Invalid States

**Action:** Write new recipe.

- [ ] **Choose core data shapes and shared foundations before features** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-foundational-thinking/SKILL.md).
- [ ] **Represent domain invariants in explicit data structures** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-model-the-domain/SKILL.md).
- [ ] **Redesign new requirements as foundational constraints** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-redesign-from-first-principles/SKILL.md).
- [ ] **Use types to exclude invalid states and exhaust variants** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-type-system-discipline/SKILL.md).

### R40. Competing Designs, Prototype Experiments, and Cross-Judging

**Action:** Write new recipe.

- [ ] **Compare competing prototypes for novel designs** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-exhaust-the-design-space/SKILL.md).
- [ ] **Compare independent design candidates with cross-judging** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md).
- [ ] **Resolve observable decisions with throwaway experiments** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md).

### R41. Architecture Sketches, Structural Red Flags, and Design Rationale

**Action:** Write new recipe.

- [ ] **Record design alternatives, accepted tradeoffs, and rationale alongside the chosen contract** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/rationale-template.md).
- [ ] **Sketch architecture first and redo it when structural red flags appear** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md).
- [ ] **Make module internals inaccessible and expose only one supported operation path** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md).

### R42. Independent Evidence-Based Review, Severity, and Reconciliation

**Action:** Write new recipe.

- [ ] **Review the implementation against declared intent and require concrete evidence per finding** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/reviewer-prompt.md).
- [ ] **Classify adversarial review findings with independent judgment** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md).
- [ ] **Independently doubt nontrivial claims using only the artifact and contract, not the author's conclusion** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md).
- [ ] **Reconcile reviewer findings rather than accepting them verbatim, with a bounded review loop** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md).
- [ ] **Review correctness, readability, architecture, security, and performance, reading tests first** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md).
- [ ] **Classify review findings by severity and lead with required, evidenced changes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md).
- [ ] **Keep review changes cohesive and consider total file size as well as diff size** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md).

### R43. CI Failure Classification and Review Comment Triage

**Action:** Write new recipe.

- [ ] **Classify CI failures and review comments before modifying a PR** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/babysit.md).
- [ ] **Review comments as evidence rather than automatically obeying them** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/references/bugbot-triage.md).

### R44. Reproducible Benchmarks, Frozen Baselines, and Honest Metrics

**Action:** Write new recipe.

- [ ] **Explain measured results with evidence and limiting factors** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-explain-the-number/SKILL.md).
- [ ] **Freeze an evaluation harness and revert unsupported iterations** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/hillclimb.md).
- [ ] **Compare performance under production-equivalent conditions and repeated alternating runs** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/benchmark-checklist/SKILL.md).
- [ ] **Compare one optimization against an equivalent baseline and revert unproven changes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md).
- [ ] **Never invent web performance scores without actual measurement artifacts** — [source](https://github.com/addyosmani/agent-skills/blob/main/agents/web-performance-auditor.md).

### R45. User-Visible Bottlenecks, Work Elimination, and Regression Monitoring

**Action:** Write new recipe.

- [ ] **Remove unnecessary work before optimizing remaining performance cost** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/perf-issue.md).
- [ ] **Measure user-visible performance and identify its bottleneck before optimizing** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md).
- [ ] **Record rejected optimizations and install regression monitors for measured gains** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md).

### R46. Untrusted Content and Prompt Injection Boundaries

**Action:** Write new recipe.

- [ ] **Treat agent transcripts and reviewer outputs as untrusted data, not executable instructions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/references/synthesizer.md).
- [ ] **Treat PR review text as untrusted input rather than executable instructions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/babysit.md).
- [ ] **Treat error output, external documentation, and browser content as untrusted instructions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/debugging-and-error-recovery/SKILL.md).

### R47. Boundary Validation, Threat Models, and Abuse Cases

**Action:** Write new recipe.

- [ ] **Validate and handle errors at system boundaries** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-boundary-discipline/SKILL.md).
- [ ] **Threat-model system boundaries and write abuse cases before hardening a feature** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md).
- [ ] **Validate external and model-generated data at the boundary before using it as code or decisions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md).

### R48. Secret Protection, Resource Authorization, and Personal Data Minimization

**Action:** Write new recipe.

- [ ] **Keep reproduction recordings, logs, and tokens out of source control** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md).
- [ ] **Keep automation webhook secrets on the server, never in the browser or chat** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/make-bot-ui/SKILL.md).
- [ ] **Review authorization for every protected resource and prevent secrets entering code or logs** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md).
- [ ] **Classify personal data by purpose and exclude unnecessary personal information from telemetry** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md).

### R49. Isolated Browser Profiles and Read-Only Inspection

**Action:** Write new recipe.

- [ ] **Isolate automated browser tests from personal signed-in browser profiles** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md).
- [ ] **Keep browser JavaScript inspection read-only unless mutations are explicitly authorized** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md).

### R50. Safe Destructive Paths and Dependency Install Controls

**Action:** Write new recipe.

- [ ] **Guard destructive operations against paths controlled by untrusted upstream processes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md).
- [ ] **Block unreviewed dependency install scripts and audit the committed lockfile** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md).

### R51. Repository Configuration, Local Edits, and Committed Automation Files

**Action:** Write new recipe.

- [ ] **Per-repository configuration resolution** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/ops-per-repo-config-resolution.md).
- [ ] **Preserve locally edited managed files and keep user configuration outside automation packs** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md).
- [ ] **Run automations from committed operational files rather than copied instructions or caches** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md).

### R52. Least-Privilege Tool Restrictions versus Preapproval

**Action:** Write new recipe.

- [ ] **Distinguish tool preapproval from true tool restrictions when configuring least-privilege agents** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md).

### R53. Version-Matched Official Sources and Cache Revalidation

**Action:** Write new recipe.

- [ ] **Revalidate cached official documentation with origin validators before using it across sessions** — [source](https://github.com/addyosmani/agent-skills/blob/main/hooks/SDD-CACHE.md).
- [ ] **Verify framework-specific decisions against version-matched official documentation** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md).
- [ ] **Cite authoritative implementation sources and label unverifiable patterns explicitly** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md).

### R54. Task-Scoped Staging and Atomic Verified Commits

**Action:** Write new recipe.

- [ ] **Inspect working-tree changes before autonomous execution and stop on unrelated dirty files** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md).
- [ ] **Stage only files belonging to the current autonomous task rather than blindly staging every change** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md).
- [ ] **Create atomic, reviewed commits and verify tests, types, lint, and secrets before commit** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md).

### R55. Isolated Worktrees and Safe Workspace Cleanup

**Action:** Write new recipe.

- [ ] **Audit live sessions and uncommitted changes before removing worktrees** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md).
- [ ] **Use isolated worktrees when parallel agents would otherwise share a working tree** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md).

### R56. Consumer Migration, Safe Deprecation, and Legacy Retirement

**Action:** Write new recipe.

- [ ] **Migrate callers and delete obsolete internal APIs together** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md).
- [ ] **Optimize planned migrations for a verified final state** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-outcome-oriented-execution/SKILL.md).
- [ ] **Prefer advisory deprecation and provide a production-proven replacement plus migration guidance** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md).
- [ ] **Verify old consumers are inactive before deleting a deprecated interface or system** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md).

### R57. Additive Schema Migration and Tested Rollback

**Action:** Write new recipe.

- [ ] **Migrate schemas additively before destructive changes and test the rollback path** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md).

### R58. Safe Feature Flags and Post-Rollout Cleanup

**Action:** Write new recipe.

- [ ] **Remove feature flags and dead branches after their rollout finishes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md).
- [ ] **Keep incomplete capabilities behind safe defaults or feature flags** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md).

### R59. Semantic Releases, Tags, and Human Changelogs

**Action:** Write new recipe.

- [ ] **Version consumer-facing releases with tags, semantic versions, and human changelogs** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md).

### R60. Launch Gates, Staged Rollout, Health Checks, and Rollback

**Action:** Write new recipe.

- [ ] **Use prelaunch gates, staged rollout thresholds, and tested rollback triggers** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md).
- [ ] **Verify critical user flows and health signals after deployment** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md).
- [ ] **Default launch decisions to NO-GO for unresolved critical findings unless the operator explicitly accepts the risk** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/ship.md).

### R61. Question-Driven Telemetry, Correlation, and Actionable Alerts

**Action:** Write new recipe.

- [ ] **Choose telemetry from explicit on-call questions instead of instrumenting indiscriminately** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md).
- [ ] **Propagate correlation and entry-point identity while bounding telemetry label cardinality** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md).
- [ ] **Make alerts actionable with runbooks and verify telemetry and notification delivery** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md).

### R62. Controlled Skill Evaluations, Observable Traces, and Repeated Trials

**Action:** Write new recipe.

- [ ] **Evaluate agent instructions with blinded candidates and judges** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md).
- [ ] **Evaluate skill behavior using isolated executable fixtures and full tool traces rather than claimed intentions** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md).
- [ ] **Use dialogue-only evaluations only when conversation itself is the skill's deliverable** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md).
- [ ] **Run skill-on versus skill-off evaluations and score observable output rather than invocation alone** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md).
- [ ] **Pin model and runtime versions and repeat trials before drawing conclusions from stochastic skill routing** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md).

### R63. Pressure Tests for Instruction Compliance

**Action:** Write new recipe.

- [ ] **Pressure-test skill compliance against shortcuts justified by urgency, authority, or sunk cost** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md).

### R64. Audience-Focused Documentation, Clear Prose, and Preserved Facts

**Action:** Write new recipe.

- [ ] **Teach behavior and rationale through incremental explanations and diagrams** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/teach/SKILL.md).
- [ ] **Select documentation structure by tutorial, how-to, reference, or explanation purpose** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md).
- [ ] **Remove generic AI phrasing while preserving the intended meaning** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md).
- [ ] **Preserve factual details and uncertainty when simplifying documentation prose** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md).

### R65. Concise Delivery Reports for Users and Maintainers

**Action:** Write new recipe.

- [ ] **Keep PR summaries short with observable verification evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/opening-a-pr.md).
- [ ] **Frame agent delivery for both the user and the future maintainer** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md).

### R66. Append-Only Decision Trails, Audit, and Independent Review

**Action:** Write new recipe.

- [ ] **Keep append-only decision records linked to real evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md).
- [ ] **Audit decision logs against transcripts and correct false or omitted claims by appending rows** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md).
- [ ] **Independently review long-running decision trails with a different model family** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md).

### R67. Architecture Decision Records, Alternatives, and Supersession

**Action:** Write new recipe.

- [ ] **Record architecture decisions with alternatives and supersede rather than erase old ADRs** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md).

### R68. Code-Path Investigation and Evidence-Calibrated Rationale

**Action:** Write new recipe.

- [ ] **Investigate the current code path before explaining it** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md).
- [ ] **Reconstruct design rationale across independent evidence sources** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md).
- [ ] **Calibrate rationale claims to direct, supported, inferred, or unknown evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/epistemics.md).

### R69. Scoped Evidence Collection, Query Logs, and Contradictions

**Action:** Write new recipe.

- [ ] **Separate evidence collection from synthesis and keep investigators within their assigned sources** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md).
- [ ] **Record exact investigation queries, empty results, and contradictory evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md).

### R70. Trusted Triage, Provenance, Deduplication, and Compensating Writes

**Action:** Write new recipe.

- [ ] **Freeze report provenance and deduplicate before filing tickets** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md).
- [ ] **Gate automatic bug fixing on a trusted triage verdict and ownership checks** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md).
- [ ] **Compensate cross-system ticket writes when the final handoff fails** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md).

### R71. Quality Floors, Measurable Thresholds, and Controlled Exceptions

**Action:** Write new recipe.

- [ ] **Define measurable project quality thresholds and record exceptions with owners and expiry** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md).
- [ ] **Apply a minimum quality floor in noninteractive runs when project thresholds are absent** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md).
- [ ] **Introduce quality checks incrementally in legacy projects rather than enabling the entire lifecycle at once** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/adoption-guide.md).

### R72. Non-Bypassable Quality Gates and Fail-Closed Verification

**Action:** Write new recipe.

- [ ] **Detect attempts to weaken checks, tests, suppressions, or quality thresholds** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md).
- [ ] **Treat a quality guard that could not run as a blocking failure rather than a clean result** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/references/floor-guard.md).
- [ ] **Run non-bypassable CI quality gates and feed failures back into agent correction** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md).

### R73. Reference-Grounded UI Contracts and Visual Parity

**Action:** Write new recipe.

- [ ] **Prove visual parity against an unchanged screenshot baseline** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/visual-parity.md).
- [ ] **Define a reference-grounded UI design contract before implementation** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md).

### R74. Live Browser Evidence, Accessibility, and UI State Coverage

**Action:** Write new recipe.

- [ ] **Verify responsive and accessible UI states including empty, loading, and error flows** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md).
- [ ] **Verify browser changes against live DOM, console, network, and before-after screenshots** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md).

### R75. Behavior-Preserving Refactoring and Protected Source Blocks

**Action:** Write new recipe.

- [ ] **Pin existing behavior before structural refactoring** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/refactoring.md).
- [ ] **Behavior-preserving agent review** — [source](https://github.com/antshc/brain/blob/main/plugins/crew/agents/chorey.agent.md).
- [ ] **Understand why existing code exists before simplifying or deleting it** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md).
- [ ] **Refactor incrementally without changing test expectations to force a pass** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md).
- [ ] **Mask protected source blocks during agent simplification and restore them from verified placeholders or backups** — [source](https://github.com/addyosmani/agent-skills/blob/main/hooks/SIMPLIFY-IGNORE.md).

### R76. Subtract Complexity, Reduce Reader Load, and Fix Suppressions

**Action:** Write new recipe.

- [ ] **Prefer the smallest change and shallowest useful abstraction** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-laziness-protocol/SKILL.md).
- [ ] **Minimize reader load from indirection and mutable state** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-minimize-reader-load/SKILL.md).
- [ ] **Remove dead or redundant complexity before additions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-subtract-before-you-add/SKILL.md).
- [ ] **Replace redundant comments and unsafe suppressions with code fixes** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/no-comments/SKILL.md).

### R77. Idempotent Operations, Retry Keys, and Unknown Outcomes

**Action:** Write new recipe.

- [ ] **Make state-changing operations converge across retries** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-make-operations-idempotent/SKILL.md).
- [ ] **Honor idempotency keys across retries, payload mismatches, and unknown outcomes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md).

### R78. Separate Shared Mutable State before Locking

**Action:** Write new recipe.

- [ ] **Separate shared mutable state before using locks** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md).

### R79. Rerunnable Tools and Automated Mechanical Refactors

**Action:** Write new recipe.

- [ ] **Build a rerunnable tool for nontrivial work** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-build-the-lever/SKILL.md).
- [ ] **Automate wide mechanical refactors instead of hand-editing large change sets** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md).

### R80. Skill Validation, Proposal Checks, and Rejected-Change Ledgers

**Action:** Write new recipe.

- [ ] **Validate authored skills, referenced files, and structural examples** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md).
- [ ] **Check existing skills, active proposals, and rejected changes before introducing a new skill** — [source](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md).
- [ ] **Record rejected skill changes with evaluation evidence in an append-only ledger** — [source](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md).

### R81. Approved Specifications, Capability Dependencies, and Living Decisions

**Action:** Write new recipe.

- [ ] **Approve the capability dependency map before specifying a multi-module initiative** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md).
- [ ] **Write a specification before implementation and stop for approval before planning** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md).
- [ ] **Update the living specification before implementing changed decisions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md).

### R82. Dependency-Ordered Vertical Slices and Executable Plan Checks

**Action:** Write new recipe.

- [ ] **Sequence changes as independently verifiable units** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-sequence-verifiable-units/SKILL.md).
- [ ] **Validate multi-phase plans with an executable checker before handoff** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md).
- [ ] **Build dependency-ordered, verifiable task slices without implementing during planning** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md).
- [ ] **Implement complete vertical slices with test, verification, and commit gates** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md).

## Coverage audit

| Check | Result |
|---|---:|
| Original principles | 244 |
| Assigned principles | 244 |
| Duplicate assignments | 0 |
| Unassigned principles | 0 |
| Already covered principles | 95 |
| Principles still awaiting coverage | 149 |
| Proposed total recipes | 82 |
| New recipes | 79 |
| Existing recipes to extend | 2 |
| Existing recipes to retain | 1 |

## Inputs

- [Grouped principle checklist](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/grouped-index.md).
- [Original principle checklist](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/index.md).
- [Combined verification recipe](https://github.com/antshc/ai-cookbook/blob/main/docs/cookbook/verification-exit-criteria-completeness-sweep.md).

Each completed recipe is committed and pushed separately with its coverage and navigation updates.

