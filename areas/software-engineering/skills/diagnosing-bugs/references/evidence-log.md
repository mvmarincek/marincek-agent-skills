# Registro de evidências do diagnóstico

## Formato de log de experimento
```
EXP-01
Hipótese: H1 (borda X não tratada em Y)
Ação: logar valor de X na entrada de Y, rodar caso do bug
Resultado: X=correto; erro persiste
Conclusão: H1 enfraquecida; seguir H2

EXP-02
Hipótese: H2 (dado chega com encoding diferente em prod)
Ação: comparar payload gravado no ambiente que falha vs. local
Resultado: prod envia JSON com charset errado; local não
Conclusão: H2 confirmada; causa raiz: ausência de charset explícito no header
```

## Regras
- Um experimento, uma variável; resultado registrado mesmo quando negativo (negativo também fecha espaço).
- Evidência citável: comando executado + saída relevante (trecho, não dump inteiro).
- Dados sensíveis em logs de produção: minimizar (mascarar CPF, token, e-mail, dado de saúde) antes de copiar qualquer trecho.
- Ao final: tabela H1..Hn com estado (confirmada / refutada / abandonada) e o experimento decisivo de cada uma.

## Episódio final (para o registro do time)
```
Bug: <contrato do bug resumido>
Causa raiz: <explicação + o que mudou para introduzi-la>
Evidência-chave: EXP-XX e o teste de regressão
Fix: <commit/PR ref>
Teste: <nome do teste de regressão; vermelho sem fix, verde com fix>
Adjacências verificadas: <módulos/callers; resultado>
```
