import json, pathlib, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]
NEW = [
    'delivery-acceptance',
    'runtime-error-triage',
    'database-blueprints',
    'deploy-diagnosis',
    'whatsapp-bot-scaffold',
    'whatsapp-brazil-knowledge',
]

class CoreDeliverySkillTests(unittest.TestCase):
    def test_six_skills_present(self):
        manifest = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
        self.assertGreaterEqual(manifest['count'], 34)
        entries = {x['id']: x for x in manifest['skills']}
        for name in NEW:
            self.assertIn(name, entries)
            p = ROOT / entries[name]['path']
            self.assertTrue(p.is_file())
            t = p.read_text(encoding='utf-8')
            self.assertTrue(('## Crit' in t) or ('## Aceite' in t))
            self.assertTrue((p.parent / 'references').is_dir() or (p.parent / 'assets').is_dir())

    def test_reference_files_exist(self):
        manifest = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
        entries = {x['id']: x for x in manifest['skills']}
        cases = {
            'delivery-acceptance': ['acceptance-checklist.md', 'playwright-smoke.md', 'mobile-print-file.md'],
            'runtime-error-triage': ['error-taxonomy.md', 'fix-workflow.md', 'common-runtime-errors.md'],
            'database-blueprints': ['core-schema.md', 'supabase-postgres.md', 'mysql.md', 'prisma.md', 'migration-safety.md'],
            'deploy-diagnosis': ['project-detection.md', 'public-url.md', 'docker-coolify.md', 'paas-targets.md'],
            'whatsapp-brazil-knowledge': ['compliance.md', 'business-api.md', 'pix-payment.md', 'merchant-workflow.md'],
        }
        for name, files in cases.items():
            root = (ROOT / entries[name]['path']).parent / 'references'
            for f in files:
                self.assertTrue((root / f).is_file(), f'{name}: {f}')

    def test_whatsapp_template_structure(self):
        base = ROOT / 'areas/web-marketing/skills/whatsapp-bot-scaffold/assets/template'
        for rel in ('package.json', '.env.example', 'src/index.js', 'src/conversation/state-machine.js', 'src/payments/pix-generator.js', 'src/utils/lgpd.js', 'src/webhook/handler.js'):
            self.assertTrue((base / rel).is_file(), rel)
        env = (base / '.env.example').read_text(encoding='utf-8')
        self.assertNotIn('STARKBANK_PRIVATE_KEY=-----BEGIN', env)

if __name__ == '__main__':
    unittest.main()
