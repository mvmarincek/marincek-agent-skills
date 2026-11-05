# Prompt para o Codex — implementação incremental no repositório da landing

Você está no repositório da aplicação web do cliente, com a biblioteca MVMarincek Skills v5 instalada.

OBJETIVO: criar ou integrar uma experiência **game 3D fotorrealista funcional** na landing page existente ou nova. Não entregar mockups, uma imagem estática ou apenas animações de CSS como se fossem uma mecânica 3D. Preservar rotas, SEO, pagamentos, design system, acessibilidade e analytics. Trabalhar em branch e feature flag.

1. Carregue `immersive-commerce-3d` e `gamified-landing-page`; para GLB/PBR carregue `photoreal-3d-assets`, para manipulação `tactile-3d-interactions`, para testes `immersive-experience-quality`. Carregue `realworld-order-digital-twin` **somente** se pedido exigir integração real após checkout.
2. Faça inventário de repo e stack, identifique se landing já existe e escreva um plano de diff pequeno. Preserve funcionalidades existentes e teste rota de compra antes de alterar.
3. Implemente PRIMEIRO vertical slice na cena: bancada inox com 3 cubas, chapa, crepe, mão/utensílio rigado, raycast, clique numa cuba, mão pega morango, transporta, deposita no crepe; o mesh fica sobre o crepe. Depois banana também permanece; undo remove o último. Texturas PBR e assets GLB verdadeiros com licença validada; não usar screenshot substituindo geometria.
4. Comprove com vídeo real de runtime, prints nos estados, testes unitários FSM, e2e, performance e acessibilidade. Não afirme sucesso se o asset ou a ferramenta não estão disponíveis. Se indisponíveis, entregue código/placeholder técnico assinalado e impedimento explícito, sem dizer que ficou fotorealista.
5. Somente após gates G0-G3, adicionar fluxo de preparo e embalagem simulados, checkout e status reais (KDS/POS/operador). Eventos reais precisam origem autenticada; sincronizar via SSE/WS e fallback, nunca por timer simulado.
6. Apresente no PR: arquivos alterados, antes/depois, video runtime, testes efetivamente executados, resultados de FPS/dispositivos, riscos/custos/licenças e etapas não concluídas. Nunca fazer deploy nem instalar ferramentas/MCP pagos sem aprovação.
