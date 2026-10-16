# Recipe: Single Coordinator for Shared PR Stack Topology

## Problem

Parallel PR owners can corrupt a dependent stack by rebasing or retargeting it independently. Stack topology needs one coordinator.

## Example

**Task:** Assemble independently verified PRs into a linear review stack.

**AI Instructions:**

> 1. Let each owner push only its own branch and report tip, base, and intended parent.
> 2. Assign all stack topology writes to one coordinator.
> 3. Append only verified work in the intended order.
> 4. Fetch the exact parent tip before rebasing the child and retargeting its PR.
> 5. Refresh CI and mergeability after rewritten pushes. Re-verify any changed patch.
> 6. Deliver the verified chain for the authorized landing process.

## Best Practices

- Separate build ownership from topology ownership.
- Serialize rebases and retargets.
- Bind verdicts to the patch that remains after restacking.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/autopilot-stack.md, lines 8–12](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-stack.md#L8-L12).
