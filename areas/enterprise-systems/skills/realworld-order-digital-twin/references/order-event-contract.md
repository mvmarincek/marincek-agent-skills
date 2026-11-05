# Eventos de cozinha — contrato lógico, não integração existente

## Transições de exemplo (personalizáveis ao sistema real)
`cart → payment_pending → paid → queued → accepted → preparing → cooking → folding → packaging → ready_for_dispatch → dispatched → delivered`.
Estados alternativos controlados: `cancelled`, `payment_failed`, `unavailable`, `refunded`, `delayed`, `waiting_manual_confirmation`.

`event_type` deve representar ação realizada, por exemplo `kitchen.cooking_started`, não timer automático do front. Idempotency key formada por `(store_id, event_id)`; `(order_id, sequence)` monotônico e atualizado em transação; event sourcing opcional.

## API de referência
- `POST /checkout` (autenticação e cotação validada no backend): cria sessão, não assume pagamento aprovado.
- `POST /webhooks/payment-provider` verifica assinatura/origem/replay; dispara `payment.confirmed` somente se confirmado.
- `POST /kds/orders/{orderId}/events` exige operador autorizado e transição válida.
- `GET /orders/{orderId}/status` devolve snapshot autorizado, sem PII excessiva.
- `GET /orders/{orderId}/events/stream` SSE de eventos autorizados; headers privados; tokens com TTL; fallback polling.

## Modos e rotulagem obrigatória
- `SIMULATION`: 'Prévia interativa — preparo ilustrativo'; a animação segue input do cliente.
- `REAL_ORDER_TRACKING`: 'Etapa informada pela cozinha em HH:MM'; animar apenas milestone correspondente ao evento confirmado, nunca fingir live-feed.
- `REAL_VIDEO_AUTHORIZED`: 'Imagem ao vivo da cozinha' só se stream real do pedido/estação for verificável, câmera legalmente autorizada e acesso controlado.

## Privacidade
Separar customerId e order public token, aplicar object-level authorization. Reduzir videomonitoramento a estação consentida e evitar faces/clientes/áudio. Retenção explicitada e auditável; não fornecer URL pública persistente do stream.
