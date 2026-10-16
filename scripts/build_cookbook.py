#!/usr/bin/env python3
"""Validate canonical cookbook metadata and build a portable static website."""
import argparse
import html
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
COOKBOOK = ROOT / 'docs/cookbook'
OUT = ROOT / 'dist'
KINDS = {'recipe', 'template', 'reference', 'source-only'}


def coverage():
    rows = re.findall(r'^- \[([ x])\] \*\*(.+?)\*\* — \[(recipe|source)\]\(([^)]+)\)', (COOKBOOK / 'index.md').read_text(), re.M)
    assert rows, 'No coverage entries found'
    assert len(rows) == len({r[1] for r in rows}), 'Duplicate principle'
    result = {}
    for check, title, kind, path in rows:
        assert (check == 'x') == (kind == 'recipe'), f'Coverage mismatch: {title}'
        if check == 'x':
            target = COOKBOOK / path
            assert target.is_file(), f'Missing recipe: {path}'
            assert '**AI Instructions:**' in target.read_text(), f'Recipe lacks actionable instructions: {path}'
        result[title] = {'covered': check == 'x', 'path': path}
    return result


def validate(catalog):
    assert catalog['schema_version'] == 1
    problems = {p['id'] for p in catalog['problems']}
    assert len(problems) == len(catalog['problems']) == 10, 'Problem IDs must be unique'
    materials = catalog['materials']
    ids = {m['id'] for m in materials}
    assert len(ids) == len(materials), 'Duplicate material ID'
    cov = coverage()
    validate_groups(catalog['principle_groups'], cov)
    pending = set()
    for m in materials:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', m['id']), m['id']
        assert m['kind'] in KINDS
        assert m['problems'] and set(m['problems']) <= problems
        assert m['applies_to'] and set(m['applies_to']) <= set(catalog['artifact_types'])
        assert m['task_types'] and set(m['task_types']) <= set(catalog['task_types'])
        assert m['use_when'] and m['provides']
        assert set(m['related']) <= ids
        assert not any(x in m['path'].split('/') for x in ['_backup', '_in-progress'])
        if m['kind'] == 'source-only':
            row = cov[m['principle']]
            assert not row['covered'] and row['path'] == m['path'], f'Stale coverage metadata: {m["id"]}'
            assert urlsplit(m['path']).scheme == 'https', f'Source link must be absolute: {m["path"]}'
            pending.add(m['principle'])
        else:
            target = (COOKBOOK / m['path']).resolve()
            assert target.is_relative_to(COOKBOOK.resolve()) and target.is_file(), m['path']
            if m['kind'] == 'recipe':
                assert '**AI Instructions:**' in target.read_text()
    assert pending == {t for t, r in cov.items() if not r['covered']}, 'Unclassified principles'
    recipe_paths = {m['path'] for m in materials if m['kind'] == 'recipe'}
    assert {r['path'] for r in cov.values() if r['covered']} <= recipe_paths
    canonical = {p.relative_to(COOKBOOK).as_posix() for p in COOKBOOK.rglob('*.md') if p.name not in ['README.md', 'index.md'] and 'problems' not in p.relative_to(COOKBOOK).parts}
    assert canonical == {m['path'] for m in materials if m['kind'] != 'source-only'}, 'Unclassified files'
    for p in COOKBOOK.rglob('*.md'):
        for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
            parsed = urlsplit(dest)
            if parsed.scheme or not parsed.path:
                continue
            assert (p.parent / parsed.path).is_file(), f'Broken link: {p}: {dest}'
    return cov


def validate_groups(groups, cov):
    assert groups, 'No principle groups'
    assert len(groups) == len({g['id'] for g in groups}), 'Duplicate principle group ID'
    assigned = []
    for group in groups:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', group['id']), group['id']
        assert group['title'] and group['question'] and group['principles'], 'Empty principle group'
        assigned.extend(group['principles'])
    assert len(assigned) == len(set(assigned)), 'Principle assigned to multiple groups'
    missing = set(cov) - set(assigned)
    unknown = set(assigned) - set(cov)
    assert not missing and not unknown, f'Group mapping mismatch: missing={sorted(missing)}, unknown={sorted(unknown)}'


