---
name: made-to-order-manufacturing-twin
description: "Projetar jornadas 3D pós-compra de produtos sob encomenda, como carros, conectando configuração, BOM aprovada, ordem de produção, MES/ERP/PLM, marcos de montagem e expedição a um gêmeo digital auditável, com indicação clara do que é real, estimado ou ilustrativo."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "enterprise-systems"
---

# Made-to-Order Manufacturing Twin — seu produto ganha vida após a compra

## Quando usar
Compra de produto personalizado físico cuja fabricação leva horas, dias, semanas ou meses, por exemplo: automóvel, moto, móvel sob medida, PC montado, bicicleta, máquina industrial, calçado, jóia e equipamentos. Ativar em conjunto com `immersive-commerce-3d` para game/configurador, `realworld-order-digital-twin` para status da operação e `immersive-experience-quality` para provas. **Não confundir o gêmeo de experiência com o controle da planta.**

## Experiência ideal — antes e depois do checkout
1. O cliente escolhe pintura, rodas, acabamento, motorização/opcionais no modelo 3D. A cena modifica materiais/meshes e persistem configuração e preço; catálogo, regras de compatibilidade e preço final são autoritativos no backend.
2. Configuração vira `configuration_revision`, `product_spec_id`, `bill_of_materials_reference` (se a fábrica oferecer), reserva/ordem de venda, aprovação técnica e comercial. Antes de aceitar pagamento/contrato, validar disponibilidade, homologação, prazo e regras da fabricante.
3. Ao receber `production_order_created` verificado, criar representação privada do produto encomendado; associar `customer_order_id` ao `production_order_id` por serviço de integração autorizado. VIN/serial **somente se oficialmente atribuído**; nunca inventar ID de linha/identidade de veículo.
4. A UI traz a jornada da linha de produção 3D: pedido aceito, produção programada, carroceria, pintura, casamento de powertrain, interior/montagem final, inspeção, testes, expedição, transporte, concessionária/entrega. O nome exato das etapas deve vir do fabricante: processos e sequência variam por planta.
5. A cada **evento confirmado** pela fonte autorizada, a estação 3D correspondente é desbloqueada: o cliente visualiza uma animação cinematicamente realista da etapa; exibir sempre `Representação 3D da etapa`, horário/precisão do último status e `Confirmado pelo sistema de produção`, nunca "você está assistindo seu próprio carro naquele exato segundo" sem telemetria e vínculo comprovados.
6. Ativar fotografia/vídeo real somente quando fabricante possui captura aprovada ligada a `production_order_id` ou estação e políticas de privacidade/segurança; detectar múltiplos carros no enquadramento e evitar revelar estratégia industrial, pessoas ou informações de terceiros.
7. Pós-fábrica: acompanhar logística, documentos, recebimento, preparação pré-entrega e retirada com eventos confirmados; expor atraso, retrabalho, recall/quality hold, alteração de pedido e previsão como **estimativa**, e não evento concluído.

## Fontes de verdade e integrações
- **ERP/CRM:** ordem do cliente, versão da configuração, preço, pagamento, disponibilidade, faturamento, logística, identidade e SLA.
- **PLM/PDM / configurador CPQ:** configuração aprovada, compatibilidade, revisão do produto; BOM/EBOM/MBOM quando disponível. Não expor propriedade intelectual da manufatura ao consumidor.
- **MES/MOM:** ordem de produção, estação, marcos e quality gates, timestamps e eventos vinculados à unidade (por exemplo VIN/serial quando existir).
- **WMS/TMS:** estoque, expedição, transportadora e last mile; nunca tratar previsão de expedição como expedição concluída.
- **SCADA/OPC UA / IoT:** opcional e **somente via integração industrial intermediária autorizada, read-only, segregada da OT**. O browser do consumidor nunca acessa CLP, máquina, MES, broker de planta ou rede industrial diretamente. Considerar ISA-95 como modelo de interoperabilidade; AAS/Eclipse Ditto são referências opcionais, não integrações existentes.
- Se nenhuma integração real estiver disponível, permitir modo **DEMO** com eventos explicitamente sintéticos e um operador autorizado para milestones. Jamais vender demo como produto rastreado em tempo real.

## Modelo de estado / fidelidade
Entidade `customer_experience_twin` vinculada a `product_spec_revision` e `physical_unit_id` **somente após atribuição real**; antes disso é digital twin da configuração/ordem, não do veículo individual. Separar `desired_spec`, `approved_spec`, `manufacturing_status` e `scene_visualization`.

