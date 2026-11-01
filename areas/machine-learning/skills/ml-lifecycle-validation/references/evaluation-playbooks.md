# Protocolos de avaliação reproduzível
## Padrão experimental
- Hipótese; métrica primária; split com IDs e hash; baseline; experiment IDs; intervalo de confiança; limiar de promoção definido antes do treino.
- Nunca ajustar hiperparâmetro olhando holdout de teste repetidas vezes. Para tuning, usar CV/split de validação.
- Calibração e threshold devem ser ajustados no conjunto adequado; avaliar fairness, robustez, slices e custo de erro.
## Checklist modalidades
**Tabular:** missingness, raros, leakage, grupo, calibration, sensitivity.
**Forecast:** rolling-origin backtest, regime shift, horizon-specific accuracy, holiday leakage.
**Vision:** annotator agreement, class-specific IoU/mAP, blurry/dark/occluded slices.
**NLP:** multilíngue, tamanho, domínio, ambiguidade, referências, PII.
**Anomalias:** alert budget, precision@k, lead time, overhead operacional.
**Recomendação:** cold start, cobertura, concentração, novelty, propensity de exposição.
**LLM:** dataset de tarefas reais, ferramentas, taxa de conclusão, custo por sucesso, segurança, repetibilidade, alucinação e abstenção.
**RL:** múltiplas seeds, recompensa hackeável, políticas de segurança, simulação→real e limites físicos.
## Entregar
Relatório com baseline e candidato, média ± variação, intervalos, erros típicos, riscos, decisão e logs de evidência. Falha no holdout significa não promover.
