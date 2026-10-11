# Recipe: Semantic Releases, Tags, and Human Changelogs

## Problem

A consumer-facing release can hide breaking changes behind an incorrect version, drift from its Git tag, or provide a changelog that only repeats commit messages.

## Example

**Task:** Prepare version metadata and release notes for a public package.

**AI Instructions:**

> 1. Compare the release with its previous public contract and classify breaking, additive, and corrective changes.
> 2. Choose a major bump for breaking changes, minor for compatible additions, and patch for fixes.
> 3. Create the release tag through the repository's release process and derive the published version from that tag.
> 4. Write a curated changelog grouped by user impact, including required migration steps and notable fixes.
> 5. Check that tag, package version, artifacts, and changelog describe the same release.

## Best Practices

- Classify compatibility before choosing the version.
- Use the tag as the version source.
- Describe user impact in release notes.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [skills/git-workflow-and-versioning/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/git-workflow-and-versioning/SKILL.md):** Example 1, adapted from [skills/git-workflow-and-versioning/SKILL.md, lines 353–355](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/git-workflow-and-versioning/SKILL.md#L353-L355).
