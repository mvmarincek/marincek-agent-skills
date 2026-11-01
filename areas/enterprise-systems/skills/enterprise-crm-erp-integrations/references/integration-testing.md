# Integração corporativa: contratos, segurança, validação e resiliência
## Blueprint de integração
`Sistema origem → adaptador autorizado → validação de schema → fila/retry/idempotência → adaptador destino → reconciliação → trilha de auditoria`.
## Exigências técnicas
- Contrato versionado; não quebrar versões anteriores sem migração; mapping com origem, destino, tipo, nulabilidade, escala decimal, timezone, owner e propósito.
- Autenticação por máquina e scopes mínimos, mTLS quando necessário; rotação de segredos; mascarar PII e prevenir vazamento por logs.
- Eventos: ao menos uma entrega é comum; idempotência; deduplicação; reprocessamento e DLQ.
- Retry: distinguir rede, 429 e 5xx transitórios de 4xx funcionais; jitter, timeouts e circuit breakers; jamais retry cego em movimentações críticas.
- Auditoria: `correlation_id`, `business_id` com masking, `attempt`, `status`, `duration_ms`, `source_system`, `target_system`, `schema_version`.
## Testes de aceite
- Unidade: mapeamento, normalização, moeda, decimais, timezone, nulos e chaves.
- Contratos: versão, aceitação e incompatibilidade intencional.
- Autorização: tenant/filial errado, objetos sem permissão, scopes mínimos.
- Resiliência: timeout antes/depois do commit, API indisponível, replay de webhook/evento, DLQ, fila atrasada, duplicidade.
- Reconciliação: contagem, total por moeda, documentos correlacionados, hashes de payload higienizado e divergências.
- Prod: plano de migração reversível, fluxo de aprovação e monitoramento de 24–72 h, conforme risco.
## Operação
Dashboard: taxa de erro, tempo, volume, atraso, divergência, retry, DLQ, custo por transação; alertar por SLO. Evidência de teste NÃO pode conter dados pessoais ou credenciais.
