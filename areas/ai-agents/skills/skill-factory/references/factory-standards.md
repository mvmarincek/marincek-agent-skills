# Padrão de criação

## Checklist de extração
- Fonte e commit/URL; licença ou atribuição; permissão de redistribuição.
- Frase de ativação e exemplos positivos/negativos.
- Entradas e saídas; dependências de LLM, ferramentas e runtime.
- Fluxos normal, falha, fallback, aprovação e auditoria.
- Evidência de eficácia medida; diferenças entre simulação e produção.
- Tamanho `SKILL.md` proporcional ao número de decisões; exemplos longos em references.

## Status
Experimental: estrutura validada. Candidata: pelo menos um experimento real. Validada: testes de contrato e regressão em projeto conhecido. Produção: observabilidade, dono, versão, changelog, rollback e revisão de segurança.

## Não fazer
Não copiar repos automaticamente para própria biblioteca; não atribuir licença MIT a código upstream sem conferir termos; não gerar Skills que se autoaprovam e se autopublicam sem guardrails.

Fonte: https://agentskills.io/specification
