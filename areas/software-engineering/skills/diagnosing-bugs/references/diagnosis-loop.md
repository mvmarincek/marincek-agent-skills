# O loop de diagnóstico detalhado

## Fase 1 — Contrato do bug
Escrever antes de investigar:
```
Dado: <pré-condição e entrada>
Quando: <ação executada>
Observado: <resultado real, com frequência>
Esperado: <resultado correto>
Ambiente: <local | CI | staging | produção; versão/commit>
```
Se "Observado" não for verificável, o bug ainda não está definido.

## Fase 2 — Reprodução
- Determinística: mesma sequência sempre dispara.
- Intermitente (flaky): rodar N vezes (ex.: 20), registrar taxa (ex.: 7/20); taxa > 0 confirma reprodutibilidade estatística.
- Irreproduzível no seu ambiente: comparar ambiente do relato (versão, dados, config, rede) antes de declarar "não reproduz".

## Fase 3 — Linha do tempo
- `git log --since` no período do relato; foco em commits que tocam o caminho do sintoma.
- `git bisect start` / `git bisect bad <último-ruim>` / `git bisect good <último-bom>` quando o sintoma é versionável; automatizar o teste do sintoma por commit quando possível.
- Correlacionar com deploys (quando entrou em produção) e mudanças de dado (migration rodada? seed alterado?).

## Fase 4 — Hipóteses rivais
Sempre >= 2. Exemplo:
- H1: a condição de borda X não é tratada na função Y.
- H2: o dado chega diferente do assumido (encoding, null, timezone).
Teste que distingue: logar/breakpoint na fronteira; se o dado está correto e o erro persiste, H1 ganha força.

## Fase 5 — Técnicas de isolamento
| Técnica | Quando usar |
|---|---|
| Redução de entrada | menor payload/CLI que ainda dispara |
| Bypass de caminho | comentar/substituir um módulo por stub |
| Troca de ambiente | local vs. CI; dev vs. prod (somente leitura em prod) |
| Binário no código | metade dos módulos stubada, fecha o suspeito |
| Comparação de dado | mesmo input no ambiente que funciona vs. falha |
| Instrumentação | log/trace pontual no caminho suspeito, removido depois |

Uma variável por experimento; registrar resultado imediatamente.

## Fase 6 — Prova da causa raiz
A causa raiz deve:
1. Explicar o sintoma observado (inclusive a frequência, se flaky).
2. Prever a ausência do sintoma quando removida (é isso que o fix testa).
3. Explicar por que "estava funcionando antes" (o que mudou).

Se o fix funciona mas a explicação não passa em 1-3, continuar investigando — o sintoma pode ter duas causas.

## Fase 7-8 — Fix e regressão
- Fix mínimo: sem refactor oportunista no mesmo commit.
- Teste de regressão: vermelho sem fix, verde com fix (verificar os dois estados antes de push).
