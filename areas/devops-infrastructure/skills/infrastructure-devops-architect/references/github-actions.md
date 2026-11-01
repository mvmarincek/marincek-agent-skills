# GitHub Actions — projeto a ambiente implantado

## Workflow básico
1. Proteger branch principal com PR obrigatório, checks, reviews e CODEOWNERS se houver equipe.
2. Criar workflows independentes: `ci.yml` (PR), `security.yml` (PR ou schedule) e `deploy.yml` (workflow_dispatch/manual/merge autorizado).
3. Definir `permissions: contents: read` global; elevar pontualmente (ex.: `id-token: write` no job OIDC) somente para o job de deploy.
4. Definir `concurrency` por ambiente, `timeout-minutes`, `environment`, caches com chaves de lockfile e dependências pinadas.
5. Validar build, testes, lockfile, scanner, IaC plan, artefato imutável + hash, deploy para staging, smoke, rollout e rollback.
6. Governar fork PRs: não executar código não confiável no contexto que tenha secrets ou escrita no repositório.

## Exemplo CI segura, ajustável
```yaml
name: CI
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
concurrency:
  group: ci-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4 # Preferir commit SHA auditado para uso crítico
      - uses: actions/setup-node@v4
        with:
          node-version-file: .nvmrc
          cache: npm
      - run: npm ci
      - run: npm run lint --if-present
      - run: npm test --if-present
      - run: npm run build --if-present
```
Não usar esse workflow sem adaptar a stack real, dependências e testes. Para produção, avaliar SHA pinning e supply-chain.

## OIDC
- AWS: `aws-actions/configure-aws-credentials` + IAM OIDC trust com claim `sub` restrito ao repo/branch/environment + role específica.
- GCP: `google-github-actions/auth` + Workload Identity Federation e Service Account com permissões mínimas.
- Azure: `azure/login` + federated identity credential do App/Managed Identity + RBAC mínimo.
- Nunca embutir Access Key, Service Account JSON, Client Secret em YAML. Testar token somente em job autorizado. Verificar políticas e limitações dos ambientes no plano GitHub atual.

## Gates
`environment: production` com regras suportadas pelo plano e pela visibilidade do repositório. Se Required reviewers não estiver disponível no plano, não presumir aprovação automática segura: exigir workflow_dispatch/manual gate no provedor e revisão de PR.

Referências: https://docs.github.com/en/actions ; https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments ; https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
