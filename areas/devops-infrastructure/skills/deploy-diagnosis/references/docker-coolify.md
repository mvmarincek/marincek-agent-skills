# Docker, Coolify e Dokploy

## Quando recomendar

Quando o usuário disser que quer colocar no servidor e parar de rodar localmente, prefira Coolify, Dokploy ou Docker Compose em VPS.

## Dockerfile

Confirme versão do runtime, instalação, build, runtime separado, bind `0.0.0.0` e porta configurável.

## Compose

Serviços comuns: app, postgres/mysql, redis e caddy/traefik. Secrets ficam em `.env`, não no repositório.

## Coolify / Dokploy

Preparar repo, build command, start command, porta exposta, envs, domínio, HTTPS, storage persistente e banco.

## Rollback

Manter release anterior, não apagar volumes, voltar app antes de mexer no banco e tratar migration separadamente.

## Persistência

Banco em Docker precisa de volume. Uploads precisam de volume ou object storage.
