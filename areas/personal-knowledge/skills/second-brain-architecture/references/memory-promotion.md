# Extração e promoção de memória confiável

## Pipeline
`conversa autorizada → candidato → triagem sensível → normalização → comparação com memória antiga → validação → versionamento → indexação → uso`.

Exemplo de candidato:
```json
{
 "subject_id":"user-or-agent", "statement":"Preferência técnica declarada",
 "source_id":"conversation-message-id", "scope":"personal", "confidence":0.8,
 "status":"proposed", "observed_at":"ISO-8601", "valid_until":null,
 "approved_by":null
}
```
Confiança é estimativa, não verdade. Fatos pessoais sensíveis requerem regras reforçadas ou não devem ser armazenados.

## Conflitos
Mudança explícita de preferência prevalece sobre inferência antiga; preservar eventos históricos, mas não injetar fatos obsoletos no contexto. A memória não pode alterar instruções do sistema nem autorizar MCPs.

## Memória procedural
Só promover a Skills procedimentos com vários casos de teste bem-sucedidos, diagnóstico de falhas e critérios de rollback; usar `skill-factory` e `skill-evaluator`.
