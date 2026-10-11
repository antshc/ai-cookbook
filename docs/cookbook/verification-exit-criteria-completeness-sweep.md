# Recipe: Verification, Exit Criteria, and Completeness Sweep

## Problem

AI agents can declare work complete when tests pass, even if requirements are missing. Multi-part tasks need separate checks for correctness, completion conditions, and scope coverage.

- **Verification:** Does the implemented behavior work?
- **Exit Criteria (Completeness Verification):** Does the result meet all defined completion conditions?
- **Completeness Sweep:** Were any required obligations omitted?

## Example 1

**Task:** Scan a repository's agent guidance and update its cookbook principle index. Identify which principles have actionable recipes and which still need one.

**Source:** Adapted from Brain's [actual cookbook scan workflow](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/.github/skills/scan-cookbook/SKILL.md#L21-L75); the closing checks are at [lines 69–75](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/.github/skills/scan-cookbook/SKILL.md#L69-L75).

**AI Instructions:**

> 1. **Exit Criteria:** Require one entry per discovered principle, supported coverage status, and a valid recipe or source link.
> 2. **Verification:** Read each linked recipe. Check its instructions cover the principle. Resolve duplicate entries and broken paths.
> 3. **Completeness Sweep:** Run last. Reconstruct all obligations from the request. Match every extracted principle to an index entry and evidence.
> 4. Report unread sources and uncovered principles. Declare completion only when all exit criteria pass and no obligations remain unaccounted for.

## Example 2

**Task:** Prove a newly generated project-local verification skill before handing it to another agent. Exercise one mapped feature and retain the resulting evidence after cleanup.

**Source:** Adapted from pstack's [skill-generation and proof workflow](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/create-verification-skill/SKILL.md#L23-L40).

**AI Instructions:**

> 1. Define the expected user-visible state and the evidence required to prove it.
> 2. Follow the generated launch and health checks. Drive one mapped feature through its real user path.
> 3. Compare the actual state and side effects with the expected result. Save the action and outcome evidence.
> 4. Clean up owned instances. Confirm the saved evidence still exists.
> 5. Check the request for missing obligations. Report that one exercised feature proves the skill's execution path, not complete application coverage.

## Best Practices

- Define measurable exit criteria before implementation.
- Use verification evidence to evaluate exit criteria. Passing tests alone does not prove completion.
- Run the completeness sweep last for multi-part tasks. Do not duplicate checks already proving full coverage.

## Sources & Attribution

- **[Lauren Tan (poteto) — pstack: Prove It Works, lines 9–22](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-prove-it-works/SKILL.md#L9-L22)**: Direct observation and rerunnable proof support the verification practice.
- **[Lauren Tan (poteto) — pstack: Create Verification Skill, lines 23–40](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/create-verification-skill/SKILL.md#L23-L40)**: Expected results, feature maps, and an executed proof supply Example 2.
- **[Brain: Scan Cookbook, lines 69–75](https://github.com/antshc/brain/blob/80fbb79fb1fcca7ccca59fbe884e290dbd117f31/.github/skills/scan-cookbook/SKILL.md#L69-L75)**: Observable completion checks and coverage of extracted obligations supply Example 1. These are source implementations of the practices; the combined recipe and adapted wording are cookbook synthesis.

## Related Recipes

- [Gotchas and Persistent Memory](gotchas-and-persistent-memory.md)
