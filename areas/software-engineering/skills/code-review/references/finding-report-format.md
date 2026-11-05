# Formato de achado e parecer final

## Achado individual
```
[SEVERIDADE] arquivo/linha — título curto
Evidência: <trecho do diff ou descrição precisa>
Padrão/Spec: <qual requisito ou documento de convenção violado>
Sugestão: <mudança concreta proposta, quando aplicável>
```

Regras:
- Um achado = um problema; não agrupar assuntos distintos.
- Sem `arquivo:linha` e evidência, o achado não entra no parecer.
- Não usar o achado para preferência pessoal de estilo não documentada.

## Parecer final (comentário de PR ou arquivo)
```
## Contexto revisado
- PR/branch/commits: <ref>
- Intenção percebida: <1-2 frases>
- Cobertura: <o que foi lido; arquivos/áreas NÃO revisados, se houver>

## Spec
- Requisito 1: atendido | parcial | não atendido | N/A
- Escopo extra: <sim/não + itens>

## Padrões
- <resumo dos achados por severidade>

## Achados
<lista de achados no formato individual>

## Veredito
APROVAR | APROVAR COM AJUSTES (<lista>) | BLOQUEAR (<bloqueantes>)
```

## Anti-padrões
- "LGTM" sem evidência de leitura do diff.
- Aprovar porque CI está verde (CI testa, não revisa intenção).
- Achado vago: "melhorar legibilidade" sem apontar linha e motivo objetivo.
- Pedir reescrita total quando a menor mudança resolve (review não é redesign).
