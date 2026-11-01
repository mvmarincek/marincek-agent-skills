# Agentes de programação — Harness², ACP, MCP, A2A e testes

## Classificação correta

| Camada | Padrão/recurso | Responsabilidade |
|---|---|---|
| Cliente IDE ↔ agente de código | **ACP — Agent Client Protocol** (`agentclientprotocol.com`) | Sessões e intercâmbio entre o front/IDE e um agente que implementa o protocolo |
| Agente ↔ ferramentas/dados | **MCP** | Tools, resources, prompts; escopos e autorização |
| Agente ↔ outros agentes remotos | **A2A** | Descoberta, delegação de tarefas e comunicação assíncrona |
| Melhoria de execução | **Harness²** | Propose–Probe–Compose em prompts, skills, políticas, memória, subagentes, scripts e plugins |
| Trabalho/código | Codex, Claude Code, OpenCode e outros | Alterações de projeto, testes e revisões em worktrees isoladas |

**Evite confusão:** ACP da IBM (Agent Communication Protocol) é um projeto histórico diferente de Agent Client Protocol. A fotografia recebida ilustra uma POSSÍVEL arquitetura, não compatibilidade garantida com todas as CLIs.

## Fatos concretos do Harness²

O repositório do Google Research chama-se `google-research/harness2`. Seu README descreve dois níveis de recursão: (1) por tarefa, refinar o harness comparando execuções; (2) atualização persistente do harness de melhoria para tarefas futuras. Pesos de modelo permanecem fixos.

- A demo local sem credenciais de modelo é documentada para **Linux, Python 3.12 e uv**.
- Executores documentados: **Codex e OpenCode**. **Claude Code e Verdent não estão automaticamente integrados**.
- Experimentos com LLM, benchmarks e execução no Windows exigem análise de dependências, adaptação e avaliação de custo.

## Fluxo recomendado para testar sem comprometer projetos

1. Extrair uma tarefa pequena e repetível de um repositório de demonstração, com testes.
2. Executar baseline do agente atual; guardar tokens, tempo, diffs, erros, métricas e taxa de aprovação.
3. Montar um worktree isolado, sem credenciais de produção e com permissão mínima.
4. Propor alterações pequenas em `AGENTS.md`, `CLAUDE.md`, definição de tools, roteamento e instruções.
5. Executar probes em entradas equivalentes. Não confiar em uma execução isolada.
6. Usar testes, análise estática, regressão, segurança e custo para decidir adoção.
7. Registrar versão do harness, resultado, rollback e aprovações humanas.

## VOKI: restrição inegociável

O VOKI utiliza exclusivamente **hardware USB HID** para ações de interface (mouse, teclado, arrastar). Pode consumir resultados do harness, mas não deve habilitar Playwright, Selenium, PyAutoGUI ou outro executor de UI por software para mover/clicar/teclar no ambiente alvo.

## Fontes

- https://github.com/google-research/harness2
- https://agentclientprotocol.com/
- https://github.com/agentclientprotocol/agent-client-protocol
