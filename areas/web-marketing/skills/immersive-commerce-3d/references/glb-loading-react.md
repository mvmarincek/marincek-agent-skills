# Carregamento de GLB em React (R3F/drei)

Contrato de runtime para assets vindos do pipeline Blender→GLB da skill
`photoreal-3d-assets`. O asset é visual; a verdade do pedido vive no
`ProductState`/backend, nunca dentro do componente 3D.

## Carregamento
- `useGLTF(url)` do drei com `<Suspense>` acima do componente; o loader
  cacheia por URL.
- Code-split: `Scene` via `React.lazy` — three.js e GLB fora do bundle inicial
  (a landing continua utilizável enquanto o 3D carrega).
- `useGLTF.preload(url)` após o viewport entrar em cena, para prefetch sob demanda.
- Versionar a URL do asset (`/assets/strawberry_v2.glb`): cache-busting sem
  invalidar a CDN inteira.

## Isolamento de falha
- ErrorBoundary em volta do componente que usa o GLB; em erro, renderizar
  geometria procedural/2D equivalente e registrar o evento — **a compra nunca
  depende do asset 3D**.
- Sem lógica de negócio (preço, pedido, FSM) dentro do componente de asset.

## Pós-processamento do mesh carregado
- `useGLTF` retorna `nodes`/`materials` por nome; clonar material antes de
  mutar (`.clone()`) — material compartilhado altera todas as instâncias.
- Peças repetidas: clonar o nodo ou usar `<instancedMesh>`; manter
  `castShadow`/`receiveShadow` por mesh.
- Escala: GLB exportado em metros carrega 1:1 no three; se aparecer 100x, o
  erro está na exportação (corrigir na fonte, não compensar no runtime).

## Aceite
- [ ] GLB carrega sob Suspense sem travar scroll/checkout.
- [ ] Falha de asset degrada para fallback sem quebrar a página.
- [ ] Nenhuma mutação de material compartilhado entre instâncias.
- [ ] Bundle: three + GLB fora do chunk inicial (verificar no build).
