# Criar ou adaptar uma nova Skill

## Quando é Skill?
Quando a competência é repetível e contém sequência, decisões, critérios de aceitação e procedimento generalizável. Um tool MCP isolado não exige uma Skill. Uma referência de site, software ou biblioteca não vira uma Skill apenas porque consta no catálogo.

## Componentes
- `SKILL.md` com YAML `name`, `description` e instruções.
- `references/*.md` para tabelas, escolhas, API contracts, segurança e casos.
- `assets/*` para modelos de relatórios, parâmetros e exemplos.
- `scripts/*` para procedimentos executáveis **revisados e testados**, nunca rodar código externo automaticamente.

## Template
```markdown
---
name: minha-skill
description: Use para [situações claras, requisitos e domínio].
---

# Competência

## Ativação
...
## Entradas, autorizações e pré-condições
...
## Processo passo a passo
...
## Regras permanentes e segurança
...
## Critérios de validação e falhas
...
## Saídas e artefatos
...
## Referências e scripts
...
```

Manter Skills pequenas e referências carregáveis sob demanda. A execução deve preservar permissionamento e evidências. Não colocar permissões como instruções textuais; validar no runtime.
