# Matriz de tecnologias: confiabilidade do agente

| Necessidade | Opção mínima | Open source especializado | Quando usar | Não usar quando |
|---|---|---|---|---|
| Tracing | JSON estruturado + IDs | OpenTelemetry + OpenInference | Vários modelos/tools e correlação de execuções | Apenas script isolado sem produção |
| UI para tracing e experimentos | Logs + SQL | Arize Phoenix | Depurar chamadas, inspecionar trajetórias, avaliar experimentos | A complexidade supera benefício |
| Observabilidade com prompt registry | Metadados em Git | Langfuse | Prompts versionados, analytics, datasets | Infrainfra extra não justificada |
| Autorização | Middleware no tool gateway | Open Policy Agent (OPA), Cedar | Múltiplos tenants, scopes, políticas revisáveis | Permissão simples já garantida por backend |
| Guardrails linguísticos | Validadores de esquema | NVIDIA NeMo Guardrails | Categorias de entradas/saídas e fluxo | Como único controle de execução real |
| Continuidade | Persistência de task state | LangGraph, filas/checkpoints | Trabalhos longos e aprovação humana | Agente stateless pequeno |
| Eval resposta | pytest/expectations | DeepEval | Testes automatizados de RAG, LLM e trajetória | Sem dataset nem critério objetivo |
| Red teaming de prompts | Casos adversariais manuais | Promptfoo | Matriz de provedores/prompts, ataques controlados | Sem isolamento dos ambientes |
| Custos | Agregação por tarefa | Langfuse/Phoenix + FinOps próprio | Modelos e ferramentas com custo variável | Atribuição de custo sem dados |

## Estratégia de escolha
A) Reaproveitar stack instalada. B) Definir 3 hipóteses mensuráveis. C) Comparar no mesmo dataset. D) Escolher a opção com menor manutenção que satisfaz o SLO. E) Registrar no ADR, inclusive alternativas rejeitadas. F) Rever depois de 30 dias de operação.

## Repositórios/documentação
- https://opentelemetry.io/docs/
- https://github.com/Arize-ai/openinference
- https://github.com/Arize-ai/phoenix
- https://github.com/langfuse/langfuse
- https://github.com/open-policy-agent/opa
- https://github.com/NVIDIA-NeMo/Guardrails
- https://github.com/langchain-ai/langgraph
- https://github.com/confident-ai/deepeval
- https://github.com/promptfoo/promptfoo

Todos requerem verificação de versões, licenças, manutenção, requisitos e disponibilidade antes de instalação.
