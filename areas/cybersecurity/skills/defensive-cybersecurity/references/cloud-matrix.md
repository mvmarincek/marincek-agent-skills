# Matriz de implantação e mitigação — local, genérico, AWS, GCP, Azure

| Objetivo | Local/genérico | AWS | GCP | Azure |
| --- | --- | --- | --- | --- |
| Identidade workload | service accounts/least-privilege | IAM roles / STS | IAM service accounts / Workload Identity | Managed Identity / Entra ID |
| Segredos | Vault ou cofre SO | Secrets Manager / KMS | Secret Manager / Cloud KMS | Key Vault |
| Proteção perímetro | reverse proxy/WAF | AWS WAF | Cloud Armor | Azure WAF |
| Detecção | SIEM/logs/EDR | GuardDuty / Security Hub | Security Command Center | Defender for Cloud |
| Auditoria | OpenTelemetry/log central | CloudTrail / CloudWatch | Cloud Audit Logs / Logging | Activity Logs / Monitor |
| Vulnerabilidades de imagem | Trivy/Grype | ECR scanning | Artifact Analysis | Defender for Containers |
| Políticas infra | OPA/Conftest | Organizations / SCP / Config | Org Policies | Azure Policy |

Avaliar custos, região, acesso, IAM e impacto antes de ativar. Os nomes e limites dos serviços devem ser verificados nas docs atuais no momento da implementação.
