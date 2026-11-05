import json, pathlib, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]

# 4 skills originais da v5.4, recriadas sob licenca MIT da biblioteca
# (capacidades equivalentes a skills de terceiros, conteudo original)
NEW_SKILLS = {
    'code-review': ['review-checklist.md', 'finding-report-format.md'],
    'diagnosing-bugs': ['diagnosis-loop.md', 'evidence-log.md'],
    'gh-cli': ['core-commands.md', 'auth-and-accounts.md'],
    'linear-workflows': ['linear-objects.md', 'graphql-cheatsheet.md'],
}

AREAS = {
    'code-review': 'software-engineering',
    'diagnosing-bugs': 'software-engineering',
    'gh-cli': 'devops-infrastructure',
    'linear-workflows': 'product-management',
}


def _manifest():
    return json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))


class V54OriginalSkillsTests(unittest.TestCase):
    def test_catalog_counts_40_skills(self):
        manifest = _manifest()
        self.assertGreaterEqual(manifest['count'], 40)
        self.assertEqual(manifest['count'], len(manifest['skills']))
        self.assertGreaterEqual(
            tuple(int(n) for n in manifest['version'].split('.')), (5, 4)
        )

    def test_four_skills_present_with_house_format(self):
        manifest = _manifest()
        entries = {x['id']: x for x in manifest['skills']}
        for name, refs in NEW_SKILLS.items():
            self.assertIn(name, entries, name)
            # area correta no catalogo e no frontmatter
            self.assertEqual(entries[name]['area'], AREAS[name], name)
            skill_path = ROOT / entries[name]['path']
            expected_path = ROOT / 'areas' / AREAS[name] / 'skills' / name / 'SKILL.md'
            self.assertEqual(skill_path, expected_path, name)
            self.assertTrue(skill_path.is_file(), name)
            text = skill_path.read_text(encoding='utf-8')
            # frontmatter da casa
            self.assertIn(f'name: {name}', text, name)
            self.assertIn('description:', text, name)
            self.assertIn('license: MIT', text, name)
            self.assertIn(f'area: "{AREAS[name]}"', text, name)
            # secoes obrigatorias
            self.assertIn('## Quando ativar', text, name)
            self.assertIn('## Contrato de entrada', text, name)
            self.assertIn('## Pipeline obrigatório', text, name)
            self.assertIn('## Segurança e permissões', text, name)
            self.assertIn('## Critério de aceite', text, name)
            # referencias declaradas existem
            ref_dir = skill_path.parent / 'references'
            self.assertTrue(ref_dir.is_dir(), name)
            for ref in refs:
                self.assertTrue((ref_dir / ref).is_file(), f'{name}: {ref}')

    def test_skills_declare_scope_boundaries(self):
        # cada skill nova distingue seu escopo de skills vizinhas
        manifest = _manifest()
        entries = {x['id']: x for x in manifest['skills']}
        boundaries = {
            'code-review': 'continuous-code-sanitization',
            'diagnosing-bugs': 'runtime-error-triage',
            'gh-cli': 'ci-fix-loop',
            'linear-workflows': 'linear-tasks-prd',
        }
        for name, neighbor in boundaries.items():
            text = (ROOT / entries[name]['path']).read_text(encoding='utf-8')
            self.assertIn(neighbor, text, f'{name}: deve delimitar escopo vs {neighbor}')
            # depende_on aponta para a vizinha
            self.assertIn(neighbor, entries[name].get('depends_on', []), name)

    def test_area_readmas_synced(self):
        checks = {
            'areas/software-engineering/README.md': ['code-review', 'diagnosing-bugs'],
            'areas/devops-infrastructure/README.md': ['gh-cli'],
            'areas/product-management/README.md': ['linear-workflows'],
        }
        for readme, names in checks.items():
            text = (ROOT / readme).read_text(encoding='utf-8')
            for name in names:
                self.assertIn(name, text, f'{readme}: {name}')

    def test_no_third_party_content_markers(self):
        # skills originais: sem caminhos ou creditos de repos de terceiros
        manifest = _manifest()
        entries = {x['id']: x for x in manifest['skills']}
        for name in NEW_SKILLS:
            skill_dir = (ROOT / entries[name]['path']).parent
            for f in skill_dir.rglob('*.md'):
                text = f.read_text(encoding='utf-8')
                self.assertNotIn('github.com/', text.replace('https://api.linear.app', ''), f'{f}')
                self.assertNotIn('adapted from', text.lower(), f'{f}')
                self.assertNotIn('Copyright (c) 20', text, f'{f}')

    def test_graphql_reference_has_auth_and_secrecy_rules(self):
        p = ROOT / 'areas/product-management/skills/linear-workflows/references/graphql-cheatsheet.md'
        text = p.read_text(encoding='utf-8')
        self.assertIn('LINEAR_API_KEY', text)
        self.assertIn('segredo', text.lower())
        # sem token literal de exemplo utilizavel
        self.assertNotIn('lin_api_', text)


if __name__ == '__main__':
    unittest.main()
