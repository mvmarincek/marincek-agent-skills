# Mapeamento de fine-tuning: local, AWS, GCP e Azure

| Necessidade | Local/genérico | AWS | GCP | Azure |
|---|---|---|---|---|
| SFT/LoRA | HF Transformers + PEFT/Unsloth | SageMaker, Bedrock customization se suportado | Vertex AI tuning/custom training | Foundry fine-tuning ou Azure ML |
| DPO/preferência | TRL, dados par-a-par | verificar modelos/métodos suportados no Bedrock/SageMaker | custom training/método quando suportado | Foundry preference DPO conforme modelos/regiões |
| RFT/RL | TRL/RL pipelines especializados | custom training/SageMaker, Bedrock se suportado | custom training e tooling próprio | Foundry RFT se modelo suportado / Azure ML |
| Datasets | JSONL versionado, DVC/Git LFS | S3 + KMS | Cloud Storage + IAM | Blob + Key Vault |
| Experimentos | MLflow, W&B opcional | SageMaker Experiments / CloudWatch | Vertex experiments/metadata | Azure ML tracking/monitoring |
| Deployment | Ollama/vLLM/SGLang conforme modelo | endpoints SageMaker/Bedrock | Vertex endpoints/Cloud Run | Foundry endpoint/Azure ML |
| Permissões | RBAC/OPA | IAM | IAM | Entra/Managed Identity |

**Não são equivalências absolutas**. Suporte varia por método, família de modelo, região, conta e versão. Verifique preço, requisitos de GPU, dataset format, disponibilidade e termos. Proibir provisionamento automático pago sem aprovação.

## Links oficiais
https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html
https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models
https://learn.microsoft.com/en-us/azure/foundry/fine-tuning/overview
https://huggingface.co/docs/peft/
