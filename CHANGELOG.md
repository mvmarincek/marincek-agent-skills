## v5.2.0 — 2026-11-05
- 34 skills: v5.1 intacta + 6 skills recreadas no formato-padrão da biblioteca a partir de versões instaladas apenas localmente (órfãs não versionadas): `delivery-acceptance`, `runtime-error-triage`, `database-blueprints`, `deploy-diagnosis`, `whatsapp-bot-scaffold`, `whatsapp-brazil-knowledge`.
- SKILL.md reescritos com frontmatter completo (license, area), Quando ativar, Contrato de entrada, Pipeline obrigatório, Segurança e permissões e Critério de aceite; referências `knowledge/` corrigidas para `references/`; template do bot movido para `assets/template/`.
- READMEs de área sincronizados com o catálogo (7 corrigidos: ai-agents, software-engineering, devops-infrastructure, web-marketing, engineering-management, machine-learning, enterprise-systems).
- Skills de terceiros (code-review, gh-cli, linear, diagnosing-bugs) NÃO copiadas: sem licença redistribuível verificada; permanecem fora do repo conforme política de triagem.
- Testes: `tests/test_v52_core_delivery.py` cobrindo presença, arquivos de referência, estrutura do template e ausência de credenciais.
- Publicado como Pull Request empilhado para revisão. Nenhum merge automático.

## v5.1.0 — 2026-11-01
- 28 skills: biblioteca v4 intacta com 22 + 5 skills v5 (games 3D comerciais) + 1 skill `made-to-order-manufacturing-twin` para automóveis/móveis/equipamentos de fabricação sob encomenda.
- Generaliza jornada: configuração 3D, aprovação, checkout, operação comprovada, assembly milestones, expedição e entrega, com categorias de evidência.
- Roteador reconhece manufatura automotiva e linha de produção; tests + docs de integração MES/ERP/PLM.
- Publicado como Pull Request para revisão em `feat/immersive-3d-realtime-commerce-v5-1`. Nenhum deploy automático.

# v5.0.0 — 2026-11-01

- Cinco novas Agent Skills originais: `immersive-commerce-3d`, `photoreal-3d-assets`, `tactile-3d-interactions`, `realworld-order-digital-twin`, `immersive-experience-quality`.
- Atualizadas `gamified-landing-page` e `smart-skill-router` para reconhecer jogo 3D realista como implementação interativa, não mero efeito de marketing.
- Contrato de integração para sites existentes/novos e UX de checkout com feature flag.
- Separação de simulação de preparo e status real de cozinha (backend/KDS/POS), stream opcional autorizado.
- Novos casos de teste de roteamento, fixtures de aceitação, fontes externas somente como referência.
- A publicação remota GitHub não foi executada nesta geração; arquivos preservam todo o conteúdo da v4 original.

# v4.0.0 — 2026-11-01

- Adicionadas 3 Skills: Company Brain, Second Brain e Code Intelligence.
- Incluídos contratos de origem, ACL, rastreabilidade, freshness, metas e testes.
- Referências para local/AWS/GCP/Azure e critérios de custo.
- Preservadas todas as 19 Skills da versão anterior e componentes de instalação/validação.
- Nenhum repositório externo clonado; nenhuma nuvem ou aplicação instalada.

# Changelog

## v3.0.0 — 2026-11-01
- Cinco novas Skills detalhadas: CRM/ERP enterprise, ML/MLOps, sanitização contínua de código, seleção de modelos LLM, gestão TI com squads híbridos.
- Quatro novas áreas; área de IA agentes expandida.
- Guias profundos separados por fornecedor, tipo de teste e modalidade, modelos editáveis e links de documentação oficial.
- Metadados de instalações permanecem `installed:false` e `verified:structure-only` até serem testados no cliente.
- Não publicado automaticamente no GitHub; bibliotecas comerciais exigem licença e credenciais próprias.

# Changelog

## v2.0.0 — 2026-11-01
- Migradas Skills canônicas para `areas/<area>/skills/<slug>` mantendo slugs e conteúdos prévios.
- Adicionadas Skill Factory, Skill Evaluator, Smart Skill Router, Linear Tasks + PRD MD/PDF, Infrastructure & DevOps Architect.
- Evoluída gamified-landing-page com storytelling cinematográfico, evento de clique, navegação, vídeo e CTA, psicologia da atenção e avaliação de conversão consentida.
- Adicionados scripts offline de scaffolding, roteamento e auditoria estática; testes unittest; CI atualizado para layout por área.
- Áreas futuras planejadas para mecânica, civil, arquitetura, eletrônica, firmware e games.
- Preservadas referências externas em catálogo com integração `reference-only` e política de propriedade intelectual.
- **Não houve publicação GitHub nem implantação em qualquer cloud.**
