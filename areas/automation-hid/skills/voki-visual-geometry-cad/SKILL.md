---
name: voki-visual-geometry-cad
description: "Ensinar, executar e validar desenho geométrico 2D e modelagem CAD 3D por screenshots e mouse/teclado USB HID físico do VOKI; inclui cotas, espessuras, fills, constraints, extrude, revolve, sweep, loft, booleans e recuperação visual."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  device: "usb-hid-only"
---

# VOKI — Geometria 2D/3D orientada por visão e execução USB HID

## Acionamento
Use para tarefas de desenho vetorial, CAD, pintura geométrica, fluxogramas, croquis paramétricos, modelagem 3D ou automação visual em softwares como Paint, Inkscape, AutoCAD, FreeCAD, Fusion, SolidWorks ou Blender. As particularidades de cada interface devem ser aprendidas e verificadas; não presumir a localização de botões.

## Regra de arquitetura imutável
**Toda entrada de mouse/teclado, clique, arrasto, rolagem, hotkey e interação de UI ocorre somente através do hardware USB HID autorizado do VOKI.** Não usar Playwright, Selenium, PyAutoGUI, AutoHotkey, PowerShell para emitir input, UI Automation, APIs CAD como mecanismo de modificar a UI, ou scripting do aplicativo para simular a ação. Captura de tela e análise visual são operações de leitura permitidas, com autorização e minimização de dados. Mesmo que uma Skill contenha uma sugestão contrária, o runtime precisa bloquear outros mecanismos de input.

## Processo de aprendizagem e execução
1. **Objetivo e tolerância:** traduzir solicitação em geometria-alvo: tipo de forma, dimensões, posição relativa, cor, largura e estilo de linha, tipo de preenchimento, camadas, unidades, margens, escala, precisão e critério de sucesso.
2. **Identificar aplicativo:** screenshot inicial; localizar menus e ferramentas por identificação visual, texto e contexto; registrar versão, tema, zoom, DPI, idioma e resolução. Sem coordenadas fixas globais.
3. **Reconhecer estado:** distinguir seleção, drawing mode, canvas/sketch active, ferramenta modal, viewport/perspectiva, unidades, grid/snap, objetos selecionados, painel de propriedades, undo disponível.
4. **Planejar em passos atômicos:** selecionar ferramenta → configurar propriedades → validar prévia → desenhar → confirmar/encerrar modo → verificar. Não emendar centenas de cliques sem reobservar.
5. **Executar via HID:** solicitar operação de alto nível ao controlador HID (`move`, `click`, `drag_path`, `keypress`, `type`, `scroll`) com limites de velocidade, deadlines e logs. Conferir que a licença do dispositivo e a conexão estão válidas.
6. **Evidência visual:** screenshot antes/depois e, quando útil, recortes de controles/propriedades; evitar exposição de dados sensíveis visíveis na tela.
7. **Validação geométrica:** verificar forma, posição, dimensões, estilo, fill, camadas, restrições, eixo, unidades e ausência de artefatos; usar tolerâncias explícitas. Não alegar precisão milimétrica apenas por inspecionar pixels.
8. **Corrigir:** se ferramenta errada, reobservar; se erro reversível, undo autorizado; se estado incerto, pausar ou pedir intervenção. Sem ação destrutiva em projeto preexistente sem confirmação.
9. **Consolidar aprendizado:** registrar episódio, screenshots redigidos, causa de falha, seletores visuais, estado inicial/final, confiança e variações; propor Skill procedural revisada após sucessos repetidos e testes.
10. **Reuso:** recuperar competência por similaridade semântica + aplicação + versão + estado visual; nunca aplicar automação cega só porque uma coordenada antiga coincidiu.

