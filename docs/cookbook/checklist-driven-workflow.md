# Recipe: Checklist-driven Workflow

## Problem

AI agents can skip actions or lose progress in tasks with several ordered steps. A context reset makes completed work hard to distinguish from planned work. Keep a saved checklist with evidence for each completed item.

## Example

**Task:** Add one cookbook recipe and expose it through coverage, navigation, and search. Save progress so another session can resume the update.

**AI Instructions:**

> Copy this checklist to `docs/plans/cookbook-update.md` before editing:
>
> **Cookbook Update Progress:**
> - [ ] 1. Write the recipe with verified source lines in `docs/cookbook/checklist-driven-workflow.md`.
> - [ ] 2. Link the recipe and mark its principle covered in `docs/cookbook/index.md`.
> - [ ] 3. Change its entry from source-only to recipe in `docs/cookbook/catalog.json`.
> - [ ] 4. Run `python scripts/build_cookbook.py` to rebuild chapter listings and the agent index.
> - [ ] 5. Run `python scripts/build_cookbook.py --check` to validate the generated documents.
>
> Complete the items in order.
> Check an item only after its output exists and its check passes.
> Record the file path or command result beside each checked item.
> Keep failed items unchecked.
> Record any skipped item with its reason.
> If the build fails, correct the recipe or metadata and repeat item 4.
> After a context reset, read the saved checklist and confirm its evidence before continuing.
> Before declaring completion, account for every unchecked item.

## Best Practices

- Give each item one action, a concrete output, and evidence that permits checking it.
- Keep skipped and failed items visible. State the recovery step.
- Save progress during execution. Run a separate completeness sweep before closing a multi-part task.

## Sources & Attribution

- **Lauren Tan (poteto) — pstack:** The example adapts the copied workflow steps and evidence-backed plan checklist to this cookbook's real files and build commands. It is an adaptation, not a verbatim source example.
- **[Brain — Checklist-Driven Workflow](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/structure-checklist-workflow.md#L3-L37):** Supporting concept for ordered steps, saved progress, named checklists, concrete outputs, and an explicit recovery path. This is a concept document, not a skill.

## Related Recipes

- [Verification, Exit Criteria, and Completeness Sweep](verification-exit-criteria-completeness-sweep.md)
- [Gotchas and Persistent Memory](gotchas-and-persistent-memory.md)

## References

- **Lauren Tan (poteto) — [Poteto Mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md#L119-L121):** Example 1, adapted from the instruction to copy workflow steps and retain skipped items with a reason. The skill routes multi-phase plans to its supporting playbook at [line 145](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md#L145).
- **Lauren Tan (poteto) — [Poteto Mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [`playbooks/multi-phase-plan.md`, lines 8–10](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L8-L10) and [lines 22–24](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L22-L24): save an ordered plan, validate it, and check each box only when evidence exists.
