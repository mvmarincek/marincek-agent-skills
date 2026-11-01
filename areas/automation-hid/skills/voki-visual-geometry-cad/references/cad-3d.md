# CAD 3D por aprendizado de interface

## Operações e pré-condições
| Operação | Entrada mínima | Propriedades verificáveis | Falhas comuns |
|---|---|---|---|
| Extrude | sketch fechado | comprimento, direção, modo add/cut/new | perfil aberto, corpo-alvo errado |
| Revolve | perfil + eixo distinto | eixo, ângulo, corpo, modo | interseção, eixo incorreto |
| Sweep | perfil + curva | percurso, orientação, corpo | twist, caminho interrompido |
| Loft | seções ordenadas | faces/guias e continuidade | seção invertida, geometria auto-intersectante |
| Fillet | arestas e raio | raio, seleção, preview | raio maior que limite geométrico |
| Chamfer | arestas | distância/ângulo | direção ou aresta errada |
| Boolean | dois sólidos | destino e tipo da operação | ordem dos sólidos invertida |

## Procedimento genérico, adaptado por software
1. Registrar software, idioma e ambiente/bench ativo.
2. Identificar plano de esboço e preparar perfil; confirmar fechamento e cotas.
3. Escolher feature pela interface via HID, confirmar diálogo e previews.
4. Inserir medida numérica via teclado HID; usar unidades explícitas.
5. Validar geometria após confirmação por viewport + árvore de features + painel de propriedades.
6. Se houver erro do kernel geométrico: interromper, capturar mensagem e revisar requisitos; nunca tentar 20 parâmetros aleatórios sem rastreabilidade.
7. Quando possível, verificar multi-vistas frontal/top/isométrica, inclusive posição de eixo e extrusão.

## Aplicativos
- **FreeCAD:** variar por workbench (Part Design, Part, Sketcher) e versão; não assumir menus fixos.
- **SolidWorks/Fusion/AutoCAD:** autorização, layouts e terminologia diferem; aprender via screenshot; respeitar licenças.
- **Blender:** extrusão e revolve/spin podem operar em Mesh/Edit Mode, com unidades e topologia diferentes de CAD paramétrico.

## Testes
Criar um cilindro a partir de extrusão de círculo, e outro por revolução de perfil retangular em torno de eixo; conferir dimensões do painel, diferença entre body/mesh e persistência de save. Evidência visual sozinha não garante sólido manifold ou fabricabilidade.
