# GUARDRAILS.md — template

## Inventário de ações
| Ação (tool/comando) | Tier (R/W1/W2/W3/S) | Camadas de controle | Aprovação | Comportamento ao bloquear | Teste dispara | Teste passa |
|---|---|---|---|---|---|---|
| (ex.) git push --force | W2 | borda: padrão banado | não exposta ao agente | n/a | `tests/guard_force_push.py` | n/a |
| (ex.) terraform apply | W3 | borda + aprovação | sim, com diff | aborta com plano salvo | `tests/guard_tf_apply.py` | `tests/legit_tf_plan.py` |

## Tiers
- **R**: leitura, idempotente, sem side effect.
- **W1**: escrita reversível local (arquivo, branch própria).
- **W2**: escrita irreversível ou compartilhada (force push, delete de branch, drop).
- **W3**: produção/pagamento/terceiros/IAM/DNS.
- **S**: acesso a dados sensíveis (tokens, PII, saúde).

## Protocolo de aprovação
1. Exibir: intenção (1 frase) + diff/comando exato + raio de blast + rollback + custo.
2. Suspender execução até decisão autenticada (canal: ______).
3. Timeout: ______ (aborta com estado consistente).
4. Registrar: aprovador, timestamp, hash do diff, o que foi exibido.

## Registro de incidentes
| Data | Incidente | Controle falhou/faltou | Correção | Regressão adicionada |
|---|---|---|---|---|

## Pendências e decisão de não controlar
| Ação | Por que sem guardrail dedicado | Revisar em |
|---|---|---|
