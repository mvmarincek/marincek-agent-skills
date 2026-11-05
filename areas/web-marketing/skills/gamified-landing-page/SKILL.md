---
name: gamified-landing-page
description: "Projetar e implementar landing pages altamente gamificadas, modernas, imersivas e focadas em conversao; React/Next.js, Three.js, shaders, graficos interativos, motion, UX, copy, SEO, performance, analytics e testes A/B."
license: MIT
metadata:
  version: "3.0.0"
  language: "pt-BR"
  category: "web-marketing"
---

# Landing pages gamificadas de alta conversão

## Ativação
Use para criar, redesenhar ou auditar landing pages que combinem estética premium e game-like com resultado de negócio. Serve para SaaS, produtos de IA, lançamentos e portfólios. Usar referências gráficas existentes na biblioteca sem copiar layouts protegidos ou descaracterizar marca.

## Prioridades ordenadas
1. Clareza da proposta e CTA de alto valor.
2. Performance e acessibilidade.
3. Narrativa interativa memorável.
4. Evidência real (demonstração, produto, casos autorizados).
5. Medição e iteração.

**Gamificação não é adicionar partículas em tudo.** Cada interação deve explicar valor, gerar feedback ou facilitar a conversão. Não manipular usuários com escassez falsa, contadores fabricados, depoimentos inventados ou padrões obscuros.

## Pipeline de implementação obrigatório
1. **Pesquisa do produto e público**: problema, oferta, diferencial, audiência, fontes verificadas, estágio do funil, objeções, CTA primário e secundário, métricas de conversão. Não inventar números, clientes ou resultados.
2. **Inventário do repositório**: framework, design system, assets, componentes, branding, integrações, analytics, testes, hosting; preservar funções existentes.
3. **Direção de arte**: construir conceito visual consistente (paleta, tipografia, profundidade, iluminação, materialidade, motion, iconografia). Preferir 1 metáfora visual de game por página. Usar `references/design-library.md`.
4. **Mapa da narrativa**: hero com proposta clara e CTA, demonstração interativa, benefícios com prova, casos de uso, detalhes/comparação, objeções, FAQ, CTA final; adaptar a produto, não impor seção desnecessária.
5. **Storyboard de experiência**: desenhar estados desktop/mobile, scroll, efeitos de entrada, loading, hover, feedback, transições e fallback sem WebGL. Inclui `prefers-reduced-motion`.
6. **Sistema de gráficos modernos**: selecionar visualização por dado, evitar chartjunk. Usar D3/ECharts/Recharts/visx, WebGL/Three.js/R3F quando justificável. Dados demonstrativos devem estar rotulados como "simulação"; nunca utilizar como métricas reais do produto.
7. **Implementação modular**: React/Next.js conforme stack, componentes tipados, CSS/tokens, Framer Motion/Motion, GSAP quando necessário, React Three Fiber/Three.js sob demanda; separar render 3D da camada semântica e dos formulários.
8. **Conversão real**: CTA coerente, prova verificável, formulários curtos, conexão com backend existente, rastreio consentido (lead_submit, CTA_click, scroll_depth, demo_start/finish), acessibilidade e microcopy honesta.
9. **Medição e experimentos**: formular hipótese, métrica primária, guardrails (LCP/CLS/INP, bounce/erro, acessibilidade); configurar eventos e comparações A/B com amostra mínima suficiente; não concluir que houve aumento sem medir.
10. **QA multiestado**: testar viewport móvel, desktop, redução de movimento, teclado, screen readers, baixa potência, WebGL indisponível, lentidão, erro de API, network failure. Renderizar e inspecionar screenshots; não declarar visualmente perfeito sem inspecionar.
11. **Otimização**: lazy load cenas/modelos, LOD, compressão, pouca luz dinâmica, limites de draw calls, texture budget, processamento assíncrono, prefetched assets quando útil, fallback estático. Medir e ajustar.
12. **Entrega**: código funcional, demonstração, métricas, checklist, assets/licenças, copy aprovada e documentação para alterações.

## Elementos de gamificação elegíveis
- **Progressão visual**: jornada de desafios/etapas mostrando valor, não bloqueando conteúdo.
- **Exploração espacial**: mapa 3D/constelação interativa de recursos, com navegação convencional equivalente.
- **Microrecompensas**: feedback de hover, seleção, conclusão de demonstração, sem animações intrusivas.
- **Painel simulado**: visualização interativa de cenário hipotético, claramente sinalizada.
- **Sistema de níveis**: benefícios por profundidade de uso, com informação acessível para todos.
- **Mini experiência**: simulação guiada do produto, sem depender da inscrição para compreender proposta.

## Contrato visual
- Evitar cara de template genérico: identidade forte, grid com respiro, tipografia hierárquica, contornos suaves, camadas glass calibradas e foco na legibilidade.
- Microinterações devem ter propósito; CSS first, motion library quando agrega, WebGL só para arte/explicação do produto.
- Definir `z-index` e sobreposição dos textos; evitar colisão com avatars, overlays e cabeçalhos.
- Não sacrificar contraste e legibilidade para neon/futurismo; dark mode sem esmagar sombras, glass sem perder contraste.
- Imagens e gráficos responsivos, limites de peso e degradação graciosa.

## Estratégia de copy e marketing
Defina proposta de valor pela fórmula `Para [público] que [dor], [produto] entrega [resultado verificável] por meio de [mecanismo], sem [objeção principal]`. Adaptar linguagem ao público. Headline concreto, subtítulo com contexto, CTA acionável, prova autorizada, benefícios específicos, objeções reais e FAQ. Documentar hipóteses (A/B), canais de aquisição, SEO semântico e métricas por estágio.

