# Contrato de experiência: 3D comercial jogável

## Design → código → prova
Cada interação requer `intent`, objeto de origem com `objectId`, ação, alvo 3D, duração, animação de ida e retorno, mutação em `ProductState`, efeito no DOM comercial, rollback/undo, evento de analytics consentido e evidência de teste.

**Game não equivale a VR, e efeitos não equivalem a experiência física.** Se nenhum modelo interativo reage ao clique, a entrega não é um game 3D.

## Estados de produto (exemplo)
`select_base → add_ingredient* → prep_simulation → package_simulation → cart → checkout → live_tracking(optional)`.
O fluxo é uma máquina de estados (FSM); estado só muda por eventos validados. Um pedido real é criado no backend pelo checkout confirmado, não pelo clique em `despachar`.

## Realismo mensurável
- Câmera player-view com escala coerente: bancada, cuba, chapa, mão no mesmo sistema de coordenadas; raycasting por mesh/collider.
- PBR: metalness/roughness map com contraste real, normais, sombras de contato, iluminação HDRI/licenciada e textura de alimento legível em close.
- Animação de manipulação: pickup sobre recipiente real, trajetória contínua, mão e ingrediente alinhados; `grab` oculta/consome porção visual no recipiente quando aplicável.
- `drop` instancia ou reparenta malha ao plano do crepe com z-offset e bounds corretos; múltiplos drops persistem em posições distintas; não renderizar apenas em card/sidebar.
- `undo` reverte a mutação e remove malha correspondente. Camadas preservam ordem e volume.

## Verificação
Vídeo/screenrecord do runtime: antes, clique, mão pegando, deslocamento, queda/depósito, acúmulo, undo, checkout. Fornecer snapshots do DOM e de estado; screenshot por si só **não prova** manipulação. Dados do checkout auditáveis no backend.
