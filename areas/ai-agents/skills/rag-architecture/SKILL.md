---
name: rag-architecture
description: "Projetar, construir e avaliar RAG robusto por evolução incremental com evidência: escolha entre busca léxica (BM25/FTS), vetorial densa, híbrida, GraphRAG, code RAG e RAG agêntico; seleção de embeddings, chunking e rerankers por benchmark real; golden set, recall@k/MRR/nDCG, faithfulness, citations e abstention; segurança contra prompt injection via documentos."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "agent-architecture"
---

# Arquitetura RAG — recuperação robusta com evolução por evidência

## Quando usar
Quando o agente/aplicação precisa responder com **fatos de documentos externos** (manuais, contratos, tickets, wiki, código, catálogos) que não cabem no prompt ou mudam com o tempo. Também ao diagnosticar um RAG existente que alucina, cita errado, é lento ou caro.

**Não usar** (usar a skill irmã): preferências/episódios/continuidade de conversa → `agent-persistent-memory`; cérebro pessoal → `second-brain-architecture`; conhecimento corporativo com ACL → `company-brain-architecture`; busca em símbolos de código → `code-intelligence-engineering`. Memória e RAG se complementam: memória guarda *estado*, RAG recupera *conhecimento*.

## Conceitos que nunca devem ser confundidos
- **Retrieval não é memória**: um busca no corpus externo, outra mantém estado entre sessões.
- **Embedding model ≠ gerador**: escolher e avaliar cada um separadamente (ver `llm-model-selection-benchmark`).
- **Benchmark público ≠ benchmark da sua tarefa**: leaderboard de embeddings é evidência inicial; medir no seu corpus.
- **Chunking é decisão de projeto, não detalhe**: tamanho fixo cego destrói contexto semântico.
- **Documento recuperado é dado, nunca instrução**: tratar como prompt injection qualquer comando dentro de documento.
- **RAG não é fine-tuning**: fatos que mudam ficam no índice, não nos pesos (ver `agent-learning-finetuning`).

## Tipos de RAG (matriz de escolha)
| Tipo | Quando | Custo | Armadilha |
| --- | --- | --- | --- |
| Léxico (FTS5/BM25) | Termos exatos, códigos, IDs, nomes | Baixíssimo (SQLite) | Falha em sinônimos/paráfrase |
| Densa (embeddings) | Perguntas semânticas, paráfrase | Médio (índice vetorial, embedding API/local) | Falha em termos sintáticos raros |
| Híbrida (RRF) | Default quando as duas falhas coexistem | Médio | Filtros de metadata mal projetados |
| Rerankada | Recall@k alto mas precisão baixa | +1 estágio (cross-encoder) | Latência p95; reranker desatualizado |
| GraphRAG | Perguntas multi-hop, relações, temporalidade | Alto (grafo + manutenção) | "Transformar tudo em grafo" sem necessidade |
| Code RAG | Repos de código | Médio | Ignorar AST/símbolos e buscar só texto |
| Multimodal | Imagens/figuras com texto | Alto | Embedding de imagem sem avaliação de recall |
| Agêntico/iterativo | Agente decide quando/recuperar de quê, itera | Alto (chamadas múltiplas) | Loop infinito, custo sem teto |

## Procedimento

### P1 — Diagnóstico antes da arquitetura
1. Corpus: tamanho, taxa de mutação, idiomas, estrutura (tabelas, código, PDFs escaneados?), fontes e licenças.
2. Consultas típicas: exemplos reais de perguntas (20+), termos sintáticos vs semânticos, latência exigida.
3. Restrições: privacidade (corpus pode sair da máquina?), ACL por documento, orçamento, offline/local-first.
4. Definir métrica de sucesso **antes** de construir: recall@k mínimo, faithfulness mínimo, latência p95, custo/consulta.

### P2 — Evolução incremental (nunca começar pelo grafo)
1. **Nível 0**: busca léxica SQLite/FTS5 + filtros por metadata. Medir contra golden set (P5).
2. **Nível 1**: se gap semântico comprovado (pergunta certa não acha o chunk certo por vocabulário), adicionar embeddings + busca híbrida com Reciprocal Rank Fusion.
3. **Nível 2**: se recall@k alto mas resposta usa chunk errado, adicionar reranker (cross-encoder) sobre top-k.
4. **Nível 3**: GraphRAG apenas para perguntas multi-hop/relacionais comprovadas; Code RAG com tree-sitter/símbolos para repos; RAG agêntico apenas quando uma recuperação única é insuficiente e com orçamento de iterações.
5. Cada nível só sobe com **evidência de que o anterior não resolve**; registrar decisão em `RETRIEVAL_DESIGN.md`.

