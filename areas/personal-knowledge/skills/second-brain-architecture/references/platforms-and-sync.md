# Infraestrutura para Second Brain

| Capacidade | Local | AWS | GCP | Azure |
|---|---|---|---|---|
| Dados estruturados | SQLite/ PostgreSQL | RDS/ DynamoDB conforme modelo | Cloud SQL/ Firestore conforme modelo | Azure PostgreSQL/ Cosmos DB conforme modelo |
| Arquivos/mídia | Volume local, MinIO | S3 | Cloud Storage | Blob Storage |
| Execução | Python/Rust/Node service | Lambda/Fargate | Cloud Run | Functions/Container Apps |
| Identidade | OS account/OIDC | Cognito/IAM | Identity Platform/ IAM | Entra External ID |
| Segredos | Keychain/OS vault | Secrets Manager | Secret Manager | Key Vault |
| Métricas | OpenTelemetry, arquivos estruturados | CloudWatch | Cloud Monitoring | Azure Monitor |

Não introduzir cloud se o requisito é estritamente local. Sincronização precisa versão, detecção de conflitos, proteção de chaves, timestamps confiáveis, backoff e resolução audível pelo usuário.

Ferramentas opcionais: https://github.com/mem0ai/mem0 , https://github.com/getzep/graphiti , https://github.com/pgvector/pgvector
