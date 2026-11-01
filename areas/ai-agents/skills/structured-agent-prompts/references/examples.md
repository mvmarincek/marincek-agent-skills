# Exemplos de ajuste e handoff

## Antipadrão
"Você é o melhor agente do mundo, use todas as ferramentas, não pare até concluir, nunca pergunte, trabalhe sozinho e otimize tudo."
Problemas: escopo ilimitado, ausência de critérios, políticas, limites e evidências.

## Versão melhor
"Você é o executor de testes para este workspace. Receba `task_id` e caminhos permitidos. Execute apenas comandos de testes aprovados, retorne status, comandos executados, logs resumidos e localização dos resultados. Não altere o ambiente sem consentimento. Timeout 90s; se falhar por dependência ausente, reporte bloqueio, não invente aprovação."

## Handoff bem definido
Orquestrador envia tarefa 'corrigir lint' com paths `src/components`, tool `shell(test-only)`, deadline e output `{changes, tests, evidence}`. Worker responde com diff/resultado. Reviewer valida o diff. Orquestrador conclui somente após confirmação de teste.

## Tarefas de prompt engineering
- Revisar um system prompt e devolver falhas e proposta revisada.
- Criar subagentes específicos sem duplicar responsabilidades.
- Elaborar política de uso de MCP, handoff e contexto de memória.
- Transformar um fluxo improvisado em procedimento versionado/testável.