def grouped_checklist(groups, cov):
    covered = sum(r['covered'] for r in cov.values())
    text = '# Grouped Principle Checklist\n\n'
    text += 'Each original principle belongs to exactly one group. Related practices remain separate checklist items; a group is a planning aid, not proof that one recipe covers every item.\n\n'
    text += f'**Coverage:** {len(cov)} principles in {len(groups)} groups; {covered} covered, {len(cov) - covered} awaiting recipes.\n\n'
    text += '[Original coverage checklist](index.md) owns titles, coverage status, and recipe/source links. Group assignments live in `catalog.json`. This page is generated; update those inputs and run `python scripts/build_cookbook.py`.\n\n'
    text += '- `[x]` means an actionable recipe covers the principle.\n- `[ ]` means the principle still needs a recipe; its link points to source evidence.\n\n'
    text += '## Groups\n\n| Group | Items | Covered | Awaiting recipes |\n|---|---:|---:|---:|\n'
    for group in groups:
        count = sum(cov[t]['covered'] for t in group['principles'])
        total = len(group['principles'])
        anchor = re.sub(r'[^a-z0-9 -]', '', group['title'].lower()).replace(' ', '-')
        text += f'| [{group["title"]}](#{anchor}) | {total} | {count} | {total - count} |\n'
    text += f'| **Total** | **{len(cov)}** | **{covered}** | **{len(cov) - covered}** |\n'
    for group in groups:
        text += f'\n## {group["title"]}\n\n{group["question"]}\n\n'
        if group['id'] == 'completion-checks':
            text += 'Verification asks whether the implemented behavior works. Exit criteria ask whether all defined completion conditions are met. A completeness sweep asks whether any required obligations were omitted. Definition of done adds standing quality requirements.\n\n'
        for title in group['principles']:
            row = cov[title]
            mark, label = ('x', 'recipe') if row['covered'] else (' ', 'source')
            text += f'- [{mark}] **{title}** — [{label}]({row["path"]})\n'
    return text


def material_url(m):
    return m['path'] if m['kind'] == 'source-only' else 'docs/cookbook/' + str(Path(m['path']).with_suffix('.html'))


def derived(catalog, cov):
    records = []
    for m in catalog['materials']:
        item = dict(m)
        item['status'] = 'recipe-needed' if m['kind'] == 'source-only' else m['kind']
        item['url'] = material_url(m)
        item['covered_principles'] = [t for t, r in cov.items() if r['covered'] and r['path'] == m['path']] if m['kind'] == 'recipe' else []
        item['path'] = m['path'] if m['kind'] == 'source-only' else 'docs/cookbook/' + m['path']
        records.append(item)
    return {'schema_version': 1, 'problems': catalog['problems'], 'principle_groups': catalog['principle_groups'], 'materials': records}


