# Execução e nuvem — Code Intelligence

| Elemento | Local/genérico | AWS | GCP | Azure |
|---|---|---|---|---|
| Worker | processo local/Docker | ECS/Fargate/Batch | Cloud Run jobs | Container Apps Jobs |
| Metadados | SQLite/PostgreSQL | RDS | Cloud SQL | Azure PostgreSQL |
| Artifacts | filesystem/MinIO | S3 | Cloud Storage | Blob Storage |
| Observabilidade | OTel | CloudWatch | Cloud Monitoring | Azure Monitor |
| Scheduler/CI | GitHub Actions/cron | EventBridge | Cloud Scheduler | Azure Logic Apps/Functions |
| Identity | Git account/OIDC | IAM | IAM | Entra ID |

Isolar jobs que analisam PRs externos. Não permitir que CI de fork tenha segredos de produção; reduzir permissões do `GITHUB_TOKEN`. Para índices vetoriais, configurar controle de repo/tenant/branch antes da busca. Evitar vector DB exclusivo se a busca lexical é suficiente.
