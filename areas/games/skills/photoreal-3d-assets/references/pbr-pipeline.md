# Pipeline PBR realista web

1. Medir objeto real e grade de câmera. Conferir unidade em metros, normals, winding e pivôs.
2. Blender/external assets → revisar topologia, UV, escala, curvas, rig, tangentes e lightmap conforme contexto.
3. Mapas relevantes: baseColor em sRGB; dados normais/roughness/metalness em espaço linear; considerar AO, clearcoat apenas quando justificável.
4. Usar meshopt/Draco/KTX2 apenas conforme suporte e ganho verificado; compare qualidade e bytes/fps no destino.
5. Nomes explícitos: `tray_strawberry`, `strawberry_slice_01`, `crepe_flat`, `crepe_folded`, `hand_rig_right`, `scoop_01`, `wrapper_open`.
6. Rig test: posição inicial, contato na cuba, grip, transporte, soltar, limpar mão, voltar. Capturar sequência com câmera travada.
7. Prefira LOD por importância, culling e instâncias onde apropriado; não usar milhares de meshes separados para confetes/granulados.
8. Defina orçamento por dispositivo e meça; imagens de IA não fornecem automaticamente UV/material/collider.

Fontes externas opcionais a verificar antes da instalação:
- https://r3f.docs.pmnd.rs/getting-started/introduction
- https://github.com/scenario-labs/skills (somente referência; hospedagem/geração pode custar)
- https://gltf-transform.dev/