def write_generated(path, text, check):
    if check:
        assert path.is_file() and path.read_text() == text, f'Generated file stale: {path.relative_to(ROOT)}; run build'
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def generate_navigation(catalog, data, check):
    write_generated(COOKBOOK / 'agent-index.json', json.dumps(data, ensure_ascii=False, indent=2) + '\n', check)
    write_generated(COOKBOOK / 'grouped-index.md', grouped_checklist(catalog['principle_groups'], coverage()), check)
    toc = '# AI Agent Cookbook\n\nFind practices for problems encountered while writing skills, agents, instructions, and templates.\n\n'
    toc += '| Problem | Practices |\n|---|---|\n'
    for p in catalog['problems']:
        toc += f'| [{p["title"]}](problems/{p["id"]}.md) | {p["practices"]} |\n'
        chapter = f'# {p["title"]}\n\n{p["description"]}\n\n'
        for kind, heading in [('recipe','Recipes'),('reference','References'),('template','Templates'),('source-only','Principles awaiting recipes')]:
            subset = [m for m in catalog['materials'] if p['id'] in m['problems'] and m['kind'] == kind]
            chapter += f'## {heading}\n\n'
            if not subset:
                chapter += 'No materials yet.\n\n'
            for m in subset:
                dest = m['path'] if kind == 'source-only' else '../' + m['path']
                chapter += f'- [{m["title"]}]({dest})\n'
            chapter += '\n'
        chapter += '[All problems](../README.md) · [Agent index](../agent-index.json)\n'
        write_generated(COOKBOOK / 'problems' / (p['id'] + '.md'), chapter, check)
    toc += '\nFilter task types: planning, debugging, review, implementation, research. Filter artifacts: skill, agent, instruction, template.\n\n'
    toc += '[Agent index](agent-index.json) · [Coverage checklist](index.md) · [Grouped checklist](grouped-index.md) · [Skill template families](skill-template-categories.md) · [Authors & sources](authors-and-sources.md)\n'
    write_generated(COOKBOOK / 'README.md', toc, check)


def render_md(path):
    text = path.read_text()
    text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
    def rewrite(match):
        dest = match.group(2)
        parsed = urlsplit(dest)
        if not parsed.scheme and parsed.path.endswith('.md'):
            dest = parsed.path[:-3] + '.html' + ('#' + parsed.fragment if parsed.fragment else '')
        return '[' + match.group(1) + '](' + dest + ')'
    text = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', rewrite, text)
    return markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc', 'sane_lists'])


def escape(value):
    return html.escape(str(value), quote=True)


def card(m, prefix):
    label = {'recipe':'Recipe','reference':'Reference','template':'Template','source-only':'Recipe needed'}[m['kind']]
    href = m['url'] if m['kind'] == 'source-only' else prefix + m['url']
    return f'<a class="card" href="{escape(href)}"><span class="badge {m["kind"]}">{label}</span><h3>{escape(m["title"])}</h3><p>{escape(m["use_when"])}</p><span class="card-end">{"Read source" if m["kind"] == "source-only" else "Open material"} <span aria-hidden="true">↗</span></span></a>'


def page(title, body, dest, catalog, default_problem=''):
    prefix = os.path.relpath(OUT, dest.parent).replace(os.sep, '/') + '/'
    if prefix == './': prefix = ''
    nav = ''.join(f'<a href="{prefix}problems/{p["id"]}.html"><span>{i:02}</span>{escape(p["title"])}</a>' for i,p in enumerate(catalog['problems'],1))
    template = (ROOT / 'site/layout.html').read_text()
    replacements = {'TITLE': escape(title), 'BODY': body, 'PREFIX': prefix, 'NAV': nav,
                    'CONFIG': json.dumps({'prefix':prefix,'problem':default_problem}).replace('<','\\u003c')}
    for k,v in replacements.items(): template = template.replace('{{'+k+'}}',v)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(template)


