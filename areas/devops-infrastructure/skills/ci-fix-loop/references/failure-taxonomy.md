# Taxonomia de falhas de CI

| Classe | Sintomas típicos | Tratamento |
|---|---|---|
| **Build** | Erro de compilação, dependência não resolvida, versão de runtime errada | Corrigir código/manifest; travar versões; conferir setup do runner |
| **Teste (assert)** | AssertionError com stack apontando arquivo:linha | Reproduzir localmente; corrigir código ou teste desatualizado (declarar qual) |
| **Teste (ambiente)** | Conexão recusada, fixture ausente, porta ocupada | Corrigir setup do job; service container/segredo ausente |
| **Lint/Format** | Erro de estilo, import não usado | Correção mecânica; configurar hook local para evitar reincidência |
| **Infra** | Runner offline, disco cheio, cache corrompido, rede | Limpar cache, trocar runner, re-run; sem mudança de código |
| **Flake** | Passa num re-run sem mudança | Evidência de intermitência (2+ runs, mesmo commit); depois isolar e corrigir causa (race, timeout, ordem) |

## Regras de classificação
- Classificar pelo **log real**, não pelo nome do check.
- Duas classes simultâneas: tratar na ordem build → infra → teste → lint; infra antes de teste evita falso negativo.
- Flake nunca é tratado com `sleep` maior; é tratado com causa raiz (espera por condição, não por tempo).

## Anti-padrões
- Re-run até passar (sem investigar).
- `continue-on-error`, `|| true`, exclusão do arquivo no lint — bypass de check.
- Marcar teste como skip para "resolver" a falha sem justificativa registrada.
