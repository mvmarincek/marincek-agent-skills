# MVMarincek — Agent Skills Library v5.4

**Fonte portátil de conhecimento operacional**: Codex, Claude Code, Verdent e OpenCode; catálogo e Skills por áreas de engenharia, IA, segurança, DevOps, produto, marketing, games 3D imersivos e manufatura.

## Status verificado
- **40 Skills completas catalogadas**: 22 preservadas da v4 + 6 de imersão 3D (v5.1) + 6 de entrega essencial recriadas (v5.2) + 2 de excelência (v5.3) + 4 originais de colaboração (v5.4, MIT) — review de código, diagnóstico de bugs, gh CLI e Linear.
- Skills de terceiros **não** são copiadas nem redistribuídas; capacidades equivalentes foram recriadas como conteúdo original sob MIT.
- `gamified-landing-page` atualizada com cinema/3D, psicologia da atenção, instrumentação de cliques, seções, vídeos, gráficos e eventos de conversão.
- Áreas ativas: ai-agents, automation-hid, cybersecurity, devops-infrastructure, enterprise-knowledge, enterprise-systems, games, machine-learning, personal-knowledge, product-management, software-engineering, web-marketing, engineering-management.
- `catalog/external-sources.json` registra fontes; **não copiamos nem publicamos automaticamente repositórios de terceiros**.
- Inclui ferramentas offline para Scaffold, roteamento, validação e instalação, sem executar infraestrutura cloud.
- Pipeline CI próprio: `validate.py` + `skill_quality.py` + unittest em cada PR (`.github/workflows/validate.yml`).

## Estrutura
```
areas/
  ai-agents/skills/             # Skills de IA, roteamento, fábrica, avaliação, memória
  devops-infrastructure/skills/ # Terraform, Actions, Kubernetes, Swarm, AWS/GCP/Azure
  product-management/skills/    # Linear, tasks, PRDs MD/PDF
  web-marketing/skills/         # Landing cinematográfica + métricas
  cybersecurity/skills/
  automation-hid/skills/
  mechanical-engineering/       # Planejado
  civil-engineering/            # Planejado
  architecture/                 # Planejado
  electronics/                  # Planejado
  firmware/                     # Planejado
  games/skills/                  # GLB/PBR, interação física e qualidade de gameplay
catalog/skills.json
catalog/external-sources.json
scripts/
tests/
.github/workflows/validate.yml
```

## Instalar no Windows
Extraia o ZIP e no terminal PowerShell da pasta extraída:
```powershell
python .\scripts\validate.py
python -m unittest discover -s tests -v
python .\scripts\install.py --scope global --targets codex claude verdent opencode --dry-run
python .\scripts\install.py --scope global --targets codex claude verdent opencode
```
Instalar somente infra:
```powershell
python .\scripts\install.py --scope global --targets codex claude verdent --skills infrastructure-devops-architect
```
Instalar por projeto:
```powershell
python .\scripts\install.py --scope project --project-path C:\dev\projeto --targets codex claude verdent --skills infrastructure-devops-architect linear-tasks-prd
```
Use `--replace` somente após revisar backups e alterações locais. Sem rede/credenciais no instalador.

## Ferramentas da biblioteca
- `scripts/scaffold_skill.py`: cria rascunho sob área escolhida; precisa revisão.
- `scripts/route_skills.py`: descoberta heurística offline, **não equivale a permissão/execução**.
- `scripts/skill_quality.py`: validação estática de completude, **não comprova funcionalidade**.
- `scripts/validate.py`: catálogos, nomes, paths, links locais, fontes.
- `scripts/install.py`: cópia para pastas suportadas, sem instalar ferramentas/cloud.
- `scripts/sync_upstream.py`: clona fontes externas seletivamente em cache local ignorado, sem incorporá-las/publicá-las automaticamente.

## Segurança e versionamento
Repositório oficial: `https://github.com/mvmarincek/marincek-agent-skills` (público, branch `main`).

Configurar branch protection, CODEOWNERS, PRs e validação Actions conforme a política do projeto. Não incluir credenciais, client data, desenhos confidenciais ou procedimentos perigosos sem revisão.

Nota sobre os diretórios: as Skills canônicas estão separadas fisicamente por área; o instalador lê os caminhos do manifesto e copia cada pasta para o layout esperado pelo agente. NÃO copiar `areas/` diretamente para a raiz do cliente e esperar descoberta automática.


## Novidades v3.0 — cinco novas Skills detalhadas
| Skill | Área | Foco |
|---|---|---|
| `enterprise-crm-erp-integrations` | enterprise-systems | Salesforce, SAP, TOTVS, integrações, processos e governança de dados |
| `ml-lifecycle-validation` | machine-learning | classificação, regressão, forecasting, visão, NLP, RL, MLOps e avaliação |
| `continuous-code-sanitization` | software-engineering | limpeza segura de legado e quality gates contínuos no PR/CI |
| `llm-model-selection-benchmark` | ai-agents | seleção de LLM por papel, benchmark, custo por sucesso, fallback |
| `hybrid-it-squad-management` | engineering-management | gestão TI, squads humano–IA, FinOps, DORA e estratégia |