def browser_body(catalog, data, problem=''):
    chosen = next((p for p in catalog['problems'] if p['id'] == problem), None)
    has_source_only = any(m['kind'] == 'source-only' for m in data['materials'])
    heading = chosen['title'] if chosen else 'Better instructions.\nMore reliable agents.'
    desc = chosen['description'] if chosen else 'A practical cookbook for engineers writing skills, agents, instructions, and templates. Start with the problem you need to solve.'
    body = '<section class="hero"><p class="eyebrow">THE ENGINEER’S FIELD GUIDE</p><h1>' + escape(heading).replace('\n','<br>') + '</h1><p class="intro">' + escape(desc) + '</p></section>'
    if not chosen:
        body += '<section class="chapter-grid" aria-label="Table of contents">'
        for i,p in enumerate(catalog['problems'],1):
            body += f'<a class="chapter" href="problems/{p["id"]}.html"><span class="chapter-no">{i:02}</span><span>{escape(p["title"])}</span><span aria-hidden="true">↗</span></a>'
        body += '</section>'
    hint = 'Recipes contain actionable instructions.'
    if has_source_only:
        hint += ' “Recipe needed” entries link to source evidence.'
    body += '<section class="library" aria-labelledby="library-title"><div class="section-heading"><h2 id="library-title">Find a practice</h2><a href="{{ROOT}}docs/cookbook/index.html">Coverage checklist ↗</a></div><p class="hint">' + hint + '</p>'
    body += '<form id="filters" role="search"><label class="search-label">Search practices<input id="search" name="q" type="search" placeholder="Try triggers, handoffs, or completion…" autocomplete="off"></label><div class="filter-row">'
    material_options = [('recipe','Recipes'),('reference','References'),('template','Templates')]
    if has_source_only:
        material_options.append(('source-only','Recipe needed'))
    for id,label,options in [('problem','Problem',[(p['id'],p['title']) for p in catalog['problems']]),('artifact','Artifact',[(a,a.title()) for a in catalog['artifact_types']]),('task','Task type',[(t,t.title()) for t in catalog['task_types']]),('kind','Material',material_options)]:
        body += f'<label>{label}<select id="{id}" name="{id}"><option value="">All {label.lower()}s</option>' + ''.join(f'<option value="{escape(v)}"'+(' selected' if id=='problem' and v==problem else '')+f'>{escape(t)}</option>' for v,t in options) + '</select></label>'
    body += '</div><button id="reset" class="text-button" type="button">Clear filters</button></form><p id="count" role="status" aria-live="polite"></p><div id="results" class="cards">'
    records = [m for m in data['materials'] if not problem or problem in m['problems']]
    records.sort(key=lambda m: ['recipe','reference','template','source-only'].index(m['kind']))
    prefix = '../' if problem else ''
    body += ''.join(card(m,prefix) for m in records)
    body += '</div><p id="empty" hidden>No matching practices. Try fewer filters or a broader search.</p><button id="more" type="button" hidden>Show more practices</button></section>'
    return body.replace('{{ROOT}}',prefix)


def build(check=False):
    catalog = json.loads((COOKBOOK / 'catalog.json').read_text())
    cov = validate(catalog)
    data = derived(catalog,cov)
    generate_navigation(catalog,data,check)
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    for name in ['style.css','app.js']: shutil.copy(ROOT/'site'/name,OUT/name)
    search = json.loads(json.dumps(data))
    for m in search['materials']:
        m['content'] = (ROOT/m['path']).read_text() if m['kind'] != 'source-only' else m['title']
    (OUT/'search-index.json').write_text(json.dumps(search,ensure_ascii=False))
    (OUT/'agent-index.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    (OUT/'.nojekyll').touch()
    page('AI Agent Cookbook',browser_body(catalog,data),OUT/'index.html',catalog)
    for p in catalog['problems']:
        page(p['title'],browser_body(catalog,data,p['id']),OUT/'problems'/(p['id']+'.html'),catalog,p['id'])
    for path in COOKBOOK.rglob('*.md'):
        dest=OUT/path.relative_to(ROOT).with_suffix('.html')
        raw_dest=OUT/path.relative_to(ROOT)
        raw_dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy(path,raw_dest)
        title = re.search(r'^# (.+)',path.read_text(),re.M)
        body=f'<div class="reading-tools"><a href="{escape(path.name)}">View Markdown ↗</a><button id="copy-instructions" type="button">Copy AI instructions</button><span id="copy-status" role="status"></span></div><article class="prose">'+render_md(path)+'</article>'
        page(title.group(1) if title else path.stem,body,dest,catalog)
    shutil.copy(COOKBOOK/'agent-index.json',OUT/'docs/cookbook/agent-index.json')
    shutil.copy(COOKBOOK/'catalog.json',OUT/'docs/cookbook/catalog.json')
    print(f'Built {len(data["materials"])} materials, {len(catalog["problems"])} problem chapters; {sum(r["covered"] for r in cov.values())}/{len(cov)} principles covered.')
    return data


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Fail when tracked generated navigation is stale')
    build(parser.parse_args().check)
