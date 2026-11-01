# Integração das três Skills — arquitetura de referência

```text
Fontes corporativas autorizadas -> Company Brain (ingestão, ACL, decisões, citabilidade)
Notas e conversas consentidas -> Second Brain (pessoa, projetos, memória, revisão)
Repositórios Git/AST/LSP/SCIP -> Code Intelligence (símbolos, versões e dependências)
                    |                 |                 |
                    +--> Context Router condicionado por identidade/tarefa <--+
                                        |
                                Agente / LLM / Skills
                                        |
                             MCP / APIs autorizadas
                                        |
                         Telemetria e validação separadas
```

## Política de isolamento
- Conteúdo pessoal **nunca** migra para Company Brain sem autorização explícita e verificação de visibilidade.
- Código privado não entra em base compartilhada ou embeddings externos sem permissão; tratar segredos com redaction.
- Em buscas federadas, o gateway aplica identidade, tenancy, autorização por fonte e registro das provas antes de o modelo receber o texto.
- Cada resultado inclui `source_id`, link, commit (para código), time bounds e nível de confiança.
- Skills são procedimentos: não instalam automaticamente componentes, não criam recursos pagos e não treinam os pesos do LLM.

## Ordem proposta
1. Local-first Second Brain pequeno para validar captura, exclusão e recuperação.
2. Indexação Code Intelligence de um repo de teste, com benchmark de perguntas e custo baixo.
3. Company Brain MVP com uma ou duas fontes, ACL e avaliação de vazamento.
4. Integração federada de três fontes, observabilidade e regras.
5. Grafo/embeddings/serviços gerenciados somente com melhoria comprovada.

## Dependências existentes
`agent-persistent-memory`, `agent-reliability-governance`, `structured-agent-prompts`, `skill-evaluator`, `smart-skill-router`, `infrastructure-devops-architect`, `continuous-code-sanitization`.

## Plataformas
- Local: SQLite/FTS5, Git/rg, parser local e pastas criptografadas.
- AWS/GCP/Azure: banco relacional gerenciado, armazenamento de objetos, worker de indexação e IAM.
- Escolher provedor pelo projeto e comparar custos antes de criar infraestrutura.
