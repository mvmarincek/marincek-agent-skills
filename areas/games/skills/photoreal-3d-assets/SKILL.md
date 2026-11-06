---
name: photoreal-3d-assets
description: "Projetar, produzir, revisar e otimizar modelos 3D fotorrealistas GLB de alimentos, mãos, utensílios, bancadas e lojas com materiais PBR, licenças e validação visual para WebGL/React Three Fiber."
license: MIT
metadata:
  version: "1.3.0"
  language: "pt-BR"
  category: "games"
---


# Photoreal 3D Assets — materialidade e pipeline game-ready

## Ativação
Projetos exigindo **geometria tridimensional real**, alimento com aparência real, metal inox, mãos ou personagens animados, texturas PBR, GLB/glTF e desempenho web. Integra `immersive-commerce-3d` ou qualquer game/3D web.

## Procedimento obrigatório
1. Organizar `AssetManifest` com `id, type, source, license, owner, checksum, scale_m, pivot, LOD, textures, polycount, animation_clips, collisions, review_status`. Auditar direitos comerciais (assets gerados, pagos e públicos). Não transferir texturas de outras marcas sem licença.
2. Produzir uma **direção de arte aprovada** antes de gerar muitos modelos: 3 ângulos, referências reais autorizadas, scale-sheet, câmera e iluminação padrão. Imagem conceitual é entrada, não GLB jogável.
3. Escolher a rota pelo tipo de saída e confirmar as ferramentas realmente disponíveis. Para malha interativa, autorar/limpar em Blender ou usar gerador text/image-to-3D conectado (por exemplo, Meshy, Tripo, Scenario ou Rodin); são opções, não dependências presumidas. Verificar licença, export GLB, custo/créditos e permissão antes de enviar ou gerar; obter aprovação antes de qualquer operação paga. Imagem gerada pode servir de referência/textura depois de validada, mas não substitui geometria manipulável. Kling, Wan, Runway e Higgsfield são rotas de vídeo: podem fornecer footage/cinemagraph decorativo autorizado, nunca malha GLB, interação ou prova de evento real.
4. Alimentos: malhas com espessura, variação natural (morango fatiado, banana, queijo), mapas baseColor, normal, roughness, metalness quando aplicável e alpha somente quando necessário. Para creme/molho usar deformação/curva/mesh funcional, não decal fixo se for manipulado.
5. Bancada/cubas: inox com micro-riscos, reflexos controlados, bevels em bordas, material metalness e roughness plausíveis, reflexos e sombras de contato; scale real da chapa e das cubas; origem no centro de massa ou ponto consistente.
6. Mãos: rig/IK com alvos de agarrar e soltar; animação sem atravessar alimento, sem dedos extras e sem derretimento anatômico. Quando rigging não disponível, declarar limitação e implementar utensílio funcional em vez de fingir mão perfeita.
7. Exportar GLB/glTF 2.0 com nomes estáveis e `animationClips`; validar normals, orientação, materiais, transforms, UV, unidades, rigs, compressão (Draco/Meshopt/KTX2 com suporte), textura e copyright. Seguir o checklist `references/blender-glb-export.md`: cena em metros com Unit Scale 1.0, transforms aplicados, Principled BSDF, opções do exportador glTF 2.0 (`export_apply`, `export_yup`, Draco apenas com decoder e ganho medido). Em pipelines automatizados exportar headless: `blender --background asset.blend --python export_glb.py`.
8. Renderizar asset no runtime web com a iluminação final e **comparar lado a lado** com referência, não aprovar por screenshot do Blender. Inspecionar desktop e mobile; estabelecer budgets mensuráveis com profiling, sem prometer tamanho fixo.

## Regras de qualidade e bloqueio
Não usar PNG, vídeo ou geometria procedural de placeholder como substituto de modelo 3D interativo nem criar cenário inteiro a partir de um único screenshot com animação aparente. `image-to-3D` requer revisão de malha/UV; modelos gerados geralmente precisam de limpeza, rig e otimização. Fallback é permitido durante carregamento/erro para preservar a compra, mas deve ser identificável como fallback e **não pode passar G2 nem ser publicado como visual final**. Se os assets reais não estiverem prontos, declarar `NOT_READY`, manter a feature flag desativada ou limitar a entrega a demo explicitamente rotulada; não maquiar o bloqueio com lighting/post ou vídeo.

Avaliar no enquadramento final e contra uma referência de direção de arte aprovada: silhueta/proporção, materiais/roughness, exposição/white balance, luz/sombras/reflexos, escala/composição, detalhe e consistência entre assets. Corrigir primeiro a causa-fonte (asset, UV, material, exposição/lights e câmera), não esconder defeitos só com pós-processamento.

## Limites
- Asset gerado não é asset validado: a aprovação só vale após render no runtime final com iluminação de produção — screenshot do Blender não é prova.
- Licença auditada é pré-requisito, não pendência: asset sem origem/licença clara no manifesto não entra em produção.
- Budget de performance é medido no dispositivo-alvo, não estimado; asset que estoura o frame budget volta para otimização, não para "aceitar assim".
- Testes estruturais do pipeline não validam qualidade visual; a comparação lado a lado com referência aprovada é inegociável.

## Critérios de aceite
- [ ] Cada asset crítico é geometria real no runtime, visualizado em close, distância de uso e ao menos 3 ângulos; nenhum placeholder visível no candidato de release.
- [ ] Pivôs/escala/colisores coerentes, UV/normals corretos, sem interpenetração grosseira.
- [ ] Mapa PBR plausível e comparativo visual contra referência aprovada, sem clipping de highlights, materiais plásticos inesperados ou detalhe ilegível na escala final.
- [ ] Manifesto de origem/licença por asset + GLB de produção; fallback está separado e explicitamente marcado como não aprovado para release.
- [ ] Frame budget medido em dispositivo-alvo e assets carregados sob demanda.
- [ ] Validação estática e visual registrada; sem inventar modelos ou testes. Resultado visual `PASS` exige inspeção humana no runtime de destino; sem ela é `NOT_TESTED`.

## Evolução contínua
A cada falha visual em runtime, registrar screenshot/condições, causa-raiz, correção e regressão no teste ou scorecard; atualizar esta skill e sua versão quando o procedimento mudar. Revisar rotas de geração/importação trimestralmente e quando houver mudança material de ferramenta/formato, confirmando disponibilidade, termos, custos, export e limitações na fonte oficial antes de recomendar.

## Referências, templates, entregáveis
Ler `references/pbr-pipeline.md` e `references/blender-glb-export.md` e preencher `assets/asset-manifest.example.json`. Entregar GLB, texturas, fonte editável quando permitido, manifesto, previews e relatório de QA.

**Aprovação e segurança:** não ativar ferramentas externas, gerar custos, publicar assets, alterar checkout ou implantar em produção sem autorização e verificação de licenças.
