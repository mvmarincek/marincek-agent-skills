---
name: deploy-diagnosis
description: "Diagnóstico de deploy para levar a aplicação de local a público estável: localhost, ngrok, link público, mobile, Docker, Coolify, Dokploy, Vercel, Railway, Render, variáveis de produção e callbacks de webhook."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "devops-infrastructure"
---

# Deploy Diagnosis — Diagnóstico de Deploy

## Quando ativar
Quando o usuário pedir `deploy`, `publicar`, `servidor`, `localhost`, `ngrok`, `acesso externo`, `link externo`, `Vercel`, `Railway`, `Render`, `Coolify`, `Dokploy`, `Docker`, `produção`, `hospedagem`, ou precisar compartilhar link, acessar pelo celular ou corrigir um deploy quebrado.

## Definição operacional
Diagnóstico de deploy é identificar o tipo de projeto, confirmar install/build/start/porta/healthcheck, escolher o caminho público adequado (tunnel, PaaS, VPS ou PaaS self-hosted), conferir variáveis de ambiente e callbacks, e validar desktop/mobile/anônimo/logado. Não é adivinhar plataforma nem recomendar "subir na Vercel" sem contexto.

## Contrato de entrada
Repositório e stack do projeto, comando de build/start, porta, variáveis de ambiente exigidas, integrações com callbacks (WhatsApp, PIX, OAuth, Supabase), restrições de custo/domínio e se o alvo é demonstração, staging ou produção.

## Pipeline obrigatório
1. **Detecção de projeto**: tipo, runtime e comandos conforme `references/project-detection.md`.
2. **Sanidade local**: install, build, start e healthcheck funcionando antes de qualquer deploy.
3. **Escolha do caminho público**: tunnel (demo rápida), PaaS (`references/paas-targets.md`), VPS ou PaaS self-hosted (`references/docker-coolify.md`); considerar custo, domínio e durabilidade.
4. **Variáveis de ambiente**: conferir todas as envs exigidas no alvo; sem expor segredos em log ou cliente.
5. **Callbacks**: atualizar URLs de webhook de WhatsApp, PIX, OAuth e Supabase para o domínio público; explicar impacto de cada mudança.
6. **Validação**: URL pública abrindo em desktop, mobile, anônimo e usuário logado; healthcheck respondendo.
7. **Saída**: tipo de projeto, comandos, status de build/start, envs aplicadas, alvo recomendado, URL validada, callbacks atualizados e rota de rollback.

## Segurança e permissões
Não tratar ngrok/tunnel como produção. Não expor secrets em comandos, logs ou cliente. Não alterar callbacks de pagamento/OAuth sem explicar impacto e confirmar. Não fazer deploy de produção sem aprovação explícita. Não dar orientação vaga; entregar comandos concretos e validados.

## Referências e artefatos
- `references/project-detection.md` — tipos de projeto e comandos.
- `references/public-url.md` — localhost, ngrok, links públicos e mobile.
- `references/docker-coolify.md` — Docker, Coolify, Dokploy e VPS.
- `references/paas-targets.md` — Vercel, Railway, Render e Fly.io.

## Critério de aceite
Projeto detectado com comandos confirmados; caminho público escolhido com justificativa; envs e callbacks aplicados; URL pública validada em desktop e mobile; riscos e rollback declarados; nenhuma credencial exposta.
