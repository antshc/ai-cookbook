# Grouped Principle Checklist

Each original principle belongs to exactly one group. Related practices remain separate checklist items; a group is a planning aid, not proof that one recipe covers every item.

**Coverage:** 244 principles in 35 groups; 38 covered, 206 awaiting recipes.

[Original coverage checklist](index.md) owns titles, coverage status, and recipe/source links. Group assignments live in `catalog.json`. This page is generated; update those inputs and run `python scripts/build_cookbook.py`.

- `[x]` means an actionable recipe covers the principle.
- `[ ]` means the principle still needs a recipe; its link points to source evidence.

## Groups

| Group | Items | Covered | Awaiting recipes |
|---|---:|---:|---:|
| [Completion checks](#completion-checks) | 5 | 5 | 0 |
| [Proof of actual behavior](#proof-of-actual-behavior) | 11 | 11 | 0 |
| [Focused testing](#focused-testing) | 6 | 6 | 0 |
| [Regression protection](#regression-protection) | 6 | 5 | 1 |
| [Root-cause diagnosis](#root-cause-diagnosis) | 7 | 7 | 0 |
| [Learning from failures](#learning-from-failures) | 9 | 3 | 6 |
| [Resumable execution](#resumable-execution) | 9 | 1 | 8 |
| [Instruction enforcement](#instruction-enforcement) | 7 | 0 | 7 |
| [Skill discovery and routing](#skill-discovery-and-routing) | 8 | 0 | 8 |
| [Context management](#context-management) | 5 | 0 | 5 |
| [Ownership and composition](#ownership-and-composition) | 11 | 0 | 11 |
| [Delegation contracts](#delegation-contracts) | 7 | 0 | 7 |
| [Worker lifecycle](#worker-lifecycle) | 9 | 0 | 9 |
| [Autonomous execution boundaries](#autonomous-execution-boundaries) | 7 | 0 | 7 |
| [Intent and assumption discovery](#intent-and-assumption-discovery) | 7 | 0 | 7 |
| [Design before implementation](#design-before-implementation) | 13 | 0 | 13 |
| [Independent review](#independent-review) | 9 | 0 | 9 |
| [Measured performance](#measured-performance) | 8 | 0 | 8 |
| [Trust and security boundaries](#trust-and-security-boundaries) | 14 | 0 | 14 |
| [Configuration and distribution](#configuration-and-distribution) | 8 | 0 | 8 |
| [Git and workspace safety](#git-and-workspace-safety) | 5 | 0 | 5 |
| [Migration and deprecation](#migration-and-deprecation) | 6 | 0 | 6 |
| [Release and rollout](#release-and-rollout) | 5 | 0 | 5 |
| [Operational evidence](#operational-evidence) | 3 | 0 | 3 |
| [Skill evaluation](#skill-evaluation) | 6 | 0 | 6 |
| [Documentation and provenance](#documentation-and-provenance) | 10 | 0 | 10 |
| [External-write consistency](#external-write-consistency) | 3 | 0 | 3 |
| [Quality thresholds and gates](#quality-thresholds-and-gates) | 6 | 0 | 6 |
| [UI contracts and verification](#ui-contracts-and-verification) | 4 | 0 | 4 |
| [Investigation and source evidence](#investigation-and-source-evidence) | 7 | 0 | 7 |
| [Safe simplification](#safe-simplification) | 8 | 0 | 8 |
| [Retries and shared state](#retries-and-shared-state) | 3 | 0 | 3 |
| [Rerunnable tools and mechanical changes](#rerunnable-tools-and-mechanical-changes) | 2 | 0 | 2 |
| [Skill authoring and maintenance](#skill-authoring-and-maintenance) | 3 | 0 | 3 |
| [Specifications and verifiable slices](#specifications-and-verifiable-slices) | 7 | 0 | 7 |
| **Total** | **244** | **38** | **206** |

## Completion checks

Does the behavior work, are completion conditions met, and were any obligations omitted?

Verification asks whether the implemented behavior works. Exit criteria ask whether all defined completion conditions are met. A completeness sweep asks whether any required obligations were omitted. Definition of done adds standing quality requirements.

- [x] **Verification** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Exit criteria (completeness verification)** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Completeness sweep** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Route tasks through explicit, falsifiable finish conditions** — [recipe](verification-exit-criteria-completeness-sweep.md)
- [x] **Apply standing definition-of-done checks separately from task acceptance criteria** — [recipe](verification-exit-criteria-completeness-sweep.md)

## Proof of actual behavior

Does direct evidence from the real artifact prove the claimed behavior?

- [x] **Prove the real artifact rather than trusting proxies or reports** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Scale verification rigor to impact and reversibility** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Prove the key safety assumption behind a change** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Create a repository-specific live verification harness** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Maintain verification feature maps with source and live checks** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Verify each PR independently at the reviewed patch before merging** — [recipe](independent-patch-verification-and-baseline-comparison.md)
- [x] **Verify dry-run claims by inspecting actual network, file, and repository effects** — [recipe](direct-evidence-safety-assumptions-and-risk-based-verification.md)
- [x] **Health-check and reset verification instances after unexpected drive failures** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Clean up only owned verification processes and preserve collected proof artifacts** — [recipe](live-verification-harness-feature-maps-and-instance-lifecycle.md)
- [x] **Compare changed behavior with current trunk on the same user-visible path** — [recipe](independent-patch-verification-and-baseline-comparison.md)
- [x] **Verify repaired behavior with focused tests, full regression checks, and runtime checks** — [recipe](independent-patch-verification-and-baseline-comparison.md)

## Focused testing

Which observable boundary and smallest relevant checks prove the outcome?

- [x] **Focused functional-slice testing** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Test observable behavior with exact expected results** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Place verification checks according to execution cost and scope expensive checks to changed code** — [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md)
- [x] **Do not repeat unchanged verification commands without intervening changes** — [recipe](verification-cost-changed-scope-and-avoiding-redundant-runs.md)
- [x] **Test observable state with descriptive tests and minimize interaction mocks** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)
- [x] **Choose test sizes by real resource boundaries and preserve the repository test conventions** — [recipe](functional-slice-tests-observable-results-and-test-boundaries.md)

## Regression protection

Does a failing test or recorded baseline expose the defect and protect existing behavior?

- [ ] **Pin existing behavior before structural refactoring** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/refactoring.md)
- [x] **Run a failing regression check before fixing a bug** — [recipe](red-green-refactor-and-failing-regression-tests.md)
- [x] **Verify an existing fix against baseline and patched live behavior before authoring another** — [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md)
- [x] **Confirm a reported defect twice through the live user interface** — [recipe](live-bug-reproduction-and-verification-of-existing-fixes.md)
- [x] **Use the red-green-refactor cycle for behavior-changing implementation** — [recipe](red-green-refactor-and-failing-regression-tests.md)
- [x] **Reproduce a reported bug with a failing regression test before applying the fix** — [recipe](red-green-refactor-and-failing-regression-tests.md)

## Root-cause diagnosis

Which runtime observations isolate the cause and reject mistaken hypotheses?

- [x] **Question a repeatedly failed premise with an actor census** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Reproduce failures and fix root causes rather than symptoms** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Eliminate debugging hypotheses using runtime observations** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Convert traces to queryable data and attribute findings to source symbols** — [recipe](queryable-traces-and-source-attribution.md)
- [x] **Keep suspected causes out of the initial agent task brief** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Stop further feature work on broken tests or builds until the failure is resolved** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)
- [x] **Isolate and reduce failures before root-cause fixes, using history bisect when useful** — [recipe](root-cause-diagnosis-hypothesis-elimination-and-premise-checks.md)

## Learning from failures

Which observed lesson should become memory, corrected guidance, or an enforced mechanism?

- [x] **Gotchas** — [recipe](gotchas-and-persistent-memory.md)
- [x] **Persistent memory** — [recipe](gotchas-and-persistent-memory.md)
- [ ] **Improvement flywheel (classify and fix observed failures)** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/ops-improvement-flywheel.md)
- [ ] **Turn recurring corrections into enforced mechanisms** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-encode-lessons-in-structure/SKILL.md)
- [ ] **Repair broken workflow skills in a separate PR from feature work** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md)
- [ ] **Limit retrospective skill changes to demonstrated use or missed triggers** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/references/synthesizer.md)
- [ ] **Turn session retrospectives into tested agent-guidance changes** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/SKILL.md)
- [x] **Infer reusable agent preferences only from stable evidence** — [recipe](gotchas-and-persistent-memory.md)
- [ ] **Apply retrospective changes to shared agent instructions only with approval** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/SKILL.md)

## Resumable execution

What progress, decisions, open questions, and remaining work must survive a session reset?

- [x] **Checklist-driven workflow** — [recipe](checklist-driven-workflow.md)
- [ ] **Open-question markers** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/str-open-question-marker.md)
- [ ] **Session ledger** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-ledger.md)
- [ ] **Summarize session progress as outcomes and human-owned decisions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/ketchup/SKILL.md)
- [ ] **Resume from the prior execution trail rather than repeating completed work** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/session-pickup.md)
- [ ] **Preserve work and a resume note when pausing an agent run** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/pause-safely.md)
- [ ] **Recover prior context within the workspace and verify live state** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/recall/SKILL.md)
- [ ] **Preserve incomplete plans and use the project's designated task tracker** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md)
- [ ] **Persist restartable session handoffs with decisions, changed files, verification, and next work** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md)

## Instruction enforcement

Which constraints must the agent follow, and how is actual compliance made observable?

- [ ] **Canary rule verification** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/ops-canary-rule-verification.md)
- [ ] **Instruction robustness** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/ops-instruction-robustness.md)
- [ ] **Constraint-first reasoning** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-constraint-first-reasoning.md)
- [ ] **Write audience-specific instructions in concise, controlled language** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md)
- [ ] **Describe goals, proof, and constraints without prescribing skill choreography** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-help/references/prompting.md)
- [ ] **Write skill procedures in model-neutral capabilities instead of model-specific workarounds** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md)
- [ ] **Include concrete anti-rationalization rebuttals, misuse red flags, and evidence-based exit checks in skills** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md)

## Skill discovery and routing

Which skill owns this request, and does the loading and routing mechanism select it?

- [ ] **Repository instruction loading** — [source](https://github.com/antshc/brain/blob/main/docs/adr/crew-agents-uses-instructions.md)
- [ ] **Skill discovery and trigger descriptions** — [source](https://github.com/antshc/brain/blob/main/.github/instructions/agent-skills.instructions.md)
- [ ] **Cross-scope specialist discovery** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-cross-scope-skill-family.md)
- [ ] **Trigger indexing** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-trigger-indexer.md)
- [ ] **Select the applicable skill before work and follow its gates in order** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
- [ ] **Avoid installing a second always-on skill router when the agent host already routes skills natively** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/getting-started.md)
- [ ] **Test skill routing with realistic positive triggers and neighboring negative triggers** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)
- [ ] **For negative routing tests, require the intended owner skill to outrank the wrong skill** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)

## Context management

Which guidance and evidence must be loaded, retained, disclosed later, or delegated?

- [ ] **Progressive disclosure of agent guidance** — [source](https://github.com/antshc/brain/blob/main/skills/engineering/writing-great-skills/GLOSSARY.md)
- [ ] **Preserve agent context by delegating bulk exploration** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-guard-the-context-window/SKILL.md)
- [ ] **Load relevant implementation, tests, types, and precedent instead of entire context dumps** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md)
- [ ] **Trim context proactively while preserving active constraints, errors, and decisions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md)
- [ ] **Keep skill entrypoints concise with trigger descriptions and load long references on demand** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md)

## Ownership and composition

Who owns each responsibility, procedure, rendering contract, implementation, and adapter?

- [ ] **Agent design and bounded responsibility** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-agents-style.md)
- [ ] **Template ownership of rendering** — [source](https://github.com/antshc/brain/blob/main/.github/instructions/agent-skills.instructions.md)
- [ ] **Skill composition and single ownership** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-skill-composition.md)
- [ ] **Delegation engine isolation** — [source](https://github.com/antshc/brain/blob/main/docs/adr/explore-codebase-is-skill-agnostic.md)
- [ ] **Repository adapter skills** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-repository-adapter-skill.md)
- [ ] **Resource access skills** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-resource-access-skill.md)
- [ ] **Skill-owned code** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/structure-skill-owned-code.md)
- [ ] **Make module internals inaccessible and expose only one supported operation path** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md)
- [ ] **Keep orchestration and code-writing responsibilities with separate owners** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [ ] **Keep reusable skills separate from repository-specific agent instructions during installation** — [source](https://github.com/addyosmani/agent-skills/blob/main/AGENTS.md)
- [ ] **Do not make agent personas invoke other personas or add routing-only hops** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/agents.md)

## Delegation contracts

What scope, inputs, outputs, restrictions, and review duties govern delegated work?

- [ ] **Agent-agnostic handoff contracts** — [source](https://github.com/antshc/brain/blob/main/docs/adr/ralph-is-agent-agnostic.md)
- [ ] **CLI JSON handoff** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/str-cli-json-handoff.md)
- [ ] **Decompose parallel work into scoped workers and aggregate results** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/swarm/SKILL.md)
- [ ] **Delegate implementation with bounded files and success criteria, then review the diff** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/feature.md)
- [ ] **Keep external writes and credentials out of delegated workers** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [ ] **Parallelize independent specialist reviews, but keep aggregation with the orchestrator** — [source](https://github.com/addyosmani/agent-skills/blob/main/references/orchestration-patterns.md)
- [ ] **Use communicating agent teams for competing-hypothesis investigations and independent subagents for report fan-out** — [source](https://github.com/addyosmani/agent-skills/blob/main/references/orchestration-patterns.md)

## Worker lifecycle

How are workers configured, started, replenished, monitored, replaced, and stopped?

- [ ] **Pilot a full work unit before scaling a multi-agent program** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [ ] **Configure model selection per agent responsibility** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/setup-pstack/SKILL.md)
- [ ] **Start fresh subagents with consolidated instructions unless local state requires a resume** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md)
- [ ] **Carry immutable standing orders into every worker spawn and resume** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [ ] **Refill a rolling worker window instead of waiting for whole batches** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [ ] **Judge agent progress by actual side effects and replace stalled workers** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md)
- [ ] **Propagate operator stop orders to all active agents as an immediate no-writes hold** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-full.md)
- [ ] **Prefer event-based agent wakeups with a heartbeat fallback over unnecessary polling** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autonomous-run.md)
- [ ] **Keep stack topology updates under one coordinator while PR owners work in parallel** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md)

