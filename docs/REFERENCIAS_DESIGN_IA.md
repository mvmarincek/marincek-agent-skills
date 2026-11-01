# Base de referências de design — pronta para briefing de agentes

Este arquivo não oferece designs licenciados para clonagem. Ele organiza repertório para que Codex, Claude Code ou Verdent possam **planejar e desenvolver interfaces próprias**, com revisão humana.

## Curadoria por tarefa

| Demanda | Fonte prioritária | Aplicação |
|---|---|---|
| Interações de jogo, transições e física visual | https://60fps.design/ | GITFY, ISYMU, Metadia; microinterações, easing, estados de loading |
| Mobile criativo, 3D e imersivo | https://loadmo.re/ | GITFY e mobile, com benchmark de desempenho |
| Tendências de interface, motion e branding | https://recent.design/ | Direção de arte e padrões de interface |
| Copiar um elemento selecionado para refatoração | https://getdesign.ai/ | Extensão opt-in; privacidade e licença; não gera DESIGN.md comprovadamente |
| Posts de marcas, gráficos para campanhas | https://posts.design/ | Marketing, You8, mentoria |
| Primeira dobra e landing pages | https://supahero.io/ | A8 Mentor e produtos digitais |
| Navegação, sidebars, mega-menus | https://www.navbar.gallery/ | GITFY, ISYMU e SaaS |
| Botões, pricing, formulário, CTA | https://www.cta.gallery/ | Landing pages de conversão |

**Inspora:** https://inspora.design/ — não confirmada; consultar apenas após verificar.

## Template de DESIGN_BRIEF.md para cada frontend

- Público, objetivo e jornada principal.
- Paleta própria e contraste (WCAG), tipografia e escala de tamanho.
- Componentes fundamentais e estados: loading, erro, vazio, sucesso.
- Navegação desktop/mobile, foco/teclado e acessibilidade.
- Animações significativas: gatilho, duração, easing, objetivo, `prefers-reduced-motion`.
- Orçamento de performance: FPS alvo, tamanho do bundle, LCP/INP e fallback sem WebGL.
- 3–5 links de referência, com observação do **princípio reutilizado**, não cópia de código/marca/imagem.
- Critérios de aceitação visual e funcional; screenshots de desktop, tablet e mobile.

## Instrução de execução para os agentes

Antes de implementar uma interface, ler as referências deste arquivo, selecionar **no máximo cinco** aderentes ao objetivo e redigir `DESIGN_BRIEF.md` específico. Priorizar acessibilidade e desempenho, reutilizar skills do catálogo e não reproduzir literalmente uma identidade visual alheia.
