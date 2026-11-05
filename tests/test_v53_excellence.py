import json, pathlib, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]

# 10 skills que nao tinham teste dedicado antes da v5.3
PREVIOUSLY_UNCOVERED = {
    'paint-draw-shapes': ['hid-input-protocol.md', 'recovery-undo-policy.md', 'visual-confirmation.md'],
    'skill-evaluator': ['metrics-and-gates.md'],
    'linear-tasks-prd': ['linear-communication.md', 'pdf-quality.md', 'prd-quality.md'],
    'authorized-security-testing': ['cloud-checks.md', 'rules-of-engagement.md', 'test-matrix.md'],
    'defensive-cybersecurity': ['ai-mcp-security.md', 'cloud-matrix.md', 'secure-sdlc.md'],
    'structured-agent-prompts': ['cloud-adapters.md', 'examples.md', 'prompt-rubric.md'],
    'agent-persistent-memory': ['cloud-mapping.md', 'data-model.md', 'storage-selection.md'],
    'agent-learning-finetuning': ['cloud-training.md', 'data-quality-and-eval.md', 'method-selection.md'],
    'voki-visual-geometry-cad': ['cad-3d.md', 'geometry-2d.md', 'visual-validation.md'],
    'agent-reliability-governance': ['cloud-mapping.md', 'contracts-evaluations.md', 'stack-matrix.md'],
}

# 2 skills novas da v5.3
NEW_SKILLS = {
    'mcp-server-factory': ['testing-distribution.md', 'tool-contract-design.md', 'transport-security.md'],
    'ci-fix-loop': ['failure-taxonomy.md', 'gh-commands.md'],
}

# skills aprofundadas na v5.3: id -> versao minima esperada no catalogo
REVISED_VERSIONS = {
    'paint-draw-shapes': '1.1.0',
    'skill-evaluator': '2.1.0',
    'delivery-acceptance': '1.2.0',
    'runtime-error-triage': '1.2.0',
    'whatsapp-brazil-knowledge': '1.2.0',
    'whatsapp-bot-scaffold': '1.2.0',
    'photoreal-3d-assets': '1.1.0',
    'mcp-server-factory': '1.0.0',
    'ci-fix-loop': '1.0.0',
}


def _manifest():
    return json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))


class V53ExcellenceTests(unittest.TestCase):
    def test_catalog_counts_36_skills(self):
        manifest = _manifest()
        self.assertGreaterEqual(manifest['count'], 36)
        self.assertEqual(manifest['count'], len(manifest['skills']))
        self.assertTrue(manifest['version'].startswith('5.3'))

    def test_ten_previously_uncovered_skills_structure(self):
        manifest = _manifest()
        entries = {x['id']: x for x in manifest['skills']}
        for name, refs in PREVIOUSLY_UNCOVERED.items():
            self.assertIn(name, entries, name)
            skill_path = ROOT / entries[name]['path']
            self.assertTrue(skill_path.is_file(), name)
            text = skill_path.read_text(encoding='utf-8')
            # formato-padrao da casa
            self.assertIn('name:', text, name)
            self.assertIn('description:', text, name)
            self.assertTrue(('## Quando ativar' in text) or ('## Ativa' in text) or ('## Quando usar' in text) or ('## Acionamento' in text), name)
            # secao de aceite/saida (nomes variam conforme a geracao da skill)
            accepted = ('## Crit', '## Aceite', '## Aceitação', '## Saída', '## Saidas', '## Entregáveis', '## Definição de sucesso')
            self.assertTrue(any(h in text for h in accepted), name)
            # referencias declaradas existem
            ref_dir = skill_path.parent / 'references'
            self.assertTrue(ref_dir.is_dir(), name)
            for ref in refs:
                self.assertTrue((ref_dir / ref).is_file(), f'{name}: {ref}')

    def test_new_skills_v53(self):
        manifest = _manifest()
        entries = {x['id']: x for x in manifest['skills']}
        for name, refs in NEW_SKILLS.items():
            self.assertIn(name, entries, name)
            skill_path = ROOT / entries[name]['path']
            self.assertTrue(skill_path.is_file(), name)
            text = skill_path.read_text(encoding='utf-8')
            self.assertIn('## Quando ativar', text, name)
            self.assertTrue(('## Crit' in text) or ('## Aceite' in text), name)
            ref_dir = skill_path.parent / 'references'
            for ref in refs:
                self.assertTrue((ref_dir / ref).is_file(), f'{name}: {ref}')

    def test_revised_versions(self):
        entries = {x['id']: x for x in _manifest()['skills']}
        for name, version in REVISED_VERSIONS.items():
            self.assertIn(name, entries, name)
            self.assertEqual(entries[name]['version'], version, name)

    def test_delivery_acceptance_regression_loop_reference(self):
        p = ROOT / 'areas/software-engineering/skills/delivery-acceptance/references/test-debug-fix.md'
        self.assertTrue(p.is_file())
        text = p.read_text(encoding='utf-8')
        self.assertIn('reprod', text.lower())
        self.assertIn('regress', text.lower())

    def test_paint_draw_shapes_depth(self):
        p = ROOT / 'areas/automation-hid/skills/paint-draw-shapes/SKILL.md'
        text = p.read_text(encoding='utf-8')
        self.assertGreater(len(text), 4000, 'SKILL.md deve ter profundidade alem do minimo')
        self.assertIn('VOKI', text)
        self.assertIn('USB HID', text)
        # rollback/limites presentes
        self.assertTrue(('recuperacao' in text.lower()) or ('rollback' in text.lower()) or ('undo' in text.lower()))

    def test_no_placeholder_references(self):
        manifest = _manifest()
        entries = {x['id']: x for x in manifest['skills']}
        checked = list(PREVIOUSLY_UNCOVERED) + list(NEW_SKILLS)
        for name in checked:
            skill_path = ROOT / entries[name]['path']
            text = skill_path.read_text(encoding='utf-8')
            self.assertNotIn('knowledge/', text, f'{name}: caminho knowledge/ legado')


if __name__ == '__main__':
    unittest.main()
