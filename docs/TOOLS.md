# Ferramentas da biblioteca — referência completa

Scripts offline em `scripts/`. Nenhum deles acessa rede (exceto `sync_upstream.py`, que clona fontes do catálogo sob demanda), instala dependências, cria recursos cloud ou executa código de Skills. Eles **não conferem autorização**: rotear/instalar uma Skill não significa permissão para executar o que ela descreve.

Requisitos: Python 3.10+ e Git. Todos rodam de qualquer OS a partir da raiz do repo.

---

## `validate.py` — integridade estrutural do catálogo

```powershell
python scripts/validate.py
```

O que checa (sem argumentos):
- `catalog/skills.json`: `count` bate com o número de entradas; ids e paths sem duplicata; slug kebab-case válido; path sem absolute/`..`.
- Consistência área/id/path: `areas/<area>/skills/<id>/SKILL.md` exato.
- `SKILL.md`: existe, tem frontmatter com `name` igual ao id, `description` preenchida, corpo não vazio.
- Referências locais (`references/`, `assets/`, `scripts/`) citadas no SKILL.md existem em disco.
- `catalog/external-sources.json`: URLs http(s) válidas e `integration: reference-only`.

Saída: `PASS structural checks; agent runtime NOT tested.` (exit 0) ou lista de `ERROR:` (exit 1). **Não testa runtime de agente** — é gate estrutural, roda no CI de todo PR.

---

## `skill_quality.py` — qualidade estática das Skills

```powershell
python scripts/skill_quality.py --all
python scripts/skill_quality.py --skill immersive-commerce-3d
```

8 checks por Skill: frontmatter presente; tamanho mínimo (850+ chars); seção de ativação; procedimento/etapas; validação/critérios; limites de segurança; entregáveis; diretório `references/` ou `assets/`. Saída JSON com score por Skill.

Exit 0 = todas passaram; exit 2 = alguma falhou. Aviso embutido no output: **revisão estática não prova segurança, execução ou uso correto por modelo**.

---

## `install.py` — instalação nos agentes

```powershell
# simular primeiro (mostra SKIP/BACKUP/INSTALL sem tocar em nada)
python scripts/install.py --scope global --targets codex claude verdent opencode --dry-run

# instalar todas as Skills globalmente
python scripts/install.py --scope global --targets codex claude verdent opencode

# instalar seleção
python scripts/install.py --scope global --targets verdent --skills code-review gh-cli

# instalar por projeto (em vez de global)
python scripts/install.py --scope project --project-path C:\dev\projeto --targets codex claude

# atualizar Skills já instaladas (backup automático antes de substituir)
python scripts/install.py --scope global --targets codex claude verdent opencode --skills photoreal-3d-assets --replace
```

Comportamento:
- **Targets** (nome exato): `codex`, `claude`, `verdent`, `opencode`.
- Pastas de destino por target — global (em `~`): `.agents/skills`, `.claude/skills`, `.verdent/skills`, `.config/opencode/skills`; project: `.agents/skills`, `.claude/skills`, `.verdent/skills`, `.opencode/skills` dentro de `--project-path`.
- Lê os caminhos do manifesto — **não copie `areas/` direto** para a raiz do cliente.
- Skill já existente: `SKIP` (nunca sobrescreve). Com `--replace`: renomeia a existente para `<slug>.backup-<timestamp>` e só então copia.
- Sem rede/credenciais. Não instala ferramentas, cloud nem modelos.
- Após instalar, **recarregue a sessão do agente** para ele descobrir as Skills.

---

## `route_skills.py` — descoberta heurística por tarefa

```powershell
python scripts/route_skills.py --task "landing page existente game 3D realista com mão pegando morango" --top 5
python scripts/route_skills.py --task "carro configurado 3D montando na fábrica MES ERP" --top 5
```

Ranking léxico offline: tokeniza a tarefa (sem acento, sem stopwords), pondera nome/description/frontmatter 4x mais que o corpo, e aplica bônus de intenção (ex.: e-commerce+3D → `immersive-commerce-3d`; sinais fortes de fábrica/MES/ERP/VIN → `made-to-order-manufacturing-twin`). Filtro por área com `--area`.

Saída JSON com `candidates` ordenados por score, cada um marcado `suggested-not-authorized`. **É sugestão de leitura, não permissão nem execução** — a decisão de acionar é do agente/humano com o contexto do projeto.

---

## `scaffold_skill.py` — rascunho de Skill nova

```powershell
python scripts/scaffold_skill.py --area games --slug meu-novo-fluxo --description "O que faz e quando ativar" --title "Título"
```

Cria `areas/<area>/skills/<slug>/SKILL.md` com template (Quando ativar / Entradas / Procedimento / Validação e segurança / Entregáveis, tudo `TODO`), pastas `references/` e `assets/`, e registra no catálogo como `status: experimental`, `verified: scaffold-only`, `version 0.1.0`. Valida kebab-case, área existente, slug não duplicado.

O rascunho **exige autoria substancial, avaliação e revisão** antes de virar Skill de verdade — o scaffold é só o esqueleto.

---

## `sync_upstream.py` — auditoria local de fontes externas

```powershell
python scripts/sync_upstream.py --list
python scripts/sync_upstream.py --name SpectRAG --clone
```

Lista as fontes de `catalog/external-sources.json` ou clona **uma** fonte exata em `.cache/upstream/` (ignorado pelo Git) para inspeção manual: clone raso (`--depth 1`), sem hooks, apenas URLs `github.com` raiz. Imprime commit e possíveis LICENSE/NOTICE encontrados na raiz.

**Nunca instala, executa, copia para `areas/` nem publica** código de terceiros. Fontes externas são referência; triagem de licença é manual e obrigatória antes de qualquer incorporação.

---

## `publish-private.ps1` — publicação única em repo privado (histórico)

```powershell
powershell -File scripts/publish-private.ps1
```

Fluxo de primeira publicação com confirmação explícita (digitar `PUBLISH-PRIVATE`): valida, `git init`, commit e cria repo privado via `gh`. Recusa rodar se já existe `.git` ou se o repo remoto já existe. **Obsoleto para o fluxo atual** — o repo oficial é público ([mvmarincek/marincek-agent-skills](https://github.com/mvmarincek/marincek-agent-skills)) e evoluções entram por branch + PR com CI. Mantido como registro.

---

## Pipeline de CI

`.github/workflows/validate.yml` roda em todo PR: `validate.py` + `skill_quality.py --all` + `python -m unittest discover -s tests`. PR só deve ser mergeado com os três verdes.

## O que as ferramentas NÃO fazem

| Não faz | Por quê |
|---|---|
| Testar runtime de agente | Gates são estruturais/estáticos por design |
| Conferir permissão/licença automaticamente | Decisão humana com o contexto do projeto |
| Instalar dependências, cloud, modelos | Skills são procedimento, não provisionamento |
| Sobrescrever instalações sem backup | `--replace` sempre gera `.backup-*` antes |
| Publicar em main direto | Fluxo é branch + PR + CI, sem autopublicação |
