# Recipe: Pressure Tests for Instruction Compliance

## Problem

An instruction can appear reliable on a neutral prompt yet collapse when urgency, authority, or prior effort encourages skipping its required checks.

## Example

**Task:** Pressure-test a test-first repair workflow.

**AI Instructions:**

> 1. Create an isolated executable fixture with a bug and observable criteria for reproduction, repair, invariant tests, and the full suite.
> 2. Run a neutral task as the control.
> 3. Create separate natural prompts that pressure the agent through a deadline, claimed senior authority, and sunk implementation effort; each argues for skipping a required step.
> 4. Keep the underlying task and grading criteria fixed. Do not reveal the rubric to the executor.
> 5. Grade full tool traces for the required ordering and final behavior, not verbal promises of compliance.
> 6. Record which pressure caused a violation, revise the instruction to address that failure, and rerun controls and pressure cases.

## Best Practices

- Test realistic shortcut arguments.
- Observe required actions and ordering.
- Retest after instruction changes.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [evals/README.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md):** Example 1, adapted from [evals/README.md, lines 38–38](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md#L38-L38).
- **Addy Osmani — [evals/README.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md):** Example 1, adapted from [evals/README.md, lines 59–88](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md#L59-L88).
