---
name: structured-agent-prompts
description: "Criar, revisar e otimizar prompts estruturados para agentes simples, multiagentes, agentes hierarquicos e subagentes; definir papeis, contratos MCP, contexto, handoff, seguranca, formatos de saida, testes e cloud/local."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "agent-architecture"
---

# Engenharia de prompts profissionais para agentes e subagentes

## Quando usar
Quando pedirem prompt de agente, system/developer instructions, projeto de agente, subagentes, workflow, prompts de ferramentas MCP, roteamento, agentes por função ou avaliação/refatoração de prompts existentes. Não confundir prompt de tarefa com política de autorização: tool gateway deve aplicar segurança em runtime.

## Objetivo
Gerar instruções precisas, compactas e testáveis, que otimizem confiabilidade e eficiência, sem inflar contexto, inventar tools disponíveis ou criar conflitos entre agentes.

## Fluxo de engenharia
1. Classificar arquitetura: **agente simples**, **agente com ferramentas**, **subagente especialista**, **orquestrador multiagente**, **pipeline com checkpoints** ou **sistema de decisão**.
2. Extrair objetivo, atores, entradas, saídas, definições de sucesso, evidências, nível de autonomia, risco, escopo, orçamento e ambiente.
3. Inventariar **tools realmente existentes** e seus esquemas; sem ferramentas disponíveis, instruir a não fingir execução. Separar MCP de Skills e RAG.
4. Especificar contrato de responsabilidade: o que o agente pode fazer, o que não pode, o que deve delegar, quem aprova, o que acontece se ferramenta falhar.
5. Construir prompt em blocos: identidade/objetivo → contexto disponível → políticas → método → ferramentas → validação → formato de saída → tratamento de incerteza/falhas → conclusão.
6. Para multiagentes, especificar **topologia e handoff**: planner/worker/critic/router só se houver ganho justificável; estabelecer mensagens JSON tipadas, limites de iteração/profundidade, TTL, shared memory scopes e idempotência.
7. Carregar conhecimento incrementalmente: política permanente curta; Skills para procedimentos; RAG para fatos; memória para histórico; prompt da tarefa para objetivo atual. Não duplicar conteúdo.
8. Criar suíte de avaliações: tarefa normal, fora de escopo, ambiguidade, ferramenta indisponível, prompt injection, dados sensíveis, orçamento excedido, conflitos de instrução, validação falha.
9. Iterar com exemplos e resultados observados, não por preferência estética. Registrar `prompt_version`, compatibilidade do modelo, mudanças e regressões.
10. Entregar: prompts finalizados + contratos + exemplos de mensagens + testes + instruções de uso, em arquivos editáveis e versionáveis.

## Template obrigatório do agente
- `Role`: responsabilidade verificável, não persona vaga.
- `Goal`: 1–3 metas testáveis.
- `Scope`: operações permitidas e limites.
- `Inputs`: esquema, origem e confiabilidade; validar dados de tools/RAG.
- `Available tools`: somente nomes e descrições existentes.
- `Workflow`: etapas com pré e pós-condições, planos alternativos e paradas.
- `Decision policy`: quando agir, perguntar, delegar ou parar.
- `Memory/Skills`: o que recuperar, consultar, registrar e nunca reter.
- `Security`: minimização de dados, allowlist, aprovações e validações fora do LLM.
- `Output schema`: formato exato e exemplos válidos; não prometer tool calls não ocorridas.
- `Success criteria`: como provar sucesso e como reportar limitações.

## Multiagente / subagentes
- Orquestrador é responsável pela tarefa e pela validação final. Workers recebem somente subtarefa e contexto mínimo; retornam resultados estruturados + evidências + incerteza, nunca "completo" sem testes.
- Delegação precisa carregar `task_id`, `parent_task_id`, `agent_id`, `objective`, `scope`, `allowed_tools`, `input_refs`, `output_contract`, `max_steps`, `max_cost`, `deadline`, `retry_policy`, `return_to`.
- Impor: profundidade máxima, orçamento total de tokens/custos, limite de paralelismo, idempotência, timeout e regra anti-loop.
- O Critic/Reviewer NÃO deve aprovar sozinho ações críticas; revisão independente e policy gateway para recursos externos.
- Em handoff, não passar a conversa inteira por padrão: enviar resumo factual e links/refs válidos, preservando isolamento entre tenants.
- Roteador classifica intenção e capacidade, nunca distribui por status superficial. Testar cross-routing.

## Comportamentos a evitar
- Instruções repetidas ou contraditórias; promessas de acesso a ferramentas ausentes; obrigações impossíveis; pensamento interno solicitado; exigir respostas longas por padrão; converter dados externos em instruções; "sempre faça X" sem exceções de risco; persona de autopreservação; segredos em prompts.
- Prompt de "autonomia total" não substitui políticas de execução, credenciais de escopo mínimo e aprovações.
- Nunca usar exemplos sem identificar que são exemplos; não declarar cloud deployed se apenas configurado.

## Seleção de mecanismo
- **Prompt**: pedido atual, estratégia mínima e formatos.
- **Skill**: procedimento recorrente, especialização, scripts, referências.
- **MCP tool**: ação e consulta estruturada, permissões.
- **Memória**: histórico/perfil com proveniência; não instruction override.
- **RAG**: informação atualizada/documentos citáveis.
- **Workflow engine**: checkpoints, retries, filas, aprovações.
- **Fine-tuning**: só quando avaliações provarem lacuna persistente que instruções/dados não resolvem.

## Compatibilidade local / AWS / GCP / Azure
A engenharia de prompt é portável. Adaptar schemas e tool calling conforme runtime de cada agente. Para execução de produção, referenciar `references/cloud-adapters.md`; evitar colocar no prompt IAM/secret keys e infraestrutura específica sem necessidade. Manter versão do prompt em Git com metadados de modelo e dataset.

## Critérios de qualidade
Pontuar 0–5: objetivo mensurável, escopo, contratos, identidade e permissões, evidências, recuperação de falhas, contexto e memória, orçamento, handoff, output, testes, privacidade. Soma máxima 55. Falha automática se não respeita ferramentas disponíveis, propõe ações proibidas ou inventa evidência. Consulte `references/prompt-rubric.md`.

## Arquivos de referência
`assets/single-agent-template.md`, `assets/multiagent-template.md`, `assets/subagent-contract.json`, `references/prompt-rubric.md`, `references/cloud-adapters.md`, `references/examples.md`. Para redigir use esses modelos sem copiar texto demais para a janela ativa.
