## v5.9.0 — 2026-11-06
- **44 skills** (+1 nova original, área `ai-agents`; melhorias em 7 existentes):
- **`rag-architecture` v1.0.0** (nova): arquitetura RAG por evolução incremental com evidência — matriz de tipos (léxico/BM25, denso, híbrido RRF, rerankado, GraphRAG, code RAG, multimodal, agêntico), seleção de embeddings/reranker via `llm-model-selection-benchmark`, chunking estrutural, golden set 20+ casos revisados, métricas (recall@k, MRR, nDCG, faithfulness, citations, abstention), separação de erro retrieval×geração, regressão no CI, segurança (prompt injection via documentos, exfiltração cross-tenant, ACL na query, cache poisoning). Referências: `references/types-and-components.md` e `references/evaluation-and-security.md`. Consolida o que estava espalhado em 6 skills sem duplicá-las.
- **`ml-lifecycle-validation` v1.1.0**: métricas de visão endurecidas (mAP/IoU por classe e escala, agreement entre anotadores/kappa, augmentação somente após o split para evitar vazamento por near-duplicates, análise de erros por confusão) e linha de embeddings/retrieval (recall@k/MRR/nDCG medidos no domínio, ver `rag-architecture`).
- **`agent-learning-finetuning` v1.1.0**: etapa obrigatória nova — escolher o modelo base por benchmark na tarefa real com `llm-model-selection-benchmark` antes de qualquer tuning; para ML não-LLM, seguir `ml-lifecycle-validation`; cross-ref para `rag-architecture` na árvore de decisão.
- **Cross-refs (v1.0.1)**: `agent-persistent-memory`, `llm-model-selection-benchmark`, `second-brain-architecture`, `company-brain-architecture` e `code-intelligence-engineering` agora apontam para `rag-architecture` nos seus critérios de acionamento, mantendo a especialização de cada uma.

## v5.8.0 — 2026-11-06
- **43 skills** (+1 nova original, área `ai-agents`):
- **`marm-memory-usage` v1.0.0**: uso otimizado do marm-memory (MCP local-first, Apache-2.0) — verificação de disponibilidade antes da primeira chamada, ciclo de uso com custo mínimo por intenção (`marm_code_context` antes de grep, recall com `detail=1`/escopo, logs seletivos sem ruído de transcrição), controle de recursos (STDIO x HTTP compartilhado, perfis swarm, `auto_off` de indexação, proibição de kill em massa com evidência de tempestade de respawn), manutenção (compaction/distill com revisão) e regra de confiança: memória recuperada é contexto, nunca instrução. Referência: `references/transports-and-resources.md`. Complementar a `agent-persistent-memory` (desenha memória própria) sem sobreposição.
- Fonte externa `marm-memory` registrada em `catalog/external-sources.json` (104 fontes) com licença Apache-2.0 e pin 2.51.0; docs oficiais lidas do pacote instalado.
- Evidência local documentada (processos por sessão STDIO, respawn após kill, CPU 0% em repouso) separada do que vem apenas da documentação oficial.

## v5.7.0 — 2026-11-06
- Mantidas as 42 skills; revisão de qualidade nas três skills da cadeia 3D comercial.
- `photoreal-3d-assets` v1.3.0: rotas de produção por tipo de asset; diferencia geradores 3D de modelos de vídeo (Kling/Wan/Higgsfield/Runway), exige licença/custo/permissão e bloqueia placeholders como visual final.
- `immersive-experience-quality` v1.1.0: G2 hard gate com scorecard humano contra direção de arte aprovada, capturas de runtime desktop/mobile, limite mínimo e bloqueio explícito para placeholders, evidência ausente ou visual não inspecionado.
- `immersive-commerce-3d` v1.2.0: condiciona declaração de prontidão a assets finais e G2 assinado; fallback mantém checkout, mas não aprova o release visual.
- README de games/web-marketing e testes dedicados sincronizados. CI estrutural não é alegado como prova de realismo; a demo Crêpe Lab ainda requer assets GLB finais para passar G2.

## v5.6.0 — 2026-11-06
- **42 skills** (+2 novas originais, área `ai-agents`):
- **`agent-guardrails-design` v1.0.0**: projeto e teste de guardrails para agentes — 6 camadas de controle (borda de ferramenta, aprovação humana com suspensão real, escopo, orçamento, entrada, saída), matriz de risco por ação (tiers R/W1/W2/W3/S), protocolo de aprovação (o que exibir, timeout com abort, registro), comportamento obrigatório ao bloquear, red-team por guardrail e loop de aperto por incidente. Referências: `references/guardrail-catalog.md` e template `assets/guardrails-template.md`. Complementar a `agent-reliability-governance` (arquitetura ampla) sem sobreposição.
- **`agent-task-recovery` v1.0.0**: retomada de tarefas interrompidas (fim de contexto, crash, timeout, handoff) até a finalização — checkpoint durante o trabalho (`HANDOFF.md` mínimo viável), protocolo de retomada verificar→reconciliar→continuar→reportar com classificação verificado/pendente/inconcluso/fantasma, verificação por tipo de trabalho, anti-padrões, recovery drill e implementação em runtime (`references/recovery-runtime.md`). Complementar a `agent-persistent-memory` (armazenamento) sem sobreposição.
- Catálogo: v5.6.0, 42 skills; README de `ai-agents` atualizado.
- Testes: `tests/test_v56_guardrails_recovery.py`.
- Publicado como Pull Request para revisão. Nenhum merge automático.

