# Decisão de armazenamento e índices

| Cenário | Primário | Busca | Blobs | Vantagens | Atenção |
|---|---|---|---|---|---|
| Agente em PC offline | SQLite | FTS5 e vetor opcional | diretórios locais | zero serviço, backup simples | simultaneidade limitada; proteger arquivo |
| MVP servidor | PostgreSQL | FTS nativo | disco/S3 compatível | ACID, transações, pesquisa lexical | vetores só se necessário |
| Plataforma multiagente | PostgreSQL + pgvector | híbrido SQL/FTS/vetorial | objeto externo | multitenancy, joins, indexação | tuning índices, ACL por tenant |
| Complexidade relacional temporal | PostgreSQL + Graphiti | grafo + SQL | objeto externo | ligações e temporalidade | custo de sincronização |
| Preferências e fatos automáticos | banco + Mem0 | memória extraída | banco | extração/dedupe | avaliação de extração e privacidade |

## Regras de desenho
1. Preferir fatos com `valid_from/valid_to` + `source_id` e `confidence` interpretável (não confiar cegamente em número criado pelo LLM).
2. Guardar embedding model/version e dataset_version para reindexações reproduzíveis.
3. Idempotência de ingestão com `content_sha256` e `source_uri`, e snapshot da versão.
4. Métricas operacionais devem usar tabela/warehouse próprio, não os vetores semânticos.
5. Indexar texto real; evitar chunks grandes ou perda de links/metadados; medir retrieval em vez de apostar em tamanho fixo de chunk.
6. Nunca usar só busca vetorial para perguntar estados transacionais exatos, datas, preços ou valores; SQL tipado é fonte primária.

## Exemplo de orçamento de contexto
Para um limite hipotético de 16k tokens, reservar saída e ferramenta, e distribuir 15% políticas/objetivo, 25% tarefa/histórico recente, 35% documentos recuperados, 15% memórias, 10% margem. Esses percentuais são pontos de partida, não regras fixas; adaptar a testes e limitações do modelo.
