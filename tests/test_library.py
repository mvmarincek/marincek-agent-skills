import sys,unittest,json,tempfile,shutil,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from route_skills import rank
from skill_quality import audit
class LibraryTests(unittest.TestCase):
 def test_manifest_and_paths(self):
  m=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
  self.assertEqual(m['count'],len(m['skills']))
  self.assertEqual(len({e['id'] for e in m['skills']}),len(m['skills']))
  for e in m['skills']:
   self.assertTrue((ROOT/e['path']).is_file(),e['id'])
 def test_router_landing(self):
  r=rank('landing page gamificada React analytics marketing CTA',top=4)
  self.assertIn('gamified-landing-page',[x['skill'] for x in r])
 def test_router_terraform(self):
  r=rank('terraform kubernetes GitHub Actions infraestrutura AWS GCP Azure',top=5)
  self.assertIn('infrastructure-devops-architect',[x['skill'] for x in r])
 def test_evaluator_new_skills(self):
  m=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
  for e in m['skills']:
   if e['version']=='2.0.0':
    self.assertEqual(audit(e)['score'],audit(e)['max_score'],e['id'])
 def test_installer_dry_run(self):
  with tempfile.TemporaryDirectory() as d:
   r=subprocess.run([sys.executable,str(ROOT/'scripts/install.py'),'--scope','project','--project-path',d,'--skills','skill-factory','infrastructure-devops-architect','--targets','codex','claude','--dry-run'],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertFalse((Path(d)/'.agents').exists())
 def test_json_event_taxonomy(self):
  e=json.loads((ROOT/'areas/web-marketing/skills/gamified-landing-page/assets/event-taxonomy.json').read_text(encoding='utf-8'))
  names=[x['name'] for x in e['events']]
  self.assertIn('generate_lead',names)
  self.assertEqual(len(names),len(set(names)))
if __name__=='__main__':unittest.main()
