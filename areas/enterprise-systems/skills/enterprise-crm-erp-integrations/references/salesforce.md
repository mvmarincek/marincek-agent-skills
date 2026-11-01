# Salesforce — playbook operacional
## Diagnóstico específico
- Determinar Sales Cloud, Service Cloud, Experience Cloud, Marketing Cloud, Data Cloud ou custom org; Enterprise/Unlimited/etc. e edição de APIs; namespaces, org ID, API version, sandbox, permission sets e limites.
- Inventariar objetos padrão/custom (`Account`, `Contact`, `Opportunity`, `Case`), relacionamentos, external IDs, validações, flows, triggers, regras de compartilhamento, perfis e CPQ/Revenue Cloud quando presentes.
- Entender FLS/CRUD, OWD, sharing, service account e Connected App/External Client App conforme configuração atual.
## Escolha técnica
- CRUD pequeno e consultas: REST API / SOQL; transações compostas: Composite API conforme limites; grandes volumes: Bulk API 2.0; eventos: Platform Events/Change Data Capture se disponíveis.
- UX Lightning: LWC, Lightning Data Service/UI API; lógica server: Apex com testes e limites de governor; automações: Flow privilegiando declarativo quando adequado.
- Integrações outbound Apex: Named Credentials/External Credentials e callouts autorizados, nunca segredos hardcoded.
- Dev lifecycle: Salesforce CLI (`sf`), metadata/source tracking, scratch orgs ou sandboxes, package deployment; confirmar CLI e metadados reais.
## Regras
1. Não escrever registros sem `externalId`/chave de deduplicação e testes de permissão.
2. Respeitar bulkification; evitar SOQL/DML em loops e consultas gigantes sem limites; não fazer fallback perigoso para privilégios administrativos.
3. Avaliar Flows e triggers existentes antes de criar outra automação; risco de recursão, dupla gravação e limites de governor.
4. Em migração, definir batch size, ordem de objetos, hierarquia, tratamento de ownership, picklists, dados sensíveis e rollback.
5. Validar ordem de atualização de Contact/Account/Opportunity/Case, auditoria e reconciliação por external ID.
## Testes
- Apex unit tests, permissões negativas, mocks HttpCalloutMock, dados artificiais de sandbox, idempotência, volume, Platform Events replay e erro de limite.
- Conferir execução de Flow e feedback de usuários-chave; requerem credencial/tenant existente.
## Referências oficiais
- https://developer.salesforce.com/docs
- https://developer.salesforce.com/docs/platform/api-asynch/guide/asynch-api-intro.html
- https://developer.salesforce.com/docs/platform/lwc/guide/data-api-calls-apex.html
- https://developer.salesforce.com/tools/salesforcecli
