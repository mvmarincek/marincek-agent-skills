---
name: whatsapp-brazil-knowledge
description: "Conhecimento do ecossistema brasileiro de WhatsApp para gerar código com melhores práticas locais: conformidade Meta/LGPD/PIX/CADE, Business API, pagamentos PIX e fluxo de pequenos comerciantes."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "web-marketing"
---

# WhatsApp Brazil Knowledge — Ecossistema WhatsApp Brasil

## Quando ativar
Quando a mensagem do usuário contiver `whatsapp`, `brazil`, `brasil`, `pix`, `lanchonete`, `bot whatsapp`, `LGPD`, ou quando for gerar código relacionado a bot/atendimento/pedidos no WhatsApp no Brasil. Injeta contexto de domínio local nas demais skills (ex.: `whatsapp-bot-scaffold`).

## Definição operacional
Skill de conhecimento: fornece o contexto regulatório, de API e de fluxo de negócio do ecossistema WhatsApp brasileiro para que o código gerado siga melhores práticas locais. Não gera código por si; complementa skills de implementação.

## Contrato de entrada
Tarefa de código ou arquitetura envolvendo WhatsApp no Brasil; estágio (pesquisa, scaffold, evolução, correção); necessidade de conformidade (Meta, LGPD, PIX/NF-e, CADE) e modelo de negócio do comerciante.

## Pipeline obrigatório
1. **Identificar camadas relevantes**: conformidade, Business API, pagamentos PIX e/ou fluxo do comerciante.
2. **Conformidade**: aplicar as 4 camadas (Meta → LGPD → PIX/NF-e → CADE) conforme `references/compliance.md`.
3. **Business API**: escolha de BSP, registro de número, aprovação de templates, limites por tier e webhooks conforme `references/business-api.md`.
4. **Pagamentos PIX**: tipos de chave, link de pagamento, Pix Automático para recorrência e fluxo ponta a ponta conforme `references/pix-payment.md`.
5. **Fluxo do comerciante**: mapear as 7 etapas (abertura, aquisição, atendimento, pedido, pagamento, entrega, pós-venda) conforme `references/merchant-workflow.md` e onde a solução entra em cada uma.
6. **Saída**: recomendações aplicadas ao código em questão, com limites regulatórios declarados.

## Segurança e permissões
Conformidade é obrigatória, não opcional: consentimento LGPD antes de armazenar dados, templates aprovados pela Meta antes do envio em massa, e atenção a riscos concorrenciais (CADE) em incentivos a pagamento. Não contornar limites de tier da Business API. Não armazenar dados sensíveis sem base legal. Dados baseados na pesquisa `brazil-portal-kb` (2026-05-16); verificar vigência antes de decisões críticas.

## Referências e artefatos
- `references/compliance.md` — 4 camadas de conformidade: Meta → LGPD → PIX/NF-e → CADE.
- `references/business-api.md` — 5 módulos da WhatsApp Business API.
- `references/pix-payment.md` — 6 módulos de PIX: fundamentos, chaves, links, recorrência, fluxo e armadilhas.
- `references/merchant-workflow.md` — 7 etapas do comerciante brasileiro.

## Critério de aceite
Camadas de conhecimento identificadas e aplicadas; conformidade LGPD/Meta tratada no código; limites regulatórios declarados; recomendações rastreáveis às referências; data dos dados verificada quando a decisão for crítica.
