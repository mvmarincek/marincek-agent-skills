---
name: code-intelligence-engineering
description: "Implementar inteligência de código e Code RAG: mapa de repositório, Tree-sitter, LSP/SCIP, símbolos, dependências, impacto de mudanças, índice por commit, busca híbrida e avaliação."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "software-engineering"
---


# Code Intelligence — compreensão estrutural de repositórios e evolução do código

## Quando usar
Acione para **code intelligence, inteligência de código, mapa de repositório, análise de dependências, compreensão de arquitetura, navegação de símbolos, impacto de mudança, knowledge graph de código, code RAG, documentação viva, onboarding de devs, análise de PR, arquitetura entre serviços ou agentes com contexto confiável de código**. Não substitui SAST/DAST ou code review; combine com `continuous-code-sanitization` e `defensive-cybersecurity`.

## Definição de sucesso
O agente deve encontrar **a implementação real**, suas dependências e referências, documentar o impacto da alteração com provas (`path:line` + commit), sugerir testes e atualizar apenas índices afetados pela mudança. Não deve responder baseado apenas em resumos genéricos de código.

## Descoberta do repo antes de qualquer índice
1. Obter caminho/repo/ref e permissão; nunca assumir que a branch atual é produção.
2. Inventariar linguagens, monorepo, pacotes, serviços, frameworks, builds, testes, CI e documentação. Respeitar `.gitignore`, segredos e arquivos gerados.
3. Identificar tarefas prioritárias: onde está a regra X? que rota usa o schema Y? qual serviço chama API Z? qual teste cobre função K?
4. Observar limites de CPU/RAM/GPU, tamanho, velocidade de checkout e custo da indexação.
5. Elaborar relatório `CODEBASE_DISCOVERY.md`, baseline de busca e critérios de sucesso.

## Modelo de conhecimento multicamada
| Camada | Exemplo | Fonte de verdade |
|---|---|---|
| Git/metadata | branch, commit SHA, autor, PR, diff | Git e host autorizado |
| Estrutura | arquivos, módulos, pacotes, manifests | sistema de arquivos + linguagens |
| Símbolos | classes, funções, métodos, endpoints | AST/Tree-sitter e LSP/SCIP |
| Relações | imports, chamadas, implementações, dependências | indexadores precisos; marcar inferências |
| Execução | testes, coverage, traces, logs | pipeline e ambiente controlado |
| Semântica | propósito, ADRs, README, contratos e comentários | docs + código citados |
| Segurança | achados SAST, auth boundaries, SBOM | scanners especializados com evidência |

## Pipeline recomendado
`discover repo/ref → filtros de escopo → índice arquivos/hash → AST/LSP/SCIP → símbolos/referências → grafo e busca textual → chunks de código semanticamente delimitados → embeddings opcionais → consulta por tarefa → evidências line-accurate → análise de impacto → testes → reindex incremental`.

### Fase A — baseline barato antes da IA
1. `git ls-files`, `git status`, manifests e lockfiles; arquivos excluídos não devem ser enviados a embeddings.
2. Criar índice por caminho, extensão, tamanho, hash e commit; busca lexical e regex (`rg` quando disponível).
3. Extrair árvore de pacotes, serviços, imports e arquivos de configuração; detectar monorepos/múltiplas linguagens.
4. Incluir `.md`, ADRs, testes e schemas de APIs como pistas, sem tratá-los como implementação comprovada.

### Fase B — indexação de precisão
1. Usar **LSP** nativo para definições, referências e tipos quando disponível; **SCIP** para navegação precisa persistida, se um indexador suportado existir.
2. Usar **Tree-sitter** para parsing robusto e incremental em linguagens diversas; AST Python nativa como fallback limitado a Python.
3. Extrair símbolos com: `symbol_id`, `qualified_name`, `kind`, `file_path`, `start_line`, `end_line`, `repo`, `commit_sha`, `language`, `visibility`.
4. Relações: `DEFINES`, `IMPORTS`, `CALLS`, `IMPLEMENTS`, `USES`, `TESTS`, `EXPOSES_ROUTE`, `DEPENDS_ON`; marcar origem e confiança. Calls dinâmicas/reflexão podem não ser resolvíveis estaticamente.
5. Armazenar estruturas sem perder versão/branch; índice de main pode divergir de worktree atual.

