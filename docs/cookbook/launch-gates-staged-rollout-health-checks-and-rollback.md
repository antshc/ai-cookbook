# Recipe: Launch Gates, Staged Rollout, Health Checks, and Rollback

## Problem

A green build alone cannot establish launch readiness. Critical findings, absent recovery plans, or unnoticed post-deploy regressions can turn a release into an incident.

## Example

**Task:** Prepare and evaluate a staged production rollout.

**AI Instructions:**

> 1. Review code quality, security, performance, accessibility, infrastructure, and documentation readiness; record unresolved findings.
> 2. Default to NO-GO for unresolved critical findings unless the operator explicitly accepts the documented risk.
> 3. Define staged exposure, health thresholds, observation windows, rollback triggers, and an owner before GO.
> 4. Prepare and test the rollback mechanism before launch.
> 5. After each stage, check health endpoint, error types and rate, latency, critical user flow, and readable log delivery against thresholds.
> 6. Stop or roll back when a trigger fires; verify restored health and communicate the result before considering further rollout.

## Best Practices

- Make launch gates and rollback triggers explicit.
- Verify the critical flow after deployment.
- Keep unresolved critical findings visible in the decision.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Addy Osmani — [.claude/commands/ship.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/ship.md):** Example 1, adapted from [.claude/commands/ship.md, lines 32–37](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/ship.md#L32-L37).
- **Addy Osmani — [.claude/commands/ship.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/ship.md):** Example 1, adapted from [.claude/commands/ship.md, lines 68–72](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/.claude/commands/ship.md#L68-L72).
- **Addy Osmani — [skills/shipping-and-launch/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/shipping-and-launch/SKILL.md):** Example 1, adapted from [skills/shipping-and-launch/SKILL.md, lines 235–242](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/shipping-and-launch/SKILL.md#L235-L242).
