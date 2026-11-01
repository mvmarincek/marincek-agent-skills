# SDL e plano de defesa técnica

## Modelo de ameaça e decisão
Modelo mínimo: ativos, identidade, entrada, processamento, trust boundaries, dependências, saída, usuários e administradores. Para cada ameaça registrar **ativo; vetor; pré-condição; impacto; controles existentes; correção; teste; responsável**. Evitar usar CVSS como substituto do impacto no contexto do negócio.

## Checklist de implementação
1. Dependências: `npm audit --audit-level=high` / `pip-audit` / OSV conforme stack; verificar falsos positivos e versões afetadas; não atualizar major cegamente.
2. SAST: Semgrep/CodeQL com configurações adequadas; revisão manual de riscos de autorização, injeção, SSRF, Open Redirect, mass assignment e IDOR.
3. Credenciais: scan de secrets no repositório; rotação caso secret real tenha sido exposto, incluindo histórico Git conforme procedimento aprovado.
4. API: schemas, auth e scope por endpoint, controles de tenant; senhas com KDF adequados; refresh token, sessão, MFA quando necessário.
5. Front: sem secrets em frontend, check de headers, CSP report-only antes de ativar CSP estrita, XSS, CSRF conforme auth, cache e conteúdo sensível.
6. Dados: retenção e exclusão, encryption-at-rest, backups testados, criptografia em trânsito, políticas de menor privilégio.
7. CI: políticas e scanners por linguagem, SBOM/assinatura quando ameaças justificarem, artefatos reproduzíveis, rollback e segregação de aprovações.
8. Produção: runbooks, alertas de mudança de privilégio, atividade anômala, erro, violação de rate limits, e restauração após incidente.

## Referenciais
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-61: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- CISA Secure by Design: https://www.cisa.gov/securebydesign

Não declarar aderência/certificação apenas porque um controle está listado.
