import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG = Path('areas/ai-agents/skills/rag-architecture/SKILL.md')
RAG_TYPES = Path('areas/ai-agents/skills/rag-architecture/references/types-and-components.md')
RAG_EVAL = Path('areas/ai-agents/skills/rag-architecture/references/evaluation-and-security.md')


def frontmatter_version(path):
    text = (ROOT / path).read_text(encoding='utf-8')
    match = re.search(r'version:\s*"([0-9.]+)"', text)
    return match.group(1) if match else None


class RagArchitectureV59Tests(unittest.TestCase):
    def test_catalog_registers_rag_skill(self):
        catalog = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
        self.assertEqual(catalog['version'], '5.9.0')
        self.assertEqual(catalog['count'], 44)
        self.assertEqual(len(catalog['skills']), 44)
        records = {item['id']: item for item in catalog['skills']}
        self.assertIn('rag-architecture', records)
        record = records['rag-architecture']
        self.assertEqual(record['version'], '1.0.0')
        self.assertEqual(record['area'], 'ai-agents')
        self.assertEqual(record['path'], 'areas/ai-agents/skills/rag-architecture/SKILL.md')
        self.assertEqual(frontmatter_version(record['path']), '1.0.0')

    def test_upgraded_skill_versions_in_catalog(self):
        catalog = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))
        records = {item['id']: item for item in catalog['skills']}
        expected = {
            'ml-lifecycle-validation': '1.1.0',
            'agent-learning-finetuning': '1.1.0',
            'agent-persistent-memory': '1.0.1',
            'llm-model-selection-benchmark': '1.0.1',
            'second-brain-architecture': '1.0.1',
            'company-brain-architecture': '1.0.1',
            'code-intelligence-engineering': '1.0.1',
        }
        for sid, ver in expected.items():
            self.assertEqual(records[sid]['version'], ver, sid)
            self.assertEqual(frontmatter_version(records[sid]['path']), ver, sid)

    def test_rag_skill_contracts_present(self):
        skill = (ROOT / RAG).read_text(encoding='utf-8')
        for term in (
            'Quando usar',
            'nunca devem ser confundidos',
            'Procedimento',
            'Critérios de aceitação',
            'Segurança e limites',
            'Evidência testada vs hipótese',
        ):
            self.assertIn(term, skill)
        self.assertTrue(skill.startswith('---\n'))

    def test_rag_skill_covers_types(self):
        skill = (ROOT / RAG).read_text(encoding='utf-8')
        for term in (
            'Léxico',
            'Densa',
            'Híbrida',
            'Rerankada',
            'GraphRAG',
            'Code RAG',
            'Multimodal',
            'Agêntico',
        ):
            self.assertIn(term, skill)

    def test_rag_skill_covers_evaluation_and_security(self):
        skill = (ROOT / RAG).read_text(encoding='utf-8')
        for term in (
            'recall@k',
            'MRR',
            'nDCG',
            'faithfulness',
            'abstention',
            'golden set',
            'prompt injection',
            'ACL',
            'chunking',
            'reranker',
        ):
            self.assertIn(term, skill)

    def test_rag_skill_requires_incremental_evolution(self):
        skill = (ROOT / RAG).read_text(encoding='utf-8')
        self.assertIn('Evolução incremental', skill)
        self.assertIn('evidência de que o anterior não resolve', skill)
        self.assertIn('RETRIEVAL_DESIGN.md', skill)

    def test_rag_references_exist(self):
        types = (ROOT / RAG_TYPES).read_text(encoding='utf-8')
        for term in ('Reciprocal Rank Fusion', 'tree-sitter', 'RRF', 'sqlite-vec'):
            self.assertIn(term, types)
        evaluation = (ROOT / RAG_EVAL).read_text(encoding='utf-8')
        for term in ('GOLDEN_SET', 'recall@k', 'Faithfulness', 'injeção', 'Rollback'):
            self.assertIn(term, evaluation)

    def test_rag_skill_defers_to_sibling_skills(self):
        skill = (ROOT / RAG).read_text(encoding='utf-8')
        for term in (
            'agent-persistent-memory',
            'second-brain-architecture',
            'company-brain-architecture',
            'code-intelligence-engineering',
            'llm-model-selection-benchmark',
            'agent-learning-finetuning',
        ):
            self.assertIn(term, skill)

    def test_ml_lifecycle_upgrades(self):
        skill = (ROOT / 'areas/machine-learning/skills/ml-lifecycle-validation/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('agreement entre anotadores', skill)
        self.assertIn('somente após o split', skill)
        self.assertIn('recall@k, MRR, nDCG', skill)
        self.assertIn('rag-architecture', skill)

    def test_finetuning_base_model_step(self):
        skill = (ROOT / 'areas/ai-agents/skills/agent-learning-finetuning/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('Escolher o modelo base por benchmark na tarefa real', skill)
        self.assertIn('llm-model-selection-benchmark', skill)
        self.assertIn('ml-lifecycle-validation', skill)
        self.assertIn('rag-architecture', skill)

    def test_cross_references_added(self):
        pairs = {
            'areas/ai-agents/skills/agent-persistent-memory/SKILL.md': 'rag-architecture',
            'areas/ai-agents/skills/llm-model-selection-benchmark/SKILL.md': 'rag-architecture',
            'areas/personal-knowledge/skills/second-brain-architecture/SKILL.md': 'rag-architecture',
            'areas/enterprise-knowledge/skills/company-brain-architecture/SKILL.md': 'rag-architecture',
            'areas/software-engineering/skills/code-intelligence-engineering/SKILL.md': 'rag-architecture',
        }
        for path, term in pairs.items():
            self.assertIn(term, (ROOT / path).read_text(encoding='utf-8'), path)

    def test_readmes_and_changelog_updated(self):
        area = (ROOT / 'areas/ai-agents/README.md').read_text(encoding='utf-8')
        self.assertIn('rag-architecture', area)
        ml_area = (ROOT / 'areas/machine-learning/README.md').read_text(encoding='utf-8')
        self.assertIn('visão e embeddings', ml_area)
        main = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('44 Skills', main)
        self.assertIn('arquitetura RAG', main)
        changelog = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
        self.assertIn('v5.9.0', changelog)
        self.assertIn('rag-architecture', changelog)


if __name__ == '__main__':
    unittest.main()
