# Playbook de conversão e mensuração

## Estrutura típica, adaptar
Hero: headline com transformação concreta, mecanismo, CTA primário, CTA secundário, imagem/mini-demo real.
Prova: logos autorizados, demonstrações verificáveis, números com fonte/data.
Benefícios: conectar dor > capacidade > resultado (sem promessa inverificável).
Como funciona: 3 passos simples e acessíveis.
Objeções: compatibilidade, implementação, privacidade, custo, prazo.
FAQ: perguntas pesquisadas e dúvidas reais; honestidade sobre limites.
CTA final: frase contextual e chamada clara.

## Eventos
`landing_view`, `hero_cta_click`, `demo_start`, `demo_finish`, `form_view`, `form_start`, `form_submit_success`, `form_submit_error`, `pricing_view`, `faq_expand`, `scroll_milestone_50`.
Não duplicar evento por re-render; respeitar consentimento e política de cookies. IDs de evento deduplicados quando houver retries.

## Experimentos
Hipótese exemplo: "Uma demonstração curta acessível acima da dobra aumenta intenção de teste comparada a imagem estática sem prejudicar LCP". Métrica primária: inscrição qualificada/visitante elegível; guardrails: Core Web Vitals, erros, abandono de formulário, reclamações. Randomização estável; registrar período, amostra e critérios. Não declarar causalidade com amostra insuficiente.

## Formulários
Pedir somente informação necessária, mensagens de validação acessíveis, feedback de erro sem limpar campos e proteção contra spam proporcional. Jamais inventar gatilhos falsos de urgência.
