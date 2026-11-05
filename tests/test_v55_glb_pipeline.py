import unittest, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def frontmatter_version(skill_md: Path) -> str:
    t = skill_md.read_text(encoding='utf-8')
    m = re.search(r'version:\s*"([0-9.]+)"', t)
    return m.group(1) if m else ''

class GlbPipelineV55Tests(unittest.TestCase):
 def test_catalog_versions_synced_with_frontmatter(self):
  m = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
  self.assertEqual(m['version'], '5.5.0')
  self.assertEqual(m['count'], 40)
  records = {x['id']: x for x in m['skills']}
  expected = {'photoreal-3d-assets': '1.2.0', 'immersive-commerce-3d': '1.1.0'}
  for sid, ver in expected.items():
   f = ROOT / records[sid]['path']
   self.assertEqual(records[sid]['version'], ver, sid)
   self.assertEqual(frontmatter_version(f), ver, sid)

 def test_blender_glb_export_reference(self):
  r = ROOT / 'areas/games/skills/photoreal-3d-assets/references/blender-glb-export.md'
  self.assertTrue(r.is_file())
  t = r.read_text(encoding='utf-8')
  self.assertGreater(len(t), 1500)
  for token in ('GLB', 'export_apply', 'export_yup', 'Draco', '--background', 'Unit Scale'):
   self.assertIn(token, t)
  s = (ROOT / 'areas/games/skills/photoreal-3d-assets/SKILL.md').read_text(encoding='utf-8')
  self.assertIn('blender-glb-export.md', s)

 def test_glb_loading_react_reference(self):
  r = ROOT / 'areas/web-marketing/skills/immersive-commerce-3d/references/glb-loading-react.md'
  self.assertTrue(r.is_file())
  t = r.read_text(encoding='utf-8')
  self.assertGreater(len(t), 900)
  for token in ('useGLTF', 'Suspense', 'ErrorBoundary', 'fallback', '.clone()'):
   self.assertIn(token, t)
  s = (ROOT / 'areas/web-marketing/skills/immersive-commerce-3d/SKILL.md').read_text(encoding='utf-8')
  self.assertIn('glb-loading-react.md', s)

 def test_no_usegltt_typo(self):
  s = (ROOT / 'areas/web-marketing/skills/immersive-commerce-3d/SKILL.md').read_text(encoding='utf-8')
  self.assertNotIn('useGLTT', s)

 def test_tools_doc_covers_all_scripts(self):
  doc = (ROOT / 'docs/TOOLS.md').read_text(encoding='utf-8')
  scripts = sorted(
   p.name for p in (ROOT / 'scripts').iterdir()
   if p.is_file() and p.suffix in ('.py', '.ps1')
  )
  self.assertTrue(scripts, 'nenhum script encontrado')
  for name in scripts:
   self.assertIn(name, doc, f'docs/TOOLS.md nao menciona {name}')
  for must in ('--dry-run', '--replace', 'suggested-not-authorized', 'codex', 'claude', 'verdent', 'opencode'):
   self.assertIn(must, doc)
  readme = (ROOT / 'README.md').read_text(encoding='utf-8')
  self.assertIn('docs/TOOLS.md', readme)

if __name__ == '__main__':
 unittest.main()
