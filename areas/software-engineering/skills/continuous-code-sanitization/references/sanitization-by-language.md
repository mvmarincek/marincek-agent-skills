# Sanitização por linguagem e fronteira de confiança
## Transversal
Validação de entrada deve ser de allowlist/schema; encoding/escaping deve ser contextual (HTML, JS, URL, SQL). Nunca sanitizar com uma função genérica para qualquer contexto. Preferir APIs parametrizadas e serializers seguros. Comprovar controle de acesso *por objeto e por tenant*, não apenas autenticação.
## React/Next/TypeScript
- Validar input no servidor (Zod, Valibot, schemas); tipos TypeScript não validam dados externos em runtime.
- XSS: JSX já escapa texto, mas HTML bruto (`dangerouslySetInnerHTML`) exige sanitização HTML madura; revisar event handlers, URL javascript:, SSRF em fetch server.
- API routes e server actions: session/authz, CSRF onde aplicável, rate limit, idempotency, safe redirect, logging seguro; credenciais fora do bundle.
- SQL: queries parametrizadas/ORM; controle transacional, migração revisada.
## Python
- Pydantic/dataclasses para schema com limites; SQL parametrizado, nunca f-string; subprocess com argumentos fixos sem `shell=True` a menos que justificado.
- Evitar pickle em dados não confiáveis; arquivos com safe paths e limite; segredos fora de logs. Ruff, mypy, Bandit, pytest com parametrização e fuzz leve.
## Java/.NET/Go
- Queries parametrizadas; serialização segura; dependency updates; authz por objeto; validação de DTO; proteção contra path traversal; timeouts e recurso máximo.
## Infra e agentes
- YAML Actions com permissions mínimas; GitHub OIDC; permitir ferramentas explicitamente e não deixar agente executar comandos arbitrários com credenciais de produção.
- MCP: autenticação/escopo de cada ferramenta, schema de parâmetros, logging redigido, allowlist de destinos, aprovação para operações destrutivas.
## Padrão de teste
Para cada alteração, anexar teste de abuso negativo e de cenário legítimo; garantir que a proteção não quebre o caso de uso válido.
