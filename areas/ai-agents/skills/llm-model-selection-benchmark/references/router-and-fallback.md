# Router de LLM, workloads e fallback
## Topologia proposta
`task → policy (dados/risco/budget) → classificador barato → modelo especializado → validar output → (fallback controlado) → resultado`.
## Exemplo de roteamento por papel
- Tarefas estruturadas e classificação: determinístico/pequeno, com recall/precision medidos.
- Programação e refatoração: modelo coder avaliado com repositório.
- Ferramentas de risco: modelo avaliado + regras determinísticas de privilégio + aprovação.
- Visão: VLM com suporte a grounding/OCR no idioma e resolução reais.
- Complexidade desconhecida: estimar dificuldade com heurística de escopo e histórico, escalar somente se qualidade exigir.
## Fallback
- Fallback não pode passar dados para provedor não aprovado; manter residência e políticas de retenção.
- Se janela de contexto insuficiente, preferir sumarização fiel/RAG, não truncar instruções de segurança.
- Limitar número de tentativas, custo acumulado e pior caso; checar schema e tool safety após fallback.
- Usar traffic mirroring somente com consentimento e dados adequadamente desidentificados.
## Deploy
Router com configuração versionada e feature flags; logs redigidos; budgets hard e monitorados; shadow test + canary; rollback para modelo anterior.
## Literatura oficial
- https://docs.litellm.ai/docs/routing
- https://docs.litellm.ai/docs/proxy/users
- https://openrouter.ai/benchmarks/routers
