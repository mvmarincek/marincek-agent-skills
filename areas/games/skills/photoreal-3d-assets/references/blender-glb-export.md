# Pipeline Blender → GLB para web (React Three Fiber)

Autoria e exportação verificáveis de assets PBR jogáveis. Nenhuma etapa aqui
substitui a validação no runtime final (ver Limites da skill). O pipeline vale
para Blender nativo (GUI) e headless em lote.

## 1. Preparo da cena no Blender
- Scene units: Metric com Unit Scale 1.0; modelar em **metros na escala real**
  — o runtime three.js usa metros 1:1 (chapa de crepe ~1,7 m, cuba ~0,5 m de
  diâmetro, morango ~0,04 m).
- Pivô consistente: origem do objeto no centro da base (utensílios, cubas) ou
  no centro de massa (alimentos); registrar o pivô no `AssetManifest`.
- Aplicar transforms (`Ctrl+A` → All Transforms) antes de exportar; escala não
  aplicada é a causa clássica de GLB "100x" ou "0,01x" no runtime.
- Nomes estáveis e semânticos: `strawberry_01`, `spatula`, `crepe_flat`;
  renomear `Cube.001` antes de exportar — o nome viaja no GLB e vira a chave
  de `nodes` no `useGLTF`.

## 2. Materiais (Principled BSDF → glTF PBR)
- Usar apenas Principled BSDF: o exportador mapeia Base Color, Metallic,
  Roughness, Normal e Emissive para o PBR do glTF. Nós exclusivos do Blender
  (Shader to RGB, texturas procedurais) **não exportam** — bakear em imagem antes.
- baseColor em sRGB; normal/roughness/metalness em espaço linear. O exportador
  classifica pela conexão do nodo, mas conferir Color Space imagem por imagem.
- Imagens embutidas no GLB (binário único) para assets pequenos;
  `GLTF_SEPARATE` apenas para debug.

## 3. Export glTF 2.0 — opções que importam
- `export_format='GLB'` para entrega; um GLB por asset com `use_selection=True`.
- `export_yup=True` (padrão): converte Z-up do Blender para Y-up do glTF.
- `export_apply=True`: aplica modifiers na exportação.
- `export_texcoords=True`, `export_normals=True`; `export_tangents=True`
  quando houver normal map.
- `export_animations` somente com clips reais nomeados; conferir range do NLA.
- `export_draco_mesh_compression_enable=True` **apenas** se o runtime tiver
  decoder (drei/DRACOLoader) e o ganho de bytes for medido no destino. Draco
  reduz vértices/atributos, não draw calls — medir fps, não só kB.

## 4. Validação no runtime (inegociável)
- Carregar no destino (`useGLTF`/GLTFLoader) — screenshot do Blender não é prova.
- Conferir: escala em metros, orientação, normals (sem faces invertidas),
  materiais por slot, animações, tri count vs. budget do dispositivo-alvo.
- Renderizar com a iluminação de produção e comparar lado a lado com a
  referência aprovada (gates da skill `immersive-experience-quality`).

## 5. Batch/headless (CI)
`blender --background asset.blend --python export_glb.py`
- O script chama `bpy.ops.export_scene.gltf` com as opções acima; falha de
  script sai com código != 0 e derruba o job.
- Um job por asset; o GLB de saída entra no manifesto com checksum e
  `review_status` antes de ir para produção.

## 6. Armadilhas conhecidas
- Escala 100x: transforms não aplicados ou Unit Scale diferente de 1.0.
- Material "lavado"/escuro: color space errado na textura.
- Asset invisível: normals invertidas ou alpha não intencional no material.
- Animação "congelada": action fora do NLA/fora do range exportado.
- Material mutado em todas as instâncias: material do GLB é compartilhado —
  clonar antes de alterar (ver `glb-loading-react.md` da skill
  `immersive-commerce-3d`).
