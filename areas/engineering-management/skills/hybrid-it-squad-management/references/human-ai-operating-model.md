# Operating Model de times humano–IA
## Princípios
1. Agente possui **owner humano**, versão, finalidade e orçamento.
2. Matriz de autonomia: `READ_ONLY`, `DRAFT`, `SANDBOX_WRITE`, `STAGING_CHANGE`, `PROD_CHANGE_WITH_APPROVAL`.
3. Tool gateway aplica permissões independentemente do prompt/Skill.
4. Rastrear entrada, modelo, ferramentas, resultado, aprovação, reviewer e rollback sem salvar PII indiscriminadamente.
5. Skill/model updates têm avaliação/regressão e PR; agentes não autopromovem sua própria capacidade em produção.
## Modelo de implantação
- 0: tarefas assistivas sem edição.
- 1: agente cria rascunhos e tests local.
- 2: agente executa em sandbox.
- 3: integração com PR / revisão humana.
- 4: ações sensíveis com aprovação e policy enforcement.
- 5: autonomia delimitada em fluxos de baixo risco com métricas e rollback.
Não associar número maior a maturidade sempre desejável; riscos ditam limite.
## Incident response
Monitorar anomalias, acesso indevido, prompts maliciosos, custo explosivo e regressões; pausa/killswitch operacional; revogar tokens, congelar releases e preservar evidências.
## Adoção
Treinar pessoas em avaliação de saídas, segurança de dados, qualidade do código e domínio; medir sobrecarga de revisão. Evitar métricas comparando indivíduos por 'uso de IA'.
