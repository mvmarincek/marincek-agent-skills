---
name: ml-lifecycle-validation
description: "Treinar, avaliar, testar, monitorar e versionar ML clássico, deep learning, séries temporais, visão, NLP e modelos generativos com MLOps local e cloud."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "machine-learning"
---

# ML Engineering & Validation — ciclo completo


## Quando ativar
Problemas de classificação, regressão, previsão temporal, recomendação/ranking, clusterização, anomalias, NLP, visão, speech, modelos multimodais, reinforcement learning ou LLM/embedding que precisem dataset, modelo, treino, avaliação, comparação, deploy e monitoramento. **Nem todo problema requer ML**: comparar baseline de regra estatística antes de treinar.

## Descoberta e contrato
Definir decisão do negócio e horizonte, população, fonte e licença dos dados, objetivo e custo de erro, tipo de tarefa, disponibilidade de labels, quantidade de dados, drift previsto, risco/fairness, LGPD, explicabilidade, restrições de dispositivo/VRAM, custo de treino/inferência, latency/SLA e periodicidade de retreino. Separar modo experimental de produção. Requisitar aprovações para dados pessoais e treinamento cloud pago.

## Processo obrigatório
1. **Formulação**: hipótese refutável, baseline não-ML, métrica primária ligada ao negócio e matriz de erros; evitar accuracy em classe desbalanceada.
2. **Dataset**: catálogo, origem, schema, qualidade, deduplicação, label policy, dados sintéticos marcados, consentimento, retenção, data lineage; definir train/validation/test *antes* de feature engineering.
3. **Split correto**: aleatório estratificado se IID, por grupo para sujeitos/clientes, temporal para forecasting, purged/time gap para evitar vazamento em mercados; holdout intocado até seleção final. Identificar target leakage, near-duplicates e features pós-evento.
4. **Exploração**: representatividade, outliers, correlação, missingness, segmentação, imbalance, drift temporal; EDA com gráficos e relatório que separa evidência de hipótese.
5. **Pré-processamento**: transformações fit somente no treino; pipelines reproduzíveis; versionamento de tokenizer, normalização e features; seed e determinismo quando possível.
6. **Modelos candidatos**: baseline linear/árvore, boosting, rede neural/transformer ou algoritmo especializado; métricas de qualidade+latência+RAM+GPU+explicabilidade; não escolher modelo grande sem evidência.
7. **Treino**: experimentos rastreados (parâmetros, dataset/hash, Git commit, métrica, artefatos, hardware), early stopping, validação cruzada apropriada, otimização limitada de hiperparâmetros.
8. **Avaliação**: métricas conforme modalidade, intervalos de confiança, performance por segmentos, robustez, calibração, custo de erro, out-of-distribution, ablação; teste de referência separado de treino.
9. **Validação científica**: repetir seeds e versões, comparar com baseline, reduzir data leakage, documentação de limitações, descrever ameaças à validade; revisão humana para aplicações de alto risco.
10. **Empacotamento**: versionar modelo, preprocessing, contrato de entrada, checkpoint e dependências; model card, dataset card, avaliação e rollback.
11. **Deploy controlado**: shadow, canary, A/B quando ético; verificar latência p50/p95, CPU/GPU, throughput, custo, compatibilidade e segurança.
12. **Operação**: data/concept drift, alertas, anotações de falhas, feedback humano, data quality, retrain candidato em sandbox; jamais retreinar/promover em produção sem avaliação + aprovação.

## Métricas por modalidade
- Classificação: precision/recall/F1, PR-AUC ou ROC-AUC, log loss, calibration/Brier, matriz de confusão, FPR/FNR por segmento.
- Regressão: MAE/RMSE/MAPE somente quando denominação apropriada; resíduos, intervalos e robustez a outliers.
- Forecast: backtesting walk-forward, MAE/MASE/sMAPE, previsão probabilística com cobertura de intervalo; proibir shuffle de futuro.
- Classificação/anomalias: precision@k, recall@alert-budget, false-alarm cost, latência de detecção; avaliação por regime.
- Ranking/recomendação: NDCG@k/MAP@k/Recall@k, cobertura/diversidade, e métricas online se houver exposição controlada.
- Visão/NLP/áudio: mAP/IoU, WER/CER, semantic metrics e revisão humana por tarefa.
- LLM/agent: execução real, tool-call success, grounding, alucinação, segurança, latência e custo por tarefa; usar `references/evaluation-playbooks.md`.

## Ferramental (opcional e justificado)
Local: Python, Pandas/Polars, scikit-learn, PyTorch, MLflow, Optuna, DVC quando justificado, Great Expectations/Pandera, evidently/equivalentes. GPU CUDA/DirectML/CPU conforme hardware.
AWS: SageMaker, S3, IAM, Step Functions/EventBridge, CloudWatch, ECS/Batch (confirmar versões/custos).
GCP: Vertex AI ou Agent Platform conforme oferta atual, Cloud Storage, BigQuery, Cloud Run, Cloud Logging.
Azure: Azure ML, Blob Storage, ACR/Container Apps/AKS, Monitor.
Infra genérica: Docker, Kubernetes apenas se justificado, MLflow tracking e registry, armazenamento de artefatos, OTel.

## Segurança, governança e ética
Sem dados de produção em prompts/serviços externos sem autorização; preservar segregação por tenant; proteger PII; checar consentimento, copyright, vieses e domain shift; revisão clínica/jurídica/financeira obrigatória quando aplicável. Não prometer causalidade em dados observacionais. Não revelar modelos experimentais como produção.

## Referências progressivas
- `references/problem-to-model.md` — seleção de família e diagnóstico de dataset.
- `references/evaluation-playbooks.md` — testes por modalidade e critérios objetivos.
- `references/mlops-and-cloud.md` — rastreamento, registry, pipelines e comparativo cloud.
- `references/retraining-and-monitoring.md` — drift, gates, replay, champion/challenger.
- `assets/experiment-card.md` — protocolo de experiência.

## Entregáveis
`ML_PROBLEM.md`, `DATASET_CARD.md`, `SPLIT_PROTOCOL.md`, `EXPERIMENT_LOG.md`, `EVALUATION_REPORT.md`, `MODEL_CARD.md`, `MODEL_DEPLOY_PLAN.md`, `DRIFT_POLICY.md` e evidências reprodutíveis. Produzir o conjunto pertinente.

## Critério de conclusão
Modelo treinado e avaliado com holdout correto; baseline superado por margem definida; runs, código e dados versionados; métricas/intervalos/segmentos documentados; teste de privacidade e robustez adequado; deploy real somente com autorização e monitoramento. Caso não tenha treinado, declarar planejamento e não modelo validado.
