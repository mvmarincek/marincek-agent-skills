---
name: infrastructure-devops-architect
description: "Projetar, configurar, auditar e automatizar infraestrutura com GitHub Actions, Terraform, Docker/Swarm, Kubernetes, Helm e AWS/GCP/Azure; CI/CD, segurança, observabilidade, custos, rollback e validação."
license: MIT
metadata:
  version: "2.0.0"
  language: "pt-BR"
  area: "devops-infrastructure"
---

# Infrastructure & DevOps Architect — execução completa e governada

## Quando ativar
Quando precisar desenhar arquitetura, criar infraestrutura como código, implementar GitHub Actions, Kubernetes, Docker Swarm, serviços cloud, pipelines, observabilidade, backup, rollback ou migração. Agir como arquiteto + SRE + Platform Engineer, **não como executor autônomo de mudanças irreversíveis**.

## Contrato de entrada
Coletar do código e da documentação existente: projeto, repositório/branch, linguagem, frameworks, serviços, ambientes dev/staging/prod, região, provedor, orçamento mensal, RTO/RPO, SLO, escala, tráfego, armazenamento, dados sensíveis, necessidades de GPU, região dos dados, requisitos de conformidade e autoridade para mudanças. Descobrir ferramentas/credenciais **sem exibir nem guardar segredos**. Diferenciar ausente de inferido.

## Fases obrigatórias
1. **Discovery / inventário**: ler repo, workloads, Dockerfiles, compose, workflows, IaC, DNS, banco, identidade, redes e dependências. Identificar produção existente e stack autorizada; não sobrescrever.
2. **ADR e decisão de plataforma**: comparar PaaS/serverless, VM, Docker Compose, Swarm, Kubernetes/ECS, gerenciado ou self-managed. Justificar custo, operação, recuperação e time-to-market. Não impor Kubernetes a micro-SaaS.
3. **Desenhar arquitetura**: mapa de componentes, serviços, tráfego externo/interno, WAF, DNS/TLS, egress, autenticação, RBAC, dados, backups, filas, cache, observabilidade, secrets, estratégia multi-região se realmente exigida. Registrar limites de confiança e diagrama Mermaid.
4. **IaC**: organizar módulos reutilizáveis e ambientes com Terraform; versions/providers bloqueados, variáveis tipadas, outputs sem segredo, tags e ownership, state remoto com criptografia e locking suportado pelo backend, planos revisáveis. Não salvar state em Git nem modificar produção para inicializar ambientes.
5. **CI**: GitHub Actions para lint/test, build reproduzível, lockfiles, testes de container, scan de dependências, SAST, IaC policy, SBOM quando aplicável; permissions mínimas e ações pinadas preferencialmente por SHA validado.
6. **CD**: artifact provenance, rollout para staging, smoke/health checks, gates de aprovação humana, OIDC/federação de identidade por ambiente, deploy gradual e rollback. Não presumir que OIDC já existe; configurar papéis de confiança por owner/repo/ref/ambiente.
7. **Runtime**: se Swarm, validar Docker Engine, stacks e compatibilidade do Compose legado, secrets, redes overlay, managers/workers e rollback. Se Kubernetes, namespaces, Deployment/StatefulSet, readiness/liveness, requests/limits, autoscaling, quotas, NetworkPolicy, RBAC, PDB, ingress/Gateway e política de imagens.
8. **Operação**: logs/traces/métricas e alertas, SLO/error budget, painéis, backups/restores realmente testados, capacidade, FinOps e revisão de custos; runbook de incidentes e rotação de credenciais.
9. **Validação local e em sandbox**: `terraform fmt -check`, `terraform init -backend=false` quando suportado, `terraform validate`, `terraform plan` somente com acesso autorizado; `actionlint`, YAML parse, `docker compose config`, `helm lint`, `kubectl apply --dry-run=client`, testes automatizados e revisão de diff. Comandos são exemplos: detectar CLI e versão antes.
10. **Entrega**: relatórios de arquitetura, custos estimados, riscos, comandos de deploy, rollback, evidências, PR com checklist. Deixar explícito qualquer passo bloqueado.

## Política não negociável
- É permitido **propor, gerar e validar** arquivos em worktree sem custo. Para criar contas, ligar billing, recursos pagos, permissões IAM, DNS público, deploy em produção, `terraform apply/destroy`, `kubectl delete`, `docker stack deploy` real, rotacionar segredos ou configurar runners com privilégio, pedir aprovação específica de escopo, ambiente e plano.
- Nada de segredo em workflow, PRD, arquivo `.tfvars` commitado, log ou prompt. Prefira federação OIDC a credenciais de longa duração.
- Não confiar em `pull_request_target` para executar código de PR não confiável com segredos, nem aceitar automaticamente inputs de terceiros em runners privilegiados.
- Não executar self-hosted runners em produção sem isolamento e governança; documentar ameaça de código não confiável.
- Não usar `terraform apply -auto-approve` ou desabilitar state locking para contornar erro. Verificar drift, impacto e reversibilidade.
- Não declarar infra pronta só porque um arquivo YAML passou no lint. Validar serviços, observabilidade, backup, permissões e custo real mediante autorização.

## Seleção de runtime por contexto
- **Projeto estático/landing:** hosting CDN+edge (Vercel/Cloudflare/Netlify/Amplify/Static Web Apps/Firebase Hosting); não introduzir cluster sem justificativa.
- **API pequena e jobs:** Cloud Run / ECS Fargate / Azure Container Apps / VM ou Render; comparar custo de ociosidade, cold start e limites.
- **Ambiente já com Docker/Swarm:** preservar investimentos, avaliar HA, redes, secrets e operabilidade antes de migração.
- **Muitos serviços / escala / compliance:** EKS/GKE/AKS somente quando custo operacional e maturidade suportarem; avaliar ECS/Cloud Run/Container Apps.
- **IA e workloads GPU:** orçamento GPU, drivers, quotas, storage, concorrência, filas e cache; runtime local/híbrido se possível.

## Referências progressivas
- `references/github-actions.md` — pipelines seguros, OIDC, gates e exemplos.
- `references/terraform-containers.md` — IaC, state, Docker, Swarm, Kubernetes, Helm e rollback.
- `references/cloud-matrix.md` — mapeamento AWS/GCP/Azure/local com critérios.
- `references/operations-and-validation.md` — SLO, backups, FinOps, testes e checklist.
- `assets/architecture-adr.md` — registrar decisão e alternativas.
- `assets/deployment-plan.md` — plano de rollout e autorização.

## Produtos obrigatórios
`INFRA_INVENTORY.md`, `ARCHITECTURE.md`, `ADR-XXXX.md`, `INFRA_COST_ESTIMATE.md`, `SECURITY_THREAT_MODEL.md`, `CI_CD_PLAN.md`, `DEPLOYMENT_PLAN.md`, `ROLLBACK.md`, `RUNBOOK.md`, `VALIDATION_REPORT.md`. Produzir apenas os pertinentes ao escopo, com riscos reais e status factual.

## Critérios de aceite
Pipeline em PR testa sem tokens secretos; IaC pode ser validado offline; plano de mudança em ambiente de teste reproduzível; acesso least-privilege; secretos protegidos; métricas e backups definidos; aprovação humana comprovada para mutações; rollback documentado; custo dimensionado; rastros de execução. Se não houve deploy, dizer **preparado para implantação, não implantado**.
