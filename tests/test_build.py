"""Check deployable links and metadata failure handling, rather than output claims."""
import copy
import importlib.util
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('builder',ROOT/'scripts/build_cookbook.py')
builder=importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        data=dict(attrs)
        if 'id' in data:self.ids.add(data['id'])
        for key in ['href','src']:
            if key in data:self.urls.append(data[key])

class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((builder.COOKBOOK/'catalog.json').read_text())
        builder.build(check=True)

    def test_all_internal_site_links_and_fragments_resolve(self):
        pages={}
        for p in builder.OUT.rglob('*.html'):
            parser=Links(); parser.feed(p.read_text()); pages[p.resolve()]=parser
        for p,parser in pages.items():
            for url in parser.urls:
                parsed=urlsplit(url)
                if parsed.scheme or parsed.netloc:continue
                target=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
                self.assertTrue(target.is_relative_to(builder.OUT.resolve()),(p,url))
                self.assertTrue(target.is_file(),(p,url))
                if parsed.fragment and target in pages:
                    self.assertIn(unquote(parsed.fragment),pages[target].ids,(p,url))

    def test_source_only_entries_are_never_marked_covered(self):
        index=json.loads((builder.OUT/'agent-index.json').read_text())
        for m in index['materials']:
            if m['kind']=='source-only':
                self.assertEqual(m['status'],'recipe-needed')
                self.assertEqual(m['covered_principles'],[])
        self.assertEqual(sum(len(m['covered_principles']) for m in index['materials']), sum(r['covered'] for r in builder.coverage().values()))

    def test_duplicate_ids_fail_validation(self):
        catalog=copy.deepcopy(self.catalog)
        catalog['materials'].append(catalog['materials'][0])
        with self.assertRaisesRegex(AssertionError,'Duplicate material'):
            builder.validate(catalog)

    def test_missing_canonical_material_fails_validation(self):
        catalog=copy.deepcopy(self.catalog)
        catalog['materials'][0]['path']='missing.md'
        with self.assertRaises(AssertionError):builder.validate(catalog)

    def test_stale_coverage_mapping_fails_validation(self):
        catalog=copy.deepcopy(self.catalog)
        source=next(m for m in catalog['materials'] if m['kind']=='source-only')
        source['path']='https://example.com/stale'
        with self.assertRaisesRegex(AssertionError,'Stale coverage'):
            builder.validate(catalog)

    def test_grouped_checklist_preserves_every_original_entry_once(self):
        pattern = r'^- \[([ x])\] \*\*(.+?)\*\* — \[(recipe|source)\]\(([^)]+)\)'
        original = re.findall(pattern, (builder.COOKBOOK/'index.md').read_text(), re.M)
        grouped = re.findall(pattern, (builder.COOKBOOK/'grouped-index.md').read_text(), re.M)
        self.assertCountEqual(grouped, original)
        self.assertEqual(len(grouped), len({row[1] for row in grouped}))

    def test_missing_group_assignment_fails_validation(self):
        catalog = copy.deepcopy(self.catalog)
        catalog['principle_groups'][0]['principles'].pop()
        with self.assertRaisesRegex(AssertionError, 'Group mapping mismatch'):
            builder.validate(catalog)

    def test_duplicate_group_assignment_fails_validation(self):
        catalog = copy.deepcopy(self.catalog)
        catalog['principle_groups'][1]['principles'].append(catalog['principle_groups'][0]['principles'][0])
        with self.assertRaisesRegex(AssertionError, 'Principle assigned to multiple groups'):
            builder.validate(catalog)

    def test_unknown_group_principle_fails_validation(self):
        catalog = copy.deepcopy(self.catalog)
        catalog['principle_groups'][0]['principles'].append('Nonexistent principle')
        with self.assertRaisesRegex(AssertionError, 'Group mapping mismatch'):
            builder.validate(catalog)

    def test_grouped_checklist_tracks_coverage_updates(self):
        cov = copy.deepcopy(builder.coverage())
        principle = next(t for t,r in cov.items() if not r['covered'])
        cov[principle] = {'covered': True, 'path': 'new-recipe.md'}
        text = builder.grouped_checklist(self.catalog['principle_groups'], cov)
        self.assertIn(f'- [x] **{principle}** — [recipe](new-recipe.md)', text)
        self.assertNotIn(f'- [ ] **{principle}**', text)

if __name__=='__main__':unittest.main()

