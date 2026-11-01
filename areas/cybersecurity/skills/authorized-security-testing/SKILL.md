---
name: authorized-security-testing
description: "Planejar e realizar testes controlados e autorizados de vulnerabilidades em sistemas próprios/laboratórios, com descoberta passiva, testes de configuração/autorização, validação não destrutiva, documentação de evidências, correção e reteste."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  domain: "defensive-security-testing"
---

# Testes de segurança autorizados — evidência antes da conclusão

## Quando usar
Quando o proprietário do sistema solicita avaliação de vulnerabilidades, red team controlado, revisão de segurança em desenvolvimento, auditoria de API ou laboratório; complementar à `defensive-cybersecurity` (correções) e `agent-reliability-governance` (políticas e observabilidade).

## Consentimento e limites
- Só atuar sobre **ativos explicitamente autorizados**, com ambientes, hosts, aplicações, contas de teste, janela, métodos e objetivos definidos. A existência de domínio público não é autorização.
- Nunca ampliar escopo por descobertas: subdomínios, provedores, terceirizados, produção e tenants de terceiros exigem inclusão expressa.
- Preferir **staging, testes isolados, dados sintéticos e modo passivo**; aprovação específica antes de varredura ativa ou carga em serviço.
- Bloquear ações destrutivas, DoS, credential stuffing, brute force, persistência, evasão de monitoramento, movimentação lateral, exportação de dados reais, payloads irreversíveis e exploração que possa afetar usuários.
- Senhas, chaves e dados reais não entram em relatórios, logs, memória ou prompts.
- Se não houver autorização comprovável, limitar-se à revisão do código fornecido, modelagem de ameaças e recomendações, sem interagir com alvo externo.

## Procedimento de avaliação
1. **ROE — rules of engagement:** confirmar responsável, ativos, URLs/endereços, data/hora, taxa máxima de requisições, restrições, contatos de emergência, contas dedicadas, monitoramento e critério para parar imediatamente.
2. **Inventário defensivo:** tecnologias conhecidas, endpoints documentados, autenticação, fluxos de dados, TLS, cabeçalhos, dependências, IaC, CI e contas/roles de teste.
3. **Hipóteses:** ASVS/OWASP como referência; testar primeiro configuração, segurança de dependência, segredo em histórico, isolamento de tenants e autorização por recurso, usando dados sintéticos.
4. **Descoberta segura:** priorizar análise estática, lockfiles, SBOM e configuração. Em ambiente explicitamente autorizado, permitir somente probes leves de conectividade e verificação de headers/certs com limite de taxa e timeout.
5. **Validação de achados:** reproduzir com testes de unidade/integração ou requests inofensivos em staging; registrar evidência mínima. Nunca coletar prova por exfiltração real. Se somente houver indício, rotular `suspeita/não confirmada`.
6. **Classificar:** contexto do negócio, probabilidade, impacto e acessibilidade; CVSS como insumo opcional, não como verdade absoluta.
7. **Remediar:** patch mínimo, testes de regressão, tests de isolamento, mudança de configuração e procedimento de rollback. Não alterar produção sem autorização.
8. **Retestar:** repetir apenas testes aprovados e comparar before/after; registrar resultados, falsos positivos, cobertura e riscos residuais.
9. **Reportar:** responsável, escopo, data, ferramenta/versão, achados, evidências redigidas, severidade, status de correção e reteste.

## Matriz rápida por categoria
- **Aplicação/API:** autenticação, autorização por objeto e por função, validação de entrada, sessão, webhooks, SSRF, upload, CORS/CSP e rate-limit.
- **Infra/cloud:** exposição não pretendida, IAM, storage público, configuração TLS, segredos, logs, backups e políticas de rede.
- **Dependências/supply chain:** versões com advisories, provenance, SBOM, lockfile, integridade de scripts e pipeline.
- **Agentes/MCP:** prompt injection em dados não confiáveis; tool permissions; separação tenants; abuso de limites; auditoria e aprovações.

## Ferramentas e execução
- CodeQL/Semgrep/Gitleaks/Trivy/OSV-Scanner: preferíveis em projeto e repositório autorizados.
- OWASP ZAP baseline: apenas em staging explicitamente autorizado, com limitação de tráfego; não usar scan ativo por padrão.
- Nuclei: somente templates benignos e revisados individualmente, sem varreduras amplas ou automáticas fora de escopo.
- Testes automatizados internos (pytest/Jest/Playwright) para controlar casos de autorização e regressão.
- Capturas de HTTP devem usar contas e dados sintéticos; redigir cookies, tokens e PII.

## Segurança operacional
- Recolher as permissões antes da ação; empregar allowlist; watchdog de taxa e tempo; pause/stop imediato; trilha de auditoria.
- Comportamento inseguro ou não permitido em uma tool MCP deve ser bloqueado em código, não apenas nesta Skill.
- Nunca informar que “não há vulnerabilidades”: relatar somente o escopo e a cobertura obtidos.

## Referências
- `references/rules-of-engagement.md`: escopo e autorização.
- `references/test-matrix.md`: matriz de testes, resultado e regressão.
- `references/cloud-checks.md`: controles local/AWS/GCP/Azure.
- `assets/finding-template.md`: achado reproduzível sem dados reais.

## Aceitação
[ ] ROE validada; [ ] execução ficou no escopo; [ ] testes não destrutivos; [ ] evidências minimizadas; [ ] achados verificáveis; [ ] correções testadas; [ ] riscos residuais documentados; [ ] nenhuma alegação não testada.

## Entregáveis
Relatório de vulnerabilidades com escopo autorizado, evidências sanitizadas, severidade, reprodução controlada, propostas de correção e regressão, além de declaração sobre limites e testes não realizados.
