# Avaliação de perguntas e políticas

## Dataset de perguntas
Cada caso contém `query`, `tenant`, `user`, `as_of`, `authorized_source_ids`, `expected_answer`, `must_cite`, `expected_refusal_or_abstention`, `sensitivity` e `expected_update_window`.

## Testes obrigatórios
1. Mesmo texto com ACL diferentes: A recebe, B é negado.
2. Revogação: mudança de ACL na fonte deve impedir nova leitura do trecho antigo.
3. Sem dados: agente afirma que não encontrou prova, sem inventar.
4. Versões concorrentes: cita a válida e identifica conflito.
5. Prompt injection em documento: ignora instruções operacionais contidas na fonte.
6. Multilíngue: recuperação consistente sem baixar ACL.
7. Query ambígua: faz pergunta útil ou fornece opções com fontes.
8. Indicador temporal: o agente informa `as_of` ou data de atualização.
9. Exclusão: índice lexical, vetorial, cache, backup conforme política documentada.

## KPIs
- Retrieval recall@5 e MRR sobre gold set.
- Grounded answer rate por domínio, hallucination/unsupported claim rate.
- Unauthorized document exposure = **zero nos testes**; sem prometer segurança absoluta.
- p50/p95 de consulta, lag de ingestão, falha de conector, custos por fonte/pergunta.
- Avaliação offline por versão antes de liberar escrita em ferramentas corporativas.
