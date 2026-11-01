# Indexação estrutural de código e contratos

## Abordagens por nível
1. **Lexical:** git/rg/SQLite FTS5: resultados rápidos, não resolvem chamadas com precisão.
2. **Sintática:** Tree-sitter/AST: estrutura, escopos e imports; sem resolução completa de tipos.
3. **Semântica precisa:** LSP/SCIP indexers: definições/referências cross-file; cobertura varia por linguagem/framework.
4. **Grafo:** CPG/Joern e derivados: relações e consultas de análise estática avançada; risco de falsos positivos/dinâmica.
5. **RAG de código:** sinal lexical + símbolo + referência + vetor opcional com reranking e orçamento de contexto.

## Schema simplificado
```text
repositories(repo_id, host, organization, visibility, owner, policy_id)
revisions(repo_id, commit_sha, ref_name, indexed_at, indexer_version)
files(repo_id, commit_sha, file_path, sha256, language, size, ignored)
symbols(symbol_id, repo_id, commit_sha, file_path, qualified_name, kind, start_line, end_line, parser, confidence)
relationships(from_symbol, to_symbol, relation, repo_id, commit_sha, provenance, confidence)
search_chunks(chunk_id, repo_id, commit_sha, file_path, start_line, end_line, text_hash, embedding_version)
```

## Regras de identificação
- `symbol_id` deve discriminar repo/versão/linguagem/qualified-name e localização, com tratamento a renames.
- `CALLS` extraído por AST pode ser heurístico; distinguir `exact`/`potential`.
- Desacoplar rastreabilidade de símbolos e embedding; retokenização não deve mudar identidade do código.
- Paths e spans devem ser rastreáveis em commit real; não afirmar linha se o indexador não a conhece.

Fontes:
- https://github.com/tree-sitter/tree-sitter
- https://github.com/scip-code/scip
- https://docs.joern.io/
