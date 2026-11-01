# Testes controlados e evidências

| Categoria | Teste preferido | Exemplo de expectativa | Evidência segura |
|---|---|---|---|
| Authentication | testes negativos em unit/integration | acesso sem sessão → 401 | teste versionado |
| Authorization | duas contas sintéticas em tenants distintos | objeto de outro tenant → 403/404 | IDs sintéticos + status |
| Rate limit | simulação limitada no backend de testes | limite de requests → 429 | logs redigidos |
| Secrets | Gitleaks em repositório próprio | nenhum segredo novo | relatório de caminhos e hashes sem segredos |
| Dependencies | OSV ou Trivy em lockfile | advisories priorizadas | SBOM e lista filtrada |
| Headers | inspeção passiva de staging | HSTS/CSP adequados | nomes de headers sem cookies |
| MCP tool | invocação sem escopo em sandbox | servidor nega operação | trace de deny |
| Prompt injection | documento sintético tenta mudar instruções | agente ignora e mantém limites | dataset sintético e avaliação |

## Severidade e validação
Cada achado exige ID, hipótese, precondição, ambiente, testes exatos, evidência redigida, impacto provável, confiança, falso positivo investigado, correção recomendada, owner, reteste e status. Não comprovar vulnerabilidade com leitura ou extração de dados de terceiros.

## Referências
https://owasp.org/www-project-web-security-testing-guide/
https://owasp.org/www-project-api-security/
https://owasp.org/www-project-application-security-verification-standard/
