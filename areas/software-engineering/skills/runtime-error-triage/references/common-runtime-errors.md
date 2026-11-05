# Erros Frequentes

## Supabase

Dados inseridos mas invisíveis: RLS, `organization_id`, filtro errado, cache ou retorno ignorado.

Múltiplos GoTrueClient: criar client em vários lugares. Use singleton.

`function_search_path_mutable`: definir `search_path` na assinatura exata da função.

## Prisma

`Unknown argument`: campo ausente no `schema.prisma` ou relação sem FK scalar.

Migration drift: não resetar produção; gerar diff e validar em staging.

## MySQL

`errno 150`: ordem de tabelas, tipo/unsigned/tamanho, índice, engine, collation ou dados órfãos.

## Web UI

Botão sem ação: handler, disabled, request, erro silencioso, estado e condição de renderização.

## PDF

Falha comum: cor inválida, fonte ausente, asset path errado, overflow ou dependência de browser no servidor.

## WhatsApp / Pagamento

Webhook recebido sem atualizar estado: assinatura, raw event, idempotência, mapeamento de status e transação.
