# AI Agent Cookbook

Problem-based practices for engineers writing AI skills, agents, instructions, and templates.

[Browse cookbook contents](docs/cookbook/README.md) · [Agent index](docs/cookbook/agent-index.json) · [Coverage checklist](docs/cookbook/index.md)

## Run locally

Requires Python 3.10+ and Node.js 22+ for search tests.

```sh
python -m pip install -r requirements.txt
python scripts/build_cookbook.py
python -m unittest discover -s tests -v
node tests/search.test.cjs
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. Build output is portable and uses relative URLs; it works at `/ai-cookbook/` without a root-domain assumption. Search uses a local JSON index, with no runtime API or external assets. Without JavaScript, chapter navigation and material pages remain available.

## Publishing

In repository **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**. The `Cookbook Pages` workflow validates pull requests and deploys pushes to `main`; it also supports a manual run after Pages is enabled. The intended URL is `https://antshc.github.io/ai-cookbook/`.

## Maintaining content

- Edit canonical Markdown and `docs/cookbook/catalog.json`. Use the ten problem IDs already defined in the catalog; task types and artifact types are filters.
- Keep `docs/cookbook/index.md` as the authority for principle coverage. A template or reference does not count as a recipe. Check a principle only when actionable recipe instructions cover it.
- When turning a source-only principle into a recipe, add the recipe entry, update the checklist link, and remove the matching source-only catalog entry in the same change.
- Run the builder and commit regenerated `docs/cookbook/README.md`, `problems/`, and `agent-index.json`. CI rejects stale generated navigation, missing classifications, and broken local links.
- The initial content is a snapshot. See [provenance](SOURCE.md) before importing upstream changes. The ten categories group materials by authoring problems, including agent behavior you want to encode in instructions.

Do not move existing recipes solely to change navigation. One canonical recipe can appear in several chapters.
