# Conformidade para WhatsApp no Brasil

## 1. Camada Meta

Use a WhatsApp Business Platform de forma compatível com as políticas da Meta:

- Obter opt-in antes de iniciar conversas comerciais.
- Usar templates aprovados para conversas iniciadas pela empresa.
- Respeitar limites de envio por tier.
- Evitar spam, scraping e automação abusiva.
- Manter logs de consentimento e origem do contato.

## 2. Camada LGPD

Dados pessoais como nome, telefone, endereço, pedidos e histórico de conversa devem ter base legal e finalidade clara.

Boas práticas:

- Coletar apenas dados necessários.
- Informar finalidade no primeiro atendimento.
- Registrar consentimento em `lgpd_consents`.
- Permitir revogação e exclusão quando aplicável.
- Proteger dados sensíveis e limitar acesso por função.

## 3. Camada PIX / NF-e

Para pagamentos e notas fiscais:

- Guardar status do pagamento separado do pedido.
- Registrar payload bruto do provedor de pagamento.
- Validar webhook por assinatura ou token.
- Não considerar pedido pago apenas por ação no front-end.
- Integrar emissão fiscal conforme o setor e a operação.

## 4. Camada CADE / concorrência

Bots de marketplaces, preços e automação comercial não devem induzir práticas anticompetitivas.

Evite:

- Compartilhamento de preços sensíveis entre concorrentes.
- Coordenação automática de preços.
- Bloqueio abusivo de fornecedores ou clientes.

## Checklist

- Opt-in registrado.
- Política de privacidade acessível.
- Templates aprovados.
- Webhook seguro.
- Pagamento confirmado no backend.
- Logs e auditoria disponíveis.
