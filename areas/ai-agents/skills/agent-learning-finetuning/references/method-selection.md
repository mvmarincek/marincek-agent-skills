# Matriz de decisão e hipóteses de aprendizado

| Falha predominante | Intervenção inicial | Intervenção avançada | Evidência necessária |
|---|---|---|---|
| Alucina fato mutável | RAG com fonte confiável e freshness | retriever/reranker tuning | groundedness, recall@k |
| Esquece preferência | memória semântica com TTL | policy/context optimization | recall de preferência e isolação |
| Erra tools | contratos, exemplos, eval trajetória | SFT tool-use se suportado | tool success rate e ação validada |
| Erra formato JSON | schema/tool calling/validação | SFT estruturado | parse pass rate |
| Não segue estilo | few-shot e skill | LoRA/SFT | avaliação cega de estilo |
| Falha em decisões subjetivas | rubrica + exemplos | DPO/preference tuning | preferências humanas pareadas |
| Falha em tarefa avaliável com reward sólido | workflow + feedback | RFT | reward hacking tests e custos |
| Modelo grande caro | model routing, cache | distillation | qualidade/custo sob mesmo benchmark |
| Regressão por prompt grande | refatorar skills e contexto | otimizar com DSPy | eval com budget tokens |

## Métricas de decisão
Para comparar A vs B: `pass_rate`, `cost_per_success`, `latency_p95`, `unauthorized_action_count`, `fallback_rate`. Exigir análise por casos e intervalos de confiança se a amostra for pequena. Testar robustez contra prompts adversariais e contextos fora da distribuição.

## Técnicas e recursos
https://github.com/huggingface/peft
https://github.com/huggingface/trl
https://github.com/unslothai/unsloth
https://github.com/stanfordnlp/dspy
https://github.com/google-research/harness2
https://huggingface.co/docs/transformers/

Não prometer suporte universal a hardware, arquiteturas ou métodos. Confirmar versões/licenças antes de instalar.
