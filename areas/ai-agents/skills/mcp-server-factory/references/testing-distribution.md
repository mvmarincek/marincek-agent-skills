# Testes e distribuição

## Suite de testes (mínimo)
1. **Contrato**: schema válido passa; entrada inválida rejeitada com erro tipado (um caso por violação).
2. **Happy path**: cada tool com entrada canônica produz a saída contratada.
3. **Erro**: backend subjacente falhando → erro tipado, sem stack trace vazando.
4. **Timeout**: chamada lenta retorna erro de timeout dentro do limite declarado.
5. **Gate de aprovação**: tool destrutiva sem confirmação é recusada.

## MCP Inspector
Antes de integrar a cliente real, verificar com o Inspector: listagem de tools/resources/prompts, execução manual com entradas válidas/inválidas e inspeção das mensagens do protocolo. Falha no Inspector bloqueia a distribuição.

## Versionamento e changelog
- Versão semântica: breaking change de contrato (remover tool, mudar schema de entrada de forma incompatível) exige major.
- `CHANGELOG` por servidor registrando: nova tool, mudança de schema, correção de handler.
- Manifest do servidor declara versão e capacidades expostas.

## Distribuição
- Empacotar (npm/PyPI/binário) com instruções de instalação por cliente alvo (Claude Code, Codex, Verdent, OpenCode).
- Documentar variáveis de ambiente exigidas com `.env.example` sem valores reais.
- Publicar somente após suite verde + Inspector — e com revisão de diff quando houver acesso a dados ou sistemas de produção.
