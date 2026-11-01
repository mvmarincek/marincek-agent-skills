---
name: enterprise-crm-erp-integrations
description: "Implementar, customizar, integrar e testar sistemas Salesforce, SAP e TOTVS com APIs oficiais, fluxos empresariais, governança e release seguro."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "enterprise-systems"
---

# Enterprise CRM & ERP: Salesforce, SAP e TOTVS


## Quando ativar
Ativar quando o projeto envolver CRM/ERP corporativo, integração entre vendas/finanças/estoque/faturamento/serviços, customização, migração, APIs, dados mestres, workflows, conformidade ou troubleshooting de Salesforce, SAP e TOTVS. Não prometer domínio de uma instalação proprietária sem descobrir versão, módulos licenciados e autorização.

## Princípio operacional
Esta Skill **orienta o agente**, não concede acesso por si só. Descobrir cliente MCP, credenciais delegadas, sandbox, SDK/CLI e permissões existentes; manter operações reais condicionadas a autorização. Não usar scraping de telas para contornar controles de API e jamais executar movimentos fiscais ou financeiros irreversíveis sem revisão humana.

## Contrato de entrada
Mapear fabricante, produto/edição/versão, país/localização, módulos ativos, arquitetura on-prem/cloud/híbrida, ambiente (sandbox/homologação/prod), endpoints publicados, tenant/company/filial, RBAC/perfis, limites de API, SLAs, fluxos dependentes, ERPs legados, volume de dados, integração síncrona/assíncrona, LGPD, finalidade e resultado verificável. Identificar quem aprova acesso, mudança cadastral e operações contábeis. Não inferir funcionalidades ausentes.

## Procedimento de engenharia
1. **Discovery**: examinar código, contratos de integração, esquemas, modelo de identidade, configuração de tenants, integrações existentes, logs e regras de negócio. Descrever arquitetura atual e limitações de licença.
2. **Modelagem de processo**: desenhar evento de negócio, estados válidos, donos do dado, códigos externos, cardinalidade, dependências, SLO, regras tributárias e validações; separar fluxo fonte da verdade de sincronização derivada.
3. **Selecionar superfície oficial**: escolher REST/OData/SOAP/BAPI/SDK/CLI/eventos conforme produto e versão; conferir documentação e habilitação no tenant antes de codificar. Ver guias `references/salesforce.md`, `references/sap.md` e `references/totvs.md`.
4. **Segurança**: identidades técnicas com menor privilégio, segredos em vault, OAuth/identidade gerenciada quando disponível, segregação por tenant/filial, políticas de acesso e mascaramento. Negar escrita por padrão.
5. **Desenhar integração**: contratos OpenAPI/JSON Schema/AsyncAPI quando aplicável; tabela de mapeamento origem→destino, regras de transformação, nulls, timezone, currency, precisão decimal, IDs compostos e external IDs. Documentar paginação, rate limit, backoff e janelas de manutenção.
6. **Implementar**: adaptadores independentes de domínio; chamadas idempotentes; retries apenas em falhas transitórias; circuit breaker; fila + DLQ em fluxos assíncronos; CDC/eventos quando suportado; reconciliação e trilha de auditoria. Nunca repetir uma operação financeira sem chave de idempotência e verificação de estado.
7. **Testes**: mocks/contratos, testes de serialização, permissões negativas, duplicate delivery, ausência de rede, timeouts, timeout após commit, divergência de moeda/data, corrida de eventos, rollback e impacto de versões; integração E2E somente sandbox aprovado.
8. **Governança e release**: migration plan e backups, changelog, approvers, feature flags, monitoramento por fluxo, dashboards de falhas/reprocessamento e rollback. Verificar compliance aplicável (dados pessoais, contábeis, fiscais) com especialista responsável.
9. **Validação**: reconciliar contagens e somatórios por chave de negócio, não somente HTTP 200; verificar registros de ambos lados e ausência de duplicação; guardar evidências redigidas sem PII.
10. **Entrega**: ADR, mapa do processo, especificação de interface, matriz de dados, matriz de acesso, plano de testes, plano de implantação/rollback e runbook.

## Playbooks progressivos
- `references/salesforce.md`: objetos, SOQL, Flow, Apex, LWC, integração, Bulk API, packaging e limites.
- `references/sap.md`: S/4HANA, SAP BTP, OData, APIs liberadas, integrações, extensões e transportes.
- `references/totvs.md`: Protheus AdvPL/TLPP, Datasul, RM e Fluig; APIs, ambientes, filial e transações.
- `references/integration-testing.md`: contratos, observabilidade, segurança e testes de reconciliação.
- `assets/interface-contract.md`: modelo de contrato de integração.

## Matriz de implantação
- **Local/on-prem**: agentes dentro da rede autorizada, VPN/zero trust, credenciais de serviço, filas gerenciadas pelo cliente e logs locais.
- **AWS**: Lambda/ECS/Step Functions/EventBridge/SQS, Secrets Manager e observabilidade; validar custo e privilégio.
- **GCP**: Cloud Run/Workflows/Pub/Sub/Secret Manager/Cloud Logging, com localização de dados definida.
- **Azure**: Functions/Logic Apps/Service Bus/Key Vault/Monitor; Managed Identity quando disponível.
A Skill não deve obrigar cloud nem instalar conectores de fornecedor sem necessidade.

## Governança e segurança
Não extrair dumps de clientes, dados de saúde, fiscal ou financeiro para prompts externos. Nunca criar pedidos, notas, pagamentos, débitos, alterar estoque ou conceder permissões em produção sem autorização explícita. Executar migrações em lotes controlados com plano de reversão. Confirmar limitações dos módulos e licenças e não burlar autenticação por RPA. Aplicar segregação de deveres e retenção de logs.

## Produtos entregáveis
`ERP_CRM_DISCOVERY.md`, `PROCESS_MAP.md`, `INTEGRATION_CONTRACT.md`, `DATA_MAPPING.md`, `SECURITY_MATRIX.md`, `TEST_PLAN.md`, `RECONCILIATION_REPORT.md`, `ROLLOUT_AND_ROLLBACK.md` — gerar somente os pertinentes e registrar o que não pôde ser verificado.

## Critérios de aceite
Contrato validado; todos os fluxos mapeados a owners; testes de duplicação/idempotência e falhas passam; credenciais não vazam; integrações com dados fictícios executadas em sandbox; reconciliação fecha; permissão e custo explicitados; mudança de produção somente com aprovação; provas e logs disponíveis.
