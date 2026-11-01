# Protocolo de benchmark de modelos por tarefa de agente
## Pré-requisitos
Congelar dataset e acessos a ferramentas; definir expected output com teste determinístico, human rubric ou judge calibrado. Registrar versão do prompt/Skill, ferramentas, modelo, provider, sampling, hardware, temperatura, preços no dia e threshold de contexto.
## Indicadores
- `completion_rate`, `valid_output_rate`, `tool_call_accuracy`, `hallucination_rate`, `security_policy_violations`.
- `cost_per_success`, `cost_per_task`, `tokens_in/out`, `context_size`, `cache_hit_rate`.
- `latency_p50/p95`, `time_to_first_token`, `time_to_complete_task`, `retries`, `throughput`.
- `user_acceptance`, `manual_corrections`, `regressions`, `fallback_frequency`.
## Desenho
- Separar prompts básicos, difíceis, falhas e tarefas multimodais; incluir português e inglês quando exigido.
- Fazer no mínimo duas execuções por caso com seeds/temperatura controladas, aumentar em caso de alta variância.
- Para coding, validar diff, lint, build, testes e security checks; para RAG checar citações e abstenção.
- Em testes críticos, blind review humano com rubric e avaliação de erro extremo.
## Métrica de ranking
Filtrar primeiro candidatos inseguros, indisponíveis ou que não cumprem contrato. Dos restantes criar fronteira de Pareto (qualidade, custo, latência). Apresentar a incerteza; jamais reduzir tudo a uma pontuação arbitrária sem pesos documentados.
## Controle de custo
Usar casos curtos primeiro; estimar chamadas, tokens e custo antes de benchmark grande. Nunca disparar carga paga sem autorização. Referências externas são apenas evidência preliminar.
