# Arquitetura — Landing page jogável → Pedido → Cozinha real

## Missão
Incorporar games 3D fotorrealistas em landing pages **existentes e novas**, mantendo compra, conversão e acessibilidade. O jogo simula a montagem física, mas os estados de atendimento reais são produzidos por sistemas operacionais autenticados.

## Visão das camadas
```text
Visitante
  ├─ Landing/SEO/CTA e modo acessível (gamified-landing-page)
  └─ Cena 3D jogável (immersive-commerce-3d)
         ├─ Assets GLB/PBR/rig (photoreal-3d-assets)
         ├─ FSM de manipulação física (tactile-3d-interactions)
         └─ Estado configurador e preço ilustrativo/validado
                  ↓ finalizar configuração
             Commerce API → preço backend → gateway → pagamento CONFIRMADO
                  ↓ somente pedido real válido
             POS / KDS / painel da cozinha
                  ↓ eventos autorizados e auditáveis
             Backend status / snapshot / SSE / WS
                  ↓
             Tracking REAL na landing (realworld-order-digital-twin)
                  └─ vídeo ao vivo opcional, consentido, acesso limitado
Todos os passos: immersive-experience-quality
```

## Fluxo de caso demonstrativo: creperia
1. Cliente entra no cenário e vê bancada inox (cubas de morango, banana, queijo, chocolate) e chapa.
2. Ao escolher ingredientes, uma mão com rig pega a porção na cuba de origem, transporta e deposita sobre massa GLB; todos os itens persistem em coordenadas da chapa. Preço configurado é atualizado e é possível desfazer.
3. Game mostra simulação de assar, dobrar e embalar. A UI chama a experiência de simulação; isso NÃO significa pedido feito.
4. Usuário confirma compra; backend calcula preço/estoque e gateway confirma pagamento.
5. Apenas com compra confirmada, cliente entra em `REAL_ORDER_TRACKING`; operador KDS ou sistemas existentes emitem etapa do próprio pedido, com timestamp.
6. Render 3D pode espelhar marco de etapa confirmada (e.g., 'na chapa') sem fingir visão do chef real. Câmera física opcional requer vínculo comprovável entre estação, pedido, privacidade e transmissão autorizada.

## Roadmap recomendado
- M0 Baseline do site e integração existente (sem regressões).
- M1 Slice mecânica 3D: uma cuba → mão → ingrediente na massa → undo; medir FPS e validar visual.
- M2 Configurador multiingredientes e preparo simulado + UX mobile/accessível.
- M3 Checkout real, catálogo/stock/preço autorizados, logs e testes de compra.
- M4 Painel da cozinha ou adaptador KDS/POS → eventos status reais; SSE e replay.
- M5 Opcional: vídeo real por estação e pedido, com autorização formal e LGPD.

## Importante
Não pedir que o cliente espere pela animação para acessar checkout. Separar tempo de game, tempo real do preparo e tempo estimado de entrega. Nenhum status real é gerado por timer ou animação da cena. Em falha de rede mostrar 'Aguardando confirmação da cozinha'.

## Projetos beneficiados
Creperia (instância demonstrativa), food commerce, configuradores de moda/mobiliário, experiências de hotelaria, showrooms e lojas físicas, além de interfaces 3D comerciais em geral.

## Stack sugerida (adaptar ao repo)
React/Next.js + @react-three/fiber + drei + React state machine, assets GLB glTF 2.0, testes unitários/e2e de estado e snapshots, backend de checkout existente, Events/API + SSE/WebSocket para operação real. Blender/Scenario e MCP externos são somente opcionais após revisão de licença/custo/permissão.

## Ampliação v5.1 — fabricação complexa e carros
Ler também `docs/REALTIME_EXPERIENCE_COMMERCE_V51.md` e skill `made-to-order-manufacturing-twin`. Mesma ideia para crepe e veículo: a experiência 3D representa configuração e eventos reais, mas produção específica da unidade só é afirmada após evidência de vínculo confiável. Fábrica pode atualizar apenas em horários/etapas; jamais inventar tempo real contínuo.
