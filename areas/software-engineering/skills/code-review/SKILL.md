---
name: code-review
description: "Revisar mudanças de código (diffs, PRs, commits) em dois eixos: conformidade com os padrões do repositório e aderência ao que a issue/spec pedia; produzir parecer estruturado com severidade, evidência e veredito."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "software-engineering"
---

# Code Review — padrões e spec, com evidência

## Quando ativar
Quando o usuário pedir revisão de PR, `review das mudanças`, `revisa esse diff`, `code review do branch`, ou antes de aprovar/mergear mudanças de outra pessoa ou de um agente. Distinto de `continuous-code-sanitization` (refatoração incremental de código existente) e de `delivery-acceptance` (validação funcional da entrega): esta skill é o **parecer técnico sobre um conjunto de mudanças**.

## Definição operacional
Revisar é: ler o diff completo, entender a intenção declarada (issue, spec, mensagem do PR), verificar conformidade com os padrões documentados do repo, verificar aderência ao escopo pedido, apontar problemas com severidade e evidência (arquivo:linha), e dar veredito explícito (aprovar / aprovar com ajustes / bloquear). Não é: opinar sem ler o código, pedir estilo pessoal como se fosse padrão, ou aprovar porque os testes passaram.

## Contrato de entrada
Um alvo de revisão (diff, PR, ou intervalo de commits), acesso de leitura ao repositório, e — para o eixo "padrões" — os documentos de convenção do repo (CONTRIBUTING, AGENTS.md, docs de arquitetura). Se não houver padrão documentado, o eixo padrões reporta apenas o que é objetivo (erro, risco, teste faltante), nunca gosto pessoal.

## Pipeline obrigatório
1. **Contextualizar**: ler descrição do PR/issue e mensagens de commit; declarar a intenção percebida da mudança antes de julgá-la.
2. **Ler o diff inteiro**: `git diff <base>...HEAD` (ou `gh pr diff`); nunca revisar só o resumo de arquivos.
3. **Eixo Spec**: para cada requisito da issue/spec, marcar atendido / parcialmente / não atendido / não aplicável; apontar escopo extra não pedido (gold-plating) como achado.
4. **Eixo Padrões**: verificar convenções do repo (naming, estrutura, tratamento de erro, testes, segurança); citar o documento de padrão correspondente em cada apontamento.
5. **Classificar achados** por severidade — `bloqueante` (erro, segredo vazado, dado corrompido, teste quebrado), `importante` (risco real, contrato violado), `menor` (estilo documentado, clareza), `observação` (alternativa, não exige mudança).
6. **Evidenciar**: cada achado cita arquivo e linha do diff, com o trecho; sem evidência, o achado não entra.
7. **Verificar testes**: mudança de comportamento sem teste correspondente é achado bloqueante ou importante, conforme criticidade.
8. **Veredito**: aprovar / aprovar com ajustes (listar) / bloquear (listar bloqueantes); jamais aprovar com bloqueante aberto.
9. **Registrar**: parecer persistido (comentário de PR ou arquivo) discriminando o que foi revisado do que não foi (arquivos ignorados, áreas não cobertas).

## Segurança e permissões
Segredos, chaves e dados sensíveis no diff são bloqueante imediato + sugestão de rotação se já expostos. Não aprovar mudança que toca produção/IAM/payments sem revisor humano responsável quando o processo do repo exigir. Revisão de código não autoriza merge: quem decide é o dono do repo. Achados não são acusações: linguagem técnica, focada no código.

## Referências e artefatos
- `references/review-checklist.md` — checklist dos dois eixos com severidades.
- `references/finding-report-format.md` — formato de achado e de parecer final.

## Critério de aceite
Diff lido por inteiro com intenção declarada; cada requisito da spec endereçado; todo achado com severidade, arquivo:linha e evidência; testes verificados; veredito explícito sem bloqueante aberto; parecer discrimina cobertura e limites da revisão.
