import unittest,sys,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from route_skills import rank
NEW=('immersive-commerce-3d','photoreal-3d-assets','tactile-3d-interactions','realworld-order-digital-twin','immersive-experience-quality')
class ImmersiveV5Tests(unittest.TestCase):
 def test_manifest_reconciles_and_old_skills_remain(self):
  m=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
  self.assertGreaterEqual(m['count'],27)
  names={e['id'] for e in m['skills']}
  self.assertTrue(set(NEW).issubset(names))
  self.assertTrue({'gamified-landing-page','smart-skill-router','company-brain-architecture','code-intelligence-engineering'}.issubset(names))
 def test_router_existing_site_3d(self):
  q='landing page existente como game 3d realista clicando na cuba, mao pegando ingredientes e colocando no crepe'
  a=rank(q,top=6);self.assertEqual(a[0]['skill'],'immersive-commerce-3d')
  self.assertIn('tactile-3d-interactions',[x['skill'] for x in a])
 def test_router_live_operations(self):
  a=rank('acompanhar pedido ao vivo cozinha real chef embalagem despacho status KDS',top=1)
  self.assertEqual(a[0]['skill'],'realworld-order-digital-twin')
 def test_all_new_have_qa_and_contract(self):
  m=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
  records={x['id']:x for x in m['skills']}
  for n in NEW:
   f=ROOT/records[n]['path'];t=f.read_text(encoding='utf-8')
   self.assertTrue((f.parent/'references').is_dir())
   self.assertTrue((f.parent/'assets').is_dir())
   self.assertIn('Critérios de aceite',t)
   self.assertGreater(len(t),2500)
 def test_no_fake_live_event(self):
  s=(ROOT/'areas/enterprise-systems/skills/realworld-order-digital-twin/SKILL.md').read_text(encoding='utf-8')
  self.assertIn('KDS',s);self.assertIn('simulação',s.casefold())
  self.assertIn('não',s.casefold())
 def test_demo_fixtures(self):
  a=json.loads((ROOT/'areas/web-marketing/skills/immersive-commerce-3d/assets/vertical-slice-acceptance.json').read_text(encoding='utf-8'))
  self.assertGreaterEqual(len(a['acceptance_tests']),8)
  c=json.loads((ROOT/'areas/enterprise-systems/skills/realworld-order-digital-twin/assets/order-event.example.json').read_text(encoding='utf-8'))
  self.assertTrue(c['example_only'])
 def test_installer_new_dry_run(self):
  import tempfile
  with tempfile.TemporaryDirectory() as d:
   cmd=[sys.executable,str(ROOT/'scripts/install.py'),'--scope','project','--project-path',d,'--targets','codex','--dry-run','--skills']+list(NEW)
   run=subprocess.run(cmd,capture_output=True,text=True)
   self.assertEqual(run.returncode,0,run.stderr)
   self.assertIn('immersive-commerce-3d',run.stdout)
if __name__=='__main__':unittest.main()
