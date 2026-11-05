# GraphQL API do Linear — guia rápido

Endpoint: `https://api.linear.app/graphql` · Auth: header `Authorization: <LINEAR_API_KEY>` · Tudo via POST.

## Queries essenciais

### Buscar issues (antes de criar — anti-duplicata)
```graphql
query {
  issues(filter: { or: [
    { title: { containsIgnoreCase: "checkout 3d" } },
    { labels: { some: { name: { eq: "bug" } } } }
  ]}, first: 20) {
    nodes { identifier title state { name } assignee { name } url }
  }
}
```

### Vocabulário do workspace (states, labels, teams)
```graphql
query {
  teams { nodes { id key name states { nodes { id name type } } labels { nodes { id name } } } }
  projects { nodes { id name state } }
}
```

### Issue específica com comentários
```graphql
query($id: String!) {
  issue(id: $id) {
    identifier title description state { name }
    comments(first: 20) { nodes { body createdAt user { name } } }
    children { nodes { identifier title } }
  }
}
```

## Mutations essenciais

### Criar issue
```graphql
mutation($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success issue { identifier url }
  }
}
```
`input` mínimo: `{ teamId, title, description, priority, labelIds, projectId? }` — `teamId`/`labelIds` vêm da query de vocabulário.

### Atualizar state / assignee
```graphql
mutation($id: String!, $input: IssueUpdateInput!) {
  issueUpdate(id: $id, input: $input) { success issue { state { name } } }
}
```

### Comentar com rastreabilidade de PR
```graphql
mutation($id: String!, $body: String!) {
  commentCreate(input: { issueId: $id, body: $body }) { success }
}
```

### Arquivar (irreversível na prática — confirmar antes)
```graphql
mutation($id: String!) { issueArchive(id: $id) { success } }
```

## Regras
- IDs (teamId, labelIds, projectId, stateId) sempre da query de vocabulário — nunca adivinhar/hardcodar.
- Paginação: `first` + `after` (cursor); o default trunca silenciosamente.
- Mutação em massa: listar alvos primeiro (`issues(filter:)`), mostrar ao usuário, confirmar, executar.
- Rate limit: consultas em lote com aliases; evitar loop de N+1.
- Erros vêm em `errors[]` com `success: false` — checar os dois.
- Token é segredo: header de auth, nunca na query string, log ou commit.
