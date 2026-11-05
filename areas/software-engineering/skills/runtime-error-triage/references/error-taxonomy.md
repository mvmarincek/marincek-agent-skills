# Taxonomia de Erros

## Front-end

Sinais: tela branca, console error, botão sem ação, hydration mismatch, null/undefined, rota ausente.

Verifique console, handler, estado, request API e renderização condicional.

## API / Backend

Sinais: 500, 404, 401, 403, CORS, validação de body, endpoint ausente.

Verifique URL, method, payload, rota, server log, middleware auth, env e SDK externo.

## Banco de dados

Sinais: migration failed, foreign key, unknown column, table does not exist, dados não salvam ou não aparecem.

Verifique schema, migration, dados pais, RLS/permissões e filtros.

## Deploy / Rede

Sinais: ngrok offline, localhost funciona e público não, build incompleto, CORS em produção, env local ausente no deploy.

Verifique comando, porta, URL pública, env, callback, proxy e HTTPS.

## Integrações

Sinais: webhook não chega, PIX pago sem atualizar, QR falha, PDF não baixa, upload abre quebrado.

Verifique credenciais, assinatura, evento bruto, idempotência, transação e refresh do estado visível.
