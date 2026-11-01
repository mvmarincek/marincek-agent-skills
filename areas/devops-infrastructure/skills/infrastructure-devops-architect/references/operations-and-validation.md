# Plano mínimo SRE, governança e validação

## SLOs e disponibilidade
Definir SLI por classe de serviço: requests com sucesso, latência p95/p99, tempo de job, freshness dos dados, disponibilidade, custo por transação. Definir janelas e origem da medição. Alertas por sintomas e risco real, evitando ruído.

## Backup e recuperação
Retenção, criptografia, controle de acesso, RPO/RTO, teste periódico de restauração num ambiente separado. Backup que nunca foi restaurado não é prova de recuperabilidade. Cobrir DB, storage, secrets críticos, IaC state, configuração e metadados.

## Segurança
IAM least privilege, OIDC, policies, WAF quando exposto, logs imutáveis quando apropriado, rotação e scanning de segredos, análise de supply chain, imagens não-root, registry verificado, segregação por ambiente, gestão de certificados. Nunca incluir segredos nos traces.

## FinOps
Dimensionar CPU/RAM/GPU, autoscaling, instâncias ociosas, retenção de logs, storage lifecycle, tráfego entre zonas, egress internet, IP, NAT, LB, quotas, alertas de orçamento. Relatar custo por usuário/tarefa e variação mensal.

## Matriz de validação
| Etapa | Validação | Critério |
|---|---|---|
| PR | testes, SAST, lint, IaC check | checks passing |
| Planejamento | ADR + diagrama + estimativa de custo | aprovação da proposta |
| Terraform | fmt / validate / plan | sem alterações não autorizadas |
| Container | build, SBOM, vuln scan, health | dentro dos limites acordados |
| Staging | smoke, E2E, observabilidade | aceite do produto |
| Produção | rollout aprovado, monitoramento | SLO sem regressão |
| Resiliência | backup restore / rollback | RTO/RPO demonstrado |

Parâmetros de entrada nunca bastam para atestar resultado: coletar logs e artefatos verificáveis, mas mascarar dados sensíveis.
