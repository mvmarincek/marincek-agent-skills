# Prompt Codex — configurador 3D com manufatura conectada

No repositório de uma landing page existente ou nova, aplique as skills `immersive-commerce-3d`, `made-to-order-manufacturing-twin`, `realworld-order-digital-twin`, `photoreal-3d-assets` e `immersive-experience-quality` do catálogo MVMarincek. `gamified-landing-page` cuida de CTA/SEO/marketing; use `tactile-3d-interactions` apenas onde houver manipulação física.

OBJETIVO: experiência premium fotorrealista, com produto configurável e compra integrada a uma jornada 3D pós-venda sincronizada por marcos de produção **verdadeiros**. Exemplo automotivo: cliente escolhe pintura, rodas e interior; visualiza exatamente a configuração em GLB; após validar preço/especificação e pagamento, vê a sua ordem percorrer cenários 3D de carroceria, pintura, montagem final, inspeção e expedição à medida que o backend confirma os eventos reais. Nunca declarar filmagem do próprio carro ou produção instantânea sem evidência.

ENTREGAS POR GATES:
- G0 inventário da landing existente, fluxo checkout, ERP/MES, permissões e baseline.
- G1 montar UM vertical slice 3D funcional: mudar pintura e rodas, persistir config e desfazer, inspeção de objetos no runtime e alternativas mobile.
- G2 backend de catálogo/CPQ/regras de variantes e preço; checkout seguro com pedido persistido.
- G3 simular `manufacturing events` em ambiente DEMO/STAGING, demonstrar estados com labels evidência e timestamp, reconexão, event idempotency, estado atrasado, hold de qualidade.
- G4 integrar ERP/PLM/MES somente com API autorizada, evento por ordem ou unidade quando comprovado, segregação OT. Nenhum browser público tem acesso direto à linha de produção.
- G5 testes E2E, vídeo gravado do runtime, performance medida, legibilidade/acessibilidade, regressão de conversão e aprovação humana antes de publicar.

Não tratar imagens geradas por IA como jogo executável. Não instalar MCP de terceiros, configurar custos ou mexer em produção sem aprovação explícita. Entregar PR com testes PASS/FAIL/NOT_TESTED, riscos e fontes, diffs e documentação de limitação de acesso.
