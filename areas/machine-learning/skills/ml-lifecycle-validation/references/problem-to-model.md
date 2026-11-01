# Seleção ML: dados, objetivo e algoritmo
## Antes de treinar
Descrever problema, variável alvo, avaliação futura, baseline heurístico, custo de falsos positivos/negativos, exigências de explicabilidade, modalidade, hardware, fonte do dado e tamanho efetivo.
## Matriz de famílias
| Problema | Baseline | Candidatos | Alertas |
|---|---|---|---|
| Tabular classificação | logistic regression | random forest, boosting, MLP | imbalance, leakage |
| Tabular regressão | mediana/linear | RF, boosting, MLP | caudas, escalas, drift |
| Séries temporais | naive sazonal | ETS/ARIMA, boosting, TFT | futuro no treino, backtest |
| Visão | features+linear | CNN, ViT, DETR/segmentação | augment no split errado |
| NLP | TF-IDF+linear | encoder, fine-tuned transformers | leakage por documento |
| Recomendação | popularidade | matrix factorization, dual encoder | exposição/feedback bias |
| Fraude/anomalia | thresholds | IsolationForest, supervised, autoencoder | rótulos atrasados |
| GenAI/LLM | RAG/prompt base | SFT/LoRA/DPO quando comprovado | avaliação com humanos |
| RL | regras ou planejamento | PPO/algoritmos específicos | simulador, reward hacking |
## Datasets
- Separação por entidade/tempo, classificação de PII, datas de corte, snapshot identificável, versão de labels, checks de schema, missing values, duplicações e representação de segmentos.
- Consentimento e retenção específicos de treino; filtrar material proibido e acessos não autorizados.
## Resultado mínimo
Tabela de modelos candidatos e justificativas; custo de treino/inferência; definição de experimentos e decisão Go/No-Go.
