"""Check deployable links and metadata failure handling, rather than output claims."""
import copy
import importlib.util
import json
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
        self.assertEqual(sum(len(m['covered_principles']) for m in index['materials']),5)

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

if __name__=='__main__':unittest.main()
