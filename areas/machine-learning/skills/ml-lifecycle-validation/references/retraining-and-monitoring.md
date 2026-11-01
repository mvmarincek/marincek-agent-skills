# Monitoramento, aprendizado incremental e governança do modelo
## Telemetria
Amostragem e logs mínimos anonimizados de entradas/saídas; métricas de qualidade com labels atrasados; esquema, drift e distribuição; por segmento/versão; latência, custo e carga de CPU/GPU; feedback e incidentes.
## Diferenciar drift
- Data drift: mudou distribuição de entrada. Nem sempre exige retreino.
- Concept drift: mudou relação entrada→alvo. Exige labels ou sinal confiável.
- Label drift: mudou base rate; investigar antes de recalibrar.
- Prompt/context drift (LLM): processo de chamada mudou; exige evals de trajetória.
## Política de atualização
1. Abrir incidente/alerta e ligar a métricas.
2. Diagnosticar upstream/dataset/serving e validação.
3. Preparar candidato com dados novos autorizado; reproduzir baseline.
4. Avaliar champion x challenger com testes de regressão, segurança e impacto econômico.
5. Registrar modelo, revisão e aprovação.
6. Implantar canário ou shadow com rollback.
7. Observar estabilidade e remover candidato se degradar.
**Nunca retreinar na primeira evidência de desvio isolado.**
