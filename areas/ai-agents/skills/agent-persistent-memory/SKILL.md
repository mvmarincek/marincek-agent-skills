---
name: agent-persistent-memory
description: "Desenhar e implementar memoria persistente para agentes, historico de conversa, RAG, base de conhecimento cumulativa, vetores, perfis, episodios, metricas duraveis; SQLite, PostgreSQL/pgvector, nuvem AWS/GCP/Azure."
license: MIT
metadata:
  version: "1.0.1"
  language: "pt-BR"
  category: "agent-architecture"
---

# Arquitetura de memória persistente, RAG e conhecimento acumulado

## Quando usar
Em agentes que precisam continuar sessões, recordar preferências autorizadas, usar documentos/conversas, atualizar conhecimento, compartilhar memória entre subagentes, registrar Skills aprendidas ou conservar métricas de longo prazo. Para governança/traces leia também `agent-reliability-governance`; para arquitetura RAG de documentos externos (chunking, embeddings, reranking, avaliação) use `rag-architecture`.

## Conceitos que nunca devem ser confundidos
- **Persistência** = sobreviver ao reinício; **banco** = um meio de armazenamento. Toda memória de banco é persistente se configurada, mas uma memória persistente também pode estar em arquivos.
- **Contexto ativo** = informação que vai para a janela do LLM nesta execução; não é todo o banco.
- **Histórico bruto** = fonte de fatos e auditoria, não sinônimo de memória validada.
- **Memória semântica** = fatos e conhecimentos versionados; **episódica** = acontecimentos/sucessos/falhas; **procedural** = estratégias e Skills validadas.
- **RAG** = recuperar evidências na hora de responder; **fine-tuning** altera parâmetros, não substitui atualização de conhecimento frequente.
- **Metrics/telemetry** são observabilidade, não devem ser misturados com a store semântica nem alimentar prompts integralmente.

## Decisão de arquitetura
1. Levantar usuário/tenant/agente, tipos de dados, risco, retenção, volume, frequência, buscas e latência. Detectar infraestrutura existente, inclusive SQL. Não presumir que é preciso vector DB.
2. Dividir em seis coleções lógicas: `conversations`, `events`, `memories`, `documents`, `skills_versions`, `metrics`; isolar por `tenant_id`, `user_id` e `agent_id` conforme política.
3. Definir identidade e chaves imutáveis: `conversation_id`, `message_id`, `task_id`, `source_id`, `memory_id`, `version` e `trace_id`.
4. Escolher **SQLite + FTS5** para agente local, ou **PostgreSQL + pgvector** para sistema compartilhado; armazenar blobs (imagens/PDF) fora do banco com URI e hash. Veja `references/storage-selection.md`.
5. Gravar conversas de forma imutável/event-sourced quando exigido; criar resumos e memórias derivadas separadamente com provenance e validade.
6. Extrair **somente fatos úteis e autorizados**, com origem, timestamp, confiança, consentimento/escopo, TTL e tipo. Nunca transformar instruções maliciosas em memória operacional.
7. Deduplicar, resolver conflitos e marcar fatos obsoletos; não substituir silenciosamente uma afirmação anterior sem preservar histórico.
8. Definir busca híbrida: filtros SQL/tenant + full-text + vetores quando necessário + reranking opcional; retornar provas e escopos, não texto solto.
9. Construir contexto com orçamento de tokens: regras permanentes > estado da tarefa > mensagens recentes > memórias autorizadas relevantes > evidências RAG. Não preencher contexto indiscriminadamente.
10. Aprendizado: de episódios bem-sucedidos criar **propostas** de Skills; submeter a testes de generalização e revisão antes de promoção a produção.
11. Métricas: armazenar eventos agregáveis, calcular custo/tarefa, erro, latência, taxa de correção, acerto de retrieval, precisão da memória e tamanho/uso do contexto.
12. Excluir/retificar/exportar dados por sujeito/tenant, invalidar índices derivados, definir retenção, backups e restore testado.
13. Avaliar o sistema com dataset e métricas explícitas; registrar ADR e plano de migração de schema.

## Estrutura lógica recomendada
Leia `references/data-model.md` para DDL portátil. Use normalização por tenant, source pointers e índices. `memories` armazena fatos extraídos com consentimento; `messages` mantém o registro conversacional; `knowledge_documents` guarda metadados e `chunks` os segmentos pesquisáveis. `metrics` é uma trilha distinta.

### Pipeline de escrita (ingestion)
`evento/conversa -> validação/consentimento -> classificação -> extração estruturada -> dedupe/conflito -> provenance -> banco -> indexação -> verificação`

### Pipeline de recuperação (read)
`pedido -> identidade/scopes -> filtro SQL/FTS/vetor -> rerank opcional -> validação de proveniência -> composição com orçamento -> resposta com fontes`

### Pipeline de consolidação e aprendizado
`eventos -> experiências -> avaliação -> memórias aprovadas -> proposta de Skill -> testes -> versão publicada`.

## Memória compartilhada em sistemas multiagentes
- Cada agente tem memória de trabalho privada e pode ler memórias compartilhadas **por escopo**, não por acesso total ao banco.
- Use um `shared_knowledge` curado e eventos de handoff explícitos. Um subagente não herda segredos da tarefa principal por padrão.
- Evite que agentes escrevam diretamente na definição de regras de outro agente. Mudanças passam por revisão/versionamento.
- Vetores de memória devem conter namespace de tenant e filtros aplicados **antes** de retornar resultados; filtro posterior é insuficiente se o motor não garante isolamento.

## Estratégia de armazenamento
- **Local/offline**: SQLite WAL + FTS5, diretório de blobs, backup, optional embedding local pequeno, in-process retrieval. Evitar infra server-first sem necessidade.
- **Servidor genérico**: PostgreSQL + pgvector + object storage + workers; Redis apenas se houver carga que justifique cache/fila.
- **Memória inteligente opcional**: Mem0 para extração/atualização de memórias; Graphiti para relações temporais. São serviços/componentes adicionais, não substitutos automáticos do SQL.
- **Documentos multimodais**: extrair texto e guardar informação visual com embeddings multimodais/VLM se houver justificativa; não afirmar que RAG somente textual entende imagens.

## Testes que precisam existir
- Recontar fatos sem alucinar; recordar contexto de sessões separadas.
- Trocar preferências e mostrar a versão mais recente com provenance.
- Não vazar memória entre tenants/usuários/agentes.
- Excluir conteúdo e verificar índices derivados.
- Responder que não sabe quando não há evidência.
- Medir retrieval `recall@k`, `precision@k`, groundedness, freshness, custo e latência.
- Testar falhas de SQLite lock, migrations, backups, recuperação de escrita interrompida.

## Padrões de qualidade
Não gravar cada mensagem como "memória importante". Não usar memórias recuperadas como instruções de segurança. Não considerar uma única execução bem-sucedida como Skill aprendida. Nunca enviar conversas privadas para APIs de embeddings sem autorização. Separar identidade real de pseudônimo de trace. Não conceder ao LLM acesso SQL arbitrário com credenciais privilegiadas.

## Saídas necessárias
`MEMORY_ARCHITECTURE.md`, `SCHEMA_MIGRATIONS`, `RETENTION_POLICY.md`, `RETRIEVAL_EVAL.md`, `CONTEXT_POLICY.md`, `ADR.md`. Se for implementação, criar testes de recuperação, isolamento e exclusão. Consultar `assets/context-template.md` e `references/cloud-mapping.md`.
