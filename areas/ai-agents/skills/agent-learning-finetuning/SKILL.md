---
name: agent-learning-finetuning
description: "Selecionar, planejar e validar tecnicas de melhoria de agentes: prompting, RAG, memoria, Skills, DSPy, preference optimization, SFT, LoRA/QLoRA, DPO, RFT e distillation; local, generico, AWS, GCP, Azure."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "agent-architecture"
---

# Arquitetura de aprendizado e fine-tuning de agentes

## Quando usar
Quando o agente comete erros recorrentes, precisa aprender habilidades, especializar domínio/estilo, adaptar tool use, reduzir custo, ou o projeto pede fine-tuning. Comece medindo o problema antes de recomendar treino. Diferencie **melhorar o agente** de **treinar pesos do LLM**.

## Árvore de decisão prioritária
1. **Faltam fatos atuais, documentos ou conhecimento?** Usar RAG/SQL/APIs e citações.
2. **Faltam preferências, histórico, episódios ou continuidade?** Memória persistente, event store e mecanismos de recuperação.
3. **Falta procedimento repetível ou uso correto de ferramentas?** Skill e contratos de MCP, exemplos e validação externa.
4. **Falha por formulação, coordenação, roteamento ou exemplos?** Prompt engineering + avaliações, DSPy ou Harness² (se compatível, experimental).
5. **O modelo não segue estilo, formato ou domínio repetidamente apesar de exemplos, avaliadores e retrieval corretos?** Considerar SFT/LoRA/QLoRA com dataset suficiente.
6. **Qualidade depende de preferências entre duas respostas?** DPO/preference tuning quando suportado.
7. **Há avaliador/reward robusto e treino é economicamente viável?** Considerar RFT/RL somente com supervisão de engenharia especializada.
8. **Quer modelo pequeno imitar comportamento confiável de grande?** Destilação com dados licenciados/autorizados e validação independente.
9. Se o objetivo é melhorar trajetória/tool calling, avaliar se tuning dos pesos é realmente necessário ou se arquitetura/capability da ferramenta é a causa.

## Etapas obrigatórias antes de treinar
1. Inventário de tarefa: quem usa, impacto, dataset, privacidade, idioma, saída, limitações e custo atual.
2. Baseline congelada: versões do modelo, prompts, Skills, RAG, ferramentas, seeds se aplicável, latência e sucesso em tarefas reais.
3. Taxonomia de erros: factual, tool misuse, formato, reasoning, stale data, hallucination, segurança, handoff, latência e custo.
4. Hipóteses: listar 2–3 intervenções mais baratas e seus efeitos esperados.
5. Dataset: procedência, licenciamento, consentimento, dedupe, limpeza PII, balanceamento, split por entidade/tempo e teste cego; prevenir data leakage.
6. Escolher abordagem com `references/method-selection.md`, estimar tokens/VRAM/storage, licença e custos completos.
7. Executar **piloto pequeno** de baixo risco com baseline e controle. Sem treino automático contínuo direto em produção.
8. Avaliar: holdout, tarefas end-to-end com ferramentas, robustez, esquecimento catastrófico, regressões, segurança, custo/tarefa e performance por idioma/grupo relevante sem inferir atributos sensíveis.
9. Decisão go/no-go; criar model card, dataset card, versionamento, rollback e monitoramento drift.
10. Promover somente após aprovação e testes com usuários/dados compatíveis com política.

