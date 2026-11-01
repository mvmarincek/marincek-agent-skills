# Validação orientada por screenshot

## Níveis de evidência
- L0: apenas intenção do agente; não é validação.
- L1: ação HID confirmada pelo controlador; não prova estado da UI.
- L2: screenshot pós-ação compatível com mudança pretendida.
- L3: interface confirma propriedades numéricas e feature tree; coerência com screenshot.
- L4: verificação adicional por vistas/propriedades/arquivo exportado sob autorização, ou intervenção humana.

## Loop de recuperação
Observar → identificar estado atual → validar precondições → escolher ação HID única → capturar → analisar diferenças → classificar `success`, `partial`, `failed`, `uncertain` → corrigir ou parar. Limitar retries (ex.: 3) e tempo total; abortar em janela desconhecida, modal inesperado ou ação destrutiva.

## Registro de episódios
`timestamp`, `goal`, `app`, `app_version`, `ui_state_before`, `hid_actions`, `ui_state_after`, `validation_level`, `confidence`, `failure_code`, `resolution`, `evidence_ids`, `skill_version`. Hash de screenshots e medidas; guardar imagens brutas somente com prazo e acesso definidos.
