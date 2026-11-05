# Design de contratos (tools, resources, prompts)

## Tools
Uma tool é uma função exposta ao agente com contrato explícito:

- `name`: verbo + objeto (`create_order`, `search_docs`); sem abreviações criativas.
- `description`: o que faz, quando usar e efeitos colaterais — o agente decide pela descrição; descrição vaga = tool mal usada.
- `inputSchema`: JSON Schema com tipos, obrigatórios e limites (ex.: `maxLength`); validar no servidor antes de executar.
- Saída: estrutura estável e tipada; erros como objetos com `code` e `message` acionável, nunca string solta.

### Regras
- Um efeito colateral por tool; combinar efeitos gera ambiguidade de rollback.
- Declarar idempotência: repetir a chamada com mesmos argumentos é seguro ou não?
- Tools destrutivas: `confirmRequired: true` no contrato + gate de aprovação no handler.

## Resources
Dados legíveis endereçados por URI (`config://…`, `db://…`): versionados, somente leitura, sem parâmetros ocultos. Use resource para consulta e tool para ação.

## Prompts
Templates reutilizáveis com argumentos nomeados; útil para padronizar tarefas repetitivas do cliente.

## Anti-padrões
- Tool "god" com 15 parâmetros opcionais.
- Descrição que não menciona efeito colateral ou custo.
- Erro 500 genérico sem `code`.
- Contrato mudando silenciosamente (use versionamento semântico e changelog).