## Autonomous execution boundaries

What may proceed independently, what stops the loop, and which actions require authorization?

- [ ] **Proceed on reversible work without human blocking** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-never-block-on-the-human/SKILL.md)
- [ ] **Keep autonomous iterations bound to an unchanged stop predicate** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autonomous-run.md)
- [ ] **Wait for an explicit operator go before executing an approved plan** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md)
- [ ] **Keep verified stacked PRs unmerged until explicitly authorized** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/autopilot-stack.md)
- [ ] **Fail closed when an external automation's target is uncertain** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md)
- [ ] **Escalate irreversible or high-risk work for fresh human approval even during an approved autonomous run** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md)
- [ ] **Require explicit authorization for each external cross-model review invocation** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md)

## Intent and assumption discovery

What does the user mean, which assumptions need evidence, and is the requested scope justified?

- [ ] **Reject unnecessary scope instead of reflexively agreeing** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md)
- [ ] **Surface assumptions and stop when requirements conflict or remain uncertain** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
- [ ] **Challenge unwarranted scope or complexity while leaving informed decisions to the user** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/using-agent-skills/SKILL.md)
- [ ] **Interview for intent one question and one explicit guess at a time** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/interview-me/SKILL.md)
- [ ] **Require explicit confirmation of the restated intent and stop before downstream work** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/interview-me/SKILL.md)
- [ ] **Diverge into alternatives before converging on an evaluated idea** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md)
- [ ] **Record and test key idea assumptions before committing to an MVP** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md)