## Comparação de métodos
- **Prompt/Skill**: modifica instruções/fluxo; barato, reversível, ideal para procedimentos.
- **RAG/memória**: altera contexto de inferência, não pesos; ideal para fatos e preferências atualizáveis.
- **DSPy/Harness²**: otimiza prompts/programas/harness por avaliações; não é automaticamente fine-tuning do modelo; validar requisitos/licença de cada projeto.
- **SFT**: usa exemplos supervisionados; bom para formato/estilo/decisões demonstráveis, requer dados bem curados.
- **LoRA/QLoRA (PEFT)**: variantes eficientes para treinar adaptadores; dependem de arquitetura, quantização, VRAM e framework.
- **DPO**: preferências vencedora/perdedora; exige pares de comparação representativos, compatibilidade do modelo e controle de reward hacks.
- **RFT/RL**: recompensas/avaliadores robustos, ciclo de treino mais complexo e caro; risco de otimizar métrica errada.
- **Distillation**: usar professor para dataset/labels com autorização de termos e avaliar autonomia do aluno.
- **Treino completo**: evitar como padrão; alto custo, dados e engenharia.

## Requisitos hardware local (inclui 4 GB VRAM)
Na GTX 1650 de 4 GB: não afirmar que modelos 7B/8B ou 40B podem ser ajustados confortavelmente. Avaliar **mini modelos**, LoRA com configurações específicas, CPU offload, pouca sequência, batch reduzido e disponibilidade de RAM; pode ser inviável ou muito lento. Priorizar RAG, Skills e ajuste de prompts. `llmfit` indica inferência/adequação, não garante treino. Validar versões de CUDA, PyTorch, Unsloth, PEFT e arquitetura antes de recomendar qualquer comando. Nunca instalar CUDA/driver automaticamente sem consentimento.

## Escolhas por ambiente
- **Local**: datasets JSONL, Hugging Face datasets/Transformers + PEFT/TRl, Unsloth quando compatível, MLflow ou arquivos e tabela de experimentos; GPU/CPU conforme recursos.
- **Servidor genérico**: CUDA GPU sob demanda, containers reproduzíveis, storage de datasets/modelos, tracking MLflow e segurança, avaliação offline e deploy em canary.
- **AWS**: SageMaker Training/Experiments ou Bedrock model customization quando método/modelo/região suportados; CloudWatch, S3, IAM, KMS.
- **GCP**: Vertex AI tuning/training/pipelines quando disponível; Cloud Storage, IAM, Vertex Model Registry/observability.
- **Azure**: Microsoft Foundry fine-tuning ou Azure ML para controle; Blob Storage, Managed Identity/Key Vault e avaliações.
Detalhes mutáveis em `references/cloud-training.md`.

## Dataset mínimo de engenharia
`data_source`, `consent_scope`, `created_at`, `example_id`, `task_type`, `input`, `target_output`, `tool_trace` (mascarado), `quality_label`, `human_reviewed`, `model_version`, `split`, `license`, `retention`. Separar exemplos de treino/avaliação e manter provas de proveniência.

## Avaliação específica de agentes
Não basta melhorar perda do modelo. Medir `task_success_rate`, tool selection, execução correta, chamadas proibidas, taxa de revisão humana, custo por tarefa, precisão factual e generalização. Testes devem executar agente completo com seus tools e políticas, e casos adversariais; comportamento em um benchmark público não prova sucesso no domínio do usuário.

## Segurança e controle de aprendizado
- Não ingerir diretamente conversas pessoais em treinamento sem autorização, políticas de retenção e revisão de PII.
- Evitar self-training sobre saídas não verificadas (model collapse, amplificação de erro).
- Memórias e Skills propostas precisam de evidência/validação antes de promover.
- Versionar checkpoint/adaptador, tokenizer, dataset, prompt, skill, harness, eval e configs de inferência.
- Verificar direitos de uso dos dados e termos do provedor; não usar modelos fechados como professores se restrito.
- Nunca iniciar jobs pagos de treino sem estimativa e autorização expressa.

## Entregáveis
`ERROR_TAXONOMY.md`, `BASELINE.md`, `METHOD_DECISION.md`, `DATASET_CARD.md`, `EXPERIMENT_PLAN.md`, `EVAL_REPORT.md`, `MODEL_CARD.md`, `ROLLBACK_PLAN.md`. Seguir `assets/experiment-template.md`. Se não houver dados, entregar plano condicionado, não fingir treino concluído.
