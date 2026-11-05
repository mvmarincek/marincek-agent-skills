# Transporte e segurança

## stdio vs. HTTP
| Critério | stdio | HTTP (Streamable HTTP) |
|---|---|---|
| Uso | Local, single-user | Remoto, multiusuário/serviço |
| Auth | Herda usuário do processo | Obrigatória (token/OAuth/mTLS) |
| Deploy | Binário na máquina do cliente | Serviço com infraestrutura própria |
| Custo de operação | Nenhum extra | Hosting, monitoramento, segredos |

Escolha stdio para ferramentas pessoais/locais; HTTP quando múltiplos clientes ou ambientes compartilhados exigirem.

## Autenticação (transporte HTTP)
- Token portador para uso interno; OAuth para multiusuário; mTLS quando a infra exigir.
- Segredos por variável de ambiente/secret manager — nunca no código, no contrato nem em logs.
- Rotação documentada; auditoria de acessos habilitada.

## Menor privilégio
- O servidor acessa somente o necessário para suas capacidades declaradas.
- Credenciais escopadas (ex.: token somente-leitura para resources de consulta).
- Nenhuma tool com acesso administrativo "por precaução".

## Rate limiting e custo
- Operações custosas (chamadas de LLM, APIs pagas): declarar custo estimado na descrição da tool.
- Limitar taxa por cliente; rejeitar com erro tipado quando exceder.
- Timeouts em toda chamada externa; circuit breaker quando o backend subjacente oscilar.

## Gate de aprovação
- Tools destrutivas ou pagas exigem confirmação explícita antes do efeito — o contrato declara `confirmRequired`, o handler exige o token de confirmação do cliente.
- Nenhum servidor MCP confere autorização: a aprovação vem do usuário, via cliente.
