# MVMarincek — Agent Skills Library v4.0

**Fonte portátil de conhecimento operacional**: Codex, Claude Code, Verdent e OpenCode; catálogo e Skills por áreas de engenharia, IA, segurança, DevOps, produto e marketing. **Preparado localmente, ainda não publicado no GitHub.**

## Status verificado
- 22 Skills completas catalogadas; 3 novas neste pacote, além das 19 anteriores.
- `gamified-landing-page` atualizada com cinema/3D, psicologia da atenção, instrumentação de cliques, seções, vídeos, gráficos e eventos de conversão.
- Novas áreas ativas: enterprise-systems, machine-learning, software-engineering, engineering-management. Áreas futuras para mecânica, civil, arquitetura, eletrônica, firmware e games sem afirmar implementações inexistentes.
- `catalog/external-sources.json` registra fontes; **não copiamos nem publicamos automaticamente repositórios de terceiros**.
- Inclui ferramentas offline para Scaffold, roteamento, validação e instalação, sem executar infraestrutura cloud.

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
  games/                        # Planejado
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
Repositório GitHub recomendado: **privado**, como `mvmarincek/agent-skills`. O repositório ainda precisa ser criado e publicado manualmente ou por ferramenta GitHub com permissão. Configurar branch protection, CODEOWNERS, PRs e validação Actions. Não incluir credenciais, client data, desenhos confidenciais ou procedimentos perigosos sem revisão.

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
