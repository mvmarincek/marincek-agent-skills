# Modelo local SQLite/FTS5 — referência inicial

```sql
PRAGMA foreign_keys=ON;
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS sources (
  source_id TEXT PRIMARY KEY, owner_id TEXT NOT NULL,
  uri TEXT, privacy TEXT NOT NULL CHECK(privacy IN ('private','shared','public')),
  content_hash TEXT NOT NULL, imported_at TEXT NOT NULL,
  original_created_at TEXT, original_updated_at TEXT,
  lifecycle TEXT NOT NULL DEFAULT 'active'
);
CREATE TABLE IF NOT EXISTS notes (
  note_id TEXT PRIMARY KEY, owner_id TEXT NOT NULL, source_id TEXT,
  title TEXT NOT NULL, body TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('proposed','verified','archived','deleted')),
  confidence REAL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
  valid_from TEXT, valid_until TEXT,
  FOREIGN KEY(source_id) REFERENCES sources(source_id)
);
CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts USING fts5(title, body, content='notes', content_rowid='rowid');
```

**Aviso**: FTS5 com tabela `content=` requer triggers/backfill para ficar sincronizada; adicionar triggers insert/update/delete ou usar FTS com cópia independente. Exemplo não constitui sistema multiusuário seguro. Nunca acessar SQLite do usuário por um processo LLM com SQL arbitrário.

## Política de contexto
`task_budget_tokens`, `recent_message_limit`, `allowed_namespaces`, `min_relevance`, `max_memory_age`, `allowed_sensitive_types`, `citation_required`, `fallback_when_missing`.

## Estrutura de arquivos
```
second-brain/
  data/second-brain.sqlite
  notes/<slug>.md
  media/<sha256>.<ext>
  exports/
  policies/CONTEXT_POLICY.md
  policies/RETENTION.md
```
Indexar arquivo por hash, respeitar política para dados sensíveis e cifrar volume se necessário.
