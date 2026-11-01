# Mapeamento local, genérico, AWS, GCP e Azure

| Responsabilidade | Local/Genérico | AWS (exemplos) | GCP (exemplos) | Azure (exemplos) |
|---|---|---|---|---|
| Identidade | OIDC/Keycloak, RBAC na API | IAM Identity Center/Cognito | Cloud Identity/IAM | Microsoft Entra ID |
| Dados transacionais | SQLite / PostgreSQL | RDS/Aurora | Cloud SQL | Azure Database for PostgreSQL |
| Texto/vetores | SQLite FTS5, PostgreSQL+pgvector | OpenSearch ou pgvector em DB gerenciado | Vertex AI Search/pgvector conforme caso | Azure AI Search ou PostgreSQL+pgvector |
| Blobs | diretório criptografado / MinIO | S3 | Cloud Storage | Blob Storage |
| Filas/jobs | cron/workers/queues existentes | EventBridge/SQS/Step Functions | Cloud Tasks/Pub/Sub/Workflows | Functions/Service Bus/Logic Apps |
| Observabilidade | OpenTelemetry + Phoenix | CloudWatch + OTel | Cloud Logging/Monitoring + OTel | Azure Monitor + OTel |
| Segredos | OS keychain/Vault | Secrets Manager | Secret Manager | Key Vault |

Escolha serviços depois de confirmar disponibilidade regional, custo, limites de quota, retenção e acesso. Não confundir disponibilidade do produto com suporte a ACL documental nativo. Para sistemas existentes, **priorizar integração ao stack já implantado**. Em RAG enterprise, implementar autorização na API mesmo que a busca suporte filtros de segurança.

Fontes oficiais:
- https://github.com/pgvector/pgvector
- https://github.com/langchain-ai/langgraph
- https://learn.microsoft.com/en-us/azure/search/search-security-overview
- https://cloud.google.com/vertex-ai-search-and-conversation
- https://docs.aws.amazon.com/opensearch-service/
