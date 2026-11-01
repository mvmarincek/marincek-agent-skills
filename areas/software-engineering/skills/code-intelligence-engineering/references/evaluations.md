# Benchmark Code Intelligence

## Gold set proposto
```json
{
 "repo":"org/repo", "commit":"sha", "query":"Onde função X é definida?",
 "expected_locations":[{"path":"src/module.py","line":18}],
 "expected_related_tests":["tests/test_module.py"],
 "allowed_repos":["org/repo"],
 "max_latency_ms":1000
}
```

## Tipos de prova
- 15 consultas de localização, 10 de referência cruzada, 5 de análise de impacto, 5 perguntas sem evidências e 5 casos de isolamento/segurança.
- Comparar lexical baseline, AST/LSP, híbrido sem vetor e híbrido com vetor.
- Medir top-1/top-5 localização, MRR, recall de relações, freshness, percentual de linhas válidas, tempo de atualização, tokens, p95 e custo por investigação concluída.
- Ao mudar branch/commit, cada citação precisa apontar para a versão correta.

## Tratamento de resultados
Resultados estáticos não provam funcionamento runtime. Rodar compilação, testes e análise de integração antes de afirmar que uma mudança é segura.
