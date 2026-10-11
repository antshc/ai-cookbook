# Recipe: Queryable Traces and Source Attribution

## Problem

Large trace files encourage visual guessing and unsupported hotspot claims. Findings need a queryable representation and a link from recorded frames to source.

## Example

**Task:** Investigate a CPU hotspot from a captured runtime trace.

**AI Instructions:**

> 1. Identify the trace format and preserve the capture.
> 2. Convert samples, frames, and timestamps into queryable rows before interpreting the trace.
> 3. Query where time accumulates. Walk the call tree from the hot frame to the responsible path.
> 4. Map the frame to its source file, symbol, and line using recorded symbols.
> 5. Compare equivalent baseline and patched captures when both exist.
> 6. Report the query, measured result, and source attribution. Mark missing symbols as an unresolved limitation.

## Best Practices

- Query reduced data before drawing conclusions.
- Keep source attribution attached to each finding.
- Compare equivalent captures rather than unrelated runs.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Lauren Tan (poteto) — [pstack/skills/poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md):** Example 1, adapted from [pstack/skills/poteto-mode/playbooks/trace-forensics.md, lines 7–12](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/trace-forensics.md#L7-L12).
