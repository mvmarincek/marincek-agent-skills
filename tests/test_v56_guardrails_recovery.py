import unittest, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def frontmatter_field(skill_md: Path, field: str) -> str:
    t = skill_md.read_text(encoding='utf-8')
    m = re.search(rf'{field}:\s*"?([^"\n]+)"?', t)
    return m.group(1).strip() if m else ''

class GuardrailsRecoveryV56Tests(unittest.TestCase):
 def test_catalog_has_both_new_skills(self):
  m = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
  self.assertGreaterEqual(tuple(int(n) for n in m['version'].split('.')), (5, 6, 0))
  self.assertEqual(m['count'], 42)
  self.assertEqual(len(m['skills']), 42)
  records = {x['id']: x for x in m['skills']}
  for sid in ('agent-guardrails-design', 'agent-task-recovery'):
   self.assertIn(sid, records)
   r = records[sid]
   self.assertEqual(r['version'], '1.0.0')
   self.assertEqual(r['area'], 'ai-agents')
   self.assertEqual(r['status'], 'stable')
   self.assertEqual(r['verified'], 'structure-only')
   f = ROOT / r['path']
   self.assertTrue(f.is_file())
   self.assertEqual(frontmatter_field(f, 'name'), sid)
   self.assertEqual(frontmatter_field(f, 'version'), '1.0.0')

 def test_guardrails_skill_content(self):
  f = ROOT / 'areas/ai-agents/skills/agent-guardrails-design/SKILL.md'
  t = f.read_text(encoding='utf-8')
  for must in (
   'Enforcement vive fora do LLM',
   'Padrão deny para o irreversível',
   'Fricção proporcional ao risco',
   'comportamento de bloqueio',
   'red-team',
   'GUARDRAILS.md',
   'agent-reliability-governance',
  ):
   self.assertIn(must, t)
  self.assertNotIn('fantasasma', t)

 def test_guardrails_references_exist(self):
  base = ROOT / 'areas/ai-agents/skills/agent-guardrails-design'
  for rel, minlen in (
   ('references/guardrail-catalog.md', 2000),
   ('assets/guardrails-template.md', 500),
  ):
   p = base / rel
   self.assertTrue(p.is_file(), rel)
   self.assertGreater(len(p.read_text(encoding='utf-8')), minlen, rel)

 def test_task_recovery_skill_content(self):
  f = ROOT / 'areas/ai-agents/skills/agent-task-recovery/SKILL.md'
  t = f.read_text(encoding='utf-8')
  for must in (
   'estado no disco/git é a verdade',
   'verificar → reconciliar → continuar → reportar',
   'fantasma',
   'HANDOFF.md',
   'próxima ação concreta',
   'recovery drill',
   'agent-persistent-memory',
  ):
   self.assertIn(must, t)
  self.assertNotIn('fantasasma', t)

 def test_task_recovery_references_exist(self):
  base = ROOT / 'areas/ai-agents/skills/agent-task-recovery'
  for rel, minlen in (
   ('references/handoff-template.md', 500),
   ('references/recovery-runtime.md', 800),
  ):
   p = base / rel
   self.assertTrue(p.is_file(), rel)
   self.assertGreater(len(p.read_text(encoding='utf-8')), minlen, rel)

 def test_area_readme_lists_new_skills(self):
  t = (ROOT / 'areas/ai-agents/README.md').read_text(encoding='utf-8')
  self.assertIn('agent-guardrails-design', t)
  self.assertIn('agent-task-recovery', t)

if __name__ == '__main__':
 unittest.main()
