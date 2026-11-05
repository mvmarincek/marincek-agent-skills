---
name: mcp-server-factory
description: "Projetar, implementar e testar servidores MCP (Model Context Protocol) para estender agentes com tools, resources e prompts: escolha de transporte stdio/HTTP, contratos com schema validado, segurança, observabilidade, testes com inspector e distribuição versionada."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "ai-agents"
---

# MCP Server Factory — Servidores MCP para Agentes

## Quando ativar
Quando o usuário pedir criação, extensão ou revisão de um servidor MCP (`Model Context Protocol`): `criar um servidor MCP`, `expor essa API como tool`, `adicionar tools ao meu agente`, `MCP server com resources`, ou quando uma integração precisar ser exposta a agentes de forma padronizada. Complementa `structured-agent-prompts` (que consome contratos MCP) e `skill-factory` (procedimento em SKILL.md); esta skill cobre o **lado servidor**.

## Definição operacional
Servidor MCP é o componente que expõe capacidades (tools executáveis, resources legíveis, prompts reutilizáveis) a clientes de agente por um contrato padronizado. Fábrica significa: capacidades delimitadas antes de codar, transporte escolhido por caso de uso, contratos com schema de entrada/saída validado, handlers com tratamento de erro explícito, suite de testes executável e distribuição versionada. Não é "wrapper HTTP genérico" nem exposição automática de funções sem contrato.

## Contrato de entrada
Lista de capacidades a expor (com entradas/saídas esperadas), alvo de consumo (qual cliente/agente), ambiente de execução (local stdio vs. remoto HTTP), requisitos de autenticação, limites de taxa/custo de operações subjacentes e política de dados (quais dados o servidor pode ler/expor).

## Pipeline obrigatório
1. **Delimitar capacidades**: enumerar tools, resources e prompts; cada tool com nome, descrição, schema de entrada e contrato de saída; cortar o que não tem consumidor definido.
2. **Escolher transporte**: `stdio` para uso local junto ao cliente; `HTTP` (Streamable HTTP) para remoto/multiusuário — critérios em `references/transport-security.md`.
3. **Desenhar contratos**: schema JSON para cada parâmetro com validação no servidor; erros tipados e mensagens acionáveis, conforme `references/tool-contract-design.md`.
4. **Implementar handlers**: validação de entrada antes de qualquer efeito colateral; timeouts; idempotência declarada por tool; nada de estado global mutável entre chamadas sem controle.
5. **Segurança**: autenticação para transporte remoto; princípio de menor privilégio nos acessos; segredos por variável de ambiente, nunca no contrato; rate limiting em operações custosas — detalhes em `references/transport-security.md`.
6. **Testar**: suite executável cobrindo contrato (schema válido/inválido), happy path, erro e timeout; verificação com MCP Inspector antes de integrar a cliente real, conforme `references/testing-distribution.md`.
7. **Distribuir**: empacotar com manifest e versão semântica; registrar changelog de contratos (breaking changes exigem major); documentar instalação por cliente alvo.

## Segurança e permissões
MCP fornece capacidades; o procedimento e a autorização vêm da skill e do usuário — **nenhum servidor MCP confere autorização por si**. Não expor tools destrutivas (delete, deploy, pagamento) sem gate de aprovação explícito no contrato. Não embutir credenciais em contratos, logs ou respostas. Operações custosas (LLM, APIs pagas) devem declarar custo estimado. Um servidor MCP de produção exige revisão de diff e aprovação, como qualquer código de integração.

## Referências e artefatos
- `references/tool-contract-design.md` — design de tools/resources/prompts com schema e erros.
- `references/transport-security.md` — stdio vs. HTTP, autenticação, menor privilégio, rate limiting.
- `references/testing-distribution.md` — suite de testes, MCP Inspector, versionamento e changelog de contratos.

## Critério de aceite
Capacidades delimitadas e justificadas; transporte escolhido com critério; todos os contratos com schema validado no servidor; suite de testes passando incluindo erros e timeouts; verificação no Inspector concluída; segredos fora do código e dos contratos; tools destrutivas com gate de aprovação; distribuição versionada com changelog de contratos.
