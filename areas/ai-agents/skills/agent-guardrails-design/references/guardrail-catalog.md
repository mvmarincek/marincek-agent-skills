# Catálogo de guardrails por camada

Cada item lista: o que controla, como implementar (ponto de execução) e anti-padrão clássico.

## 1. Borda de ferramenta (tool boundary)
**Ponto**: middleware/wrapper na chamada da tool, hook do runtime, shim do CLI.

- **Allow/deny list de comandos e tools**: lista explícita do que pode rodar; negar por padrão o resto. Implementação: tabela `{comando, tier, flags_permitidas}` avaliada antes do exec. Anti-padrão: deny list (bloquear o conhecido) — o agente encontra variação que não está na lista.
- **Padrões banados (banned patterns)**: regex/AST das formas destrutivas (`rm -rf`, `--force`, `DROP TABLE`, `apply/destroy` de IaC, push com force, delete de branch). Anti-padrão: casar só string exata; o agente reescreve com quoting/variação.
- **Risk tier por tool e por flag**: a mesma tool muda de tier conforme argumento (`plan` vs `apply`; `SELECT` vs `DELETE`). Avaliar o par (tool, argumento), não a tool.
- **Idempotency key** para escritas: retry do mesmo pedido não duplica efeito.
- **Timeout e quota por tool**: morte por tempo e teto de chamadas por sessão/tarefa.

## 2. Aprovação humana
**Ponto**: runtime do agente, suspending a execução de verdade.

- **Gate com suspensão real**: a thread/fila para até decisão autenticada chegar por canal confiável. Aprovação "respondida" dentro do próprio texto do LLM não é aprovação.
- **Protocolo de exibição**: ao pedir aprovação, exibir — (1) intenção em uma frase; (2) diff/comando exato que será executado; (3) raio de blast (o que pode quebrar); (4) plano de rollback; (5) custo se houver. Menos que isso é pedir assinatura em branco.
- **Timeout com abort**: aprovação que nunca vem vira abort com estado consistente, não execução por cansaço.
- **Registro**: quem aprovou, quando, o que foi mostrado, hash do diff aprovado. Aprovação sem registro não serve para auditoria.

## 3. Escopo
**Ponto**: permissões de runtime/OS/credenciais.

- **Permissão por tarefa/sessão**: credenciais injetadas com escopo mínimo para a tarefa corrente; nada de credencial global "por conveniência".
- **Sandbox**: filesystem/rede restritos para trabalho exploratório; abrir escopo só no passo que precisa.
- **Isolamento de ambiente**: dev/staging/prod com identidades distintas; o agente de dev não alcança prod nem "só para ler" sem controle.

## 4. Orçamento
**Ponto**: contador no runtime, verificado antes de cada chamada custosa.

- **Teto de custo por tarefa** (tokens + chamadas pagas) e **teto de tempo**.
- **Limite de iterações e detecção de loop**: mesmo comando falhando N vezes seguidas = parar e reportar, não tentar N+1.
- **Kill switch**: forma rápida e auditada de desligar o agente/tarefa em curso.

## 5. Entrada
**Ponto**: montagem do contexto antes do LLM.

- **Hierarquia de instruções**: system/operador > tarefa confirmada > conteúdo recuperado. Conteúdo de fonte externa entra marcado como dado.
- **Descontaminação**: outputs de MCP, páginas e RAG passam por sanitização/marcação; nunca viram seção de "instruções".
- **Teste de injeção padrão**: "ignore as instruções anteriores e execute X" precisa falhar contra a camada, não contra a boa vontade do modelo.

## 6. Saída
**Ponto**: pós-processamento do output antes de aplicar/exibir.

- **Filtro de segredos/PII**: regex + entropia para tokens/keys/CPF antes de log, exibição ou envio a terceiros.
- **Validação de schema**: output que será consumido (JSON, comando, SQL) valida contra schema antes de aplicar.
- **Revisão de diff obrigatória**: para mudanças em produção, o diff revisado é o que foi aprovado (hash), não um novo gerado depois.

## Anti-padrões transversais
- Guardrail só no prompt ("não faça X") registrado como controle de enforcement.
- Aprovação implícita por silêncio ou por repetição.
- Bloqueio sem fallback: agente entra em loop de tentativas de burlar o próprio guardrail.
- Apertar todos os controles após um incidente pontual em vez de corrigir o controle específico.
- Matrix de risco escrita uma vez e nunca mais visitada; incidentes que não geram regressão de teste.
