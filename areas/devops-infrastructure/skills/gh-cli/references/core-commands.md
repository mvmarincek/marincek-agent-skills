# Mapa de subcomandos do gh por tarefa

## Autenticação
```
gh auth status                      # quem está logado (sempre primeiro)
gh auth switch --user <user>        # trocar conta ativa
gh auth login                       # login interativo
```

## Repos
```
gh repo view <owner>/<repo> --json name,visibility,defaultBranchRef
gh repo list --limit 50 --json name,updatedAt
gh repo clone <owner>/<repo>
gh repo create <name> --public --source=. --push   # criar a partir do dir atual
```

## Issues
```
gh issue list --state open --json number,title,labels --limit 50
gh issue view 42 --json title,body,comments
gh issue create --title "..." --body-file issue.md
gh issue close 42 --comment "resolvido no PR #43"
```

## Pull requests
```
gh pr create --base main --head feat/x --title "..." --body-file pr.md
gh pr list --state open --json number,title,headRefName
gh pr view 3 --json baseRefName,headRefName,state,mergeable
gh pr diff 3                        # diff completo
gh pr checks 3                      # status dos checks
gh pr merge 3 --merge               # merge commit (não squash em PRs empilhados)
gh pr view 3 --json url --jq .url   # link para reportar
```

## Actions
```
gh run list --branch feat/x --limit 10
gh run view <run-id> --log-failed   # só o trecho da falha
gh run watch <run-id>
gh run rerun <run-id> --failed
```

## Releases
```
gh release list --limit 10
gh release create v1.2.0 --title "v1.2.0" --body-file notes.md
gh release upload v1.2.0 dist/app.zip
```

## API direta (quando não há subcomando)
```
gh api repos/{owner}/{repo}/branches --paginate --jq ".[].name"
```

## Armadilhas
- `--limit` ausente = lista truncada silenciosamente; paginar com `--limit 200` ou `--paginate`.
- Output humano (tabela) muda entre versões; sempre `--json` + `--jq` para scripts.
- Corpo multilinha em argumento quebra em cmd.exe; usar `--body-file`.
- PRs empilhados: merge com `--merge` (merge commit), nunca squash — squash colapsa os commits e quebra a pilha.
