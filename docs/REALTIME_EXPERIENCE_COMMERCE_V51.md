# Experiência comercial 3D → produção física → entrega

## Visão transversal
Uma compra online deixa de ser um formulário: cliente **constrói/seleciona em 3D**, confirma a compra, e acompanha a produção do seu pedido através de um gêmeo **de experiência**. Esse gêmeo é uma UI interativa sincronizada por evidências; não há controle de manufatura pelo navegador. Aplicável a crepes, carros, móveis e qualquer produto configurável.

```text
Landing existente ou nova (SEO, conversão, CTA, acessibilidade)
  ├─ Game/configurador (R3F / GLB / PBR / animação interativa)
  ├─ Product configuration / variant state / preço estimado
  └─ Cart/checkout (backend faz validação comercial + pagamento)
                  │
                  ▼
          Backend: Sales order
                  │
            ┌─────┴───────────────┐
            │                     │
     Cozinha/POS/KDS       Fábrica ERP/PLM/MES
     Evento por pedido     Evento por ordem/lote/unidade
            └─────┬───────────────┘
                  ▼
     Eventos normalizados + evidence level + auditoria
                  ▼
         Snapshot + SSE/WebSocket autorizado
                  ▼
    Jornada 3D pós-compra (milestone mapeado em cena)
                  ▼
           Despacho / entrega
```

## Separação obrigatória de verdades
- `GAME`: simulação livre, sem efeitos reais.
- `ORDER_CONFIRMED`: compra/produção cadastrada no backend.
- `OPERATIONS_CONFIRMED`: marco operacional verificado por sistema autorizado.
- `UNIT_VERIFIED`: vínculo do evento à unidade física individual autenticado (quando existir).
- `LIVE_CAMERA`: vídeo de câmera autorizada e contextualizada, não substitui status estruturado.
- `ESTIMATE`: prazo estimado, nunca apresentado como etapa concluída.

## Cenário A — creperia
O cliente toca na cuba 3D de morangos → mão animada retira porção realista → deposita sobre massa e permanece; o jogo mostra crepe assando e embalagem (simulação). Checkout confirma; KDS/chef registra preparo, chapa, embalagem e despacho; UI 3D evolui *somente* com confirmação real. Live cam por estação, se viável, opt-in e autorização.

## Cenário B — montadora de carros
Cliente escolhe versão, pintura, rodas, acabamento e opcionais em modelo 3D navegável. Ao comprar, cria-se configuração aprovada ligada à ordem; cronograma pode mostrar milestones planejados como previsão. O MES/ERP envia atualizações quando carroceria, pintura, montagem final, inspeção e expedição ocorrerem. Cada milestone confirmado habilita uma **representação cinematográfica 3D** coerente com o carro escolhido, não video ao vivo. Sem identificação oficial da unidade, não se afirma que aquela é sua carroceria específica. Com identificação + evidência autorizada, pode-se evoluir a rastreabilidade por unidade. Quando fabricante disponibiliza vídeo ligado à estação/pedido e autorização, UI pode apresentar mídia real com rótulo e horário corretos.

## Modelo de integração genérico
ProductSpec + ConfigurationRevision + Order + ProductionOrder? + PhysicalUnit? + EventLog + EvidenceLevel + SceneMilestone + Shipment.

## Cadência e experiência
- O nível de tempo real depende da fonte. Uma cozinha pode informar um marco após minutos; uma montadora pode disponibilizar marcos diários, não telemetria segundo a segundo. A UI nunca deve interpolar verdade.
- Front deve expor `Última atualização`, demonstrar coerência entre cenas e pedido, tolerar desconexão, atrasos, retrabalho, mudanças de configuração e opções indisponíveis.
- Efeitos 3D e vídeo precisam ser opcionalmente reduzidos, com modo HTML acessível para completar compra e acompanhar etapa.

## Skills recomendadas
Orquestração: `immersive-commerce-3d`. Visual: `photoreal-3d-assets`, `tactile-3d-interactions`. Comercial: `gamified-landing-page`. Operações: `realworld-order-digital-twin`, `made-to-order-manufacturing-twin` quando fabrica sob encomenda. Qualidade: `immersive-experience-quality`.

## Plano de implementação seguro
P0 Inspeção da landing e fontes reais; P1 vertical slice funcional; P2 pricing+checkout; P3 backend de eventos sintéticos com etiquetas DEMO; P4 staging integrado ao KDS/MES mediante autorização; P5 piloto com dados e câmera opcional; P6 deploy depois de testes e aprovação. Sem acesso à fonte real, só possível criar demonstrador técnico e contrato de integração.
