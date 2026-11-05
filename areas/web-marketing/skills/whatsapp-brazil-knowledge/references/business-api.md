# WhatsApp Business API

## Visão geral

A WhatsApp Business API deve ser tratada como canal oficial de relacionamento, não como simples automação de navegador.

Componentes principais:

- Conta Business Manager.
- Número de WhatsApp Business.
- Provedor BSP ou Cloud API direta.
- Templates de mensagem.
- Webhooks para mensagens e status.
- Sistema interno de pedidos, clientes e consentimentos.

## Escolha de BSP

Avalie:

- Suporte no Brasil.
- Custo por conversa.
- Facilidade de webhook.
- SLA e estabilidade.
- Suporte a templates e mídia.
- Integração com CRM, atendimento e pagamentos.

## Templates

Use templates para mensagens iniciadas pela empresa:

- Confirmação de pedido.
- Link de pagamento.
- Atualização de status.
- Lembrete.
- Pós-venda.

Evite mensagens genéricas demais; templates devem ser claros e ligados à finalidade.

## Tier e limites

O volume depende da qualidade e do tier do número. Não faça disparos agressivos sem controle de opt-in e qualidade.

## Desenvolvimento

Fluxo recomendado:

1. Receber webhook.
2. Validar assinatura/token.
3. Normalizar telefone em E.164.
4. Salvar mensagem bruta.
5. Atualizar estado da conversa.
6. Executar regra de negócio.
7. Enviar resposta.
8. Registrar status de entrega.
