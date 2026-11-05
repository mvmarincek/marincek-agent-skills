---
name: paint-draw-shapes
description: "Executar e verificar desenho de formas geométricas no Paint por observação visual e ações USB HID físicas do VOKI: círculo, elipse, retângulo, com cor, posição e tamanho, verificação antes/depois e recuperação limitada autorizada."
license: MIT
metadata:
  version: "1.1.0"
  language: "pt-BR"
  area: "automation-hid"
---

# Paint Draw Shapes — Desenho de Formas no Paint via VOKI

> STATUS: `verified-structure`. Exemplo operacional executado por hardware; cada execução exige verificação visual própria. Não confiar em coordenadas fixas.

## Quando ativar
Quando o usuário pedir desenho de formas geométricas no Paint (ou app equivalente) executado pelo VOKI: `desenhe um círculo`, `faça um retângulo azul`, `desenhar elipse`, `forma no Paint`. Também como exercício-base para validar o pipeline visual + HID antes de tarefas mais complexas (ver `voki-visual-geometry-cad`).

## Regra de arquitetura imutável
O VOKI usa **exclusivamente hardware USB HID físico** para mouse e teclado. Nenhuma automação de interface por software (API de acessibilidade, injeção de eventos sintéticos, scripts de UI). Esta regra não é negociável e vale para todo o pipeline.

## Definição operacional
Desenhar uma forma geométrica no Paint significa: observar a tela real, localizar visualmente as ferramentas, selecionar forma/cor por entrada física HID, arrastar com trajetória adequada e **verificar por captura de tela** que a forma, cor, posição e tamanho correspondem ao pedido. Sucesso sem evidência visual não é sucesso.

## Contrato de entrada
- `shape`: círculo, elipse, retângulo ou outra forma suportada pelo aplicativo.
- `color`: cor solicitada (nome ou aproximação visual).
- `position`: região relativa do canvas (não coordenadas absolutas).
- `size`: dimensões desejadas (relativas à área visível).
- Autorização de Undo: se o usuário autorizou desfazer tentativas incorretas que possam afetar conteúdo existente.

## Pipeline obrigatório
1. **Pré-condições**: confirmar aplicativo, versão e estado por captura visual; confirmar dispositivo USB HID conectado e autorizado; garantir canvas visível e sem diálogos sobrepostos; checar dados sensíveis na tela antes de gravar evidências.
2. **Observação inicial**: capturar a tela e recuperar memória visual relevante para este layout/versão (tema, DPI, resolução).
3. **Seleção de ferramenta**: identificar **visualmente** a ferramenta de formas e acessá-la somente com entrada HID física, conforme `references/hid-input-protocol.md`.
4. **Seleção de cor e espessura**: localizar paleta, selecionar e confirmar a indicação visual de seleção.
5. **Cálculo de área**: identificar área livre e calcular coordenadas relativas **a partir da tela atual** — nunca coordenadas fixas memorizadas.
6. **Execução do arrasto**: movimento físico USB HID com trajetória e velocidade adequadas à forma.
7. **Verificação**: capturar a tela pós-execução e comparar forma, cor, posição e tamanho com o pedido, conforme `references/visual-confirmation.md`.
8. **Recuperação**: em caso de falha, registrar o motivo, reobservar e aplicar recuperação limitada conforme `references/recovery-undo-policy.md` — no máximo 3 tentativas, depois escalar ao usuário.
9. **Registro**: gravar episódio e evidências com metadados, sem expor dados privados.

## Segurança e permissões
- Nunca insistir indefinidamente nem clicar em local incerto.
- Não executar Undo se puder apagar conteúdo não pertencente à tarefa, sem autorização explícita.
- Não gravar ou compartilhar screenshots com dados sensíveis sem aprovação.
- Não promover a skill para confiável após um único sucesso; promoção exige a bateria de testes abaixo.
- Limite de tentativas por forma: 3; excedido, parar e reportar estado.

## Variações e tolerâncias
- Versões do Paint / janela maximizada ou não / tema claro-escuro / DPI e resolução distintos.
- Reclassificar interface e solicitar intervenção humana quando a confiança visual for baixa.

## Testes antes da promoção
- Desenho com variações de forma, cor e tamanho.
- Mudança de resolução, janela, versão e layout entre execuções.
- Recuperação de seleção incorreta com Undo autorizado e não autorizado.
- Limite de tentativas e parada pelo usuário respeitados.

## Referências e artefatos
- `references/visual-confirmation.md` — evidências de sucesso e falha.
- `references/hid-input-protocol.md` — protocolo de entrada física, trajetórias e tolerâncias.
- `references/recovery-undo-policy.md` — recuperação, política de Undo e limites de tentativa.

## Critério de aceite
Forma visível e reconhecível com cor e posição consistentes; verificação antes/depois registrada com evidência; entrada 100% USB HID física; recuperação dentro dos limites; nenhuma ação destrutiva sem autorização; episódio documentado para reexecução.