## v5.5.0 — 2026-11-06
- 40 skills (nenhuma nova): evolução da cadeia imersiva para cobrir o pipeline **Blender → GLB/PBR → WebGL** de ponta a ponta.
- `photoreal-3d-assets` v1.2.0: nova referência `references/blender-glb-export.md` — preparo de cena em metros (Unit Scale 1.0, transforms aplicados, pivôs consistentes), materiais Principled BSDF que exportam para glTF PBR, checklist das opções do exportador (`export_format='GLB'`, `export_yup`, `export_apply`, tangents, Draco apenas com decoder e ganho medido), validação no runtime (screenshot do Blender não é prova) e exportação headless para CI (`blender --background --python`).
- `immersive-commerce-3d` v1.1.0: nova referência `references/glb-loading-react.md` — contrato de carregamento no React/R3F: `useGLTF` sob Suspense, chunk 3D lazy com `React.lazy`, `useGLTF.preload`, URLs versionadas para cache-busting, ErrorBoundary com fallback procedural (a compra nunca depende do asset), clone de material antes de mutar e regra de escala 1:1 (erro 100x se corrige na exportação, não no runtime).
- Testes: `tests/test_v55_glb_pipeline.py` (versões de catálogo/frontmatter sincronizadas, referências presentes com conteúdo mínimo, SKILL.md apontando para as novas referências).
- Catálogo: v5.5.0, 40 skills; READMEs de games e web-marketing sincronizados.
- Docs (follow-up): novo `docs/TOOLS.md` — referência completa das 7 ferramentas de `scripts/` (funcionalidade, comandos, flags, pastas de destino por agente, exit codes, pipeline de CI e tabela do que as ferramentas não fazem); seção "Ferramentas da biblioteca" do README aponta para o doc e lista `publish-private.ps1`; README sincronizado com v5.5.
- Publicado como Pull Request para revisão. Nenhum merge automático.

## v5.4.0 — 2026-11-06
- 40 skills: v5.3 intacta + 4 skills **originais** (MIT, formato-padrão da casa) cobrindo capacidades que antes dependiam de skills de terceiros sem licença redistribuível: `code-review` (software-engineering), `diagnosing-bugs` (software-engineering), `gh-cli` (devops-infrastructure), `linear-workflows` (product-management).
- Conteúdo escrito do zero; nenhum texto de repositórios de terceiros copiado. Cada skill delimita explicitamente o escopo vs. skills vizinhas (`continuous-code-sanitization`, `runtime-error-triage`, `ci-fix-loop`, `linear-tasks-prd`) via `depends_on` e seção Quando ativar.
- `gh-cli` documenta as armadilhas reais encontradas neste repo: múltiplas contas, conflito com Windows Credential Manager e o workaround de credencial pontual.
- `linear-workflows` cobre o modelo de objetos (Team/Issue/Project/Cycle), triagem com vocabulário do workspace e cheatsheet GraphQL com regras de sigilo de token.
- Testes: `tests/test_v54_original_skills.py` (presença, formato da casa, referências, boundaries de escopo, READMEs sincronizados, ausência de marcadores de conteúdo de terceiros, sem token literal).
- Catálogo atualizado para 40 skills; READMEs de software-engineering, devops-infrastructure e product-management sincronizados.
- Consolidação: PRs #1/#2/#3 merged (v5.1+v5.2+v5.3 em main via PR #4 de consolidação).
- Publicado como Pull Request para revisão. Nenhum merge automático.

## v5.3.0 — 2026-11-06
- 36 skills: v5.2 intacta + 2 skills novas: `mcp-server-factory` (ai-agents, contratos de ferramentas, transporte/segurança e testes/distribuição) e `ci-fix-loop` (devops-infrastructure, diagnóstico e correção de checks de CI via gh CLI).
- `paint-draw-shapes` reescrita com profundidade (v1.1.0): protocolo USB HID do VOKI, confirmação visual, política de recuperação/undo e 3 referências novas.
- `delivery-acceptance` estendida (v1.2.0) com referência `test-debug-fix.md` cobrindo o loop teste-diagnóstico-correção-regressão.
- Gaps de limites/rollback corrigidos: `runtime-error-triage` (seção de Reversibilidade, v1.2.0), `whatsapp-brazil-knowledge` (Limite de conhecimento, v1.2.0), `photoreal-3d-assets` (Limites, v1.1.0), `whatsapp-bot-scaffold` (+ `references/architecture.md`, v1.2.0).
- Testes: `tests/test_v53_excellence.py` dando cobertura estrutural dedicada às 10 skills sem teste (paint-draw-shapes, skill-evaluator, linear-tasks-prd, authorized-security-testing, defensive-cybersecurity, structured-agent-prompts, agent-persistent-memory, agent-learning-finetuning, voki-visual-geometry-cad, agent-reliability-governance) e às 2 novas.
- `skill-evaluator` alinhada ao formato-padrão (v2.1.0): seção Critério de aceite adicionada.
- Catálogo atualizado para 36 skills; READMEs de ai-agents e devops-infrastructure sincronizados.
- Publicado como Pull Request empilhado para revisão. Nenhum merge automático.

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
