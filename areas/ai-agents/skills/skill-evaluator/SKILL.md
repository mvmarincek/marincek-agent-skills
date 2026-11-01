---
name: skill-evaluator
description: "Verificar Skills e comportamento de agentes com testes estruturais, gatilhos, tool calls, cenários adversariais, regressões e métricas de qualidade/custo/latência."
license: MIT
metadata:
  version: "2.0.0"
  language: "pt-BR"
  area: "ai-agents"
---

# Skill Evaluator — qualidade mensurável, não só aparência

## Ativação
Executar quando Skill é criada/atualizada, quando muda LLM/ferramenta, quando uma execução de produção falha ou quando usuário solicita benchmark comparativo.

## Duas camadas de avaliação
**Estrutural e estática (offline):** validar frontmatter, links, duplicatas, escopo, termos, políticas, scripts, direitos e conflitos. `scripts/validate.py` e `scripts/skill_quality.py` operam sem LLM e comprovam apenas integridade documental.
**Funcional (com runtime autorizado):** executar a Skill em tarefas reais, sandbox sem credenciais, comparar baseline com e sem Skill, inspecionar tool calls, outputs, segurança, custo, latência, retries, comportamento de recuperação e regressão. Nunca declarar funcionalmente validada sem essa fase.

## Pipeline de avaliação
1. Inventariar Skill e definir contrato de sucesso e veto (por exemplo, alteração indevida em produção).
2. Criar dataset versionado de cenários: positivo normal, negativo que NÃO deve ativar, ambiguidade, inputs hostis, falha de ferramenta, permissão ausente, regressão e fallback.
3. Congelar versão de Skill, modelo, ferramenta, dataset e prompt; registrar hash e ambiente.
4. Executar determinístico quando possível; isolar tarefas que modificam arquivos; utilizar fixture para cada cenário, com limpeza posterior.
5. Julgar gatilho correto, parâmetros MCP, validação de outputs, conformidade com limites, sucesso medido por teste externo e reação a falha. Evitar que o LLM avalie sozinho a própria resposta como prova definitiva.
6. Medir `pass_rate`, `tool_call_validity`, `false_trigger_rate`, `unsafe_action_rate`, `avg_latency_ms`, `p95_latency_ms`, `cost_per_success`, `context_tokens`, `retry_count`, `regression_delta`.
7. Comparar por bootstrap/intervalos quando amostra comporta, explicitando ruído; não declarar 100% com 2 testes; testes críticos têm gate sem violação.
8. Gerar relatório com evidências e classificação: `experimental` / `validated` / `production_candidate` / `blocked`; se falhou, propor correção como PR; não autopublicar.

## Ferramentas
Python pytest, schema validation e snapshot tests local; Promptfoo / DeepEval / Phoenix/OTel opcionais; harness2/DSPy sob supervisão para exploração. Cloud GCP/AWS/Azure seguem mesmas métricas e instrumentação via OpenTelemetry. Levar em conta custo API e privacidade; não enviar conversas sensíveis a serviços externos sem consentimento.

## Regras
Testes ofensivos apenas em sandbox escopado; secrets omitidos; fairness/acessibilidade quando relevante; avalie agente+Skill+ferramentas e não só texto. Evidências registradas com dados minimizados; relatório final discrimina testes executados dos apenas sugeridos.

Referências: `references/metrics-and-gates.md` e `assets/evaluation-case.json`.

## Entregáveis
`EVAL_REPORT.md`, logs sanitizados, baseline, matriz de casos, métricas, proposta de correção e evidências por etapa; explicitamente não afirmar que avaliações funcionais foram executadas quando só houve auditoria estática.
