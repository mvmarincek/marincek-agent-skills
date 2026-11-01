# Adaptação de prompts aos runtimes

| Contexto | Agente simples | Multiagente / workflow | Segurança e memória |
|---|---|---|---|
| Local | OpenCode/Codex/Claude CLI/agent próprio | orquestrador de aplicação, tarefas tipadas, checkpoints | SQLite, allowlist do runtime, Skills locais |
| Genérico | FastAPI/Node agent service, MCP | LangGraph ou engine própria com filas | PostgreSQL, OTel, RBAC/OPA |
| AWS | Bedrock/AgentCore conforme necessidade | Step Functions/AgentCore, fila | IAM, Secrets Manager, AgentCore Memory/CloudWatch |
| GCP | Vertex AI/Agent Platform conforme necessidade | Cloud Run/Workflows/PubSub | IAM/Secret Manager, Cloud SQL, Cloud Logging |
| Azure | Microsoft Foundry/Functions | Durable Functions/Agent Service | Entra, Key Vault, PostgreSQL, App Insights |

**Importante:** integrações dependem de disponibilidade e versões. Não pressupor que engines compartilhem o mesmo schema de tool calls; exigir testes por provedor. Prompts e contratos devem ser independentes de clouds quando possível.
