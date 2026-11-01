---
name: paint-draw-shapes
description: Executar e verificar desenho de formas geométricas no Paint por observação visual e ações USB HID físicas.
---

# Paint — desenhar formas (exemplo de Skill candidata)

> STATUS: `candidate`. Exemplo conceitual **não testado** no VOKI. Não confiar em coordenadas fixas.

## Parâmetros de entrada

- `shape`: círculo, elipse, retângulo ou outra forma suportada.
- `color`: cor solicitada.
- `position`: região relativa do canvas.
- `size`: dimensões desejadas.

## Pré-condições

1. Confirmar aplicativo e versão/estado por captura visual.
2. Confirmar dispositivo USB HID autorizado, conexão válida e tools de observação disponíveis.
3. Garantir canvas visível; identificar possíveis diálogos, mudanças de UI ou dados sensíveis antes de gravar screenshots.

## Procedimento orientado a estados

1. Observar a tela atual e recuperar memória visual relevante para essa versão/layout.
2. Identificar **visualmente** a ferramenta de formas e verificar se pode ser acessada.
3. Selecionar a forma solicitada usando **somente** tools HID autorizadas.
4. Localizar e selecionar cor; verificar a indicação visual de seleção.
5. Identificar área livre e calcular coordenadas relativas a partir da **tela atual**.
6. Executar movimento/arrasto físico USB HID com trajetória adequada.
7. Capturar a tela, verificar correspondência da figura, da cor e da posição.
8. Se houver falha, registrar o motivo, reobservar e tentar recuperação limitada e segura.
9. Registrar episódio e evidências com metadados, sem expor dados privados.

## Critérios de sucesso

- Forma visível e reconhecível; cor e posição consistentes com pedido.
- Evidências de antes/depois acessíveis ao usuário dentro das permissões.
- Nenhum executor de interface por software foi usado.

## Variações e tolerâncias

- Aplicativo versão X/Y; janela maximizada ou não; tema claro/escuro; escala DPI e resolução distintas.
- Permitir reclassificar interface e solicitar intervenção se confiança visual baixa.

## Falhas e segurança

- Nunca insistir indefinidamente nem clicar em local incerto.
- Não executar Undo se puder apagar conteúdo não pertencente à tarefa sem autorização.
- Não promover automaticamente para confiável após um único sucesso.

## Testes antes da promoção

- Teste de desenho com variações de forma/cor/tamanho.
- Teste com mudança de resolução/janela, versão/layout.
- Teste de recuperação de seleção incorreta.
- Teste de limitação de tentativas e parada pelo usuário.

## Entregáveis
Registro de tarefa, screenshots antes e depois, validação visual e procedimento de reexecução.
## Referências
Consulte `references/visual-confirmation.md` para evidências de sucesso e falha.
