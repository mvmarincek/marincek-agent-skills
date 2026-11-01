---
name: linear-tasks-prd
description: "Criar PRDs estruturados em Markdown e PDF, preparar issues e comentários técnicos para Linear, documentar progresso, bloqueios, aceite, escopo e rastreabilidade sem inventar status."
license: MIT
metadata:
  version: "2.0.0"
  language: "pt-BR"
  area: "product-management"
---

# Linear Tasks + PRD — comunicação técnica verificável

## Ativação
Quando criar ou revisar PRD, descrever épicos/stories/bugs, preparar issues, comentar progresso, impedimentos, code review, homologação e entrega no Linear, ou gerar documentação de requisitos em `.md` e `.pdf`. Funciona sem Linear conectado: produzir arquivo pronto para copiar, **não alegar publicação**.

## Contrato de início
Identificar produto, problema, público, stakeholders, objetivo/metric, fase, escopo, não-escopo, requisitos funcionais/não funcionais, aceites, dependências, riscos, decisões, cronograma, arquitetura, referências/links e idioma. Consultar fontes primárias no repo e no Linear **se disponível e autorizado**. Separar fatos, hipóteses e pendências.

## PRD de alta qualidade — pipeline
1. Criar um resumo de decisão executiva em 1 página com valor, custo e métricas.
2. Definir contexto, problema, público-alvo e jobs-to-be-done; pesquisa/insights citados e não inventados.
3. Separar metas mensuráveis e não-metas; métricas com baseline, target, janela, método e owner.
4. Descrever escopo e fluxos de ponta a ponta, jornadas, protótipos, eventos, estados de erro, integrações e permissões.
5. Especificar requisitos numerados `FR-001...` e `NFR-001...`, com prioridade, critérios de aceite verificáveis e dependências.
6. Documentar arquitetura de alto nível, contratos API/eventos, estratégia de dados, privacidade, acessibilidade, observabilidade, segurança e FinOps.
7. Descrever rollout, feature flags, métricas, testes, migração/rollback, suportabilidade, riscos e perguntas em aberto.
8. Criar matriz de rastreabilidade `Objetivo → requisito → issue → teste → evidência`.
9. Revisar se termos são consistentes, se números têm fonte, se decisões são explícitas e se não há afirmação de entrega sem testes.
10. Exportar Markdown renderizável; produzir PDF com sumário/links, hierarquia tipográfica, numeração, cabeçalho/rodapé e paginação; **abrir e inspecionar páginas** para verificar tabelas e quebras. Consultar `references/pdf-quality.md`.

## Linear — issue e comentários
Use `assets/linear-issue.md` para criação e `assets/linear-comment.md` para comentários. Em atualizações: contexto/resumo, realizado com evidência (PR/commit/test), próximo passo, impedimento, risco e solicitação de decisão. Diferenciar `planejado`, `em execução`, `validado`, `bloqueado` e `concluído`. Não inventar datas, links, donos, métricas, percentuais nem números de testes.
- Evitar duplicar conteúdo integral do PRD no issue: criar documento Linear ou vincular Markdown/PDF quando possível; issues desdobram execução.
- Só postar no Linear depois de conferir issue/projeto e permissão de publicação. Não modificar status sem autorização quando não solicitado.
- Comentários são legíveis e acionáveis: não slogans, não logs enormes, não parágrafos sem evidência.
- Para bug: passos reproduzíveis, esperado/obtido, ambiente, impacto, logs sanitizados, hipótese e critério de correção.
- Para delivery: PR, commits, check CI, deploy, feature flag, testes, riscos residuais e validação pelo responsável.

## PDFs / Markdown
Use `assets/prd-template.md` como contrato. Converter com ferramenta disponível (Pandoc+engine, ReportLab, tipografia HTML→PDF, pipeline de docs). Verificar dependências e licenças; nunca declarar PDF criado sem arquivo concreto e inspeção visual. Guardar fonte Markdown como referência versionada e PDF como distribuição. Evitar rasterizar texto desnecessariamente.

## Variantes de implantação
Local: `.md` versionado e PDF build local. GitHub: Markdown + PR + checks e artefato release. AWS/GCP/Azure: objeto privado com ACL, links expirados, logs de aprovação e retenção; não criar bucket ou projeto cloud sem autorização. Em projetos regulados acrescentar classificação/confidencialidade e revisão humana.

## Saída e aceite
Fornecer PRD completo, sumário executivo, tabela de requisitos, backlog de issues, comentários Linear prontos, ligações com código, evidências e auditoria de hipóteses. Testar links, ortografia, renderização, hierarquia e consistência dos IDs. Declaração explícita do que foi postado vs. apenas gerado.

## Referências progressivas
`references/prd-quality.md`, `references/linear-communication.md`, `references/pdf-quality.md`, `assets/prd-template.md`, `assets/linear-comment.md`, `assets/linear-issue.md`.
