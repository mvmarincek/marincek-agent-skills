---
name: database-blueprints
description: "Desenho de tabelas e segurança de migrações: Supabase/Postgres, MySQL, Prisma, RLS, foreign keys, ordem de migração, validação de persistência e schemas comuns para SMB no Brasil."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "software-engineering"
---

# Database Blueprints — Desenho de Schema e Migração Segura

## Quando ativar
Quando o usuário pedir `database`, `banco`, `tabela`, `schema`, `migration`, `supabase`, `mysql`, `postgres`, `prisma`, `drizzle`, `RLS`, `foreign key`, `dados não salvam`, ou quando um sistema de negócio exigir modelagem de dados, correção de persistência ou integração com Supabase/Postgres/MySQL/Prisma.

## Definição operacional
Blueprint é transformar requisitos em schema executável com segurança: entidades extraídas antes do SQL, ordem de migração definida, dados existentes preservados e persistência validada de ponta a ponta (formulário → API → DTO → banco → UI). Não é gerar DDL solto sem dependências nem rollback.

## Contrato de entrada
Requisitos funcionais do negócio, alvo (Supabase/Postgres, MySQL, Prisma ou SQLite), dados existentes e criticalidade, volume esperado, regras de acesso por papel, requisitos LGPD (consentimento, auditoria) e política de rollback.

## Pipeline obrigatório
1. **Extração de entidades**: clientes, pedidos, pagamentos, arquivos, mensagens, permissões e auditoria antes de escrever SQL; ver `references/core-schema.md`.
2. **Escolha do alvo**: Supabase/Postgres (`references/supabase-postgres.md`), MySQL (`references/mysql.md`) ou Prisma como camada (`references/prisma.md`).
3. **Desenho de tabelas**: responsabilidades, campos, chaves primárias/estrangeiras, índices, constraints e papéis de acesso.
4. **Ordem de migração**: lista ordenada por dependência com script de seed; ver `references/migration-safety.md`.
5. **Segurança**: RLS por papel no Supabase, limites da service role, consentimento LGPD e logs de auditoria.
6. **Validação de persistência**: cada campo crítico gravado e lido de volta; classificar erros como schema mismatch, foreign key, RLS, conexão, ordem de migration ou mapeamento.
7. **Rollback**: plano de reversão testado para cada migração destrutiva ou irreversível.

## Segurança e permissões
Não sugerir apagar dados de produção sem backup e aprovação. Não gerar migrations sem ordem de execução. Não corrigir só o front-end sem verificar colunas e DTOs. Não guardar identidade, pagamento ou permissões apenas em localStorage. Não omitir RLS ou limites da service role no Supabase. Migrações em produção exigem aprovação explícita.

## Referências e artefatos
- `references/core-schema.md` — tabelas centrais e extensões por negócio.
- `references/supabase-postgres.md` — Supabase/Postgres, RLS, Storage e Edge Functions.
- `references/mysql.md` — MySQL, foreign keys, charset e erros comuns.
- `references/prisma.md` — Prisma schema, relations, migrations e seed.
- `references/migration-safety.md` — ordem, preservação de dados, rollback e checklist.

## Critério de aceite
Entidades extraídas e aprovadas; tabelas com responsabilidades, chaves e índices definidos; ordem de migração com seed; persistência validada campo a campo; RLS/papéis configurados; plano de rollback documentado; nenhuma alteração destrutiva sem backup e aprovação.
