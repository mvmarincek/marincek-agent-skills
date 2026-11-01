# MEMORY.md — VOKI (modelo ilustrativo)

> **Exemplo de formato, não memória real nem evento executado.** O banco estruturado é a fonte de verdade; aqui entram apenas fatos estáveis, curtos e confirmados.

## Metadados

- Contexto: exemplo local / aplicação Paint
- Atualizado: a cada consolidação validada
- Escopo: por usuário + aplicação + workspace

## Competências conhecidas

| Competência | Versão | Estado | Evidência |
|---|---|---|---|
| Desenhar formas no Paint | 0.1.0 | candidate (exemplo) | `skills/paint-draw-shapes/` |

## Fatos semânticos verificados

- Incluir somente detalhes observados: aplicação e versão, onde uma ferramenta foi encontrada, em que resolução/layout, e *quando* isso ocorreu.
- Registrar nível de confiança e validade. Não presumir que um controle terá sempre a mesma posição.

## Lições aprendidas (exemplos de campos, NÃO fatos ocorridos)

- `contexto`: aplicativo, versão e estado visual.
- `dificuldade`: o que falhou e como foi detectado.
- `recuperacao`: qual estratégia corrigiu o problema.
- `evidencia`: ID de episódio / screenshot, quando permitido.
- `validade`: última confirmação, versão e condições.

## Preferências locais autorizadas

- Preferências de trabalho explicitamente aprovadas (ex.: idioma das instruções, necessidade de confirmação para ações sensíveis).
- Não gravar segredos, senhas, tokens ou dados privados da tela.

## Links para memória profunda

- Índice/banco SQLite local: referência de caminho **configurável**, sem armazenar dados sensíveis no Markdown.
- Episódios e artefatos: IDs/URIs locais com controle de acesso.

## Alertas

- Skill que falhar por mudança visual deve perder confiança e regressar para `testing`.
- Este arquivo **não concede permissões** e não substitui política ou autorização de tools.