### Instalar as cinco novas Skills globalmente (PowerShell)
```powershell
python .\scripts\validate.py
python .\scripts\install.py --scope global --targets codex claude verdent opencode --dry-run --skills enterprise-crm-erp-integrations ml-lifecycle-validation continuous-code-sanitization llm-model-selection-benchmark hybrid-it-squad-management
python .\scripts\install.py --scope global --targets codex claude verdent opencode --skills enterprise-crm-erp-integrations ml-lifecycle-validation continuous-code-sanitization llm-model-selection-benchmark hybrid-it-squad-management
```

**Importante:** Skills não substituem credenciais/licenças de Salesforce/SAP/TOTVS nem atualizam modelos LLM automaticamente. Requisitos, versões, preços e permissões devem ser confirmados no ambiente real. Não cria recursos cloud, executa exames em produção nem instala ferramentas por padrão.


## Novidades v4.0 — cérebro empresarial, segundo cérebro e inteligência de código

| Skill | Área | Finalidade |
|---|---|---|
| `company-brain-architecture` | enterprise-knowledge | Fontes corporativas, ACL, decisões, RAG, ingestão e avaliação |
| `second-brain-architecture` | personal-knowledge | Contexto, notas/conversas autorizadas, memória, recuperação, revisão e exportação |
| `code-intelligence-engineering` | software-engineering | Tree-sitter/LSP/SCIP, símbolos, grafo de dependências, Code RAG e impacto de mudanças |

Três abordagens distintas: Company Brain compartilha **conhecimento institucional governado**, Second Brain mantém **memória pessoal e de agentes com privacidade**, e Code Intelligence entende a **estrutura verificável do código-fonte**.

### Instalar somente as novas (PowerShell)
```powershell
python .\scripts\validate.py
python -m unittest discover -s tests -v
python .\scripts\install.py --scope global --targets codex claude verdent opencode --dry-run --skills company-brain-architecture second-brain-architecture code-intelligence-engineering
python .\scripts\install.py --scope global --targets codex claude verdent opencode --skills company-brain-architecture second-brain-architecture code-intelligence-engineering
```

**Nota**: não inclui servidor/company brain/segundo cérebro implementado nem índice real de código. As Skills descrevem e guiam agentes para criar e validar essas soluções conforme o projeto. A execução de cada integração depende de credenciais, acesso a arquivos e aprovação.


## Novidades v5 — landing pages 3D jogáveis + produção real

| Skill | Área | Papel |
|---|---|---|
| `immersive-commerce-3d` | web-marketing | Líder para landing existente/nova com game 3D comercial funcional |
| `photoreal-3d-assets` | games | Assets GLB, iluminação PBR, escala, rig, textura, licença e LOD |
| `tactile-3d-interactions` | games | Mão/utensílio pega ingrediente, transporta, deposita e persiste no produto |
| `realworld-order-digital-twin` | enterprise-systems | Pedido pós-checkout, eventos de produção real e transmissão opcional autorizada |
| `immersive-experience-quality` | games | Gates visual, interação e conversão, e2e, performance e fallback |

Ver `docs/IMMERSIVE_COMMERCE_3D_V5.md` e `docs/CODEX_PROMPT_V5_3D.md`. Histórico completo de versões no `CHANGELOG.md`; a `main` remota está publicada na versão **5.4.0** (40 skills, CI verde).

### Validar e instalar somente v5
```powershell
python .\scripts\validate.py
python .\scripts\skill_quality.py --all
python -m unittest discover -s tests -v
python .\scripts\route_skills.py --task "landing page existente game 3D realista com mão pegando morango da bancada inox e colocando no crepe" --top 5
python .\scripts\install.py --scope global --targets codex --dry-run --skills immersive-commerce-3d photoreal-3d-assets tactile-3d-interactions realworld-order-digital-twin immersive-experience-quality gamified-landing-page smart-skill-router
python .\scripts\install.py --scope global --targets codex --replace --skills immersive-commerce-3d photoreal-3d-assets tactile-3d-interactions realworld-order-digital-twin immersive-experience-quality gamified-landing-page smart-skill-router
```

**Atenção:** `--replace` faz backup das instalações existentes antes da cópia. Revisar o diff e os backups. Este pacote **não** instala Blender, Three.js, Scenario MCP, licenças, GLBs, jogos ou integrações em produção; implementações e testes reais são executados no repositório da aplicação pelo agente.

## Evolução v5.1 — experiência 3D do pedido ao produto fabricado
**Não é um template de creperia**: permite aplicar em sites existentes e novas landings uma jornada 3D de configuração → compra → operação física → entrega, incluindo linhas de montagem automotiva e outras manufaturas sob encomenda. A skill nova `made-to-order-manufacturing-twin` conecta conceitos de catálogo/CPQ, PLM, ERP, MES, WMS e status da unidade física quando houver ID verificado. A interface exibe **animação ilustrativa da etapa** e a fonte/data real, sem alegar transmissão da unidade física sem suporte. Ver `docs/REALTIME_EXPERIENCE_COMMERCE_V51.md`, `docs/CODEX_PROMPT_V51_MANUFACTURING.md`.

Instalar apenas a skill industrial no Codex (PowerShell):
```powershell
python .\scripts\validate.py
python -m unittest discover -s tests -v
python .\scripts\install.py --scope global --targets codex --dry-run --skills made-to-order-manufacturing-twin
python .\scripts\install.py --scope global --targets codex --skills made-to-order-manufacturing-twin
```
Instalação acima copia instruções SKILL.md, **não conecta** fábrica, integrações, API nem cria modelos 3D. Verificar status remoto separadamente.
