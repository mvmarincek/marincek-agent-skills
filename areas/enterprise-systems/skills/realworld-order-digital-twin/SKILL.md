---
name: realworld-order-digital-twin
description: "Conectar experiência 3D de compra a eventos autenticados de cozinha/fabricação/logística/loja com eventos verificáveis, com máquina de estados, KDS/POS, WebSocket/SSE, vídeo opcional e distinção clara entre simulação e operação real."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "enterprise-systems"
---


# Realworld Order Digital Twin — operação real x game

## Ativação
Use quando a landing/game 3D precisa acompanhar produto físico preparado por uma equipe: creperia, cozinha, restaurante, confeitaria, fábrica sob encomenda, montagem automobilística, móveis, computadores personalizados, dark kitchen e despacho. Combina `immersive-commerce-3d` com rastreio real, sem confundir os dois.

## Limites essenciais
**Um game 3D não é a cozinha real.** A animação em 3D de preparar o crepe é uma demonstração. Apenas eventos emitidos/confirmados por sistema operacional autorizado (KDS/POS/ERP, app do chef, sensores específicos com validação) podem levar o status **real** a `preparing`, `cooking`, `packaging`, `ready`, `dispatched`.
Vídeo real ao vivo é um produto extra, não assumido. Exige câmera autorizada, transparência, privacidade/LGPD, controle de acesso, consentimento quando aplicável, sem captar outras pessoas/clientes indevidamente.

## Etapas de integração
1. Mapear checkout e gestão: pedido criado → pagamento confirmado → roteado à loja → fila → aceite → preparo → chapa → embalagem → pronto → entregador/retirada → saiu. Se o gateway não confirma, mostrar pagamento pendente, nunca preparo iniciado automaticamente.
2. Inventariar POS/KDS/ERP existente e seus webhooks/APIs. Se inexistente, criar painel mínimo de cozinha com botões de mudança de estado e logs por funcionário. Não inventar integrações nativas.
3. Definir contrato event-driven `order_id`, `store_id`, `sequence`, `event_id`, `event_type`, `occurred_at`, `received_at`, `source`, `actor_role`, `proof?`, `schema_version`; idempotência, deduplicação, ordenação, auditoria, controle multi-tenant, autenticação e autorização por papel.
4. Backend autoritativo valida transições; publica snapshot + stream por SSE ou WebSocket autenticado com `Last-Event-ID`/reconnect; polling de fallback, backfill, expiração; não transmitir PII ao front desnecessariamente.
5. Front com **dois mundos:** `mode: 'SIMULATION'` enquanto monta no game; `mode: 'REAL_ORDER_TRACKING'` após checkout confirmado. Se o backend informa `cooking`, a animação espelha essa etapa com rótulo claro `Etapa confirmada pela cozinha`; não representa automaticamente ações, pessoas, temperatura exata ou vídeo real.
6. Se oferecer câmera/stream, especificar fonte de verdade, consentimento, operador, retenção, criptografia, janela de acesso e planos de indisponibilidade. A câmera não substitui confirmação estruturada de etapa; sem suporte ao vínculo pedido↔câmera, não afirmar que aquele vídeo é do pedido do cliente.
7. Tratar compensações reais: indisponibilidade de item, cancelamento, reembolso, troca de loja, entrega externa, atrasos e eventos fora de ordem; sinalizar incerteza em vez de simular progresso.
8. Executar integração em staging com eventos sintéticos e depois piloto com autorização da cozinha, observabilidade e logs de auditoria antes de produção.

## Exemplo creperia (fases de implantação)
Fase A: usuário cria crepe no jogo e conclui checkout; após pagamento, acompanha statuses confirmados em KDS com timestamps. Fase B: funcionários registram início de chapa, dobra, embalagem, saída; 3D reage às mensagens, com labels e reconexão. Fase C **opcional**: vídeo da bancada autorizada com acesso temporário do cliente, quando for possível associar stream e pedido com evidência real.

## Generalização: da cozinha à linha de montagem
Para produto personalizado complexo, acionar `made-to-order-manufacturing-twin`: relacionar configuração comercial, revisão de especificação, ordem de produção, identidade física eventual e eventos de MES/ERP/PLM/WMS/TMS. O motor de eventos é genérico; os adaptadores e estados específicos por indústria são plug-ins. Uma animação de robôs montando o carro **representa uma etapa real confirmada**, não é filmagem ou prova de ações individuais. Se a produção estiver somente programada ou prevista, apresentar estado e incerteza corretos. O browser público nunca se conecta diretamente a sistemas OT.

## Segurança
Não permitir que cliente envie eventos `order_cooking` ou `order_dispatched`. Não capturar dados de funcionários indevidamente, não confundir telemetria de jogo com cadeia de pagamentos, não exibir dados de outros pedidos, não armazenar vídeo sem necessidade e base legal. Aprovação obrigatória antes de integrar credenciais/webhooks/sistemas de produção.

## Critérios de aceite
- [ ] Pedido tem origem comprovável, states válidos e autorização de leitura por pedido/tenant.
- [ ] Eventos com sequence/eventId deduplicados; mensagens fora de ordem não retrocedem indevidamente.
- [ ] Desconectado: app exibe `aguardando atualização` e não inventa `despachado`.
- [ ] Checkout e pagamento nunca são confirmados por game/front; logs auditáveis.
- [ ] Replay/reconexão e observabilidade operam em staging com fixtures sintéticas.
- [ ] Simulação, status real e transmissão de vídeo têm labels distintos e políticas próprias.

## Referências e entregáveis
Ler `references/order-event-contract.md`, `assets/order-event.example.json`; entregar arquitetura, schema de eventos, adaptadores, painel operacional (se aplicável), diagrama de estados, matriz de falhas, testes em staging e evidências do piloto quando realizado.
