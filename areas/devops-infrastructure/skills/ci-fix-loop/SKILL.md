---
name: ci-fix-loop
description: "Diagnosticar e corrigir checks de CI falhando em pull requests: coleta de status e logs via gh CLI, classificação da falha, plano de correção, implementação mediante aprovação e verificação com re-run até o pipeline verde."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "devops-infrastructure"
---

# CI Fix Loop — Correção de Checks de CI

## Quando ativar
Quando o usuário relatar pipeline vermelho, checks falhando em PR, `CI quebrou`, `testes falhando no GitHub Actions`, `build error no pipeline`, ou pedir análise de logs de execução de CI. Distinto de `infrastructure-devops-architect` (que cria/configura o pipeline); esta skill é o **loop de diagnóstico e correção** de pipelines existentes.

## Definição operacional
Corrigir CI é: coletar o estado real dos checks, ler o log da falha específica (não o resumo), classificar a causa, propor correção mínima, implementar após aprovação e confirmar com re-run. Não é reexecutar esperando passar, desabilitar check ou "dar commit de novo para ver se agora vai".

## Contrato de entrada
Repositório com pipeline configurado, número da PR ou branch com a falha, acesso `gh` autenticado com permissão de leitura, e — para implementar a correção — permissão de push na branch. Se a falha for em provedor externo (ex.: Buildkite), apenas o link do detalhe é reportado; o diagnóstico fica fora de escopo.

## Pipeline obrigatório
1. **Coletar estado**: `gh pr checks <PR>` (ou `gh run list` para branch) para enumerar checks, status e duração.
2. **Isolar a falha**: identificar o check vermelho relevante; múltiplos vermelhos podem ter causa única — correlacionar antes de abrir frente por check.
3. **Ler o log real**: `gh run view <run-id> --log-failed` para o trecho da falha; extrair arquivo, linha, comando e mensagem de erro — taxonomia em `references/failure-taxonomy.md`.
4. **Classificar**: build (compilação/dependência), teste (assert/flake/ambiente), lint/format, infra (runner, rede, cache, secret ausente) ou flake (intermitente) — cada classe tem tratamento distinto.
5. **Plano de correção mínima**: descrever causa raiz e a menor mudança que a resolve; flake exige evidência de intermitência (re-run controlado) antes de qualquer mudança.
6. **Implementar após aprovação**: aplicar a correção, push na branch; nunca desabilitar/bypassar check para ficar verde — se o check estiver errado, corrigir o check explicitamente com justificativa.
7. **Verificar**: re-run do pipeline e confirmação de verde; se novos vermelhos aparecerem, reiniciar o loop no passo 1 documentando iteração.
8. **Registrar**: PR, check, causa raiz, correção e resultado — para alimentar estatística de falhas recorrentes.

## Segurança e permissões
Implementar correção somente após aprovação quando a mudança tocar código além do escopo óbvio do check. Não expor segredos que apareçam nos logs (reportar como `***` e sugerir rotação se vazaram). Não fazer force push nem rebase que esconda histórico de falha. Provedores externos de CI são out of scope: reportar apenas a URL de detalhes. Não declarar "CI corrigido" sem re-run verde como evidência.

## Referências e artefatos
- `references/failure-taxonomy.md` — classes de falha e tratamento de cada uma.
- `references/gh-commands.md` — comandos gh para checks, runs, logs e re-runs.

## Critério de aceite
Falha isolada com log real lido e citado; causa classificada com evidência; correção mínima aprovada e aplicada; re-run verde confirmado; nenhum check desabilitado sem justificativa explícita; episódio registrado com causa raiz.
