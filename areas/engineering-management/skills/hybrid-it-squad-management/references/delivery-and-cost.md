# DORA, desempenho e custo operacional com agentes
## Métricas
Entrega: deployment frequency, change lead time, change failure rate, recovery time; interpretar contexto e sistemas, não usar para punir pessoas.
Qualidade: defeitos escapados, regressões, vulnerabilidades abertas/fechadas, uptime e SLO.
Produto: conversão, ativação, retenção, engajamento saudável e suporte reduzido.
Agentes: completion rate, manual corrections, tool-call errors, policy blocks, latency p95, retries e custo por tarefa aprovada.
Pessoas: satisfação, foco, burnout, revisão, tempo perdido com ferramentas, aprendizagem; métricas qualitativas são tão importantes quanto numéricas.
## FinOps
`Custo_total = pessoal + contratação + SaaS + API/LLM + cloud + rede + GPU + storage + CI + observabilidade + incidentes + retrabalho`.
`Custo_por_entrega_aceita = Custo_total_atribuível / Entregas_validadas`.
`ROI_piloto = (benefícios_verificados - custos_totais) / custos_totais` quando benefícios comparáveis puderem ser atribuídos, sem multiplicador inventado.
## Acompanhamento
Revisão semanal: bloqueios e lead time; quinzenal: qualidade e capacidade; mensal: custo e produto; trimestral: portfólio, novas skills e maturidade.
## Fonte de dados
GitHub PR/deploy/CI + Linear issues + cloud billing + observabilidade; nunca inferir produtividade somente do número de commits, tokens ou pull requests.
