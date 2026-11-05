# Digital thread — contrato de interoperabilidade (referência, não integração implementada)

## Fabricação sob encomenda
Mapear `sales_order` → `approved_configuration_revision` → `manufacturing_order` → `physical_unit_id` (quando emitido) → `work_center` → `production_milestone` → `quality_release` → `shipment` → `delivery`. Não assumir que o ERP/MES expõe eventos por unidade; solicitar contrato de integração ao fabricante.

## Níveis de precisão do real-time
- `SIMULATED`: animação decorrente de escolha do usuário, sem estado real.
- `ESTIMATED`: previsão calculada ou importada, sem prova de execução.
- `ORDER_VERIFIED`: pedido/configuração registrados no backend.
- `SYSTEM_CONFIRMED`: etapa confirmada por ERP/MES; pode ser por lote/fase, não unidade individual.
- `UNIT_VERIFIED`: associação do evento a VIN/serial/produção individual foi verificada por sistema autorizado.
- `CAMERA_VERIFIED`: imagem real autorizada e com vínculo ao pedido/estação autenticado.

Na UI exibir `Ultima atualização`, `Fonte: produção` (se permitido) e `Tipo: representação 3D`, `Vídeo ao vivo da estação` apenas no último caso. Se não existe fonte de telemetria, nunca dizer 'montando agora'.

## Eventos tolerantes a falhas
Identidade + idempotência: `source_system`, `source_record_id`, `event_id`; cursor monotônico por pedido. Snapshot versionado, SSE/WS para fan-out somente de read-model autorizado, replay desde última sequência, dedupe, reconciliador de estado para payload atrasado, status estáveis após desconexão. Regras de cancelamento, retrabalho e hold são transições explícitas.

## Integrações padrões e opções
ISA-95/IEC 62264: modelo entre níveis de negócio e manufatura, não API universal. OPC UA pode ser encontrado em planta, mas não faz conexão automática com marca/linha. AAS representa ativos e instâncias. Eclipse Ditto oferece mecanismo de digital twins/streaming, não resolve identidade e autorização de pedidos por si. Ingress industrial read-only, separado de clientes e do gateway público. Custos e permissões dos ERPs/MES são específicos de cada fabricante.

Referências públicas verificadas em 2026-11-01:
- https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- https://reference.opcfoundation.org/specs/OPC-30270/4
- https://eclipse.dev/ditto/httpapi-overview.html