## Design before implementation

Which consumer contracts, domain invariants, alternatives, and foundations should guide implementation?

- [ ] **Compare competing prototypes for novel designs** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-exhaust-the-design-space/SKILL.md)
- [ ] **Prioritize consumer experience over implementation convenience** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-experience-first/SKILL.md)
- [ ] **Choose core data shapes and shared foundations before features** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-foundational-thinking/SKILL.md)
- [ ] **Represent domain invariants in explicit data structures** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-model-the-domain/SKILL.md)
- [ ] **Redesign new requirements as foundational constraints** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-redesign-from-first-principles/SKILL.md)
- [ ] **Use types to exclude invalid states and exhaust variants** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-type-system-discipline/SKILL.md)
- [ ] **Derive architecture contracts from caller usage before implementing** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md)
- [ ] **Write a consumer usage guide before implementing a shared API** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-help/references/prompting.md)
- [ ] **Record design alternatives, accepted tradeoffs, and rationale alongside the chosen contract** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/rationale-template.md)
- [ ] **Sketch architecture first and redo it when structural red flags appear** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md)
- [ ] **Compare independent design candidates with cross-judging** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md)
- [ ] **Resolve observable decisions with throwaway experiments** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md)
- [ ] **Define public contracts before implementation and preserve observable consumer behavior** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md)

