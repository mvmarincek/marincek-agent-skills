---
name: immersive-experience-quality
description: "Criar quality gates automatizados para game 3D em landing pages: provas de interação, screenshots comparativos, regressão visual, performance em WebGL, teclado, mobile, checkout, fallback e eventos reais."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "games"
---


# Immersive Experience Quality — prova de realidade e conversão

## Ativação
Qualquer experiência de jogo 3D no browser, landing page com cena realista, configurador de produto 3D, live-tracking com cenas ou integração de WebGL no site comercial existente.

## Pipeline de QA obrigatório
1. Estabelecer baseline de funcionalidades e métricas do site existente: rotas/links, formulário, gateway, SEO e acessibilidade. Salvar screenshots referência desktop e mobile, sempre com autorização e sem dados sensíveis.
2. Definir **vertical slice verificável** antes de escalar o escopo; destacar uma ação crítica e mensurar entrada → objeto 3D → animação → estado → checkout. Ex.: selecionar ingrediente na cuba → mão pega → morango no crepe → soma atualizada → desfazer.
3. E2E com navegador/Playwright quando autorizado para **testar a landing**: capturar Canvas e estados via hooks de teste confiáveis, clicks, timestamps, snapshots; no VOKI (se envolvido) UI deve ser exclusivamente USB HID, não Playwright. Testes não criam exceção à regra do VOKI.
4. Testar `ProductState` unitariamente para persistência, duplicação, rollback, price/stock, state machine; testar e2e com backend simulado e backend real só em staging.
5. Revisão visual humana: mesmo enquadramento, foco, reflexos, nitidez de PBR, mão sem clipping, objeto transportado, deposição exata, geometria acumulada. Comparar vídeos de runtime, não confundir imagens estáticas renderizadas por IA com app funcional.
6. Perf budgets definidos por perfil dispositivo (mobile low-end, laptop integrado, desktop): coletar FPS p50/p95, memória/GPU quando disponível, draw calls, tamanho/tempo de GLB, LCP/CLS/INP. Ajustar sombras/reflexos, texturas, instâncias, LOD, lazy, DR/LQ e fallback conforme dados reais; nunca declarar '60 fps garantidos' sem medição.
7. Accessibility: teclado/touch, hit targets, motion reduction, legendas de estados, leitores de tela no DOM, contraste, alternativa sem WebGL e formulários convencionais até pagamento.
8. Testes de integração live: evento pago assinado, pedido aceito, duas mensagens duplicadas, evento atrasado, reconexão, expiração token, store mismatch, ausência de evento; jamais incrementar status por timer sem fonte real.
9. Revisar licenças e proveniência de cada GLB/texture, coleta de eventos e segurança de credenciais; gate de consentimento para analytics e vídeo.

## Gate adicional para manufatura sob encomenda
Para automóveis e produtos fabricados sob encomenda, exigir asserts: seleção 3D igual à configuração aprovada no backend, preço/compatibilidade validados, identidade física ausente antes de atribuição oficial, marcos MES/ERP isolados dos eventos do game, congelamento em quality hold, mudança de revisão sem atualização indevida da peça virtual, latência/freshness explícitas e ausência de claims de filmagem real sem prova. Testar `ESTIMATED`, `SYSTEM_CONFIRMED`, `UNIT_VERIFIED` e indisponibilidade de stream.

## Gates inegociáveis
**G0 Inventário:** baseline medido e backup das rotas. **G1 Mecânica:** vídeo capturado de runtime exibindo manipulação física real de um ingrediente. **G2 Visual:** assets aprovados em close e na cena. **G3 Conversão:** fluxo de pedido/checkout validado e fallback. **G4 Operação:** se houver live, estados verificados por backend, sem progressão falsa. Reprovar o gate se só houver PNG/mockup ou HTML decorativo.

## Exemplo de verificação
`click(bin_morango) → await state == 'reaching' → await state == 'carrying' → await state == 'committed' → assert scene.mesh(instanceId).parent == crepeGroup → assert quantity == 1`; repetir com banana, observar que ambos permanecem; desfazer banana e confirmar preço. Prova precisa de pelo menos uma gravação do runtime.

## Relatório e segurança
Usar `references/quality-gates.md` e `assets/quality-report.example.json`. Resultados não testados devem ser **NOT_TESTED**, nunca PASS. Testes devem rodar em sandbox com dados sintéticos; mudanças e deploy de produção exigem aprovação.

## Critérios de aceite e entregáveis
Relatório de gates PASS/FAIL/NOT_TESTED com evidências, URLs/paths de gravações quando existirem, métricas medidas, bugs priorizados, rollback plan, CVEs/licenças/PII. Nenhuma declaração 'game realista pronto' sem G1, G2 e G3.
