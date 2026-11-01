# Memória e conhecimento: local, AWS, GCP, Azure

| Camada | Local / vendor-neutral | AWS | GCP | Azure |
|---|---|---|---|---|
| SQL principal | SQLite, PostgreSQL | RDS/Aurora PostgreSQL | Cloud SQL/AlloyDB PostgreSQL | Azure Database for PostgreSQL |
| Busca vetorial | pgvector, vetor local | Aurora/RDS pgvector, OpenSearch, Bedrock Knowledge Bases | AlloyDB pgvector, Vertex AI Vector Search/RAG Engine conforme disponibilidade | Azure AI Search, PostgreSQL + pgvector |
| Armazenamento blobs | disco criptografado, MinIO compatível S3 | S3 | Cloud Storage | Blob Storage |
| Embeddings/LLM | Ollama/embeddings locais | Bedrock models | Vertex AI models | Foundry models |
| Memória gerenciada de agente | SQL + middleware, Mem0 | Bedrock AgentCore Memory (se adequado) | Agent Engine/Memory Bank (verificar disponibilidade) | Foundry Agent Service state/storage ou app próprio (verificar capacidades) |
| Segredos / identidades | OS Vault/OPA | Secrets Manager/IAM | Secret Manager/IAM | Key Vault/Entra |
| Telemetria | OTel/Phoenix | CloudWatch | Cloud Logging/Monitoring | Application Insights/Monitor |

## Observações
- Nomes comerciais, suporte a região, APIs e preços mudam. Não inferir equivalência funcional só pelo nome.
- Exportabilidade: versionar schema SQL, documentar extração de docs/vetores, evitar formatos proprietários como única cópia.
- Para privacidade/LGPD, classificar finalidade, base legal, retenção, acesso por tenant, portabilidade e exclusão de derivados.
- Nunca ativar embedding remoto em conversas privadas sem autorização explícita.

## Fontes para checagem antes do uso
https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html
https://cloud.google.com/sql/docs/postgres
https://learn.microsoft.com/en-us/azure/postgresql/
https://github.com/pgvector/pgvector
https://github.com/mem0ai/mem0
https://github.com/getzep/graphiti
