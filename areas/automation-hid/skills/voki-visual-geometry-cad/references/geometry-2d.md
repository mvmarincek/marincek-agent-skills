# Desenho geométrico 2D com controle HID visual

## Contrato da tarefa
Registrar: `application`, `canvas_size`, `coordinate_system`, `shape`, `width`, `height`, `radius`, `center`, `rotation_deg`, `stroke_color`, `stroke_width`, `stroke_style`, `fill_type`, `fill_color`, `fill_opacity`, `layer`, `tolerance`, `expected_evidence`. Campos desconhecidos não devem ser fabricados: pedir interpretação por defaults visíveis ou indicar estimativa.

## Precisão
Pixel não é milímetro. Para precisão dimensional: conferir unidade/cota no painel do programa e calibrar zoom/canvas; estimativas de screenshot devem ter limite de tolerância declarado. Evitar `drag` com coordenadas absolutas imutáveis. Usar layout/âncoras visuais e screenshot a cada mudança de estado importante.

## Estilos
Traço pode ser pixels, pt, milímetros, espessura da caneta ou style props; não assumir equivalência. Preenchimento: vazio/solid/gradient/pattern/hatch/opacity; confirmar se contorno é independente do fill. Há diferenças importantes entre Paint, Inkscape e CAD: observar o software concreto.

## Estratégia de detecção
1. Captura do estado da interface; detectar app, menu/ribbon, canvas, painéis de configuração.
2. Encontrar entrada de seleção de shape e confirmar overlay visual.
3. Configurar cor/linha/preenchimento; screenshot das propriedades.
4. Executar caminho HID suave com início/fim controlados.
5. Validar contorno e preenchimento em crop, dimensões, alinhamento e z-order; se tolerância apertada, abrir painel numérico pela UI via HID.
6. Registrar evidências e progresso, conservar versão anterior para undo.
