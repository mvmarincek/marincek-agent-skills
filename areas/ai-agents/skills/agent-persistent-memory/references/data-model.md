# Modelo lógico de persistência (adaptar ao SGBD)

## Tabelas
- `conversations(id, tenant_id, user_id, created_at, updated_at, status)`
- `messages(id, conversation_id, actor, content_uri_or_encrypted, created_at, seq, pii_class)`
- `events(id, trace_id, conversation_id, task_id, agent_id, type, payload_redacted, created_at)`
- `memories(id, tenant_id, subject_id, kind, fact_text, source_message_ids, confidence, valid_from, valid_to, status, updated_at)`
- `knowledge_documents(id, tenant_id, uri, title, source_system, acl, sha256, ingested_at, version)`
- `chunks(id, document_id, ordinal, text, embedding_model, embedding_version, embedding, token_count)`
- `skill_versions(id, skill_name, version, status, evidence_refs, created_at, approved_by)`
- `metric_events(id, trace_id, task_id, agent_id, metric_key, value, unit, observed_at, tags_json)`

## Identidade e isolamento
`tenant_id` em todas as entidades consultáveis e políticas no banco/serviço. Para SQL com multi-tenant, considerar row-level security do PostgreSQL mais identidade do serviço. Não dar ao LLM acesso ao DSN de superusuário.

## Índices
- unicidade em eventos por `(conversation_id, seq)` quando aplicável;
- índices de filtro `(tenant_id, subject_id, status)` para memórias;
- índice FTS para `chunks.text` e `memories.fact_text`;
- índice vetorial `pgvector` com condições de tenant/filtros e teste de planos;
- TTL/retention de eventos e métricas segundo política.

## Consistência
Escrita de mensagem e outbox de processamento em transação; workers idempotentes para embedding/indexação; versionamento da versão de skill/prompt/modelo. Não apagar imediatamente experiências históricas se houver obrigação legal de auditoria; aplicar política de privacidade/retention conciliada.

## Schema ilustrativo de memória
```json
{
 "memory_id":"uuid", "tenant_id":"t", "subject_id":"user-hash",
 "kind":"semantic", "fact":"O usuário prefere respostas em português",
 "source_ids":["message-123"], "created_at":"2026-11-01T00:00:00Z",
 "valid_from":"2026-11-01T00:00:00Z", "valid_to":null,
 "status":"proposed", "verification":"user_statement",
 "privacy_class":"low", "retention_policy":"user_choice"
}
```
Não preencher propriedades pessoais com inferência sem confirmação, nem manter dados sensíveis desnecessários.
