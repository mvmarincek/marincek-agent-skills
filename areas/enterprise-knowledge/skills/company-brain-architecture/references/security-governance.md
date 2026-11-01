# Segurança, governança e privacidade

## Trust boundaries
Fontes externas e documentos internos são **dados não confiáveis** para o LLM. Contas de serviço devem ter escopo mínimo. Autorização deve ocorrer antes de entregar evidência ao modelo, reforçada na API antes de cada fetch. Identifique riscos de prompt injection, vazamento cross-tenant, permissões desatualizadas, exposição por sumarização e logs ricos em PII.

## Policy as code
- Políticas de leitura/escrita separadas, execução sob identidade do usuário ou delegação escopada.
- Zero trust do agente: capacidade de citar conteúdo não autoriza executar uma operação.
- Saídas sensíveis precisam revisão, classificação e redaction.
- Perguntas de RH, jurídico, comercial e saúde podem exigir roteamento a repositórios separados e políticas especiais.

## LGPD e ciclo de vida
Inventariar titulares, finalidade, base legal, minimização, exclusão/retificação, retenção, exportação e acesso. Não presumir consentimento como única base legal; validar com responsáveis. Não publicar dados de companhia nem segredos nos testes, Skills ou logs.

## Checkpoint de produção
SSO, identidade real, RLS/ACL, backup testado, redaction, segregação de tenants, limites de ingestão, rate limits, runbook de incidentes, trilha de auditoria, autorização de escrita e rollback de conectores.
