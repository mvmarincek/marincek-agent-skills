import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class VisualQualityV57Tests(unittest.TestCase):
    def test_catalog_and_frontmatter_versions(self):
        catalog = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
        self.assertEqual(catalog['version'], '5.7.0')
        self.assertEqual(catalog['count'], 42)
        expected = {
            'photoreal-3d-assets': '1.3.0',
            'immersive-experience-quality': '1.1.0',
            'immersive-commerce-3d': '1.2.0',
        }
        records = {item['id']: item for item in catalog['skills']}
        for skill_id, version in expected.items():
            with self.subTest(skill=skill_id):
                record = records[skill_id]
                self.assertEqual(record['version'], version)
                text = (ROOT / record['path']).read_text(encoding='utf-8')
                match = re.search(r'version:\s*"([0-9.]+)"', text)
                self.assertIsNotNone(match)
                self.assertEqual(match.group(1), version)

    def test_generation_routes_are_not_confused(self):
        skill = (ROOT / 'areas/games/skills/photoreal-3d-assets/SKILL.md').read_text(encoding='utf-8')
        for term in ('Kling', 'Wan', 'Higgsfield', 'GLB', 'custo/créditos', 'aprovação'):
            self.assertIn(term, skill)
        self.assertIn('nunca malha GLB', skill)
        self.assertIn('não pode passar G2', skill)

    def test_visual_gate_blocks_placeholder_and_requires_evidence(self):
        skill = (ROOT / 'areas/games/skills/immersive-experience-quality/SKILL.md').read_text(encoding='utf-8')
        for term in ('placeholder', 'FAIL', 'NOT_TESTED', 'Scorecard humano', 'média ≥4.5/5', 'runtime real', 'assinatura explícita'):
            self.assertIn(term, skill)

    def test_commerce_release_requires_visual_signoff(self):
        skill = (ROOT / 'areas/web-marketing/skills/immersive-commerce-3d/SKILL.md').read_text(encoding='utf-8')
        for term in ('Gate de liberação visual', 'G2 `PASS` assinado por humano', '`NOT_READY`', 'não chamar a cena de pronta'):
            self.assertIn(term, skill)

    def test_area_readmes_document_the_hard_gate(self):
        games = (ROOT / 'areas/games/README.md').read_text(encoding='utf-8')
        web = (ROOT / 'areas/web-marketing/README.md').read_text(encoding='utf-8')
        self.assertIn('não passa gate visual de release', games)
        self.assertIn('NOT_READY', web)


if __name__ == '__main__':
    unittest.main()
