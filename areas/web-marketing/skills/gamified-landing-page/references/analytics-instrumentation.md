# Instrumentação responsável de uma landing page

## Contrato de eventos
Use os eventos do `assets/event-taxonomy.json`. Inclua versão da taxonomia, session-id pseudônimo rotativo quando permitido, page_variant, section_id, CTA_id, campaign UTM após sanitização e consent status. Não registrar texto digitado, teclas, senhas, dados pessoais nem percurso bruto de mouse.

## Evento e ação
- `cta_click`: clique em CTA primário ou secundário, com id estável e seção.
- `section_view`: seção visível >=50% por >=1000ms com IntersectionObserver, evento uma vez por visita/versão, observação ≠ leitura.
- `video_start`, `video_progress_25/50/75`, `video_complete`: apenas primeiro marco por visita do vídeo; DNT/consentimento respeitados.
- `graphic_interaction`: interação com bolhas/mapa/gráficos agregada, evento explicitamente nomeado; sem guardar coordenadas do cursor.
- `form_start`, `form_error`, `generate_lead`: sucesso somente após confirmação do servidor, sem campos pessoais nos parâmetros.
- `experiment_exposure`: salvar atribuição a variação estável, evitando contaminação entre sessões quando aplicável.
- `conversion_verified`: evento no backend mediante confirmação, deduplicado por id não sensível.

## Fluxo analytics
Cliente com consent gate → fila local curta em memória → endpoint próprio / GA4 / Matomo / PostHog conforme escolha → store agregado → dashboard de funil; consentimento revogável e retenção configurada. Bots e tráfego de teste separados; deduplicação e anti-spam no backend.

## Gráficos e indicadores
Funnel Sessions→CTA→Form Start→Lead; conversão por canal/campanha/dispositivo/variante (com privacy thresholds), vídeos por milestone, atenção aproximada por seção, p95 de carregamento, abandono de formulário, revenue per qualified lead quando viável. Não usar métricas fictícias em dashboard real.

## GA4
`generate_lead` é recomendado; os demais custom events precisam de configuração e event parameters de documentação. Configurar via gtag/Tag Manager *somente após consentimento pertinente*. Referências: https://developers.google.com/analytics/devguides/collection/ga4/events e https://support.google.com/analytics/answer/9267735
