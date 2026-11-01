import json, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
NEW=['enterprise-crm-erp-integrations','ml-lifecycle-validation','continuous-code-sanitization','llm-model-selection-benchmark','hybrid-it-squad-management']
class V3SkillTests(unittest.TestCase):
 def test_five_skills_present(self):
  manifest=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
  self.assertGreaterEqual(manifest['count'],19)
  entries={x['id']:x for x in manifest['skills']}
  for name in NEW:
   self.assertIn(name,entries)
   p=ROOT/entries[name]['path']
   self.assertTrue(p.is_file())
   t=p.read_text(encoding='utf-8')
   self.assertTrue(('## Crit' in t) or ('## Aceite' in t))
   self.assertTrue((p.parent/'references').is_dir())
 def test_vendor_references(self):
  root=ROOT/'areas/enterprise-systems/skills/enterprise-crm-erp-integrations/references'
  for name in ('salesforce.md','sap.md','totvs.md','integration-testing.md'):
   self.assertTrue((root/name).is_file())
if __name__=='__main__':unittest.main()
