# Segurança de Code Intelligence

## Ameaças
Segredos hardcoded, arquivos ignorados indevidamente capturados, PRs maliciosos, prompt injection em comentários/READMEs, execução de scripts arbitrários em dependências, confusão de branch, saída de código privativo em logs/embeddings externos e vazamento entre repositórios.

## Mitigações
- Descoberta e indexação somente para escopos explicitamente autorizados.
- Não rodar scripts de build/configuração desconhecidos sem sandbox e revisão.
- Tratamento de conteúdo indexado como **dados**, não instruções para agente.
- Proteger caches, artefatos e embedders por política de dados.
- Proibir exportação de código privado para serviço externo sem aprovação.
- Auditoria com `repository_id`, `ref`, commit, `query_id`, `subject_id` e rastreabilidade de fonte.
- Revisão separada para análise de vulnerabilidades e ações de alteração de código.

Fontes auxiliares:
- https://github.com/github/codeql
- https://github.com/ast-grep/ast-grep
- https://github.com/returntocorp/semgrep
