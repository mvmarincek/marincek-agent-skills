import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = Path('areas/ai-agents/skills/marm-memory-usage/SKILL.md')
REF_PATH = Path('areas/ai-agents/skills/marm-memory-usage/references/transports-and-resources.md')


class MarmUsageV58Tests(unittest.TestCase):
    def test_catalog_registers_new_skill(self):
        catalog = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
        self.assertGreaterEqual(tuple(int(n) for n in catalog['version'].split('.')), (5, 8, 0))
        self.assertGreaterEqual(catalog['count'], 43)
        self.assertGreaterEqual(len(catalog['skills']), 43)
        records = {item['id']: item for item in catalog['skills']}
        self.assertIn('marm-memory-usage', records)
        record = records['marm-memory-usage']
        self.assertEqual(record['version'], '1.0.0')
        self.assertEqual(record['area'], 'ai-agents')
        self.assertEqual(record['path'], 'areas/ai-agents/skills/marm-memory-usage/SKILL.md')
        text = (ROOT / record['path']).read_text(encoding='utf-8')
        match = re.search(r'version:\s*"([0-9.]+)"', text)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), '1.0.0')

    def test_skill_contracts_present(self):
        skill = (ROOT / SKILL_PATH).read_text(encoding='utf-8')
        for term in (
            'Quando usar',
            'Procedimento',
            'Critérios de aceitação',
            'Segurança e limites',
            'Evidência testada vs hipótese',
        ):
            self.assertIn(term, skill)
        self.assertTrue(skill.startswith('---\n'))

    def test_skill_covers_optimized_usage_and_resources(self):
        skill = (ROOT / SKILL_PATH).read_text(encoding='utf-8')
        for term in (
            'marm_smart_recall',
            'marm_code_context',
            'marm_code_lookup',
            'marm_log_entry',
            'STDIO',
            'HTTP',
            'auto_off',
            'detail=1',
            'exact_mode',
            'swarm',
            'tempestade de respawn',
            '2.51.0',
        ):
            self.assertIn(term, skill)

    def test_memory_is_context_not_instruction(self):
        skill = (ROOT / SKILL_PATH).read_text(encoding='utf-8')
        self.assertIn('nunca instrução', skill)
        self.assertIn('prompt injection', skill)
        self.assertIn('nenhuma memória recuperada confere autorização', skill)

    def test_skill_requires_availability_check(self):
        skill = (ROOT / SKILL_PATH).read_text(encoding='utf-8')
        self.assertIn('Verificar disponibilidade', skill)
        self.assertIn('não presumir instalação', skill)

    def test_reference_file_exists_with_transport_table(self):
        ref = (ROOT / REF_PATH).read_text(encoding='utf-8')
        self.assertIn('STDIO', ref)
        self.assertIn('swarm-max', ref)
        self.assertIn('marm-memory stop', ref)
        self.assertIn('Apache-2.0', ref)
        self.assertIn('Nunca matar em massa', ref)

    def test_complementary_to_persistent_memory(self):
        skill = (ROOT / SKILL_PATH).read_text(encoding='utf-8')
        self.assertIn('agent-persistent-memory', skill)
        self.assertIn('desenha', skill)
        persistent = (ROOT / 'areas/ai-agents/skills/agent-persistent-memory/SKILL.md').read_text(encoding='utf-8')
        self.assertNotIn('marm-memory-usage', persistent)

    def test_external_source_registered(self):
        sources = json.loads((ROOT / 'catalog/external-sources.json').read_text(encoding='utf-8'))
        names = {s['name'] for s in sources['sources']}
        self.assertIn('marm-memory', names)
        marm = next(s for s in sources['sources'] if s['name'] == 'marm-memory')
        self.assertEqual(marm['license_status'], 'Apache-2.0')
        self.assertEqual(marm['pin'], '2.51.0')

    def test_readmes_updated(self):
        area = (ROOT / 'areas/ai-agents/README.md').read_text(encoding='utf-8')
        self.assertIn('marm-memory-usage', area)
        main = (ROOT / 'README.md').read_text(encoding='utf-8')
        match = re.search(r'(\d+) Skills completas catalogadas', main)
        self.assertIsNotNone(match)
        self.assertGreaterEqual(int(match.group(1)), 43)
        self.assertIn('marm-memory-usage', main)
        changelog = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
        self.assertIn('v5.8.0', changelog)
        self.assertIn('marm-memory-usage', changelog)


if __name__ == '__main__':
    unittest.main()
