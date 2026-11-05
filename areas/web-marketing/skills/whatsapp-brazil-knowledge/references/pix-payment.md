# Pagamentos PIX

## Fundamentos

PIX deve ser processado no backend. O front-end apenas exibe QR Code, código copia-e-cola e status.

## Tipos de chave

Comuns no Brasil:

- CPF/CNPJ
- E-mail
- Telefone
- Chave aleatória

Não exponha chaves sensíveis desnecessariamente.

## Link e QR Code

O sistema deve armazenar:

- `payment_id`
- `provider`
- `status`
- `amount`
- `copy_paste_code`
- `qr_code`
- `expires_at`
- payload bruto do provedor

## Pix Automático

Para recorrência, separar:

- assinatura
- autorização
- cobrança
- pagamento efetivo
- falha/cancelamento

## Fluxo recomendado

1. Criar pedido.
2. Criar pagamento pendente.
3. Gerar PIX.
4. Exibir QR/copia-e-cola.
5. Receber webhook.
6. Validar assinatura.
7. Marcar pagamento como aprovado.
8. Atualizar pedido/assinatura.
9. Enviar confirmação por WhatsApp.

## Armadilhas

- Não confiar em botão “já paguei”.
- Não atualizar premium sem webhook confirmado.
- Não perder eventos duplicados; use idempotência.
- Não usar float para dinheiro.
