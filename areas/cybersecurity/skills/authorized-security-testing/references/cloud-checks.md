# Controles autorizados por ambiente

**Local / genérico:** IAM, portas expostas, firewall configurado, logs, patches, dependências, backups, criptografia e acesso remoto. Revisar configuração antes de qualquer scan de rede.

**AWS:** IAM Access Analyzer, Security Hub, GuardDuty, CloudTrail, Config e ECR; priorizar leitura de configurações, não mudanças automáticas. APIs de consulta podem gerar custo; verificar permissões.

**GCP:** Security Command Center, Cloud Audit Logs, Cloud Asset Inventory, IAM Recommender, Artifact Analysis; jamais varrer recursos de terceiros por associação de projeto.

**Azure:** Defender for Cloud, Azure Policy, Entra permissions, Activity Logs, Resource Graph, container scanning; limitar ao subscription e scope autorizados.

Selecionar ferramentas por ambiente existente e orçamento; não criar recursos pagos ou ativar produtos sem aprovação. Validar URLs/nomes atuais junto ao fornecedor antes de executar.
