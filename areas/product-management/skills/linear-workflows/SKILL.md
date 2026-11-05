---
name: linear-workflows
description: "Operar o workspace Linear: criar, consultar e atualizar issues, projects, cycles e triagem de states/labels/prioridades — via interface, Linear CLI/MCP quando disponível, ou GraphQL API — sem inventar status nem duplicar issues existentes."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "product-management"
---

# Linear Workflows — issues, projects e cycles com rastreabilidade

## Quando ativar
Quando a tarefa envolver o workspace Linear do time: consultar/atualizar issues e projects, organizar cycles, fazer triagem (states, labels, prioridade, assignees), ou espelhar trabalho de código (PRs, branches) em issues. Distinto de `linear-tasks-prd` (que escreve PRDs e documentos técnicos a partir do contexto Linear): esta skill é a **operação do workspace** — CRUD e triagem.

## Definição operacional
Operar Linear é: consultar antes de criar (issue duplicada é bug de processo), usar os states/labels/prioridades que existem no workspace (não inventar valores), e manter rastreabilidade (issue ↔ PR ↔ branch com referência cruzada). Não é: criar issues genéricas "fazer coisas" sem contexto, mover state para "pronto" sem evidência, ou reportar status que o Linear não confirma.

## Contrato de entrada
Acesso ao workspace (interface logada, integração Linear CLI/MCP configurada, ou token de API com escopo adequado). Para GraphQL: `LINEAR_API_KEY` no ambiente. Conhecer o vocabulário do workspace: states (backlog/todo/in progress/done ou custom), teams, labels e prioridades existentes — consultar antes de usar.

## Pipeline obrigatório
1. **Consultar antes de agir**: buscar issues existentes por título/label antes de criar (`issues(filter:)`); duplicata = comentar na existente, não criar nova.
2. **Respeitar o vocabulário**: states, labels e prioridades vêm do workspace; se o valor desejado não existe, propor ao time em vez de improvisar.
3. **Criar com contexto mínimo**: título acionável, descrição com critério de aceite, team, prioridade e labels; issue sem descrição é débito imediato.
4. **Atualizar com rastreabilidade**: ao abrir PR, referenciar a issue (branch/commit com `LIN-123` ou comentário com link); ao mergear, mover state conforme definição do time (não automaticamente "Done" sem verificação).
5. **Projects e cycles**: issue pertence a um project quando há entrega rastreável; ciclo agrupa o que o time comprometeu — não alocar tudo no ciclo corrente por conveniência.
6. **Reportar com fonte**: todo status reportado ao usuário vem de consulta ao Linear (número da issue, state, assignee), nunca de memória.

## Segurança e permissões
Token de API é segredo: nunca em commit, log ou command line visível. Conteúdo de issues pode conter informação interna do negócio — não copiar para repositórios públicos ou relatórios externos sem verificação. Issues com dados sensíveis (cliente, CPF, dados de saúde) seguem a política do time: internal note no máximo. Operações em massa (bulk update, archiving) são irreversíveis na prática: listar o alvo e confirmar antes.

## Referências e artefatos
- `references/linear-objects.md` — modelo de objetos (Team, Issue, Project, Cycle, Label, State) e relações.
- `references/graphql-cheatsheet.md` — queries e mutations essenciais da GraphQL API.

## Critério de aceite
Nenhuma issue criada sem consulta de duplicatas; states/labels/prioridades existentes no workspace; issue nova com descrição e critério de aceite; rastreabilidade issue↔PR mantida; status reportado sempre com número/state de issue consultada; nenhuma operação em massa sem confirmação; nenhum token exposto.
