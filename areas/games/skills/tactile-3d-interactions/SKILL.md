---
name: tactile-3d-interactions
description: "Implementar mecânicas reais de picking, drag/pickup/drop, hands rig/IK, física leve, acúmulo persistente de ingredientes, preparo e embalagem em configuradores e jogos 3D para web."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "games"
---


# Tactile 3D Interactions — game loop verificável

## Quando ativar
Usuário quer clicar em objetos 3D reais, pegar ingrediente ou produto com mão/utensílio, transferir para outra superfície, montar um item fisicamente, assar/dobrar/embalar, desfazer ou explorar em primeira pessoa.

## Pipeline
1. Definir `SceneGraph` e `ProductState` separados. Cada ingrediente tem `ingredientId`, `instanceId`, `sourceBin`, `meshRef`, `quantity`, `placementTransform`, `price`, `sequence`. As cubas possuem bounding volume, capability e estoque virtual/regras.
2. Criar `InteractionFSM`: `idle → hover → selected → reaching → grasping → carrying → placing → committed` ou `rollback/error`. Bloquear ação duplicada e invalidar comando obsoleto; suportar cancelar.
3. Entrada: raycast/pointer/touch/teclado; objetos só interagem quando alvos 3D visíveis e habilitados, com hover e foco acessível. Converter hit point para coordenadas locais da bandeja/chapa.
4. Mão: clip de idle, reach, grip, carry, release + IK para posição alvo; ingrediente segue attachment point da mão/utensílio **sem nascer no crepe no momento do clique**. Mostrar contato de retirada na cuba; animar caminho contínuo até o local do depósito.
5. Depositar: usar shape/mesh real e `placementTransform` validado na área do crepe. Instanciar mesh na cena e persistir no estado independente de `useFrame`; colisões suaves e limites impedem item cair fora. Não desenhar somente textura no painel lateral.
6. Composição: posição discreta/random determinística com seed, zonas válidas para diferentes recheios; aplicar molho como geometria/decal dinâmico quando apropriado, fatiados como instâncias e queijos com materiais animados. Evitar sobreposição impossível.
7. Cozimento simulado: mudança gradual de material ou morph conforme temperatura **simulada**, vapor sutil, tempo realista configurável sem confundir com acompanhamento real; dobrar com rig/morph/cinematic animation, embalagem com hierarquia GLB e animação de peças.
8. Sync: ao commit atualiza preço/resumo no DOM e `ProductState`, emite telemetria consentida e grava undo log. Se houver servidor, valida preço, combinações/quantidade e estoque antes do pedido real.
9. Testar input simultâneo, reversibilidade, FPS, partes do corpo cruzando malhas, persistência, visão mobile, navegação por teclado e rollback após erro.

## Exemplo verificável
`select('strawberry')` não adiciona imediatamente. `reach` move mão à cuba de morango; `grasp` anexa fatia visível ao `gripAnchor`; `carry` transporta; `release` coloca a fatia em `crepeSpace`; `commit` registra `instanceId` e preço; depois selecionar banana **não remove morango**; `undo` remove somente a banana e seu preço. São necessários vídeo de execução e asserts de estado.

## Não fazer
Não usar CSS transform de uma foto como se fosse mão 3D, não renderizar efeitos de partículas para disfarçar falta de pickup, não alterar state comercial durante `hover`, não escrever diretamente em pedido pago por ação de demonstração, não automatizar cozinha física sem projeto e aprovação de segurança específicos.

## Critérios de aceite
- [ ] A sequência inteira é visível no Canvas com clips e attachment; mínimo dois ingredientes permanecem sobre o crepe em GLB/geometry.
- [ ] Preview/commit/undo são testados com posições, instâncias e soma de preço determinística.
- [ ] Dois cliques rápidos não duplicam textura/checkout ou criam estados inválidos.
- [ ] Prep/package têm estados separados, não avançam sozinhos sem conclusão de animação.
- [ ] Visual, toque, teclado, GPU fraca e ausência de WebGL possuem tratamento testado.

## Referências e entregáveis
Ler `references/interaction-fsm.md`, `assets/interaction-case.json`. Entregar componentes TypeScript, state machine, clips/targets, sequência gravada no runtime, testes e relatório com limitações.
