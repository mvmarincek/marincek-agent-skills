# Recovery em runtime — checkpoint/resume no produto

Quando a retomada não é entre sessões de um agente interativo, mas uma capacidade do produto (agent em produção que sofre restart, deploy, crash de worker).

## Onde persistir
- **Mínimo viável**: arquivo de estado da tarefa no workspace (`task_state.json` / `HANDOFF.md`), atualizado a cada marco. Já cobre restart de processo e handoff entre agentes.
- **Robusto**: fila/tabela de tarefas com estados (`running/checkpointed/interrupted/resuming/done/failed`), cada item de trabalho com status próprio e evidência de verificação. Ver `agent-persistent-memory` para a arquitetura de armazenamento.

## Regras de implementação
1. **Checkpoint transacional**: gravar o estado de forma atômica (write-temp + rename / transação); checkpoint pela metade é pior que nenhum.
2. **Evidência junto do status**: cada item concluído carrega a prova (hash, id do commit, output resumido) — o resumo não é confiável sem a prova anexada.
3. **Idempotência na retomada**: retomar não reexecuta efeitos já aplicados (usar idempotency keys nas ações de escrita; ver `agent-guardrails-design`).
4. **TTL e abort**: tarefa interrompida há muito tempo não retoma automaticamente; expira com relatório do estado.
5. **Retomada audita antes de executar**: o código de resume valida o estado persistido contra o real (repositório, fila, filesystem) antes de prosseguir — mesmo schema, mesma regra do protocolo interativo.
6. **Gates finais invariáveis**: a retomada termina com os mesmos gates da execução original; não existe "modo retomado com menos testes".

## Sinais de que o produto precisa disso
- Tarefas > alguns minutos ou multi-etapas com efeitos externos.
- Deploys/restarts acontecem durante tarefas (sempre acontecem).
- Mais de um agente/worker pode pegar a mesma tarefa (precisa de lease/lock + checkpoint).

## Falhas clássicas
- Estado só em memória da conversa: qualquer restart perde tudo.
- Checkpoint só no fim da tarefa: interrupção no meio = recomeço total.
- Confiar no campo `status` sem re-verificar: campo diz `done`, disco diz outra coisa.
- Retomada que reexecuta ações não idempotentes (pagamento duplicado, email reenviado).
