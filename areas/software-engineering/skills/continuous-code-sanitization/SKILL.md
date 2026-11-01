---
name: continuous-code-sanitization
description: "Auditar e sanitizar código existente e mudanças incrementais com refatoração segura, análise estática, segredos, dependências, IaC e testes automatizados."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "software-engineering"
---

# Continuous Code Sanitization & Quality Gates


## Quando ativar
Quando houver código legado, dívida técnica, segurança, vazamento de segredos, entradas não validadas, SQL injection/XSS, qualidade de PRs, padronização, refatoração, sanitização de PII ou necessidade de evitar regressões **a cada alteração do agente**.

## Definição operacional
Sanitização aqui significa simultaneamente **higienização e proteção de código/dados** e **qualidade de engenharia**: entrada/saída segura, segredos, vulnerabilidades, dependências, padrões, manutenção e legibilidade. **Não** significa remover dados relevantes indiscriminadamente nem reescrever tudo para agradar uma ferramenta. Operações bloqueadas e testes governam a mudança.

## Contrato de entrada
Linguagem/stack, repositório/branch, cobertura e execução de testes, política de formatting/lint, dados críticos, clientes/tenants, regras de auditoria, níveis de risco, dependências, deploy pipeline, domínio de produção e permissões para correção. Mapear file ownership e código gerado (não reformate gerados sem validação).

## Pipeline obrigatório
1. **Inventário e baseline**: tipo de projeto, lockfiles, CI, branch limpa, testes, lint, build, cobertura, dependências e exceções. Abrir worktree/branch, não modificar main diretamente.
2. **Threat model + regras**: entradas não confiáveis, APIs, autenticação, autorização, objetos, logs, arquivos, credenciais e terceiros. Priorizar CWE/OWASP conforme stack, não apenas style.
3. **Análise passiva**: executar lint/formatter/checkers, SAST, secret scanning, dependency advisories, SBOM, IaC scanning e license compliance conforme adequação. Ver `references/tooling-matrix.md`.
4. **Triagem**: classificar cada achado como confirmado, potencial ou falso positivo; severidade x exposição x explorabilidade x impacto; evidência e arquivo/linha; não afirmar exploit sem prova autorizada.
5. **Sanitização de dados**: input validation por schema, canonicalização cuidadosa, encoders contextualizados, escaping onde exigido, queries parametrizadas, limites de tamanho, upload seguro, PII redaction em logs, verificações de SSRF/path traversal e deserialização. Não confiar somente em regex.
6. **Refatoração mínima**: resolver vulnerabilidade e causa raiz sem remover funcionalidade; manter assinatura pública/contrato, feature flag, migrations e compatibilidade; mudanças pequenas e compreensíveis.
7. **Segurança preventiva**: hooks/CI com PR-only scans, thresholds de severidade, testes, coverage/diff, branch protection e revisão; preferir incremental/changed-files para feedback rápido mais full scans periódicos.
8. **Validação**: comparar baseline e depois; testes unit/integration/E2E, snapshot, security regression, lint e build, scans sem findings novos e performance; registrar exceções justificadas e riscos aceitos.
9. **Release**: PR com diff, achados e evidência, mitigação, plano de rollback; aprovação explícita antes de deploy em produção.
10. **Monitoração contínua**: monitorar advisories de dependências, issues de security scanning, regressões, tendência e MTTR; rastrear dívida por ownership.

## Modo 1: limpar código existente
- Baseline de scanners não deve bloquear a adoção; separar dívida histórica do que é novo (ratchet).
- Priorizar secrets expostos, execução remota não controlada, privilégio indevido, acesso a dados entre tenants, SQLi e RCE; impacto operacional primeiro.
- Agrupar correções por domínio/módulo com teste existente, sem big-bang rewrite.

## Modo 2: sanitização contínua enquanto o agente desenvolve
Em **cada ciclo** de mudança: especificação→código→formatter/lint/typecheck→teste→scan incremental→verificação de secrets→diff→commit. Se falhar, corrigir antes da próxima funcionalidade. Preservar performance, acessibilidade, interfaces públicas e relatórios.

## Tipos de ferramentas
- JS/TS: ESLint, TypeScript strict, Prettier/Biome, npm audit/pnpm audit, Zod ou schema equivalente para input.
- Python: Ruff, mypy/pyright, Bandit, pytest, pip-audit e esquemas Pydantic quando aplicável.
- Java: Checkstyle/SpotBugs, tests, SCA; C#/.NET: analyzers, dotnet format/test, NuGet advisories; Go: gofmt, staticcheck, govulncheck, tests.
- Multi-stack: Semgrep, CodeQL conforme licença, Gitleaks, Trivy, OSV-Scanner, OpenSSF Scorecard; `references/tooling-matrix.md`.
- IaC: Checkov/tfsec/Trivy, `terraform fmt/validate`, `actionlint`, Dockerfile/Helm scan.
Nunca assumir que a ferramenta está instalada ou é gratuita para qualquer tipo de repositório/licença.

## Implantação
Local: pre-commit hooks opcionais com tempo controlado. GitHub: Actions em PR + scans agendados; preferir versionamento/pin SHA. AWS/GCP/Azure: IAM/secret managers e security scanning próprios como camada complementar, preservando pipeline portátil.

## Segurança e permissões
Não enviar o código completo para scans SaaS sem autorização. Não mover segredos para prompts/logs. Redigir os segredos detectados; se um segredo foi commitado, iniciar revogação/rotação com aprovação apropriada e investigar histórico. Análise de vulnerabilidade apenas nos sistemas autorizados; sem exploit contra terceiros.

## Referências e artefatos
- `references/sanitization-by-language.md` — controles e práticas por stack.
- `references/tooling-matrix.md` — ferramentas e integração CI.
- `references/continuous-gates.md` — fluxo incremental, baseline e regressão.
- `assets/security-quality-review.md` — saída de PR.
- `assets/gate-policy.json` — exemplo de limiares, *não é executor*.

## Critério de aceite
Sem segredo novo, sem regressão de teste/contrato, sem alertas novos críticos sem justificativa, lint/typecheck/teste aceitos conforme projeto, PR com alterações auditáveis, dívida anterior diferenciada, aprovação para risco residual e nenhuma alteração de produção não autorizada.
