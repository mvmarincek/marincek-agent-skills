---
name: llm-model-selection-benchmark
description: "Selecionar modelos de IA por agente e por aplicação com comparação atualizada de qualidade, tool calling, custo, contexto, latência, segurança e hardware local ou cloud."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "ai-agents"
---

# LLM Selection & Agent Benchmark Architect


## Quando ativar
Ao planejar sistema com um ou vários agentes, escolher modelos para coding, execução de ferramentas, visão, OCR, voz, RAG, classificação, roteamento, matemática, grandes contextos, agentes complexos, fine-tuning e inference local. Também ativar quando trocar modelo, sofrer regressões, restrições de custo ou necessidade de fallback.

## Regra fundamental
**Não selecionar LLM por rankings gerais ou nomes conhecidos sem medir a tarefa real.** Um benchmark da internet é evidência inicial, não validação para aquele aplicativo. Informações sobre preços, versões, contexto, privacidade e capacidades mudam: verificar documentação e fontes atuais no momento do projeto; registrar data/versão. Se sem rede, marcar dados como `stale/unverified` e exigir confirmação antes de contratação/implantação.

## Contrato de entrada
- Inventário de agentes e subagentes: responsabilidades, ferramentas MCP, nível de autonomia, frequência, payload de entrada/saída, modalidades, idioma, criticidade e SLA.
- Infra local (CPU, RAM, VRAM e SO), cloud/provider permitido, privacidade/localização de dados, orçamento por mês e por sucesso, disponibilidade, limitações de armazenamento e conectividade.
- Contexto necessário p50/p95, RAG, geração estruturada/JSON, tool calling, streaming, retries, tokens, paralelismo e custos de falha.
- Dataset de benchmark representativo com critérios objetivos e restrições éticas/legais. Sem pipeline real, criar baseline e declarar teste como pendente.

## Procedimento
1. **Decompor por capacidade**: quais agentes realmente precisam pensar, codificar, executar tools, ver imagens, planejar e julgar resultados? Evitar LLM para roteamento trivial quando regras determinísticas resolvem.
2. **Criar perfis de carga**: volume, prompts, formatos, tamanho de contexto, função de perda (erros x custo), ferramentas, limites de tempo, privacidade, por idioma; incluir paths críticos e edge cases.
3. **Pré-filtrar candidatos**: modelos com API/local e licenças adequadas, limitações de uso, compliance, suporte estruturado e hardware. Para local: usar llmfit/Ollama e medir VRAM, KV cache e throughput real.
4. **Consultas de mercado**: docs de provedor e benchmarks recentes (releases e datas); coletar snapshots versionados do preço, limites, latência e qualidades observadas; não declarar 'melhor absoluto'.
5. **Benchmark por trajetória**: para cada agente executar tarefas reais com mesmos inputs, ferramentas, acessos e ambiente. Medir resultado, validação determinística, chamadas corretas e comportamento em falhas; registrar tokens, throughput, p50/p95, custo e custo por tarefa concluída.
6. **Comparação multiobjetivo**: segurança e taxa de sucesso como limites; ranking entre elegíveis por qualidade, latência e custo; curva de Pareto, pesos documentados, incerteza e sensibilidade a volume.
7. **Arquitetura de roteamento**: local-first quando adequado, especialistas por modalidade, modelos pequenos para classificação/extração e modelo mais forte para planejamento difícil; fallback com orçamento e contexto/redaction. Ver `references/router-and-fallback.md`.
8. **Validação de sistema**: end-to-end com todos os agentes, handoff, memoria/RAG, tool calling, dados reais anonimizados/sintéticos, carga e segurança; evitar medir apenas respostas isoladas.
9. **Entrega**: tabela de decisão por agente, modelos elegíveis, testes reproduzíveis, custos mensais/por sucesso, políticas de fallback, riscos de lock-in e condições de revisão.
10. **Atualização periódica**: reavaliar quando sair versão relevante, preço mudar, regressão ocorrer ou métricas ultrapassarem threshold; benchmarks 'current' expiram.

## Matriz de seleção (não prescritiva)
- **Classificador/roteador simples**: regras, modelos pequenos e Laya/Jev quando validação local provar vantagem.
- **Agente coder**: medir implementações reais, edição de arquivos, uso de ferramentas, testes, repositório grande, recuperação de erro.
- **Agente visual**: avaliar OCR, grounding, reconhecimento de UI, resolução, PII redaction e latência.
- **Agente RAG**: embeddings e reranker escolhidos separadamente do gerador; medir recall@k, faithfulness, citations, abstention.
- **Decisão crítica**: política determinística + autorização e validação; LLM não é substituto de policy enforcement.
- **Agente multi-etapas**: estimar custo total de chamadas, context replay, retries e delegação; simular carga real.

## Infra e gateways
Local: Ollama, llama.cpp, vLLM quando GPU adequada, llmfit; inferência CPU/GPU com quantização validada, nunca prometer que modelo MoE cabe só pelos parâmetros ativos.
Genérico: OpenAI-compatible gateway, adaptadores por provedor, OTel traces, Redis opcional para quotas e rate limits, storage de avaliações.
AWS: Bedrock e modelos/self-host em SageMaker/ECS/EKS; GCP: Vertex AI/Agent Platform; Azure: Azure AI/Foundry/ML conforme catálogo vigente, com IAM e observabilidade.
LiteLLM para gateway/roteamento/fallback quando necessário: confirmar disponibilidade de drivers, limites, armazenamento de budgets e licenças. **Os budgets rígidos dependem de configuração do backend**, portanto custo crítico requer enforcement independente quando apropriado.

## Segurança e padrões de validação
Não transmitir prompts com PII a benchmarks públicos; dados de cliente protegidos; limitar saídas que executam ferramentas, validar JSON/schema e autorização; red team em sandbox para prompt injection e exfiltração. Modelos e provedores podem variar política de retenção. Obter aprovação para API paga, dados sensíveis ou recursos cloud.

## Referências progressivas
- `references/benchmark-protocol.md` — dataset, scores, análise estatística e reprodutibilidade.
- `references/router-and-fallback.md` — exemplos de topologia de agentes, roteamento e custo.
- `references/model-capability-matrix.md` — especialidades, requisitos e decisão por papel.
- `assets/model-decision-record.md` — matriz de decisão com data/snapshot.
- `assets/model-eval-case.json` — schema de teste com ground truth.

## Produtos
`AGENT_WORKLOAD_INVENTORY.md`, `MODEL_CANDIDATES.md`, `LLM_BENCHMARK_RESULTS.md`, `MODEL_ASSIGNMENT.md`, `ROUTING_POLICY.md`, `MODEL_COST_PROJECTION.md`, `ROLLBACK_POLICY.md` e evidências.

## Aceite
Modelos disponíveis e condições verificados na data, benchmark de tarefas representativas concluído com medidas; mínimo de qualidade/safety atingido; custo por sucesso e p95 observados; fallback testado; ambientes/dados protegidos; nenhum upgrade de produção ou cobrança sem aprovação. Se benchmarks não foram executados, relatório descreve hipóteses, não ranking validado.
