# Fluxo de Correção

1. Copie o erro original com informações críticas.
2. Extraia arquivo, linha, status, tabela, campo e provedor.
3. Classifique o erro.
4. Monte reprodução mínima.
5. Leia código relacionado.
6. Corrija a causa raiz com mudança pequena.
7. Execute validação.
8. Relate resultado e risco residual.

## Princípios

- Corrigir causa, não sintomas.
- Alterar poucos arquivos por erro.
- Confirmar schema antes de mudar código em erro de banco.
- Confirmar identidade e policy em erro de permissão.
- Salvar raw event antes de atualizar estado em webhook.

## Reteste

Use testes, Playwright, lint/typecheck, startup, acesso manual ou comando reproduzível. Se não puder validar, diga o motivo.

## Evitar falso pronto

Evite “tudo corrigido” ou “zero erros” sem evidência. Prefira: “corrigi o erro X e validei com Y”.
