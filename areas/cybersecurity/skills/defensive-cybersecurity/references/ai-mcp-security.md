# Segurança de agentes e ferramentas MCP

## Modelo de confiança
- Mensagens de usuário autenticado, políticas do sistema, instruções de skill e outputs de MCP têm graus diferentes de confiança. Material de retrieval é sempre não confiável.
- Isolar textos recuperados; nunca permitir instruções escondidas em PDF, site, imagem, PR ou comentário ordenarem uso de credenciais, alterações de arquivos, download de scripts ou exfiltração.
- Ferramentas de leitura e escrita precisam de identidade e permissão reais. O agente não concede a si mesmo scopes via prompt.
- Tool schemas tipados, limites, allowlists e auditoria; autorização fora do LLM no servidor/backend; revalidar no momento da execução.

## Controles testáveis
1. Testar ataque de prompt injection presente em dados de usuário e documentos consultados.
2. Testar tentativa de fazer agente chamar tool não autorizada, usar escopo de outro tenant ou revelar segredo em resposta.
3. Testar exigência de aprovação em pagamentos, deleções, emails, deploys e acesso privilegiado.
4. Testar tool output com URL arbitrária; egress permitir apenas destinos autorizados.
5. Limitar tempo, custo, ciclos e profundidade de delegação; tornar operações de escrita idempotentes.
6. Não guardar tokens, segredos ou payloads completos em spans; anonimizar user_id quando possível.

## Referências
- OWASP Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/
- OWASP Agentic AI: https://genai.owasp.org/
- MCP Specification: https://modelcontextprotocol.io/specification
- OPA: https://www.openpolicyagent.org/docs/latest/
- NeMo Guardrails: https://github.com/NVIDIA-NeMo/Guardrails
