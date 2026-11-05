# Loop test-debug-fix-regression

Ciclo de correção durante a aceitação. Cada falha aprovada passa por ele antes de ser marcada como corrigida.

## O loop

```
FALHA REGISTRADA
   │
   ▼
[TEST] reproduzir com evidência ── não reproduz? coletar mais dados, é hipótese
   │
   ▼
[DEBUG] isolar camada (UI → handler → API → permissão → dados)
   │
   ▼
[FIX] menor correção segura na causa raiz
   │
   ▼
[RETEST] mesma falha reexecutada ── falhou? volta ao DEBUG (máx. 3 iterações, depois escalar)
   │
   ▼
[REGRESSION] reexecutar itens já aprovados do checklist
   │
   ▼
FECHAR ITEM COM EVIDÊNCIA
```

## Coleta de evidência (antes de corrigir)
- **Trace Playwright** (`trace: 'on'`): snapshots DOM passo a passo da falha.
- **Screenshot** do estado visual no momento do erro.
- **Console log** do navegador: erros e warnings da sessão.
- **Network**: requisição feita, status, payload enviado e resposta — "botão não funciona" se resolve em qual destas camadas.
- **Log do servidor**: stack trace correspondente ao timestamp da falha.

Sem pelo menos duas fontes de evidência (ex.: screenshot + network), a causa provável é hipótese, não diagnóstico.

## Regras de correção
- Uma hipótese por iteração; confirmada por evidência antes de virar código.
- Correção mínima na causa raiz — não em sintoma (ex.: `setTimeout` maior não corrige race condition).
- Toda correção que altera estado persistente declara como reverter; para falhas complexas de runtime, escalonar para `runtime-error-triage`.

## Regressão
- Checklist atualizado: itens aprovados são reexecutados após cada fix que tocou módulo compartilhado.
- Falha nova introduzida por correção é registrada como item próprio — nunca "ajuste" silencioso.

## Limite de iterações
- 3 iterações test-debug-fix por item; excedido, escalar com evidências acumuladas e hipóteses descartadas documentadas.
