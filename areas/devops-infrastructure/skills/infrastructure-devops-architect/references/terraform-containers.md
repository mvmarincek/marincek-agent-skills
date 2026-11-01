# IaC, Swarm, Kubernetes e entrega confiável

## Terraform
Arquitetura preferencial: `infra/modules/{network,iam,compute,db,observability}/`, `infra/environments/{dev,staging,prod}/`; provider e lockfile; outputs explicitamente classificados; tags; policy-as-code. Backend state remoto criptografado e com locking quando suportado. Estado não é artefato de CI público; outputs sensíveis não entram em logs. `terraform import` e `moved` blocks devem ser considerados para recursos existentes; evitar recriação involuntária. Nunca commitar plan com segredos inadvertidos.

Checkpoints: `terraform fmt -check -recursive`, `terraform init -backend=false`, `terraform validate`, lint (`tflint`/`checkov` se aprovados), plan em ambiente autorizado, `terraform show` para revisão, apply só depois de aceite. Usar `-lock=false` apenas em contexto excepcional e autorizado; padrão é locking.

## Docker Compose e Swarm
Compose é bom para ambiente local e poucas instâncias, mas `docker compose up` não substitui `docker stack deploy` para Swarm. Swarm usa managers/workers, overlay networks, deploy replicas, secrets/configs, health checks e rollback. `docker stack deploy` aceita subset legado do formato Compose (não pressupor todas as opções Compose modernas). Revisar serviços stateful/volumes, disponibilidade do manager, firewall, registry, TLS e descoberta de serviços. Gerenciar join tokens como segredos.

## Kubernetes
Workloads declarativos; namespace por limite de confiança, RBAC mínimo, NetworkPolicy com CNI que as aplique, Pod Security Admission, serviceAccount restrita, no privileged pods, secrets externos; requests/limits, probes, HPA, PDB, rollout/rollback, Helm lint/template, políticas e autoscaling. StatefulSet/CSI para dados quando operacionalmente justificável; frequentemente banco gerenciado mais simples. Monitorar etcd/control plane como responsabilidade diferente em clusters auto-gerenciados.

## Helm e GitOps
Helm charts com values por ambiente sem segredos, smoke tests e `helm upgrade --atomic` somente depois de plano aprovado. GitOps Flux/Argo CD opcional quando equipes e clusters justifiquem; evitar duplicar controladores deploy do Actions.

Referências: https://developer.hashicorp.com/terraform/language/state/locking ; https://docs.docker.com/engine/swarm/stack-deploy/ ; https://kubernetes.io/docs/concepts/ ; https://helm.sh/docs/