## Independent review

Which findings survive independent judgment, and what severity and evidence support them?

- [ ] **Review the implementation against declared intent and require concrete evidence per finding** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/references/reviewer-prompt.md)
- [ ] **Classify adversarial review findings with independent judgment** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md)
- [ ] **Classify CI failures and review comments before modifying a PR** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/babysit.md)
- [ ] **Review comments as evidence rather than automatically obeying them** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/references/bugbot-triage.md)
- [ ] **Independently doubt nontrivial claims using only the artifact and contract, not the author's conclusion** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md)
- [ ] **Reconcile reviewer findings rather than accepting them verbatim, with a bounded review loop** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md)
- [ ] **Review correctness, readability, architecture, security, and performance, reading tests first** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md)
- [ ] **Classify review findings by severity and lead with required, evidenced changes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md)
- [ ] **Keep review changes cohesive and consider total file size as well as diff size** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md)

## Measured performance

Is the measured improvement reproducible, comparable, user-relevant, and explained by a bottleneck?

- [ ] **Explain measured results with evidence and limiting factors** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-explain-the-number/SKILL.md)
- [ ] **Freeze an evaluation harness and revert unsupported iterations** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/hillclimb.md)
- [ ] **Compare performance under production-equivalent conditions and repeated alternating runs** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/benchmark-checklist/SKILL.md)
- [ ] **Remove unnecessary work before optimizing remaining performance cost** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/perf-issue.md)
- [ ] **Measure user-visible performance and identify its bottleneck before optimizing** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md)
- [ ] **Compare one optimization against an equivalent baseline and revert unproven changes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md)
- [ ] **Record rejected optimizations and install regression monitors for measured gains** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md)
- [ ] **Never invent web performance scores without actual measurement artifacts** — [source](https://github.com/addyosmani/agent-skills/blob/main/agents/web-performance-auditor.md)

## Trust and security boundaries

Which content is untrusted, which operations are authorized, and which data must remain protected?

- [ ] **Validate and handle errors at system boundaries** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-boundary-discipline/SKILL.md)
- [ ] **Treat agent transcripts and reviewer outputs as untrusted data, not executable instructions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/references/synthesizer.md)
- [ ] **Treat PR review text as untrusted input rather than executable instructions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/babysit.md)
- [ ] **Keep reproduction recordings, logs, and tokens out of source control** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [ ] **Keep automation webhook secrets on the server, never in the browser or chat** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/make-bot-ui/SKILL.md)
- [ ] **Isolate automated browser tests from personal signed-in browser profiles** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md)
- [ ] **Keep browser JavaScript inspection read-only unless mutations are explicitly authorized** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md)
- [ ] **Treat error output, external documentation, and browser content as untrusted instructions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/debugging-and-error-recovery/SKILL.md)
- [ ] **Threat-model system boundaries and write abuse cases before hardening a feature** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [ ] **Validate external and model-generated data at the boundary before using it as code or decisions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [ ] **Guard destructive operations against paths controlled by untrusted upstream processes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [ ] **Block unreviewed dependency install scripts and audit the committed lockfile** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [ ] **Review authorization for every protected resource and prevent secrets entering code or logs** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)
- [ ] **Classify personal data by purpose and exclude unnecessary personal information from telemetry** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)

