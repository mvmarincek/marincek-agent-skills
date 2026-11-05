# Diagnóstico de URL Pública

## localhost

`localhost` só funciona na própria máquina. Para externos, use IP de rede local, tunnel, PaaS ou VPS.

## ngrok

Bom para demo, ruim para produção.

Problemas comuns: endpoint offline, ERR_NGROK_3200, domínio gratuito muda, callback aponta para link antigo, celular bloqueia.

Correção: confirmar serviço local, reiniciar tunnel, atualizar link exibido, atualizar webhooks e explicar que é temporário.

## Mobile

Verifique URL pública, bind em `0.0.0.0`, firewall, HTTPS e cache do navegador.

## Link de compartilhamento

Não hardcode localhost ou ngrok antigo. Use `PUBLIC_APP_URL`, request origin ou `window.location.origin`.

## Callback

Ao trocar URL, atualizar WhatsApp, Mercado Pago, Stripe, Supabase Auth, OAuth e rotas de QR/checkin.
