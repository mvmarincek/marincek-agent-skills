# Arquitetura do template — decisões e extensões

## Decisões tomadas (não remover sem motivo declarado)

| Decisão | Por quê |
|---|---|
| Express + webhook único (`/webhook`) | Ponto de entrada único validado; simplifica deploy em PaaS e tunnel |
| Máquina de estados por sessão (`src/conversation/state-machine.js`) | Conversa de pedido é sequencial; estado explícito evita árvore de if em handler |
| Camada de pagamentos abstrata (`src/payments/`) | Trocar Stark Bank por Mercado Pago/PagSeguro sem tocar na conversa |
| `MOCK_PAYMENTS=true` | Demo e desenvolvimento sem credenciais reais; confirmação automática simulada |
| LGPD embutido (`src/utils/lgpd.js`) | Consentimento e exclusão fazem parte da espinha dorsal, não do "depois" |
| `menu.json` como dado (`src/data/`) | Cardápio muda sem tocar código; interface única de customização |

## Pontos de extensão previstos
1. **Gateway**: implementar a mesma interface em `src/payments/` e registrar no factory.
2. **Novos fluxos de conversa**: estados novos na máquina (`confirmar_endereco`, `acompanhar_entrega`).
3. **Persistência real**: substituir store em memória por Postgres/Redis mantendo a interface de sessão.
4. **Templates de mensagem**: `src/whatsapp/templates.js` concentra persona e textos — nenhum texto solto no handler.

## Limites conhecidos
- Store de sessão em memória: reinício do serviço perde conversas em andamento (aceitável em demo; trocar antes de produção).
- Sem fila/retry de webhook: proveedores esperam resposta rápida; processamento pesado deve sair do request.
- Um número WhatsApp por instância; multi-loja exige multiplexação por número ou por payload.

## Evolução para produção (checklist)
- [ ] Credenciais reais no lugar do mock (`MOCK_PAYMENTS=false` + envs do gateway)
- [ ] Persistência de sessão e pedidos em banco
- [ ] Fila para processamento de webhook (BullMQ/SQS)
- [ ] Logs estruturados + monitoramento
- [ ] Webhook HTTPS com verificação de assinatura ativa
- [ ] Revisão de conformidade com `whatsapp-brazil-knowledge` vigente
