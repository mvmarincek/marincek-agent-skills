# Métricas e gates

| Métrica | Fonte de verdade | Exemplo de gate |
|---|---|---|
| Ativação correta | Casos rotulados | >= limite definido pelo projeto |
| Tool-call validity | Schema de tool e logs | 100% dos contratos críticos |
| Sucesso de tarefa | Teste end-to-end independente | Meta por caso |
| Violação de escopo | Ferramentas/auditoria | 0 para ações críticas |
| Custo/latência | OTel/APM | Não regressão relevante |
| Recuperação | Simular tool timeout e erro | Fallback aprovado |
| Regressão | Baseline gravado | Nenhum teste crítico quebrado |

Pontuações estáticas são sinais fracos. Não substituir avaliações reais por LLM-as-judge sem calibragem humana. Regras de aprovação ficam em branch protection, codeowners e runtime, não só em texto.
