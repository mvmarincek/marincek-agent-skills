# Linguagem visual de game / cinema para landing pages

## Criar assinatura visual inédita
1. Definir linguagem de mundo (ex.: mapa de constelações das features, jornada espacial interativa, cockpit de missão, laboratório digital). Não copiar marca alheia.
2. Storyboard com 5–7 batidas visuais: tensão/objetivo → solução → demonstração → prova → confiança → objeções → ação. A estética leva a informação, nunca substitui.
3. Hero cinematográfico: camadas com luz volumétrica simulada, gradientes, materiais glass calibrados e vídeo original de produto. Preload apenas thumbnail/poster e recursos acima da dobra; vídeo adaptativo com H.264/AV1/WebM conforme compatibilidade.
4. Personagem/objeto 3D: orçamento de polígonos, materiais, texturas compressed KTX2, Draco/meshopt, LOD, bake e ambient occlusion. R3F/Three.js em island com lazy import, nunca como dependência para formulário básico.
5. Gráficos interativos: nodes/bubbles, sankey, temporal flows e 3D somente se ajudam a entender. D3/ECharts/visx; manter tabela textual/sumário acessível e dados verificáveis.
6. Motion system: entradas curtas e significativas, camera/parallax controlados, scroll progress sutil, idle loops limitados, hover/focus equivalentes. `prefers-reduced-motion` desativa animações não essenciais.
7. Vídeo de demonstração: sound OFF by default, controle pausa/replay/legendas, vídeo sem loop agressivo, não bloquear CTA ou scroll. A/B testar vídeo hero vs screenshot estático para medir efeito real.
8. Performance budget: definir bytes por tela, limites de LCP/CLS/INP, taxa de quadros alvo e modo economia em mobile/CPU fraca; WebGL fallback estático sempre.
9. QA: snapshots reais desktop/mobile, contraste WCAG, teclado, leitor de tela, scroll e vídeo, offline/3G, reduced motion, falhas de GPU e sem JavaScript.

Referências próprias já catalogadas: Hallmark, frontend-design, GameDev Agent Skills, awwwards-motion, 60fps.design, Scenario 3D OS, Platform Design Skills e React Best Practices. Preservar autoria e licenças. Não presumir que a Skill dispõe de gerador de vídeo: vídeo original precisa ser fornecido ou produzido por ferramentas autorizadas.
