---
name: gh-cli
description: "Operar GitHub pelo CLI gh: autenticação e contas múltiplas, repos, issues, pull requests, Actions, releases e extensões — com os comandos corretos por tarefa e as armadilhas comuns (conta errada, paginação, flags interativos)."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "devops-infrastructure"
---

# gh CLI — GitHub pela linha de comando

## Quando ativar
Quando a tarefa envolver operações no GitHub a partir do terminal: criar/consultar PRs e issues, ler logs de Actions, publicar releases, gerenciar repos, ou quando scripts precisarem de gh. Distinto de `ci-fix-loop` (que usa gh para um fim específico — corrigir checks vermelhos): esta skill é a **referência geral de operação do gh**. Para autenticação conflitante, ver `references/auth-and-accounts.md` antes de qualquer push.

## Definição operacional
Usar gh corretamente é: verificar quem está autenticado antes de agir, escolher o subcomando certo para a tarefa, usar flags não-interativos em scripts (`--json` + `--jq` em vez de parsear texto), e respeitar os limites do CLI (não force push, não bypass de proteção de branch). Não é: tentar comando às cegas quando o erro é de permissão, ou parsear output humano com regex.

## Contrato de entrada
`gh` instalado e autenticado (`gh auth status`). Permissões da conta determinam o que é possível: leitura para consultas, push para criar PRs, admin para settings de repo. Ambientes CI podem usar `GH_TOKEN` em vez de login interativo.

## Pipeline obrigatório (por tarefa)
1. **Identidade primeiro**: `gh auth status` — confirmar conta ativa (múltiplas contas: `gh auth switch --user <user>`); erros 403 em push são quase sempre conta errada.
2. **Escolher o subcomando**: repos / issue / pr / run / release / api — mapa em `references/core-commands.md`.
3. **Consultar estruturado**: `--json <campos>` com `--jq` para extrair; nunca parsear tabela humana.
4. **Criar com conteúdo de arquivo**: PR e release bodies multilinha vão via `--body-file` (citar newline direto em argumento falha no Windows e é frágil em qualquer shell).
5. **Verificar resultado**: após criar/mergear, re-consultar o objeto (estado, URL) e reportar o link.
6. **Paginar quando listar**: listas grandes exigem `--limit` explícito (o default do gh trunca silenciosamente).

## Segurança e permissões
Nunca commitar tokens; `gh auth status` pode exibir máscara — copiar apenas a máscara. Push com credencial do gh em Windows com `credential.helper=manager` conflita: usar override pontual `git -c credential.helper= -c "credential.helper=!gh auth git-credential" push`. Não usar `--admin` para bypassar proteção de branch sem aprovação explícita. `gh repo delete`, force push e alteração de settings de repo são destrutivos: exigem confirmação. Em scripts, sempre `--yes` explícito é perigoso — preferir falhar a confirmar automático em operação destrutiva.

## Referências e artefatos
- `references/core-commands.md` — mapa de subcomandos por tarefa, com flags essenciais.
- `references/auth-and-accounts.md` — múltiplas contas, tokens, CI e o workaround de credencial do Windows.

## Critério de aceite
Identidade confirmada antes de agir; comando certo com flags não-interativos (`--json`/`--jq`/`--body-file`); operação verificada por re-consulta com link; nenhuma operação destrutiva sem confirmação; nenhum token exposto em comando, log ou commit.