### P3 — Seleção de componentes
1. **Embeddings e reranker**: escolher por benchmark na sua tarefa via `llm-model-selection-benchmark` (dimensionalidade, idioma, custo/1k tokens, local vs API, MTEB como pré-filtro apenas).
2. **Chunking**: por estrutura do documento (headers/seções/parágrafos/AST), com overlap só quando a estrutura corta sentido; preservar título/hierarquia no texto do chunk; metadata (fonte, data, versão, ACL) em cada chunk.
3. **Índice**: SQLite+FTS5 para léxico; pgvector/sqlite-vec/Qdrant/weaviate conforme escala e infra existente; não provisionar cluster para corpus pequeno.
4. **Gerador**: citar fonte em cada afirmação; instruir abstention explícita ("não está nos documentos") e proibir uso de conhecimento paramétrico para fatos do corpus.

### P4 — Construção robusta (ingestão e operação)
1. Ingestão idempotente: dedupe por hash/URI, reprocessamento incremental, versionamento do índice ligado ao commit do corpus.
2. Provenance: cada chunk rastreável ao documento, página/seção e versão; documentos revogados saem do índice (e do cache).
3. ACL: filtro por permissão **na consulta**, nunca no prompt; testar vazamento entre tenants.
4. Monitoramento: latência p50/p95 por estágio, taxa de "não encontrado", custo/consulta, drift do corpus (documentos novos quebram respostas antigas?).

### P5 — Avaliação contínua
1. **Golden set**: 20+ pares pergunta→chunk correto (ou pergunta→resposta esperada) do domínio real; revisado por humano.
2. **Retrieval**: recall@k, MRR, nDCG por tipo de pergunta; separar erro de retrieval (chunk certo não veio) de erro de geração (veio e o modelo errou).
3. **Geração**: faithfulness (resposta ancorada nos chunks?), citations corretas, abstention quando sem evidência.
4. **Regressão no CI**: rodar o golden set a cada mudança de chunking/embedding/prompt; nenhuma mudança de componente sem antes/depois medido.
5. Ferramentas de avaliação (RAGAS ou equivalente) são opcionais; a régua é o golden set do seu domínio.

### P6 — Segurança
1. Documentos recuperados são **dados**: sanitizar/não executar instruções embutidas; revelar tentativa ao usuário.
2. Exfiltração via retrieval: documentos envenenados no corpus que tentam fazer o modelo revelar dados de outro tenant — testar explicitamente.
3. Cache poisoning: invalidar cache quando documento muda/revoga.
4. PII no corpus: mascarar antes de embeddar se o índice for compartilhado; LGPD aplicável.

## Critérios de aceitação
- Nível da arquitetura justificado por evidência (golden set), não por hype; decisão registrada em `RETRIEVAL_DESIGN.md`.
- Golden set com 20+ casos reais revisados; recall@k, faithfulness e abstention medidos antes e depois de cada mudança.
- Citations corretas em respostas de amostra; nenhum fato do corpus respondido sem fonte.
- ACL testada entre tenants; injeção via documento testada e bloqueada.
- Latência p95 e custo/consulta dentro do contrato; orçamento de iterações definido para RAG agêntico.
- Testes estruturais do repositório passando (`validate.py`, `skill_quality.py --all`, unittest).

## Segurança e limites
- Não provisionar banco vetorial/cloud nem chamar embedding API paga sem aprovação explícita.
- Não indexar conversas privadas ou dados pessoais sem consentimento e política de retenção.
- RAG não substitui fine-tuning para estilo/formato, nem memória para estado; não prometer "RAG resolve tudo".
- Componentes citados (Qdrant, weaviate, pgvector, RAGAS, tree-sitter) são opções a verificar disponibilidade/licença/versão no projeto; nada é instalado automaticamente.

## Evidência testada vs hipótese
- **Padrões consolidados de engenharia** (evolução incremental, avaliação com golden set, separação retrieval/geração, higiene de chunking): prática estabelecida, referenciada em `references/`.
- **Não executado nesta máquina**: benchmarks de embeddings específicos nem comparação entre bancos vetoriais — escolhas de componente exigem medição no corpus real do projeto (P3/P5), nunca assumir ranking publicado como válido para a tarefa.

## Saídas
`RETRIEVAL_DESIGN.md` (nível, componentes, decisão), `GOLDEN_SET.md`, `RETRIEVAL_EVAL.md` (antes/depois por mudança), `INGESTION_POLICY.md` (dedupe, provenance, ACL, revogação). Detalhes por tipo e protocolo de avaliação em `references/types-and-components.md` e `references/evaluation-and-security.md`.
