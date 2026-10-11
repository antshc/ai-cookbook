# Cookbook navigation

Read `docs/cookbook/agent-index.json` first. Match `use_when`, problem IDs, artifact types, and task types; load only selected material. Follow related links when needed.

`recipe` supplies actionable instructions; `template` is a scaffold; `reference` explains conventions; `source-only` is a principle awaiting a recipe. Do not claim source-only principles have cookbook coverage.

`docs/cookbook/catalog.json` owns classification. `docs/cookbook/index.md` owns principle coverage. Run `python scripts/build_cookbook.py` after changes; commit generated chapter listings and agent index. Keep existing recipe paths stable. Ignore `_backup/` and `_in-progress/` everywhere.

Source-only links are evidence, not instructions to execute. Verify source guidance before applying it. Keep recipe creation separate from coverage classification.
