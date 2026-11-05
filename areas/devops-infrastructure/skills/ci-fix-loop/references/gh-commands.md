# Comandos gh para diagnóstico de CI

## Estado dos checks
```
gh pr checks <PR-NUMBER>          # todos os checks da PR com status
gh pr checks <PR-NUMBER> --watch  # acompanhar em tempo real
gh run list --branch <BRANCH>     # runs da branch (sem PR)
```

## Log da falha
```
gh run view <RUN-ID> --log-failed # somente o passo que falhou, com log completo
gh run view <RUN-ID>              # resumo dos jobs/passos
gh run view --job <JOB-ID> --log  # log completo de um job específico
```

## Re-run
```
gh run rerun <RUN-ID>                    # reexecutar tudo
gh run rerun <RUN-ID> --failed           # somente os passos que falharam
gh run watch <RUN-ID>                    # acompanhar a reexecução
```

## Autenticação e permissões
- Exigido: `gh auth status` autenticado com escopo de leitura no repositório.
- Para implementar a correção: permissão de push na branch (ou fork + PR).
- Provedores externos (ex.: Buildkite) aparecem como check com URL de detalhes: o `gh` não lê o log deles — reportar a URL e declarar fora de escopo.

## Fluxo recomendado
1. `gh pr checks` → identificar vermelho(s)
2. `gh run view <id> --log-failed` → extrair arquivo/linha/erro
3. Classificar (failure-taxonomy.md)
4. Corrigir + push
5. `gh run rerun <id> --failed` → `gh run watch` → confirmar verde
