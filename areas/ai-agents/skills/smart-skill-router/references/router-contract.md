# Contrato do roteador
Entrada: `{task,agent,area?,available_tools?,os?,ram_gb?,gpu_vram_gb?,budget?,security_level?}`.
Saída: `{skills:[{name,reason,required_tools,limitations}],excluded,consent_required,confidence,tests_to_run}`.
A saída do roteador não equivale a executar Skills. Para tarefas críticas aplicar IAM e policy engine no serviço executor; checar tool params contra schemas.

## Política de ranking
Aplicar filtros rígidos antes da pontuação; depois combinar relevância lexical/semântica, cobertura, maturidade e custo. Penalizar redundância, fontes não auditadas e restrições de hardware. Não usar benchmarks de modelos como verdade permanente.
