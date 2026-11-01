# Matriz de ferramentas de qualidade e segurança
| Uso | Opções | Verificar antes de habilitar |
|---|---|---|
| Formatter/Lint | ESLint/Biome, Ruff, golangci-lint, dotnet format | Linguagem e regras atuais |
| Static typing | TypeScript, mypy/pyright, Java/Kotlin, Go | Tolerância a legado e erros |
| SAST | Semgrep, CodeQL, Bandit, SpotBugs | Licença, cobertura, false positives |
| Secrets | Gitleaks, TruffleHog | Redação de logs e história Git |
| SCA | OSV-Scanner, osv.dev, npm/pip audit | Lockfile e versionamento |
| Container/IaC | Trivy, Checkov, tfsec, actionlint | Versão do IaC, falso positivo |
| Supply chain | Syft/SBOM, Cosign, OpenSSF Scorecard | Origem de artefatos e acesso |
| Dynamic authorized | ZAP baseline em ambiente controlado | Escopo/approval, disponibilidade |
## Sequência recomendada
1. Local rápido: formatter, lint, typecheck e testes da área alterada.
2. PR: SAST, secret scan, SCA, diff coverage, IaC.
3. Noturno/semanal: varreduras integrais, SBOM, dependências, scorecard.
4. Pré-deploy: release artifact, assinatura, permissões, rollback.
## Cuidado com GitHub CodeQL
A disponibilidade do GitHub Code Security depende do tipo de repositório e plano; consultar documentação atual. Evitar afirmar acesso irrestrito gratuito em repositório privado.
## Fontes
- https://scorecard.dev/
- https://docs.github.com/en/code-security
- https://github.com/trufflesuite/trufflehog
- https://github.com/gitleaks/gitleaks
- https://github.com/semgrep/semgrep
- https://github.com/aquasecurity/trivy