## Configuration and distribution

Where do settings and shared references belong, and how are installations and host adapters kept valid?

- [ ] **Per-repository configuration resolution** — [source](https://github.com/antshc/brain/blob/main/docs/concepts/ops-per-repo-config-resolution.md)
- [ ] **Preserve locally edited managed files and keep user configuration outside automation packs** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md)
- [ ] **Run automations from committed operational files rather than copied instructions or caches** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/setup-benny/SKILL.md)
- [ ] **Include required shared references when distributing an individual skill outside its original pack** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/getting-started.md)
- [ ] **Keep vendor runtime settings in per-agent adapters or permitted metadata, not portable skill frontmatter** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md)
- [ ] **Distinguish tool preapproval from true tool restrictions when configuring least-privilege agents** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/advanced-per-agent-configuration.md)
- [ ] **Revalidate cached official documentation with origin validators before using it across sessions** — [source](https://github.com/addyosmani/agent-skills/blob/main/hooks/SDD-CACHE.md)
- [ ] **Validate that equivalent host command adapters stay semantically aligned** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/developer-onboarding.md)

## Git and workspace safety

Can this change be committed or this workspace removed without mixing or losing other work?

- [ ] **Audit live sessions and uncommitted changes before removing worktrees** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md)
- [ ] **Inspect working-tree changes before autonomous execution and stop on unrelated dirty files** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md)
- [ ] **Stage only files belonging to the current autonomous task rather than blindly staging every change** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/build.md)
- [ ] **Create atomic, reviewed commits and verify tests, types, lint, and secrets before commit** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)
- [ ] **Use isolated worktrees when parallel agents would otherwise share a working tree** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)

