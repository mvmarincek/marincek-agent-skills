# Autenticação, múltiplas contas e CI

## Múltiplas contas
O gh suporta várias contas logadas simultaneamente, mas **uma** é a ativa por host:
```
gh auth status          # lista contas; marca a ativa
gh auth switch --user mvmarincek   # trocar a ativa
```
Sintoma clássico de conta errada: `403 Permission denied to <outro-user>` no push, mesmo o repo sendo seu.

## gh como credential helper do git
```
git config --global credential.helper "!gh auth git-credential"   # helper global
```

## Conflito no Windows
Se `.gitconfig` tem `credential.helper=manager` (Windows Credential Manager), o manager **tem precedência** sobre o helper do gh — o push usa a credencial velha mesmo após `gh auth switch`. Workaround pontual (sem mudar config global):
```
git -c credential.helper= -c "credential.helper=!gh auth git-credential" push origin <branch>
```
Nota: o caminho com espaço do gh.exe falha se expandido com aspas (`"C:\Program Files\..."` vira `C:Program`); a forma curta `!gh auth git-credential` resolve porque depende do PATH.

## CI (GitHub Actions)
- O runner injeta `GH_TOKEN`/`GITHUB_TOKEN` automaticamente; não usar `gh auth login` em CI.
- `gh` em script de CI: sempre flags não-interativos; falha de permissão do token = revisar `permissions:` do workflow.
- Nunca fazer echo do token; o runner mascara, mas só o valor exato — concatenações vazam.

## Regras de segurança
- Token no comando (`--field token=...`), em log ou em commit = incidente; rotacionar imediatamente.
- `gh auth refresh -s <scope>` só quando o escopo atual é insuficiente; não logar com escopos além do necessário.
- Sair de conta compartilhada após uso: `gh auth switch` de volta para a conta padrão.
