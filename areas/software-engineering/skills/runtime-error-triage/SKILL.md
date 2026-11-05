---
name: runtime-error-triage
description: "Diagnosticar erros em runtime com classificação, localização de causa raiz, correção mínima e reteste: console, API, banco, migration, Prisma, Supabase, CORS, upload, PDF, QR, WhatsApp e callbacks de pagamento."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "software-engineering"
---

# Runtime Error Triage — Triagem de Erros em Runtime

## Quando ativar
Quando o usuário enviar erro, log, stack trace, traceback, console output, erro de migration, ou disser `não funciona`, `não abre`, `não salva`, `corrija`, `bug`, `falha`, `500`, `404`, `CORS`, `foreign key`, `migration failed`, `Invalid prisma`. Ativa em qualquer relato de comportamento quebrado em runtime.

## Definição operacional
Triagem é classificar o erro, reproduzir de forma mínima, localizar a camada responsável, aplicar a menor correção segura e retestar o mesmo erro. Não é adivinhar a causa nem empilhar tentativas; cada hipótese é confirmada por evidência antes de virar correção.

## Contrato de entrada
Mensagem de erro completa (texto, screenshot ou log), arquivo/linha/URL quando disponível, ambiente (local/staging/produção), passos de reprodução, stack trace, mudanças recentes relacionadas e acesso ao código-fonte. Se faltar informação, pedir antes de diagnosticar.

## Pipeline obrigatório
1. **Extração de fatos**: tipo, arquivo, linha, URL, status HTTP, ambiente, momento e frequência.
2. **Classificação**: enquadrar na taxonomia de `references/error-taxonomy.md` (front-end, API, banco, autenticação, integração, infraestrutura).
3. **Reprodução mínima**: reproduzir o erro no menor cenário possível; sem reprodução, tratar como hipótese e coletar mais dados.
4. **Localização da camada**: isolar UI, handler, API, banco, permissão, cache ou integração externa; verificar erros frequentes em `references/common-runtime-errors.md`.
5. **Correção mínima**: aplicar a menor mudança segura que resolve a causa raiz, seguindo `references/fix-workflow.md`; preservar contratos e dados.
6. **Reteste**: reexecutar o mesmo erro e confirmar resolução; verificar riscos semelhantes no mesmo módulo.
7. **Saída**: resumo do erro, categoria, raiz provável, módulos afetados, correção aplicada, validação e bloqueios restantes.

## Segurança e permissões
Não declarar "zero erros" sem prova. Não ignorar o erro específico com resposta genérica. Não confundir erro de banco/permissão com problema de UI. Não usar comandos destrutivos (drop, reset, delete em massa) por padrão; exigir aprovação e backup antes de qualquer ação destrutiva.

## Referências e artefatos
- `references/error-taxonomy.md` — categorias e entrada de diagnóstico.
- `references/fix-workflow.md` — correção mínima e reteste.
- `references/common-runtime-errors.md` — erros frequentes em stacks de usuários brasileiros.

## Critério de aceite
Erro classificado com evidência, reproduzido (ou hipótese declarada como tal), causa raiz localizada, correção mínima aplicada, mesmo erro retestado com sucesso e riscos correlatos verificados.