## Migration and deprecation

Have consumers moved to the replacement, can the transition roll back, and is retirement safe?

- [ ] **Migrate callers and delete obsolete internal APIs together** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md)
- [ ] **Optimize planned migrations for a verified final state** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-outcome-oriented-execution/SKILL.md)
- [ ] **Remove feature flags and dead branches after their rollout finishes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)
- [ ] **Prefer advisory deprecation and provide a production-proven replacement plus migration guidance** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)
- [ ] **Migrate schemas additively before destructive changes and test the rollback path** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)
- [ ] **Verify old consumers are inactive before deleting a deprecated interface or system** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)

## Release and rollout

Is release readiness proven, is rollout controlled, and do critical flows remain healthy?

- [ ] **Keep incomplete capabilities behind safe defaults or feature flags** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md)
- [ ] **Version consumer-facing releases with tags, semantic versions, and human changelogs** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/git-workflow-and-versioning/SKILL.md)
- [ ] **Use prelaunch gates, staged rollout thresholds, and tested rollback triggers** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)
- [ ] **Verify critical user flows and health signals after deployment** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)
- [ ] **Default launch decisions to NO-GO for unresolved critical findings unless the operator explicitly accepts the risk** — [source](https://github.com/addyosmani/agent-skills/blob/main/.claude/commands/ship.md)

## Operational evidence

Can telemetry and actionable alerts answer the questions needed to operate the system?

- [ ] **Choose telemetry from explicit on-call questions instead of instrumenting indiscriminately** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [ ] **Propagate correlation and entry-point identity while bounding telemetry label cardinality** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)
- [ ] **Make alerts actionable with runbooks and verify telemetry and notification delivery** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md)

