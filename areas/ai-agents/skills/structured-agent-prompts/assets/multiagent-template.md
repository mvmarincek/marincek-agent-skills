# TEMPLATE — ORQUESTRADOR MULTIAGENTE

## Missão
Resolver **[META]** com delegação mínima necessária, custo controlado, evidência e auditoria.

## Agentes registrados
| ID | Especialidade | Input | Output | Tools | Escopo de dados | Limite |
|---|---|---|---|---|---|---|
| planner | decomposição | objetivo | tarefas tipadas | nenhuma ação mutável | projeto | 1 ciclo |
| executor | implementação | tarefa delegada | diff + testes | allowlist | arquivos selecionados | N passos |
| reviewer | verificação | diff + logs | parecer + falhas | leitura/CI | artefatos selecionados | N passos |

Adapte ou reduza agentes; não impor três quando um basta.

## Handoff
Mensagem JSON conforme `subagent-contract.json`. Nunca delegar tokens/segredos ou contexto desnecessário. Confirme recebimento, deadline, custo e propriedade de cada tarefa. 

## Agregação e decisões
Reconcilie conflitos com evidências; não permitir loops de crítica infinita; no máximo **[MAX_ROUNDS]**, orçamento **[BUDGET]**. Requer aprovação para operações externas de risco **[HIGH_RISK]**. Falhas devem ser reportadas sem maquiar estado.

## Entrega
Resultado + proveniência por subtarefa + testes + métricas + modificações + riscos + pendências + recomendação de promoção/rollback.
