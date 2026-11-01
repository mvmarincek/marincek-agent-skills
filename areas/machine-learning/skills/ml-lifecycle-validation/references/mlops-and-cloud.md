# MLOps e comparativo de execução
## Rastreio mínimo
Para cada run: `run_id`, `git_sha`, `dataset_version/hash`, `feature_code_version`, `seed`, `hyperparameters`, `metrics`, `duration`, `cpu/gpu`, `memory`, `cost`, `artifact_uri`, `approved_by`.
## Opções de stack
| Camada | Local | AWS | GCP | Azure |
|---|---|---|---|---|
| Experimento | MLflow + storage local | SageMaker/MLflow | Vertex AI/Agent Platform | Azure ML |
| Dataset/artifact | FS/S3-compatible | S3 | Cloud Storage | Blob Storage |
| Jobs | Python/Cron/Docker | Processing/Training/Batch | Custom Jobs/Pipelines | Jobs/Pipelines |
| Registry | MLflow Registry | SageMaker Registry | Model Registry | Azure ML Registry |
| Serving | FastAPI/ONNX | endpoints/ECS | endpoints/Cloud Run | endpoints/Container Apps |
| Monitor | OTel/Evidently | CloudWatch | Cloud Monitoring | Azure Monitor |
## Escolha por custo
Menor modelo adequado, cache, batch, escala até zero, spot só com checkpoint, dados na mesma região, ingestão incremental. Comparar custo *total de ciclo* incluindo etiquetagem, treinamento, avaliação, serving e manutenção.
## Políticas de deploy
Aprovação humana quando houver custo ou dados sensíveis; GitHub Actions OIDC preferencialmente; separar papéis; chaves no vault; audit log e retenção. `terraform apply` somente após review e autorização. Sem claim de training cloud realizado se só existe YAML.
## Referências
- https://www.mlflow.org/docs/latest/tracking/
- https://learn.microsoft.com/azure/machine-learning/concept-model-management-and-deployment
- https://docs.aws.amazon.com/sagemaker/
- https://cloud.google.com/vertex-ai/docs
