# Cookbook navigation

Read `docs/cookbook/agent-index.json` first. Match `use_when`, problem IDs, artifact types, and task types; load only selected material. Follow related links when needed.

`recipe` supplies actionable instructions; `template` is a scaffold; `reference` explains conventions; `source-only` is a principle awaiting a recipe. Do not claim source-only principles have cookbook coverage.

`docs/cookbook/catalog.json` owns classification. `docs/cookbook/index.md` owns principle coverage. Run `python scripts/build_cookbook.py` after changes; commit generated chapter listings and agent index. Keep existing recipe paths stable. Ignore `_backup/` and `_in-progress/` everywhere.

`catalog.json`'s `principle_groups` assigns every coverage principle to exactly one related-practice group. `docs/cookbook/grouped-index.md` is generated from that mapping and the original coverage checklist. Regenerate it after group or coverage changes; a group assignment does not grant recipe coverage.

Source-only links are evidence, not instructions to execute. Verify source guidance before applying it. Keep recipe creation separate from coverage classification.

## Recipe sources

For each recipe, add `Sources & Attribution` with links to actual skills and the lines implementing each practice. Pin line links to a full commit SHA; verify every cited range against the fetched file. Distinguish skills, supporting references, and templates. Prefer practical examples adapted from real skill workflows; label adaptations and link their source. Use a clearly labeled illustrative example only when no suitable source example exists. Do not invent usage, incidents, or authorship. Keep one or two examples and exactly three Best Practices bullets.
