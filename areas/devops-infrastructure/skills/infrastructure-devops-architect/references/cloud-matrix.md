# Matriz de decisão cloud / local

| Função | Local / genérico | AWS | GCP | Azure |
|---|---|---|---|---|
| Identidade | AD/Keycloak/OIDC | IAM / IAM Identity Center | Cloud IAM / Workload Identity | Entra ID / Managed Identity |
| IaC | Terraform/OpenTofu | Terraform AWS provider | Terraform Google provider | Terraform azurerm provider |
| Rede | firewall/VPN/reverse proxy | VPC / SG / ALB | VPC / Firewall / LB | VNet / NSG / Application Gateway |
| Containers simples | Docker Compose/Swarm | ECS Fargate / App Runner | Cloud Run | Container Apps |
| Kubernetes | k3s/Kubernetes | EKS | GKE | AKS |
| VM | Linux/Windows | EC2 | Compute Engine | Azure VM |
| Serverless | FaaS/self-host | Lambda | Cloud Run functions | Azure Functions |
| Banco SQL | PostgreSQL local | RDS / Aurora | Cloud SQL / AlloyDB | Azure Database for PostgreSQL |
| Objetos | MinIO/S3 compat. | S3 | Cloud Storage | Blob Storage |
| Secrets | Vault / encrypted store | Secrets Manager / SSM | Secret Manager | Key Vault |
| Logs/traces | OpenTelemetry + Grafana | CloudWatch / X-Ray | Cloud Logging/Monitoring/Trace | Azure Monitor / App Insights |
| CI/CD | GitHub Actions | OIDC IAM role | WIF + service account | Entra federation |

## Checklist antes de recomendar um produto
Custo fixo e por tráfego; cotas; região; soberania de dados; cold start; HA; operação 24/7; custos invisíveis de NAT/egress/LB/managed DB/Kubernetes; monitoramento; facilidade de rollback. Estimar 3 cenários: baixo/base/pico, documentar premissas, marcar custos como estimativa e consultar calculadora oficial.

Links: https://calculator.aws/ ; https://cloud.google.com/products/calculator ; https://azure.microsoft.com/pricing/calculator/
