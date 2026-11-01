# Quality Gates incrementais e sanitização progressiva
## Regras de proteção
- Gates priorizam findings **novos** nos arquivos modificados, mantendo backlog separado para passivo histórico.
- Toda exceção tem owner, motivo, ticket, prazo de expiração e mitigação.
- Ações automáticas não reformatam todo repositório sem necessidade; alterações com milhões de linhas exigem revisão.
- Lint, typecheck e security scan não substituem testes comportamentais.
## Fluxo da PR
`diff → formatter → lint → typecheck → tests changed → SAST/SCA/secrets → integration tests relevantes → relatório → review → merge`.
## SLO de qualidade
Registrar build pass rate, flake rate, vulnerabilities opened/closed, lead time de correção, change failure rate, cobertura de mudança e technical debt (tendência). Não usar 'linhas de código' como principal proxy de produtividade.
## Fail modes
Se runner não tiver acesso a secrets do PR, projetar CI sem segredo. Se tool estiver indisponível, marcar gate como não executado — não afirmar PASS. Se teste falhar, distinguir falha introduzida de falha preexistente com reprodução.
## Checklist de revisão
- O input não confiável passa por validação antes da operação sensível?
- O código mantém autenticação e *autorização por objeto*?
- O log contém segredos/PII?
- Há dependências vulneráveis e SDKs não pinados?
- Existem testes de sucesso e de abuso?
- O diff altera interfaces públicas sem migração?
- O custo/performance piorou significativamente?
- Há rollback viável?
