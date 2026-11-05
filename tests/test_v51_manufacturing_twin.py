import json,sys,unittest,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from route_skills import rank

class ManufacturingTwinTests(unittest.TestCase):
 def test_manifest_and_version(self):
  m=json.loads((ROOT/'catalog/skills.json').read_text('utf-8'))
  self.assertGreaterEqual(m['version'],'5.1.0')
  self.assertGreaterEqual(m['count'],28)
  self.assertEqual(len({s['id'] for s in m['skills']}),m['count'])
  self.assertIn('made-to-order-manufacturing-twin',{s['id'] for s in m['skills']})
 def test_industrial_repo_shape(self):
  d=ROOT/'areas/enterprise-systems/skills/made-to-order-manufacturing-twin'
  s=(d/'SKILL.md').read_text('utf-8')
  self.assertIn('MES',s)
  self.assertIn('VIN',s)
  self.assertIn('Critérios de aceite',s)
  self.assertIn('sem',s.casefold())
  self.assertGreater(len(s),4500)
  a=json.loads((d/'assets/car-config-and-milestones.example.json').read_text('utf-8'))
  self.assertTrue(a['synthetic'])
  self.assertTrue(a['example_only'])
  self.assertIsNone(a['physical_unit_id'])
  self.assertTrue(all(x['evidence_level']=='DEMO_SYNTHETIC' for x in a['milestones']))
 def test_route_car_factory(self):
  q='cliente compra carro 3d configurado online e aparece montando na fabrica com eventos reais da linha de producao MES ERP em tempo real'
  self.assertEqual(rank(q,top=5)[0]['skill'],'made-to-order-manufacturing-twin')
 def test_route_3d_landing_stays_existing(self):
  q='landing page existente game 3d realista com mão pegando ingredientes e colocando no crepe'
  self.assertEqual(rank(q,top=5)[0]['skill'],'immersive-commerce-3d')
 def test_installer_manifest_new_dry_run(self):
  import tempfile
  with tempfile.TemporaryDirectory() as d:
   r=subprocess.run([sys.executable,str(ROOT/'scripts/install.py'),'--scope','project','--project-path',d,'--targets','codex','--dry-run','--skills','made-to-order-manufacturing-twin'],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertIn('made-to-order-manufacturing-twin',r.stdout)
 def test_existing_skill_ids_remain(self):
  import zipfile
  origin=Path('/mnt/data/files/Agent_Skills_mvmarincek_v4_22_Skills.zip')
  if not origin.exists():self.skipTest('Original v4 zip not included in isolated CI')
  with zipfile.ZipFile(origin) as z: old=json.loads(z.read('catalog/skills.json'))
  cur=json.loads((ROOT/'catalog/skills.json').read_text('utf-8'))
  self.assertTrue({x['id'] for x in old['skills']}.issubset({x['id'] for x in cur['skills']}))

if __name__=='__main__':unittest.main()
