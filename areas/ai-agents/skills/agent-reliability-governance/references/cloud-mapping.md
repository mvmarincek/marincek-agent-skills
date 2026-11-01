# Mapeamento de infraestrutura para confiabilidade

| Capacidade | Local / neutro | AWS | GCP | Azure |
|---|---|---|---|---|
| Traces | OTel Collector + Phoenix/Langfuse | CloudWatch + Bedrock AgentCore Observability / OTel | Cloud Logging/Trace + Agent Platform/Vertex tracing | Azure Monitor + Application Insights + Foundry tracing |
| IAM/policies | OPA + gateway próprio | IAM + STS + IAM roles + Verified Permissions, se pertinente | IAM + Workload Identity + políticas no gateway | Microsoft Entra ID + RBAC + Managed Identity |
| Segredos | OS keychain / Vault | Secrets Manager / KMS | Secret Manager / Cloud KMS | Key Vault |
| Aprovação | workflow + registros assinados | Step Functions / filas / workflow próprio | Workflows / Pub/Sub / workflow próprio | Logic Apps / Durable Functions / workflow próprio |
| Testes | pytest + DeepEval/Promptfoo | Bedrock evaluations e CI/CD | Vertex/Agent Platform evaluation e CI/CD | Microsoft Foundry evaluation e CI/CD |
| Métricas | Prometheus + Grafana | CloudWatch | Cloud Monitoring | Azure Monitor |
| Auditoria | logs append-only + hashes | CloudTrail + CloudWatch | Cloud Audit Logs | Azure Activity Logs + Monitor |

## Pontos de atenção
- Serviços gerenciados variam por região, conta, modalidade e custos. **Verifique documentação oficial antes de provisionar**.
- No AWS, não confundir Bedrock Agents Classic com AgentCore; produtos/limites mudam.
- Na GCP, nomenclatura de Vertex AI Agent Engine/Agent Platform muda com releases; confirme APIs.
- Na Azure, confirmar distinção Foundry/Foundry classic e APIs correspondentes.
- Para zero cloud, selecione primeiro as opções locais. Nunca abrir endpoints de telemetria para Internet sem autenticação e TLS.

## Fontes
https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html
https://cloud.google.com/products/agent-builder
https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-data