## Reutilização da nossa biblioteca
Consultar se disponíveis e **instaladas**: Hallmark, `frontend-design`, `vercel-react-best-practices`, Matt Pocock Skills, GameDev Agent Skills, Platform Design Skills, `awwwards-motion`, `60fps.design` (referências/MCP conforme caso), Scenario 3D OS apenas se produção 3D real. Não presumir compatibilidade nem instalar automaticamente. Veja `references/design-library.md`.

## Arquitetura local / neutra / cloud
React/Vite para simples; Next.js quando SSR, SEO e rotas exigirem. Deploy pode ser estático em Cloudflare Pages/Netlify/Vercel, ou AWS Amplify/CloudFront, GCP Firebase Hosting/Cloud Run, Azure Static Web Apps. Não recomendar apenas pela marca; comparar requisitos, custo, privacidade e equipe. Veja `references/cloud-deployment.md`.

## Critérios de aceite
- [ ] Proposta e CTA compreensíveis em 5 segundos de leitura.
- [ ] Mobile funcional e acessível; navegação por teclado e alternativa à animação.
- [ ] Rota de conversão testada end-to-end, sem dados fictícios.
- [ ] LCP, CLS, INP reportados em ambiente de teste e metas acordadas.
- [ ] Sem travamento em GPU fraca; fallback quando WebGL indisponível.
- [ ] Não há dark patterns nem alegações de conversão sem experimentos.
- [ ] Screenshots realistas e revisão das animações/estados.
- [ ] Analytics com consentimento conforme requisitos locais.

## Entregáveis
`DESIGN_DIRECTION.md`, `COPY_STRATEGY.md`, `UX_FLOW.md`, `EVENT_PLAN.md`, `PERF_REPORT.md`, `EXPERIMENTS.md`, código, screenshots e instruções de deploy. Use `assets/landing-brief.md` e `assets/qa-matrix.md`.

## Módulos avançados obrigatórios na v2 (quando relevantes)
- **Direção de arte de alto impacto:** usar `references/cinematic-experience.md` para storytelling, cenas 3D, vídeo com controle de autoplay/som e estética diferenciada, com performance budget e fallback.
- **Psicologia da atenção e decisão:** `references/attention-ethics.md` para hierarquia, saliência, curiosidade informacional, feedback e redução de atrito; basear hipóteses em testes, nunca prometer neurociência milagrosa ou usar dark patterns.
- **Medição de comportamento consentida:** `references/analytics-instrumentation.md` + `assets/event-taxonomy.json` para medir seções, CTAs, interações com gráficos, vídeo, form e conversão; diferencia observação agregada de rastreamento individual.
- **Experimentos responsáveis:** `references/experimentation.md` detalha hipóteses, guardrails, eventos, A/B e análise de resultados.
- **Interações reais:** `assets/analytics-adapter.ts` oferece adapter consent-aware sem dependência externa, para ligar a GA4/Matomo/PostHog apenas depois de consentimento e configuração.

**Padrão premium**: efeitos de game e vídeo precisam servir narrativa/CTA, manter conteúdo útil acessível por teclado/touch e no modo sem WebGL, sem ocultar preço ou condições. Medir como pessoas avançam no conteúdo, mas não capturar PII, cliques em campos sensíveis ou movimento individual do mouse sem base legal clara e consentimento.

## Segurança, privacidade e aprovação
Não instalar analytics sem consentimento e conformidade; solicitar aprovação antes de ativar trackers externos, publicar experimentos, criar contas pagas ou alterar políticas de cookies. Proteger visitantes contra rastreamento sensível e manipulação indevida.

## Evolução v5 — quando a landing deve ser um game 3D realista

Quando o usuário pedir **game 3D realista, cozinha de verdade, montar produto com mãos, apanhar ingredientes de recipientes, interações físicas, produto configurável em tempo real ou experiência jogável**, priorizar `immersive-commerce-3d` (especialista principal), que aciona `photoreal-3d-assets`, `tactile-3d-interactions` e `immersive-experience-quality` conforme necessidade. Aqui continuam os requisitos de funil, design, CTA, performance, marketing e SEO. Não converter solicitação 3D real em cards CSS, GIF, mockup, página plana, imagem estática ou vídeo pré-renderizado como entrega final.

- **Sites existentes:** inventário, feature flag, design tokens, checkout e rotas preservados. Teste de não regressão obrigatória.
- **Sites novos:** cena jogável como centro da jornada; criar fallback comercial HTML antes de depender só do WebGL.
- **Mecânica:** exigir vertical slice com item retirado da fonte 3D, transportado por mão/utensílio e depositado sobre o produto, persistindo em cena, com preço/resumo alterados e undo.
- **Produção real após pedido:** somente `realworld-order-digital-twin` integra eventos verificados da cozinha/KDS e/ou vídeo autorizado. Prévia simulada e eventos reais precisam ser explicitamente distintos.
- **Entrega:** evidência de runtime e testes, não apenas screenshots, boards e texturas.

## Evolução v5.1 — jornada comercial 3D continua após o checkout
Se o usuário quiser **carro, PC, móvel ou outro produto montando-se visualmente à medida que é produzido no mundo físico**, encaminhar para `immersive-commerce-3d` + `made-to-order-manufacturing-twin` + `realworld-order-digital-twin`; a landing faz UX, SEO e conversão, enquanto gêmeo de experiência controla configuração, status e cenas 3D. Não prometer visualização direta da fábrica sem vínculo de evento/identidade e autorização do fabricante. Rotular animação ilustrativa, status confirmado e câmera real com distinção explícita.