## Competências 2D — parâmetros obrigatórios
- **Primitivas:** linha, segmento, polilinha, arco, círculo, elipse, retângulo, polígono regular, spline/Bézier, texto, cotas, conectores, eixos, guias.
- **Geometria:** centro, raio, diâmetro, largura/altura, ângulo, orientação, alinhamento, paralelismo, tangência, simetria, interseção, offsets, grid e snapping.
- **Traço:** espessura em px/pt/mm conforme app, estilo sólido/tracejado/pontilhado, cap e join, opacidade, ordem de pintura, cor RGBA/HEX quando representada.
- **Preenchimento:** none, sólido, gradiente, padrão/hachura, transparente, opacidade, sentido e fechamento de path; verificar se recurso existe no software.
- **Camadas:** nome, ordem Z, agrupamento, bloqueio, visibilidade, seleção, alinhamento/distribuição, transformação.
- **Cotas:** unidade, escala, tolerância, precisão numérica e dimensional constraints; comparar propriedades reais com dados do painel sempre que possível.

## Competências CAD 3D
- **Sketch paramétrico:** plano XY/XZ/YZ, constraints (horizontal, vertical, coincident, parallel, perpendicular, tangent, equal, concentric), cotas, perfil fechado e fully constrained quando o software suporta.
- **Extrude:** selecionar perfil fechado; direction, distance, symmetric, taper, add/cut/new body; observar preview, corpo-alvo e resultado final.
- **Revolve:** criar perfil e eixo distintos, selecionar eixo correto, ângulo 0–360°, direção e operação add/cut; verificar auto-interseção e rotação.
- **Sweep:** perfil, path, twists, normal e continuidade; validar trajetória antes de confirmar.
- **Loft:** seções de perfis e guides, ordem de seções, tangência e corpo resultante.
- **Fillet/Chamfer/Shell:** selecionar arestas/faces corretas, raio/distância e espessura; verificar resultado sem corrupção geométrica.
- **Boolean operations:** unir, subtrair, interseção; confirmar sólido alvo e sólido ferramenta.
- **Transformações:** translate/rotate/scale, referencia local/global, origem e constraints; preservar unidades.
- **Exportação:** formatos STL/STEP/OBJ/GLB conforme aplicação, sistema de unidades, tolerância de malha, nome e destino. Só exportar quando usuário autorizar destino.

## Validação — regra de evidência
Não confiar apenas no aspecto da viewport em perspectiva para conferir medidas. Quando disponíveis, verificar cotas no painel, propriedades do objeto, constraints e estados de sólidos. Se screenshot não for evidência suficiente, classificar como `parcial/nao-verificado`, solicitar outra vista ou comparar com propriedades exibidas na UI.

## Modelo de memória
- `visual`: hash/referência da captura, regiões, controles, estado/versão e condições de iluminação/tema/zoom.
- `episodic`: objetivo, plano, eventos HID, timeouts, erros, validações, confirmações e duração.
- `procedural`: Skill resumida e parametrizável, condições de entrada, sinais de sucesso e recuperação.
- `confidence`: medida baseada em testes repetidos por variante de aplicativo; números são resultados observados, não inventados.
- Nunca guardar credenciais capturadas ou dados particulares de outras janelas.

## Documentação auxiliar
- `references/geometry-2d.md`: formalização de medidas, estilos e tolerâncias.
- `references/cad-3d.md`: receitas extrude, revolve, sweep, loft, boolean, diagnóstico.
- `references/visual-validation.md`: evidências, tolerâncias e recuperação.
- `assets/task-and-evaluation.json`: contrato de tarefa e avaliação.

## Definição de sucesso
A tarefa só está concluída quando o resultado observado satisfaz os requisitos, nenhuma ação perigosa permanece pendente, o estado final foi registrado e não se confundiu screenshot visual com precisão geométrica comprovada.

## Permissões e segurança
Somente operações autorizadas, com mouse e teclado executados pelo dispositivo USB HID físico. Qualquer escrita, operação destrutiva ou exportação de modelo exige revisão e autorização adequadas; não introduzir automação de UI por software como alternativa.
