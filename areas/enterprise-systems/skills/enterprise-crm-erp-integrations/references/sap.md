# SAP — S/4HANA, SAP BTP e integrações
## Primeiro reconhecer o produto
S/4HANA Cloud Public/Private/On-Prem; ECC legado; SuccessFactors; Ariba; SAP Business One; Business ByDesign; BTP e integração. Nunca presumir que toda API SAP é habilitada em cada produto/versão. Identificar mandante (client), empresa (company code), centros, plantas, módulos FI/CO/MM/SD/PP/HR e país.
## Interfaces suportadas conforme cenário
- Descobrir APIs e eventos suportados via SAP Business Accelerator Hub / `api.sap.com`.
- S/4HANA: OData V2/V4 e APIs released; SOAP quando publicado; RFC/BAPI somente onde permitido e com conectividade autorizada, sem acesso direto ao banco.
- SAP BTP / Integration Suite: integração, autenticação, adaptadores, monitoring; custom extensions via CAP e SAP Cloud SDK, respeitando clean core.
- ABAP: código e extensões documentadas, autorização transacional e transportes por landscape DEV→QA→PROD; verificar objetos e release strategy.
## Ciclo de implementação
1. Identificar processo, documentos SAP, estados, autorizadores e regras financeiras.
2. Definir dados mestres (Business Partner, materiais, centros), unidades, conversões, moeda, idioma, timezone e vínculo organizacional.
3. Selecionar API oficialmente lançada, checar contrato/versão e controles de acesso; prototipar no sandbox.
4. Planejar retries para operações idempotentes; usar IDs de negócio e reconciliação de documentos; não repetir lançamento contábil em timeout sem consulta de confirmação.
5. Proteger PI/financeiro/logística com segregação de papéis, auditoria, restrições de mandante e environment binding.
6. Testar eventos, erros SAP, commit/rollback, integrações via fila e consistência eventual; transportes rastreáveis.
## Antipadrões
SQL direto em tabelas produtivas, scripts que contornem transações/autorizações, acesso com SAP_ALL, mudanças massivas sem backup, expor RFC sem VPN, duplicar documentos financeiros.
## Referências
- https://api.sap.com/
- https://help.sap.com/
- https://community.sap.com/
