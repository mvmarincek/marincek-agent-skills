# Matriz de capacidades necessárias por função
| Agente | Capacidades mínimas | Teste decisivo |
|---|---|---|
| Planner | planejamento multi-passos, consistência, schema | plano executável sem tool call perigosa |
| Coder | diff, tool calling, testes, contexto de repo | bugfix em repo real com CI |
| Research | citações, web/tool use, síntese | fatos corretos e fontes auditáveis |
| RAG support | contexto, grounded citations, abstention | resposta a perguntas fora da base |
| Vision | grounding, OCR, resolução, latência | screenshots reais e mudança de layout |
| Data analysis | código/SQL seguro, estatística | queries e gráficos com ground truth |
| Decision | score/yes-no calibrados | precisão, recall, tempo de decisão |
| Safety validator | avaliar riscos sem falso positivo excessivo | corpus de ataques e pedidos legítimos |
## Local vs remoto
- Registrar CPU, GPU, VRAM, RAM, runtime, quantização, tamanho de contexto e KV cache; medir saturação real.
- MoE com parâmetros ativos pequenos pode ainda exigir muitos GB de pesos residentes.
- Remoto: custos por token não contam chamadas de ferramenta, retries, embeddings, storage e latência de rede.
## Reavaliação
Data de validade do benchmark; triggers de atualização: mudança do modelo, schema, preço, política de retenção, SDK e volume.
