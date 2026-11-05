# Modelo de objetos do Linear

## Hierarquia
```
Workspace
 └─ Team (chave: ENG, PROD, ...)       → prefixo das issues (ENG-123)
     └─ Issue
         ├─ Label(s)                    → classificação transversal
         ├─ State                       → dentro do workflow do team
         ├─ Assignee(s)                 → responsável(is)
         ├─ Project (opcional)          → entrega rastreável com target date
         └─ Cycle (opcional)            → compromisso do período
 └─ Project (cross-team possível)
```

## Issue — campos essenciais
| Campo | Uso | Cuidado |
|---|---|---|
| title | ação concreta, não tópico | "Corrigir validação X no endpoint Y", não "Validação" |
| description | contexto + critério de aceite | sem descrição = débito |
| state | posição no workflow do team | usar os states existentes; não inventar |
| priority | 0 Urgente … 4 No priority | convenção do workspace |
| labels | bug, feature, débito, ... | classificação, não status |
| assignee | responsável | unassigned = ninguém comprometeu |
| project | entrega com prazo | project ≠ ciclo |
| estimate | pontos do time | só se o time estima |

## States típicos
`Backlog → Todo → In Progress → In Review → Done` (+ `Canceled`).
- `In Progress` = alguém está trabalhando agora; não usar como "planejado".
- `In Review` = existe PR/revision aberta; linkar.
- `Done` = critério de aceite verificado; não = "merge feito" automaticamente.

## Project vs. Cycle
- **Project**: entrega com início/fim e target date (ex.: "Checkout 3D"); agrupa issues de times diferentes.
- **Cycle**: cadência fixa do time (ex.: 2 semanas); agrupa o comprometido do período.
- Uma issue pode estar nos dois; colocar tudo no ciclo corrente infla o compromisso e esconde risco.

## Relações entre issues
- `blocks` / `blocked by`: dependência real — a blocker precisa terminar antes.
- `duplicate` / `relates to`: referência cruzada; duplicata real deve ser cancelada, não deixada aberta.
- Sub-issues: decomposição; pai sem filhos úteis é só uma pasta.

## Regras de ouro
1. Consultar antes de criar (título, label, project).
2. Uma issue = uma entregável verificável.
3. State reflete realidade verificável, não otimismo.
4. Toda issue em In Review/Done tem link de PR/ evidência.