### Fase C — code RAG orientado a pergunta
1. Primeiro filtrar repo, branch, ACL, linguagem e pacote; recuperar candidatos por símbolo/FTS/caminho; adicionar vetor apenas após avaliar melhoria.
2. Recuperar **código relacionado** (função/chamador/chamado/teste/schema) sem estourar o contexto; re-rank com sinal estrutural.
3. Exibir resposta citando `arquivo:linha`, commit e grau de certeza; não simular navegação precisa se só houver similaridade textual.
4. Desambiguar símbolo homônimo, gerado e dependência de terceiro; apontar fonte correta.
5. Planejar impacto de edição: assinaturas, interfaces, migrações, testes, segurança, custos, clientes e deploy.

### Fase D — atualização contínua
1. Incremental: detectar arquivos modificados pelo Git/FS com hash, invalidar símbolos e arestas afetadas, reparar índice; indexar branch/worktree separadamente.
2. Em PR: anexar resumo de mudanças, dependências impactadas, testes relevantes e riscos; não publicar código privado fora do ambiente autorizado.
3. Rastrear artefatos por `repository_id`, `ref`, `commit_sha`, `indexer_version`, `indexed_at`, `content_hash`.
4. Projetos grandes: shards por pacote e paralelismo com limite, lock/transaction e retry; benchmark tempo de atualização.

### Fase E — avaliação
- **Definição**: pergunta sobre símbolo conhecido deve apontar para arquivo e linha corretos.
- **Referências**: recall de chamadas/dependências com status `exact` vs `heuristic`.
- **Impacto**: alterações de assinatura devem encontrar usos e testes relevantes.
- **Frescor**: mudança e remoção de arquivo devem alterar o índice.
- **Controle de acesso**: subagentes não devem recuperar símbolos de repositório sem permissão.
- **Confiança**: sem evidência, declarar incerteza em vez de inventar APIs.
- **Custos**: tokens e tempo por resposta, index time, storage, falso positivo de impacto.

## Ferramentas e tecnologias
- `git`, `rg`, ferramentas nativas do compilador, LSP server do ecossistema, coverage e testes: primeira escolha.
- `tree-sitter/tree-sitter`: parser incremental de vários idiomas.
- `scip-code/scip`: protocolo de indexação e navegação precisa, quando há indexadores por linguagem.
- `Joern`: code property graph para investigação profunda/segurança, opcional e potencialmente pesado.
- `SQLite/FTS5`, PostgreSQL/pgvector: índice lexical + vetor opcional. Grafos são opcionais.
- `Sourcegraph Precise Code Navigation` pode ter limitações de plano; **não presumir gratuidade do produto hospedado**.
- `CodeQL`, `Semgrep`, `ast-grep`: análise de regras, em conjunto com Skill de sanitização.

## Infraestrutura proporcional
- **Local**: `Git + ripgrep + Tree-sitter/LSP + SQLite FTS5`; sem LLM obrigatório na indexação.
- **Servidor**: workers de indexação, API read-only e PostgreSQL ou buscador existente; controle por repo/tenant.
- **AWS/GCP/Azure**: contêiner de indexação com storage de artefatos e Postgres/serviço gerenciado, identidade e segregação; conferir custo de rebuild.
- **CI/GitHub Actions**: indexação incremental após PR/merge, com permissões mínimas e artifacts protegidos; pipelines isolados para branches não confiáveis.

## Critérios de aceite
- [ ] Busca lexical e símbolos com resultados `path:line` reproduzíveis.
- [ ] Pelo menos 10 perguntas reais e 3 casos adversariais com avaliação automática.
- [ ] Diff altera índice de arquivo afetado e não invalida repo inteiro sem necessidade.
- [ ] Respostas fundamentadas em commit/ref atual, não somente branch default.
- [ ] Análise de impacto aponta testes relevantes e limitações de dependências dinâmicas.
- [ ] Segurança: respeita Gitignore/credenciais, ACL e executa parsers em sandbox quando não confiáveis.
- [ ] Comparação demonstrada com busca simples sem embeddings.

## Entregáveis
`CODE_INTELLIGENCE_ARCHITECTURE.md`, `REPOSITORY_MAP.md`, `SYMBOL_INDEX_SPEC.md`, `DEPENDENCY_GRAPH.md`, `CHANGE_IMPACT.md`, `INDEXING_RUNBOOK.md`, `CODE_RETRIEVAL_EVAL.md`, ADRs e scripts de validação. Consulte `references/structural-indexing.md`, `references/architecture-cloud.md`, `references/evaluations.md`, `references/security-and-provenance.md`, `assets/code-intelligence-report.md`.

## Skills complementares
`continuous-code-sanitization` para correções de qualidade e segurança; `company-brain-architecture` para contexto de projetos/decisões; `agent-persistent-memory` para memória duradoura; `infrastructure-devops-architect` para indexação em CI/cloud.
