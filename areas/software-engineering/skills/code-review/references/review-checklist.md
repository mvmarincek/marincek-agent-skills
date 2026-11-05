# Review checklist — dois eixos

## Eixo 1: Spec (o que foi pedido)
- [ ] Intenção da mudança declarada antes do julgamento (issue/PR/commits lidos).
- [ ] Cada requisito mapeado: atendido / parcial / não atendido / N/A.
- [ ] Escopo extra não pedido identificado (gold-plating).
- [ ] Efeitos colaterais em callers/consumidores do código alterado verificados.
- [ ] Migrações/breaking changes explicitados na descrição.

## Eixo 2: Padrões (como o repo exige)
- [ ] Convenções de naming e estrutura do repo seguidas (citar doc).
- [ ] Tratamento de erro conforme padrão do repo (não silenciar, não engolir).
- [ ] Logs sem dados sensíveis (token, CPF, saúde, conversa privada).
- [ ] Funções novas têm teste; bug fix tem teste de regressão.
- [ ] Dependência nova justificada e compatível com licenças do projeto.
- [ ] Sem código morto, comentário de debug ou TODO sem issue.

## Segurança (sempre)
- [ ] Nenhum segredo/credencial no diff.
- [ ] Input externo validado antes de uso (query, payload, path de arquivo).
- [ ] Query SQL/ORM parametrizada; sem concatenação de input.
- [ ] Mudança em auth/IAM/production flagged para revisor humano.

## Severidades
| Severidade | Definição | Ação |
|---|---|---|
| bloqueante | erro, segredo vazado, corrupção de dado, teste quebrado | bloqueia merge |
| importante | risco real, contrato violado, teste faltante em mudança crítica | corrigir antes do merge |
| menor | estilo documentado, clareza | corrigir, não bloqueia |
| observação | alternativa/sugestão | não exige mudança |
