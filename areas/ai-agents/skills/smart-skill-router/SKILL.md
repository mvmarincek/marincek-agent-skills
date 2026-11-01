---
name: smart-skill-router
description: "Selecionar Skills relevantes por objetivo, domínio, dependências, risco, orçamento, disponibilidade local e características do agente; evitar carregar bibliotecas inteiras."
license: MIT
metadata:
  version: "2.0.0"
  language: "pt-BR"
  area: "ai-agents"
---

# Smart Skill Router — seleção justificável e mínima

## Ativação
Quando o usuário pedir que agente escolha conhecimentos/Skills/MCPs, quando o objetivo atravessa domínios ou quando há muitas Skills candidatas que competem por contexto. Este roteador recomenda, **não concede permissões**.

## Procedimento
1. Ler objetivo, área, deliverable, stack existente, sistema operativo, custo permitido e tipo de agente. Nunca selecionar skill apenas por semelhança lexical com um comando inseguro.
2. Consultar catálogo `catalog/skills.json` e descrições frontmatter; descobrir dependências reais e diferenças entre referências externas e skills instaladas.
3. Rejeitar candidatas incompatíveis (ambiente, requisitos, licença, ferramentas ausentes, acesso insuficiente, risco e custo).
4. Classificar relevância, especialização, maturidade, evidências de eficácia, consumo de contexto e dependências. Dar preferência à menor coleção que cobre o objetivo com qualidade. Evitar Skills que só duplicam fluxo.
5. Selecionar 1-3 Skills principais e referências estritamente necessárias; apresentar justificativas, pré-condições e o que fica excluído.
6. Fazer inspeção de segurança e autorização independente do ranking. Nunca instalar código de terceiros, pagar API ou habilitar MCP apenas por recomendação do roteador.
7. Registrar seleção, resultado, métricas e feedback para calibração futura do classificador. Não alterar automaticamente a Skill de produção.

## CLI offline opcional
No repositório usar `python scripts/route_skills.py --task "Criar landing page com experimentos" --area web-marketing --top 3`. A pontuação lexical serve apenas para descoberta inicial; exige revisão humana, não comprova qualidade semântica.

## Hierarquia quando objetivo contém várias competências
Orquestrador/Skill de área → especialistas por necessidade → tools MCP na menor permissão → validação independente. Documentar handoff e responsabilidades de cada Skill, sem construir time multiagente quando um agente basta.

## Cloud e hardware
Compatibilizar execução local com recursos reais (CPU/GPU/RAM/OS), modelos disponíveis, restrições de dados, custo de infra AWS/GCP/Azure; preferir opção comprovada e econômica em vez da mais complexa.

## Não fazer
Não assumir que arquivos MD são executores de ferramentas. Não tratar links externos como Skills instaladas. Não ler/ativar 100 SKILL.md no contexto inicial. Não usar ranking como autorização para executar pentest, movimentar fundos ou modificar produção.

Veja `references/router-contract.md` e `assets/selection-template.md`.

## Entregáveis
Relatório de seleção, justificativa, limites, MCPs necessários, custo e risco, checklist de permissão, plano de validação e evidência de execução quando houver.
