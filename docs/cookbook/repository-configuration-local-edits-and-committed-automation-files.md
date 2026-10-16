# Recipe: Repository Configuration, Local Edits, and Committed Automation Files

## Problem

Automation packs can overwrite local edits or resolve configuration from inconsistent roots. Live runs need repository-owned configuration and committed operational instructions.

## Example

**Task:** Refresh an installed automation pack while preserving repository-specific configuration.

**AI Instructions:**

> 1. Read each plugin's configuration from its single fixed path under the declared harness repository root.
> 2. Keep developer settings in the plugin's own ignored file and read credentials only in the script branch that uses them.
> 3. Create missing managed files and preserve destination-only files.
> 4. Inspect differing managed files and merge without discarding local edits. Stop before replacement when ownership is ambiguous.
> 5. Keep user configuration and routing maps outside the managed automation pack.
> 6. Have the live automation read the exact committed repository-relative operational file. Do not copy cached instructions into its prompt.

## Best Practices

- Use one configuration root and lookup path.
- Preserve local and user-owned files.
- Run from committed operational guidance.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [docs/concepts/ops-per-repo-config-resolution.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-per-repo-config-resolution.md):** Example 1, adapted from [docs/concepts/ops-per-repo-config-resolution.md, lines 11–33](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/docs/concepts/ops-per-repo-config-resolution.md#L11-L33).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/setup-benny/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/setup-benny/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/setup-benny/SKILL.md, lines 25–30](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/setup-benny/SKILL.md#L25-L30).
- **Lauren Tan (poteto) — [pstack/automations/benny/skills/setup-benny/SKILL.md](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/setup-benny/SKILL.md):** Example 1, adapted from [pstack/automations/benny/skills/setup-benny/SKILL.md, lines 179–187](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/automations/benny/skills/setup-benny/SKILL.md#L179-L187).
