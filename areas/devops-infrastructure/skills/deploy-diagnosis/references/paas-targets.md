# Alvos PaaS

## Vercel

Bom para Next.js, static sites e APIs serverless. Não é ideal para worker/bot de longa duração. Configurar envs e callbacks no domínio de produção.

## Railway

Bom para Express, WhatsApp webhook, bot backend e serviços pequenos. Usar `process.env.PORT` e observar logs.

## Render

Bom para web service, static site e worker. Atenção a cold start e disco temporário.

## Fly.io

Bom para app Dockerizado e regiões específicas. Planejar volumes e banco separadamente.

## Escolha rápida

- Next.js landing/admin: Vercel.
- Express webhook/Bot: Railway ou Render.
- Entrega SMB de longo prazo: Coolify/Dokploy + Docker.
- Dados e arquivos duráveis: Supabase, managed DB ou object storage.