## Skill evaluation

Do controlled, observable, repeated trials show that the guidance improves behavior?

- [ ] **Evaluate agent instructions with blinded candidates and judges** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md)
- [ ] **Evaluate skill behavior using isolated executable fixtures and full tool traces rather than claimed intentions** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)
- [ ] **Use dialogue-only evaluations only when conversation itself is the skill's deliverable** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)
- [ ] **Pressure-test skill compliance against shortcuts justified by urgency, authority, or sunk cost** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)
- [ ] **Run skill-on versus skill-off evaluations and score observable output rather than invocation alone** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)
- [ ] **Pin model and runtime versions and repeat trials before drawing conclusions from stochastic skill routing** — [source](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md)

## Documentation and provenance

Does the document explain the right thing clearly while preserving facts, evidence, and decision history?

- [ ] **Teach behavior and rationale through incremental explanations and diagrams** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/teach/SKILL.md)
- [ ] **Keep PR summaries short with observable verification evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/opening-a-pr.md)
- [ ] **Select documentation structure by tutorial, how-to, reference, or explanation purpose** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md)
- [ ] **Keep append-only decision records linked to real evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [ ] **Audit decision logs against transcripts and correct false or omitted claims by appending rows** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [ ] **Independently review long-running decision trails with a different model family** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md)
- [ ] **Remove generic AI phrasing while preserving the intended meaning** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md)
- [ ] **Frame agent delivery for both the user and the future maintainer** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md)
- [ ] **Record architecture decisions with alternatives and supersede rather than erase old ADRs** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md)
- [ ] **Preserve factual details and uncertainty when simplifying documentation prose** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md)

## External-write consistency

Is the external action based on trusted, deduplicated evidence, and can partial writes be compensated?

- [ ] **Freeze report provenance and deduplicate before filing tickets** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md)
- [ ] **Gate automatic bug fixing on a trusted triage verdict and ownership checks** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md)
- [ ] **Compensate cross-system ticket writes when the final handoff fails** — [source](https://github.com/cursor/plugins/blob/main/pstack/automations/benny/skills/triage-issue-reports/SKILL.md)

## Quality thresholds and gates

Which quality floor applies, are exceptions controlled, and did every required gate actually run?

- [ ] **Define measurable project quality thresholds and record exceptions with owners and expiry** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [ ] **Apply a minimum quality floor in noninteractive runs when project thresholds are absent** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [ ] **Detect attempts to weaken checks, tests, suppressions, or quality thresholds** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/SKILL.md)
- [ ] **Treat a quality guard that could not run as a blocking failure rather than a clean result** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/constraint-driven-development/references/floor-guard.md)
- [ ] **Run non-bypassable CI quality gates and feed failures back into agent correction** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)
- [ ] **Introduce quality checks incrementally in legacy projects rather than enabling the entire lifecycle at once** — [source](https://github.com/addyosmani/agent-skills/blob/main/docs/adoption-guide.md)

## UI contracts and verification

Does the interface match its visual contract and support responsive, accessible, and failure states?

- [ ] **Prove visual parity against an unchanged screenshot baseline** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/visual-parity.md)
- [ ] **Define a reference-grounded UI design contract before implementation** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md)
- [ ] **Verify responsive and accessible UI states including empty, loading, and error flows** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md)
- [ ] **Verify browser changes against live DOM, console, network, and before-after screenshots** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/browser-testing-with-devtools/SKILL.md)

