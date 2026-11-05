---
name: whatsapp-bot-scaffold
description: "Esqueleto de projeto para Bot de pedidos no WhatsApp no Brasil: webhook validado, máquina de estados, cobrança PIX e conformidade LGPD com Node.js + Express, pronto para customizar e publicar."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "web-marketing"
---

# WhatsApp Bot Scaffold — Bot de Pedidos (Brasil)

## Quando ativar
Quando o usuário pedir "fazer um Bot de pedidos no WhatsApp", "bot para lanchonete ou delivery no Brasil", "WhatsApp + recebimento por PIX" ou "bot de cardápio". Fornece a base executável; a skill complementar `whatsapp-brazil-knowledge` fornece o contexto de domínio.

## Definição operacional
Scaffold é um template de projeto completo e executável em modo demo (pagamentos simulados), com validação de webhook, máquina de estados de conversa e fluxo LGPD como espinha dorsal. Não é snippet avulso: o projeto deve instalar, iniciar e responder localmente antes da entrega.

## Contrato de entrada
Tipo de negócio (lanchonete, delivery, restaurante), cardápio/categorias/preços, gateway de pagamento desejado (Stark Bank, Mercado Pago, PagSeguro), persona do bot e alvo de deploy (Railway, Render, Fly.io, Coolify, Dokploy).

## Pipeline obrigatório
1. **Cópia do template**: usar `assets/template/` como base do projeto do usuário.
2. **Customização**: ajustar cardápio (`src/data/menu.json`), gateway (`src/payments/`), persona (`src/whatsapp/templates.js`) e deploy (`railway.toml`) conforme `Contrato de entrada`.
3. **Preservação da espinha dorsal**: validação de webhook, máquina de estados e fluxo LGPD não são removidos sem motivo declarado.
4. **Autoteste**: detectar node/npm (instalar se ausente), `npm install`, configurar `.env` em modo demo (`MOCK_PAYMENTS=true`), iniciar o serviço e validar resposta em localhost; falhas são corrigidas pelo agente, sem exigir ação manual do usuário.
5. **Entrega**: projeto rodando em modo demo, instruções para trocar mock por credenciais reais e rota de deploy.

## Variáveis de ambiente
| Variável | Uso | Obrigatória |
|----------|-----|-------------|
| `PORT` | Porta do serviço | Não, padrão 3000 |
| `TWILIO_ACCOUNT_SID` | SID da conta Twilio | Sim |
| `TWILIO_AUTH_TOKEN` | Token de autenticação Twilio | Sim |
| `TWILIO_WHATSAPP_NUMBER` | Número WhatsApp da Twilio | Sim |
| `WEBHOOK_VERIFY_TOKEN` | Token de verificação do webhook | Sim |
| `STARKBANK_PROJECT_ID` | Projeto Stark Bank | Não em modo mock |
| `STARKBANK_PRIVATE_KEY` | Chave privada Stark Bank | Não em modo mock |
| `MOCK_PAYMENTS` | Ativa pagamentos simulados | Não, padrão false |

## Modo mock
Com `MOCK_PAYMENTS=true`: PIX não chama API real, um link PIX simulado é retornado e a confirmação é disparada automaticamente após alguns segundos. Ideal para desenvolvimento e demonstração.

## Segurança e permissões
Nunca finalizar apenas com código gerado — verificar que o serviço inicia. Nunca pedir ao usuário para instalar o ambiente manualmente. Nunca exigir API keys reais em modo demo. Não commitar `.env` com credenciais; usar `.env.example`. Não expor tokens de webhook no cliente.

## Referências e artefatos
- `assets/template/` — projeto Node.js + Express completo (webhook, conversa, pagamentos, WhatsApp, dados e utils).
- Skill irmã: `whatsapp-brazil-knowledge` — conformidade, Business API, PIX e fluxo do comerciante.

## Critério de aceite
Template copiado e customizado; `npm install` e start executados com sucesso; resposta validada em localhost em modo mock; webhook, máquina de estados e LGPD preservados; instruções de credenciais reais e deploy entregues; nenhuma credencial real exigida em demo.
