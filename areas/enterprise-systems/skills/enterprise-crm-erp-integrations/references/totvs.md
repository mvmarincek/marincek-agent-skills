# TOTVS — Protheus, Datasul, RM, Fluig
## Descoberta obrigatória
Identificar produto (Protheus, Datasul, RM, Fluig), release, patch, ambiente (DB, AppServer, REST), empresas e filiais, módulos, dicionário de dados, customizações e licença. A TOTVS não é uma API uniforme; evitar aplicar AdvPL a todos os produtos.
## Protheus
- Investigar APIs padrão em https://api.totvs.com.br/ e catálogo de developers; preferir APIs oficiais existentes.
- Personalizações Protheus usam AdvPL/TLPP e serviços REST com AppServer configurado; analisar pontos de entrada, métodos, workareas, locks, transações e filial compartilhada antes de alterar.
- Respeitar versões suportadas, índices, integridade de registros, empresa/filial, rotinas de contabilização e nota fiscal.
- Examinar regras de produto sem criar manipulações SQL que ignorem o framework transacional.
## Datasul/RM/Fluig
- Datasul: confirmar stack OpenEdge/Progress e interfaces/REST específicas da versão; não supor compatibilidade Protheus.
- RM: conferir serviços/WebServices publicados e documentação oficial; evitar inventar endpoints.
- Fluig: APIs e workflows/documentos/autorização; checar lifecycle de documentos, usuários e permissões.
## Implementação segura
1. Inventariar endpoints reais e token/credencial no cofre.
2. Contrato por filial, tenant, versão e entidade; timezone, moeda, cadastro fiscal e campos obrigatórios.
3. Upsert com chave externa, paginação, idempotência, fila, compensação e reconciliação.
4. Dados reais somente em ambiente aprovado; transações fiscais/contábeis exigem revisão especializada.
5. Homologar layout de XML/NFe, estoque e financeiro antes da produção quando afetados.
6. Monitorar erros de AppServer/serviços, respostas REST e impacto de customizações.
## Referências oficiais
- https://developers.totvs.com/
- https://api.totvs.com.br/
- https://tdn.totvs.com/
