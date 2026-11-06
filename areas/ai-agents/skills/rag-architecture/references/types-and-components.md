# RAG: tipos, componentes e decisões

Referência da skill `rag-architecture`. Padrões de engenharia consolidados; números e rankings de ferramentas mudam — verificar no momento do projeto.

## Árvore de decisão rápida

1. A pergunta usa termos exatos (códigos, IDs, nomes de função, chaves de erro)? → **Léxico** (SQLite FTS5/BM25) resolve; custo mínimo, local-first.
2. A pergunta parafraseia o documento ("como faço pra cancelar" vs "política de cancelamento")? → precisa de **densa/híbrida**.
3. O chunk certo chega no top-k mas o modelo escolhe o errado? → **reranker** cross-encoder.
4. A resposta exige encadear fatos de vários documentos ("quem é o gestor do projeto que o fornecedor X participa?")? → **GraphRAG**.
5. O corpus é código? → **Code RAG** com tree-sitter/LSP (símbolos, definições, call graph), não só texto plano.
6. Uma recuperação não basta e o agente precisa decidir buscar de novo ou em outra fonte? → **RAG agêntico** com orçamento de iterações.

## Componentes por estágio

### Chunking
- Base estrutural, não tamanho fixo: headers/seções Markdown, nós AST de código, artigos de contrato, páginas de manual.
- Chunk carrega contexto próprio: título/hierarquia prefixada, metadata (source_id, url, data, versão, tenant/ACL).
- Overlap apenas quando a estrutura corta sentido no meio (parágrafos longos); medir impacto no golden set.
- Tabelas e código: manter coesos (não fatiar linha a linha); avaliar serialização de tabela em texto.

### Embeddings
- Seleção por benchmark na tarefa (ver `llm-model-selection-benchmark`): MTEB é pré-filtro; medir recall@k no corpus do projeto.
- Critérios: idioma (pt-BR incluso?), dimensionalidade (custo de armazenamento), local vs API, custo/1M tokens, licensa.
- Re-embeddar tudo ao trocar de modelo: embeddings de famílias diferentes não são comparáveis; versionar o índice por modelo.

### Reranker
- Cross-encoder sobre top-k (10–50): melhora precisão à custa de latência; medir p95.
- Avaliar se o ganho em faithfulness/citation justifica o custo por consulta.

### Índice vetorial
- Escala pequena/média (até ~centenas de milhares de chunks): SQLite (sqlite-vec) ou pgvector no Postgres existente.
- Escala grande/filtros complexos/HA: Qdrant, Weaviate, etc. — provisionar somente com necessidade comprovada e aprovação (custo/infra).
- Híbrido: guardar FTS e vetor no mesmo banco quando possível; fusão por Reciprocal Rank Fusion (RRF).

### GraphRAG
- Justificativa: perguntas multi-hop, relações entidades-tempo, "por quê/caminho".
- Custo: extração de entidades/relações (LLM), manutenção do grafo, re-extrair em mudança de corpus.
- Alternativa mais barata primeiro: híbrido + metadata filters + joins em SQL resolvem muitos casos "multi-hop".

### RAG agêntico
- Agente decide: buscar ou responder, qual fonte, quantas iterações, quando parar.
- Obrigatório: orçamento de iterações/chamadas, custo por consulta limitado, loop de parada (resposta suficiente ou desiste com abstention).

## Padrões de falha comuns (diagnóstico)

| Sintoma | Causa provável | Correção |
| --- | --- | --- |
| Alucina fato do domínio | Retrieval falhou e gerador usa conhecimento paramétrico | Medir recall@k; instruir/proibir fallback paramétrico; abstention |
| Cita fonte errada | Rerank ausente ou chunk sem metadata | Reranker; provenance por chunk |
| Termo exato não acha | Só embeddings (denso falha em sintático) | Híbrido com FTS |
| Pergunta parafraseada não acha | Só léxico | Embeddings + RRF |
| Resposta quebra após update do corpus | Chunking/índice sem versionamento; cache stale | Ingestão incremental versionada; invalidar cache |
| Latência p95 alto | Reranker pesado, k grande, grafo grande | Reduzir k, rerank só top-10, medir por estágio |
| Fatura surpresa | Embedding API em ingestão grande, iterações agênticas sem teto | Estimativa antes de ingestão; orçamento de iterações |