Cada marco inclui: `event_id`, `order_id`, `production_order_id?`, `physical_unit_id?`, `sequence`, `source_system`, `source_record_id`, `event_type`, `occurred_at`, `ingested_at`, `confirmed_at?`, `data_freshness`, `evidence_level`, `plant_stage?`, `config_revision`, `status` e `schema_version`. Descrever nível de evidência `DEMO_SYNTHETIC`, `ESTIMATED`, `OPERATOR_REPORTED`, `SYSTEM_CONFIRMED`, `UNIT_VERIFIED`, `CAMERA_VERIFIED`; um evento de fábrica só se torna `UNIT_VERIFIED` se sua associação ao item encomendado for comprovada.

Projeções para UI devem passar por backend autorizado com snapshot e stream SSE/WebSocket; usar replay, ids idempotentes, ordering, backfill, limites de retenção e reconexão. Sem evento fresco, mostrar `Última atualização: HH:mm — aguardando nova confirmação`. Nunca adicionar estágio por timer, nem avançar enquanto o usuário está assistindo animação. Não fornecer datas exatas quando o fabricante fornece apenas estimativas.

## Arquitetura de integração proposta
`Configurador 3D → Configuração validada/CPQ → checkout/contrato → ERP (sales order) → PLM/MES (production order e marcos) → Integration Service (normalização, ACL, idempotência, auditoria) → Customer Digital Twin Read Model → API/SSE autenticado → Cena 3D + trilha de produção → WMS/TMS → entrega`.

Sem acoplamento entre componentes 3D e controladores industriais. Separar event bus privado, roteamento multi-tenant, escopo por pedido, JWT de curta duração, observabilidade, DLQ/reprocessamento e controles contra reordenação. Nunca propor integração direta ao ambiente industrial público.

## Storyboard obrigatório — automóvel configurado
- Escolher pintura azul, rodas esportivas, interior claro e multimídia; girar veículo, abrir portas, ver acabamento **no objeto 3D**, não em cards ou fotos trocadas.
- Confirmar configuração; gerar representação fiel das opções realmente compradas, mantendo consistência de materiais e de versionamento.
- Fábrica confirma início de carroceria: cenário 3D mostra robôs soldando **como animação ilustrativa da fase**, com data do evento real. Se ainda está agendado, informar explicitamente.
- Pintura confirmada: transição para célula de pintura; renderizar escolha do cliente sem prometer que a animação corresponda a filmagem da unidade.
- Montagem final confirmada: rodas, interior e opcionais são mostrados sendo colocados em sequência coerente, jamais concluir que cada parafuso foi instalado se o único dado é o fim da estação.
- Quality hold: congelar avanço e explicar `Em verificação` sem expor informações confidenciais; após aprovação, exibir etapa de testes.
- Expedição → transporte → entrega: status enviado por parceiros autorizados; snapshots e timestamps respeitam atraso de atualização do provedor.

## Fases incrementais
**Fase 0** catálogo e site existentes, contratos e integrações; **1** configurador 3D funcional; **2** checkout e pedido reais; **3** integração staging ERP/MES com eventos de exemplo; **4** piloto autorizado com dados de produção; **5** mídia real opcional e expansão multiunidade. Cada fase com critério explícito de aceitação; em nenhuma usar estoque/preço do client como autoritativos.

## Critérios de aceite
- [ ] Configuração visual do carro bate com especificação efetivamente vendida e persistida, com snapshot e revisão.
- [ ] Se identidade física VIN/serial ainda não existe, UI não afirma rastrear uma unidade específica.
- [ ] Milestones são executados somente por eventos autenticados da fábrica/operador autorizado; overlays diferenciam animação ilustrativa, previsão, confirmação e câmera real.
- [ ] Eventos duplicados, fora de ordem, cancelamentos, alteração de opções, hold de qualidade, atraso e reconexão testados.
- [ ] Não há acesso direto do navegador à rede OT, máquinas industriais, MES ou credenciais do fornecedor.
- [ ] A UX inclui 3D navegável e modo acessível sem WebGL; checkout segue disponível independente da cena.
- [ ] A evidência inclui vídeo **do aplicativo executando** com evento mock e, separadamente, teste em staging autorizado; nada é declarado LIVE sem validação operacional.

## Referências e entregáveis
Ler `references/manufacturing-digital-thread.md`, `assets/car-config-and-milestones.example.json`. Produzir integração adaptadora documentada, state chart e mapping de estação para animação, matriz source→evidence, plano de segurança de OT, evidência de E2E com cenários de falha, orçamento de assets e documentação dos estados confirmados versus previstos. `immersive-experience-quality` é gate obrigatório.
