---
name: hybrid-it-squad-management
description: "Planejar e gerir engenharia, TI, squads híbridos humanos/agentes IA, alocação de pessoas, portfólio, FinOps, DORA, governança, entregas e evolução organizacional."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "engineering-management"
---

# IT Leadership & Human-AI Squad Operating System


## Quando ativar
Planejamento de área de TI/engenharia, operação de software factory, squads de produto, liderança técnica, portfolio management, orçamento/FinOps, desenho organizacional, human-in-the-loop, adoção de IA no SDLC, maturidade de plataforma, governança, recrutamento, capacidades, qualidade e métricas.

## Princípio de liderança
O objetivo não é substituir pessoas por automações indiscriminadamente: estruturar sistemas em que humanos continuam donos de decisões, riscos, produto e responsabilidade, enquanto agentes recebem competências delimitadas, avaliação e permissão mínima. **Agentes não são equivalentes legais de funcionários**; ownership, accountability, compliance e segurança ficam com responsáveis humanos.

## Diagnóstico inicial
Visão e estratégia, produtos, clientes e metas, tamanho e senioridade do time, contratos, fornecedores, stack, dados de incidentes/CI, backlog, riscos, custo operacional, maturidade de documentação, volume de features, compliance, carga de suporte e grau de autonomia permitido aos agentes. Entender capacidade e sazonalidade antes de propor headcount.

## Processo operacional
1. **Mapear o fluxo de valor**: da descoberta ao deploy e manutenção; medir espera, filas, retrabalho, dependências, incidentes e desperdício.
2. **Segmentar carteira**: Run (operação), Grow (features), Transform (inovação), Risk (segurança/compliance). Cada iniciativa tem patrocinador, outcome, orçamento, owner, deadline e hipótese.
3. **Projetar squads**: team topology (stream-aligned, platform, enabling, complicated-subsystem) quando pertinente; escolher pods pequenos e contratos de serviço claros, sem imitar cerimônias por obrigação.
4. **Alocar agentes por papel**: triagem de issues, QA, code review, documentação, pesquisa, coding assistido, SRE monitor, FinOps analyst; limitar ferramentas e dados; atividades críticas exigem gate humano.
5. **Definir RACI/DACI**: owner humano para produção, orçamento e incidentes; agents como executores assistidos com evidências e possibilidade de rollback. Não criar cargo humano fictício para agentes.
6. **Planejar capacidade**: horas humanas disponíveis por skill/nível, throughput observado dos agentes, taxa de falha/rework, lead time e custos; não contabilizar token como produtividade.
7. **Definir delivery system**: discovery→PRD→task→desenvolvimento→CI→review→deploy→telemetria→aprendizado. Integrar GitHub/Linear quando acessos existirem; não publicar/editar sem autorização.
8. **Gestão financeira**: headcount e burden, SaaS/licenses, cloud, storage, redes, CI minutes, observabilidade, API tokens, GPU, suporte; calcular cost per outcome, ambiente e owner; orçamento e chargeback/showback.
9. **Governança do uso de IA**: agentes registrados com finalidade, versão/LLM, owner humano, tools/MCP, dados autorizados, auditoria, avaliação, incident response e política de retenção. Ver `references/human-ai-operating-model.md`.
10. **Rituais eficientes**: planejamento semanal, revisão quinzenal de métricas, monthly business review, postmortems sem culpabilização, trimestral de estratégia e skills. Evitar excesso de cerimônia.
11. **Monitorar resultados**: valor para usuário, DORA (lead time de mudanças, frequência deploy, falha de mudança, recuperação), qualidade e segurança, satisfação da equipe, incidentes, custo, acessibilidade e satisfação do cliente.
12. **Melhoria contínua**: identificar gargalo comprovado, testar solução em piloto, avaliar contra baseline, registrar evidência e decidir escala/reversão.

## Diferença de gestão tradicional
Agentes ampliam throughput potencial mas criam novos riscos: dependência de provedor, revisão e testes, custo de correções, contexto, hallucination, exfiltração, pipeline de avaliações e impossibilidade de atribuir responsabilidade a um 'agente'. Medir sucesso pelo efeito **líquido** em qualidade e valor do produto; adoção de IA como objetivo isolado não é outcome.

## Catálogo de times híbridos
- **Product squad**: PM, designer, lead dev, QA, agentes de documentação/testes/coding; humanos validam user research e prioridade.
- **Platform/SRE**: platform engineer/SRE + agente de CI, IaC e observabilidade; deployments de produção aprovados.
- **Data/ML squad**: data engineering, ML engineer e analytics + agentes para datasets/EDA/evals; privacidade e validação humana.
- **Security squad**: AppSec e compliance + agentes SAST/triagem; pentest apenas autorizado.
- **IT Operations**: suporte, infraestrutura, identity admin + agentes de triagem e runbooks; escalonamento e controle de acesso.
- **Enterprise integration**: especialistas de domínio SAP/TOTVS/Salesforce + agentes para mapeamento/contratos, sem auto-posting financeiro.

## Ferramentas e cloud
Local: GitHub Projects/Linear, métricas por CI, OpenTelemetry, Postgres/SQLite, MLflow/Langfuse quando IA, relatórios de custo. Cloud: AWS Cost Explorer/Budgets, GCP Billing/Cost Management, Azure Cost Management, CloudWatch/Cloud Monitoring/Azure Monitor. Dados financeiros não devem ser copiados para serviços externos sem autorização.

## Referências
- `references/org-topologies.md` — tipos de equipe, ownership e squads.
- `references/delivery-and-cost.md` — DORA/SPACE, KPIs e FinOps.
- `references/human-ai-operating-model.md` — responsabilidades, risco, autonomia e treinamento.
- `references/portfolio-roadmap.md` — portfólio, governança e planejamento.
- `assets/squad-charter.md` — contrato e objetivos da equipe.
- `assets/agent-role-card.md` — governança por agente.

## Entregáveis
`IT_ASSESSMENT.md`, `ORGANIZATION_TOPOLOGY.md`, `SQUAD_CHARTERS.md`, `AGENT_WORKFORCE_REGISTRY.md`, `DELIVERY_SCORECARD.md`, `COST_ALLOCATION.md`, `RISK_REGISTER.md`, `90_DAY_ROADMAP.md` e rituais executivos proporcionais ao contexto.

## Critérios de aceite
Cada produto/squad tem owner; métricas com fontes e baseline; agentes inventariados e com permissões proporcionais; orçamento e forecast auditáveis; feedback humano e segurança incluídos; mudança de estrutura aprovada; ausência de promessas de produtividade não medidas; plano 30/60/90 executável.
