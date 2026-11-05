---
name: delivery-acceptance
description: "Levar o projeto de código pronto para usuário conseguindo usar: checklist de aceitação, smoke test Playwright, mobile, upload, PDF, QR, CRUD, permissões e reteste antes de declarar o sistema pronto."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "software-engineering"
---

# Delivery Acceptance — Aceitação de Entrega

## Quando ativar
Quando uma entrega de Web/App/painel/sistema de negócio for declarada pronta, revisada ou testada; quando o usuário pedir `testar`, `verifique`, `revisar`, `corrija`, `não funciona`, `não aparece`, `botão`, `mobile`, `PDF`, `QR Code`, `upload`, `checkin` ou `admin panel`. Ativa **antes** de qualquer afirmação de conclusão.

## Definição operacional
Aceitação é a validação funcional de ponta a ponta por rotas críticas reais, com evidência. Não é revisão estática de código, não é "compilou então funciona". O critério é o usuário conseguir completar as jornadas essenciais, incluindo mobile e persistência.

## Contrato de entrada
Escopo da entrega (páginas, contas, papéis), jornadas críticas definidas pelo usuário, ambiente de teste disponível (local/staging), contas de teste por perfil, dados de exemplo, o que ficou fora de escopo e o roteiro de rollback em caso de falha.

## Pipeline obrigatório
1. **Escopo de aceitação**: listar páginas, contas/papéis, CRUDs, uploads, pagamentos, mensagens, mobile e erros conhecidos.
2. **Checklist**: gerar checklist conforme `references/acceptance-checklist.md`; marcar cada item como verificado, falha ou fora de escopo.
3. **Smoke test**: rodar testes existentes ou criar smoke test Playwright conforme `references/playwright-smoke.md`; cobrir login, jornada principal e refresh.
4. **Execução manual assistida**: percorrer rotas críticas com evidência (screenshot/log), cobrindo mobile, impressão/PDF, upload e QR conforme `references/mobile-print-file.md`.
5. **Registro de falhas**: cada falha com reprodução, esperado, atual e causa provável; classificar UI, handler, API, permissão ou dados — "botão não funciona" exige verificação de handler, API, permissão e persistência, não só CSS.
6. **Correção e reteste**: corrigir e retestar o mesmo item até passar; não marcar como corrigido sem reexecução.
7. **Relatório de aceite**: escopo, itens verificados, falhas, correções, retestes e riscos não cobertos.

## Segurança e permissões
Não declarar "tudo funciona" sem validação executada. Não validar apenas estrutura estática. Não ignorar mobile, refresh, persistência e permissão. Não executar testes destrutivos contra dados reais sem aprovação; usar contas e dados de teste.

## Referências e artefatos
- `references/acceptance-checklist.md` — checklist geral de entrega.
- `references/playwright-smoke.md` — estratégia de smoke test com Playwright.
- `references/mobile-print-file.md` — mobile, impressão/PDF, upload e QR.

## Critério de aceite
Todas as rotas críticas do escopo executadas com evidência; falhas registradas com causa e retestadas; mobile e persistência verificadas; riscos não cobertos declarados explicitamente; nenhum item marcado como pronto sem prova de execução.
