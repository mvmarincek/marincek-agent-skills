# Checklist de engenharia de datasets para agentes

- [ ] Fontes autorizadas/consentimento/privacidade.
- [ ] Licenças e termos de uso verificados.
- [ ] Sem senhas, tokens, PII desnecessária ou segredos nos exemplos.
- [ ] Separação treino/dev/test por unidade de negócio, documento, usuário ou período para evitar vazamento.
- [ ] Representação de falhas/retries, e não apenas sucessos artificiais.
- [ ] Classes raras e casos difíceis presentes; pesos transparentes.
- [ ] Rótulos revisados, anotadores e critérios de concordância.
- [ ] Dataset card com proveniência, versão, restrições e retenção.
- [ ] Métricas de baseline e pares de controle.
- [ ] Testes end-to-end no agente completo e no modelo isolado.
- [ ] Alertas de regressão e desvio depois da promoção.

## Exemplo de JSONL de SFT (esquema abstrato, converter ao formato do modelo/provedor)
```json
{"example_id":"e001","messages":[{"role":"user","content":"Classifique o pedido"},{"role":"assistant","content":"categoria: suporte"}],"source":"approved-dataset","split":"train"}
```
Não misturar metadados de auditoria com schema exigido pelo provedor; adaptar ingestão.

## Exemplo de preferência DPO (abstrato)
```json
{"prompt":"...","chosen":"resposta verificada","rejected":"resposta incorreta","reviewer":"human","split":"train"}
```

## Experimento
Começar com ablação: baseline, baseline+Skill, baseline+RAG, baseline+prompt, SFT piloto. Documentar hipótese e decidir por qualidade/custo/risco, não apenas benchmark sintético.
