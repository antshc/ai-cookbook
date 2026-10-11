# Recipe: Agent-Agnostic Contracts and Structured CLI Handoffs

## Problem

An orchestrator coupled to agent internals or free-form CLI output breaks when implementations change. Handoffs need explicit invocation and data contracts.

## Example

**Task:** Connect a repository coordinator to a replaceable worker and configuration-producing CLI.

**AI Instructions:**

> 1. Resolve ambient workspace paths once at the entry edge and pass only required trusted inputs.
> 2. Invoke the worker in its documented directory. Require its documented status, changes, verification, findings, and blockers report.
> 3. Treat implementation and review internals as opaque. Use the documented unavailable-worker policy.
> 4. Use pure cross-platform CLI commands; put branching and parsing in a portable helper.
> 5. Emit exactly one JSON payload on producer stdout. Send non-secret diagnostics to stderr.
> 6. Parse JSON and require producer success before continuing. Do not scrape stdout or silently accept partial payloads.

## Best Practices

- Depend on exposed contracts.
- Keep stdout a pure data channel.
- Make producer failures visible to consumers.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/adr/ralph-is-agent-agnostic.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/ralph-is-agent-agnostic.md):** Example 1, adapted from [docs/adr/ralph-is-agent-agnostic.md, lines 3–8](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/adr/ralph-is-agent-agnostic.md#L3-L8).
- **Brain — [docs/concepts/str-cli-json-handoff.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/str-cli-json-handoff.md):** Example 1, adapted from [docs/concepts/str-cli-json-handoff.md, lines 7–19](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/str-cli-json-handoff.md#L7-L19).