## Investigation and source evidence

Which sources and queries support an explanation, and what remains inferred, contradictory, or unknown?

- [ ] **Investigate the current code path before explaining it** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md)
- [ ] **Reconstruct design rationale across independent evidence sources** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md)
- [ ] **Calibrate rationale claims to direct, supported, inferred, or unknown evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/epistemics.md)
- [ ] **Separate evidence collection from synthesis and keep investigators within their assigned sources** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md)
- [ ] **Record exact investigation queries, empty results, and contradictory evidence** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/investigator-prompt.md)
- [ ] **Verify framework-specific decisions against version-matched official documentation** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md)
- [ ] **Cite authoritative implementation sources and label unverifiable patterns explicitly** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md)

## Safe simplification

Which complexity can be removed while preserving behavior, conventions, and protected content?

- [ ] **Behavior-preserving agent review** — [source](https://github.com/antshc/brain/blob/main/plugins/crew/agents/chorey.agent.md)
- [ ] **Prefer the smallest change and shallowest useful abstraction** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-laziness-protocol/SKILL.md)
- [ ] **Minimize reader load from indirection and mutable state** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-minimize-reader-load/SKILL.md)
- [ ] **Remove dead or redundant complexity before additions** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-subtract-before-you-add/SKILL.md)
- [ ] **Replace redundant comments and unsafe suppressions with code fixes** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/no-comments/SKILL.md)
- [ ] **Understand why existing code exists before simplifying or deleting it** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [ ] **Refactor incrementally without changing test expectations to force a pass** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [ ] **Mask protected source blocks during agent simplification and restore them from verified placeholders or backups** — [source](https://github.com/addyosmani/agent-skills/blob/main/hooks/SIMPLIFY-IGNORE.md)

## Retries and shared state

Do retries converge safely, and can independent actors avoid conflicting writes?

- [ ] **Make state-changing operations converge across retries** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-make-operations-idempotent/SKILL.md)
- [ ] **Separate shared mutable state before using locks** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md)
- [ ] **Honor idempotency keys across retries, payload mismatches, and unknown outcomes** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md)

## Rerunnable tools and mechanical changes

Can a repeatable tool perform or prove work more reliably than manual edits?

- [ ] **Build a rerunnable tool for nontrivial work** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-build-the-lever/SKILL.md)
- [ ] **Automate wide mechanical refactors instead of hand-editing large change sets** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)

## Skill authoring and maintenance

Does the skill have a justified owner, valid supporting files, and evidence for accepted or rejected changes?

- [ ] **Validate authored skills, referenced files, and structural examples** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md)
- [ ] **Check existing skills, active proposals, and rejected changes before introducing a new skill** — [source](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)
- [ ] **Record rejected skill changes with evaluation evidence in an append-only ledger** — [source](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md)

## Specifications and verifiable slices

Which approved specification and dependency order define independently verifiable implementation units?

- [ ] **Sequence changes as independently verifiable units** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-sequence-verifiable-units/SKILL.md)
- [ ] **Validate multi-phase plans with an executable checker before handoff** — [source](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md)
- [ ] **Approve the capability dependency map before specifying a multi-module initiative** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [ ] **Write a specification before implementation and stop for approval before planning** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [ ] **Update the living specification before implementing changed decisions** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- [ ] **Build dependency-ordered, verifiable task slices without implementing during planning** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md)
- [ ] **Implement complete vertical slices with test, verification, and commit gates** — [source](https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md)
