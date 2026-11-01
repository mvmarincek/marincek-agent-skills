# Arquitetura organizacional e squads
## Tipos de times
- Stream-aligned: entrega valor continuamente a um domínio/fluxo.
- Platform: fornece serviços self-service, golden paths, templates e observabilidade.
- Enabling: capacita outros times temporariamente em qualidade, segurança, dados e IA.
- Complicated-subsystem: especialidade isolada que exige expertise rara.
Não criar dezenas de squads sem justificativa de dependências e número de profissionais.
## Responsabilidades por papel
| Papel humano | Responsabilidade irredutível | Possível suporte agente |
|---|---|---|
| Product Manager | discovery, valor, prioridade, tradeoffs | resumo de feedback, PRD draft |
| Engineering Manager | equipe, segurança, desempenho, saúde do time | métricas e riscos |
| Tech Lead | arquitetura, revisão, qualidade | code review preliminar |
| Developer | desenvolvimento e manutenção responsáveis | coding agent e testes |
| QA | estratégia de risco e critérios | geração de casos/regressão |
| Security | políticas e resposta | triagem de findings |
| SRE | confiabilidade e incident command | monitoramento e diagnóstico |
| Data/ML | qualidade e governança de dados | EDA e experimentos |
## RACI
Sempre existir 'Accountable' humano por dados, orçamento, deploy e incidentes. Um agente pode ser 'Responsible assistant' apenas no sentido de executor delegado, nunca responsável legal ou aprovador único.
## Dependências
Identificar team API, critérios de pronto e contrato de interações; apoiar 'platform as a product'.
