# Plano de avaliação Second Brain

## Casos de ouro
- Mesmo contexto com e sem memória: comparar utilidade.
- Recuperar frase e decisão originadas em conversa antiga.
- Reconhecer mudanças de planos ao longo do tempo.
- Buscar por significado e keyword.
- Limpar conteúdo errado e verificar não reaparecimento.
- Recuperar `source_id` e referência original em todas as respostas.
- Não reutilizar dados pessoais em outro escopo.

## Métricas
`memory_precision`, `memory_recall_at_k`, `unsupported_claim_rate`, `staleness_rate`, `correction_latency`, `forget_propagation_delay`, `median_retrieval_ms`, `p95_context_tokens`, `cost_per_resolved_task`.

Não usar somente nota subjetiva do LLM para comprovar qualidade. Empregar fixtures rastreáveis e casos adversariais.
