---
name: diagnosing-bugs
description: "Loop sistemático de diagnóstico de bugs difíceis e regressões: reproduzir de forma confiável, isolar variáveis, encontrar causa raiz com evidência, corrigir o mínimo necessário e verificar sem introduzir regressão."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  area: "software-engineering"
---

# Diagnosing Bugs — causa raiz com evidência, não chute

## Quando ativar
Quando o usuário relatar comportamento quebrado, errático ou lento (`isso não funciona`, `bug estranho`, `regressão`, `estava funcionando antes`, `debug this`), ou quando uma correção anterior não resolveu. Distinto de `runtime-error-triage` (classificação de erros de runtime por categoria: console, API, migration, CORS): esta skill é o **método geral de investigação** para bugs de lógica, intermitentes e regressões, com ou sem stack trace.

## Definição operacional
Diagnosticar é: transformar um relato vago em uma reprodução confiável, fechar o espaço de causas até uma única explicação suportada por evidência, e corrigir a causa — não o sintoma. Diagnóstico sem reprodução é hipótese; hipótese não autoriza correção. "Era cache" / "funciona na minha máquina" são conclusões, desculpas só com evidência.

## Contrato de entrada
Relato do sintoma (o que aconteceu vs. o esperado), ambiente onde ocorre (local, CI, produção), e acesso ao código. Reprodução em produção exige cuidado: apenas observação passiva e leitura de logs, salvo aprovação explícita para qualquer ação que altere estado. Dados sensíveis em logs são minimizados, nunca copiados para o relatório.

## Pipeline obrigatório
1. **Definir o contrato do bug**: entrada, ação, resultado observado, resultado esperado. Ambiguidade aqui invalida tudo depois.
2. **Reproduzir**: menor sequência determinística que dispara o sintoma; registrar taxa de reprodução (intermitente ≠ irreproduzível — usar loop com N tentativas quando flaky).
3. **Linha do tempo**: quando parou de funcionar? Cruzar com commits, deploys, mudanças de dados e de ambiente (`git bisect` quando o sintoma é versionável).
4. **Formular hipóteses rivais**: ao menos duas explicações plausíveis; desenhar como distingui-las antes de testar.
5. **Isolar**: reduzir entrada (menor caso), reduzir código (comentar/bypassar caminhos), alternar ambiente (local vs. CI vs. prod) — uma variável por vez, registrando o resultado de cada experimento.
6. **Provar a causa raiz**: a explicação final prevê o sintoma E sua ausência quando a causa é removida; se a correção "funciona" mas a explicação não prevê nada, a causa raiz não foi achada.
7. **Correção mínima**: menor mudança que elimina a causa; mudanças de oportunidade ficam fora do fix (commits separados).
8. **Teste de regressão**: teste que falha sem o fix e passa com ele; adicionado à suíte antes de fechar.
9. **Verificar adjacências**: o fix quebra outros callers do código tocado? Rodar testes do módulo, no mínimo.
10. **Registrar**: sintoma, causa raiz, evidência-chave, fix e teste — episódios alimentam a seção de bugs conhecidos.

## Segurança e permissões
Investigação em produção é leitura primeiro: logs, métricas, traces; qualquer ação com efeito (reproduzir um bug em dado real, rodar script de correção) exige aprovação. Nunca alterar dado de produção para "testar uma teoria". Não expor conteúdo sensível de logs no relatório. Se a causa estiver fora do código (infra, dependência upstream, dado corrompido), escalar com evidência em vez de improvisar workaround em produção.

## Referências e artefatos
- `references/diagnosis-loop.md` — o loop detalhado com técnicas de isolamento.
- `references/evidence-log.md` — formato de registro de experimentos e evidências.

## Critério de aceite
Reprodução confiável (ou taxa de reprodução medida para flaky); causa raiz com evidência que a distingue das hipóteses rivais; correção mínima aplicada; teste de regressão que falha sem o fix; verificação de adjacências executada; episódio registrado sem dado sensível.
