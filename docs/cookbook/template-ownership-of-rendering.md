# Recipe: Template Ownership of Rendering

## Problem

A skill that restates template layout creates two sources of rendering rules. Output structure and local conditions need one template owner.

## Example

**Task:** Generate a decision document from an established template.

**AI Instructions:**

> 1. Select the matching template and supply its required inputs.
> 2. Follow the template's headings, field hints, rendering conditions, and local constraints.
> 3. Keep the skill responsible for workflow order, selection, inputs, and shared rules.
> 4. Place field guidance beside the field and keep hidden rendering directives to one terse line.
> 5. Change template-specific rules in the template. Do not restate them in the orchestrating skill.
> 6. Check the rendered document against the selected template.

## Best Practices

- Give rendering one owner.
- Keep field guidance local.
- Separate selection and workflow from output layout.

## Related Recipes

- [Verification, Exit Criteria, Completeness Sweep, and Definition of Done](verification-exit-criteria-completeness-sweep.md)

## Sources & Attribution

Examples adapt the cited workflows. Task details illustrate their use; they do not claim a recorded incident.

## References

- **Brain — [.github/instructions/agent-skills.instructions.md](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/.github/instructions/agent-skills.instructions.md):** Example 1, adapted from [.github/instructions/agent-skills.instructions.md, lines 69–73](https://github.com/antshc/brain/blob/848fe1995686604340262a54904f61ebf82ef9b3/.github/instructions/agent-skills.instructions.md#L69-L73).
