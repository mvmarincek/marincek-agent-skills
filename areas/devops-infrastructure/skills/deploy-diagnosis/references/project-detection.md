# Detecção de Projeto

## Node / Web

Leia `package.json`:

- Next.js: `next dev`, `next build`, `next start`.
- Vite: `vite`, `vite build`, `vite preview`.
- Express: `server.js`, `src/index.js`, `app.listen`.
- Outros frameworks: verificar adapter e alvo de deploy.

Confirme install, build, start, porta, assets e envs.

## Python

FastAPI usa `uvicorn`, Flask usa `flask`/gunicorn, Streamlit usa `streamlit run`. Confirme Python, dependências, entrada e bind em `0.0.0.0`.

## PHP

Confirme Laravel/Symfony/plain PHP, composer, web root, `.env`, migrations e permissões de storage.

## Healthcheck

Forneça `/health` ou `/api/health` sem vazar secrets. Deve indicar app, banco e envs críticas presentes.
