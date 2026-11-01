# Contratos de dados e ingestão do Company Brain

## Registro mínimo de fonte (exemplo)
```json
{
  "source_id": "linear:issue:TEAM-123",
  "source_kind": "issue",
  "tenant_id": "tenant-a",
  "workspace_id": "workspace-main",
  "owner_id": "owner-team",
  "visibility": "private",
  "classification": "internal",
  "acl_subjects": ["group:engineering"],
  "acl_version": "2026-11-01T10:00:00Z",
  "canonical_uri": "https://example.invalid/TEAM-123",
  "title": "Somente exemplo",
  "source_updated_at": "2026-11-01T10:00:00Z",
  "retrieved_at": "2026-11-01T10:01:00Z",
  "content_sha256": "sha256-por-calcular",
  "lifecycle": "active",
  "retention_policy": "policy-id"
}
```
A URI é placeholder, não uma integração real. Nunca confiar em `acl_subjects` enviados pelo próprio modelo; devem vir do sistema de identidade e fonte.

## Coleções lógicas
`identity_mapping`, `source_registry`, `documents`, `document_versions`, `segments`, `citation_refs`, `decisions`, `retrieval_events`, `access_events`, `ingestion_jobs`, `tombstones`.

## Estratégias
- Criar `source_id` e versão estáveis, `(tenant_id, source_id, content_hash)` para idempotência.
- Seguir backoff/exponential jitter nas quotas e honrar `Retry-After`; usar watermark com overlap para evitar eventos perdidos.
- Tombstone + invalidação de índice/cache antes de afirmar exclusão concluída.
- Não inserir transcrição de reunião sem base legal/consentimento aplicável.
- Tabelas/figuras: preservar referências de página e heading; criar modalidades separadas para OCR e visão.
- Contratos de migração: compatibilidade retroativa, dupla leitura temporária e reconciliação.
