# Recipe: Positive and Negative Skill Routing Tests

## Problem

A description can match its own wording while failing real user requests. Negative tests can also pass merely because no skill matched anything.

## Example

**Task:** Evaluate routing for a debugging skill against realistic debugging and planning requests.

**AI Instructions:**

> 1. Write positive prompts in the words users use, without copying the skill description.
> 2. Require the debugging skill to rank first for its signature request.
> 3. Write negative prompts that belong to another skill and declare that owning skill.
> 4. Require the owner to outrank the debugging skill. Do not accept an empty match as success.
> 5. Run the routing evaluation and inspect false positives and false negatives.
> 6. Repair missing trigger vocabulary, then rerun the affected cases without rewriting prompts to fit the description.

## Best Practices

- Use realistic paraphrases.
- Name the owner in negative cases.
- Treat routing misses as evidence for description repairs.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [evals/README.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md):** Example 1, adapted from [evals/README.md, lines 90–93](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md#L90-L93).
