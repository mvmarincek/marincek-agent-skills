---
name: photoreal-3d-assets
description: "Projetar, produzir, revisar e otimizar modelos 3D fotorrealistas GLB de alimentos, mãos, utensílios, bancadas e lojas com materiais PBR, licenças e validação visual para WebGL/React Three Fiber."
license: MIT
metadata:
  version: "1.2.0"
  language: "pt-BR"
  category: "games"
---


# Photoreal 3D Assets — materialidade e pipeline game-ready

## Ativação
Projetos exigindo **geometria tridimensional real**, alimento com aparência real, metal inox, mãos ou personagens animados, texturas PBR, GLB/glTF e desempenho web. Integra `immersive-commerce-3d` ou qualquer game/3D web.

## Procedimento obrigatório
1. Organizar `AssetManifest` com `id, type, source, license, owner, checksum, scale_m, pivot, LOD, textures, polycount, animation_clips, collisions, review_status`. Auditar direitos comerciais (assets gerados, pagos e públicos). Não transferir texturas de outras marcas sem licença.
2. Produzir uma **direção de arte aprovada** antes de gerar muitos modelos: 3 ângulos, referências reais autorizadas, scale-sheet, câmera e iluminação padrão. Imagem conceitual é entrada, não GLB jogável.
3. Criar 3D via Blender modelagem/escultura ou ferramenta compatível com assets reais; plugins e Scenario MCP são opcionais e podem demandar GPU, autenticação e créditos; verificar disponibilidade/custo antes de solicitar geração. Não afirmar que ferramentas foram instaladas.
4. Alimentos: meshs com espessura, variação natural (morango fatiado, banana, queijo), mapas baseColor, normal, roughness, metalness quando aplicável e alpha somente quando necessário. Para Nutella/creme usar deformação/curva/mesh funcional, não decal fixo se for manipulado.
5. Bancada/cubas: inox com micro-riscos, reflexos controlados, bevels em bordas, material metalness e roughness plausíveis, reflexos e sombras de contato; scale real da chapa e das cubas; origem no centro de massa ou ponto consistente.
6. Mãos: rig/IK com alvos de agarrar e soltar; animação sem atravessar alimento, sem dedos extras e sem derretimento anatômico. Quando rigging não disponível, declarar limitação e implementar utensílio funcional em vez de fingir mão perfeita.
7. Exportar GLB/glTF 2.0 com nomes estáveis e `animationClips`; validar normals, orientação, materiais, transforms, UV, unidades, rigs, compressão (Draco/Meshopt/KTX2 com suporte), textura e copyright. Seguir o checklist `references/blender-glb-export.md`: cena em metros com Unit Scale 1.0, transforms aplicados, Principled BSDF, opções do exportador glTF 2.0 (`export_apply`, `export_yup`, Draco apenas com decoder e ganho medido). Em pipelines automatizados exportar headless: `blender --background asset.blend --python export_glb.py`.
8. Renderizar asset no runtime web com a iluminação final e **comparar lado a lado** com referência, não aprovar por screenshot do Blender. Inspecionar desktop e mobile; estabelecer budgets mensuráveis com profiling, sem prometer tamanho fixo.

## Regras
Não usar PNG como substituto de modelo 3D interativo nem criar cenário inteiro a partir de um único screenshot com animação aparente. `image-to-3D` requer revisão de malha/UV; modelos gerados geralmente precisam de limpeza, rig e otimização.

## Limites
- Asset gerado não é asset validado: a aprovação só vale após render no runtime final com iluminação de produção — screenshot do Blender não é prova.
- Licença auditada é pré-requisito, não pendência: asset sem origem/licença clara no manifesto não entra em produção.
- Budget de performance é medido no dispositivo-alvo, não estimado; asset que estoura o frame budget volta para otimização, não para "aceitar assim".
- Testes estruturais do pipeline não validam qualidade visual; a comparação lado a lado com referência aprovada é inegociável.

## Critérios de aceite
- [ ] Cada asset crítico é geometria real no runtime, visualizado de pelo menos 3 ângulos.
- [ ] Pivôs/escala/colisores coerentes, UV/normals corretos, sem interpenetração grosseira.
- [ ] Mapa PBR plausível e comparativo visual com referência aprovada.
- [ ] Manifesto de origem/licença por asset + GLB de produção e fallback.
- [ ] Frame budget medido em dispositivo-alvo e assets carregados sob demanda.
- [ ] Validação estática e visual registrada; sem inventar modelos ou testes.

## Referências, templates, entregáveis
Ler `references/pbr-pipeline.md` e `references/blender-glb-export.md` e preencher `assets/asset-manifest.example.json`. Entregar GLB, texturas, fonte editável quando permitido, manifesto, previews e relatório de QA.

**Aprovação e segurança:** não ativar ferramentas externas, gerar custos, publicar assets, alterar checkout ou implantar em produção sem autorização e verificação de licenças.
