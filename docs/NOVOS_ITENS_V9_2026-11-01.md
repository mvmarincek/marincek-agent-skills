# Lote v9 — Verificação de fontes, design, agentes de código e direito brasileiro

**Data de verificação:** 2026-11-01  
**Ponto de partida:** v8.1.  
**Resultados:** 12 referências novas verificadas, 1 site em pendência, 3 processos de aplicação documentados. **Zero instalações, benchmarks ou modificações em repositórios externos.**

## Entradas confirmadas

| Recurso | Tipo certo | Utilidade | Observação |
|---|---|---|---|
| [Google Research Harness²](https://github.com/google-research/harness2) | Framework de pesquisa/harness recursivo | Melhorar componentes do ambiente dos agentes, com probes e comparação | Não é modelo LLM nem skill. Demo pede Linux + Python 3.12 + uv; integração e custos a validar |
| [Agent Client Protocol](https://agentclientprotocol.com/) | Protocolo agente de código ↔ cliente/IDE | Portabilidade de integração | ACP Agent Client ≠ ACP da IBM; MCP e A2A têm papéis diferentes |
| [getdesign.ai](https://getdesign.ai/) | Extensão/produto | Capturar elementos UI como código | Não está confirmado que produza DESIGN.md automaticamente; pode ser pago |
| [posts.design](https://posts.design/) | Galeria | Social posts e anúncios | Referência criativa, não skill |
| [loadmo.re](https://loadmo.re/) | Galeria | Mobile, 3D, sites imersivos | Priorizar GITFY |
| [recent.design](https://recent.design/) | Galeria | Tendências de UI, motion, branding | Referência visual |
| [60fps.design](https://60fps.design/) | Galeria de motion com seção MCP | Microinterações para interfaces game-like | Prioridade máxima para UX; validar MCP no projeto |
| [supahero.io](https://supahero.io/) | Galeria de hero sections | Landing pages | Site informa incorporação ao screensdesign |
| [navbar.gallery](https://www.navbar.gallery/) | Galeria | Navegação e menus | Para design de menus de GITFY/ISYMU |
| [cta.gallery](https://www.cta.gallery/) | Galeria | CTAs e componentes de conversão | Para landing pages e checkout |
| [llm-legislativo](https://github.com/BaruqueRodrigues/llm-legislativo) | Pesquisa + datasets + modelo pequeno | Pipeline de coleta, splitting por famílias, tokenização e treino de LLM | Não é modelo jurídico confiável para aconselhamento; contexto de 512 tokens descrito no README |
| [ctresb/leis](https://github.com/ctresb/leis) | Corpus legislativo Markdown | Fonte documental para RAG com citações | Cobertura variável, OCR, vigência e fontes oficiais exigem checagem |

## Site não consolidado

- **inspora.design:** URL enviada, mas inacessível nesta verificação. Mantida em `pendencias` sem declarar recursos ou licença como confirmados.

## Duas correções necessárias

1. A imagem do ACP apresenta **Agent Client Protocol**, cujo propósito é ligar clientes (por exemplo IDEs) e agentes de código. Não confundir com o antigo **Agent Communication Protocol** da IBM. O MCP disponibiliza ferramentas/recursos; o A2A é comunicação/delegação entre agentes independentes. Um orquestrador multi-agente sobre ACP exige adaptadores, autorização, isolamento e validação.
2. Os sítios de design são **referências visuais**, não skills instaladas. `getdesign.ai` copia código de elementos selecionados; a produção de um arquivo `DESIGN.md` global não foi confirmada. Observar licença e privacidade.

## Fontes consultadas

- https://github.com/google-research/harness2
- https://github.com/agentclientprotocol/agent-client-protocol
- https://github.com/BaruqueRodrigues/llm-legislativo
- https://github.com/ctresb/leis
- URLs dos sites da tabela acima.
