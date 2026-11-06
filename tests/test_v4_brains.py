import json, pathlib, unittest, sys, re
ROOT_TEMP=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT_TEMP/'scripts'))
from route_skills import rank
ROOT=pathlib.Path(__file__).resolve().parents[1]
NEW=('company-brain-architecture','second-brain-architecture','code-intelligence-engineering')
class BrainSkillTests(unittest.TestCase):
 def test_three_new_skills_and_references(self):
  manifest=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
  self.assertGreaterEqual(manifest['count'],22)  # preserve v4 skills as library evolves
  records={x['id']:x for x in manifest['skills']}
  for name in NEW:
   self.assertIn(name,records)
   p=ROOT/records[name]['path']
   self.assertTrue(p.is_file())
   content=p.read_text(encoding='utf-8')
   self.assertIn('## Critérios de aceite' if name!='second-brain-architecture' else '## Testes de validação',content)
   self.assertGreater(len(content),4000)
   self.assertGreaterEqual(len(list((p.parent/'references').glob('*.md'))),4)
 def test_router_brains(self):
  queries={
   'company-brain-architecture':'company brain corporativo Linear GitHub Drive ACL RAG',
   'second-brain-architecture':'second brain pessoal notas conversas memória persistente',
   'code-intelligence-engineering':'code intelligence AST SCIP simbolos dependencias repositório',
  }
  for slug,query in queries.items():
   results=rank(query,top=1)
   self.assertTrue(results)
   self.assertEqual(results[0]['skill'],slug)
 def test_no_secrets_in_manifest(self):
  m=(ROOT/'catalog/skills.json').read_text(encoding='utf-8')
  # padrao de chave real (sk- seguido de run alfanumerico longo), nao substring solta:
  # ids como agent-task-recovery (ta"sk-r"ecovery) sao falsos positivos do check ingenuo
  self.assertIsNone(re.search(r'sk-[A-Za-z0-9_-]{16,}',m))
  self.assertNotIn('BEGIN PRIVATE KEY',m)
  self.assertNotIn('ghp_',m)
  self.assertNotIn('AKIA',m)
if __name__=='__main__':unittest.main()
