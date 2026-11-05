# Protocolo de entrada HID

Regras para toda entrada de mouse e teclado durante o desenho.

## Princípio
Toda ação é física, via hardware USB HID do VOKI. Proibido: APIs de automação de UI, injeção de eventos sintéticos, atalhos por software de terceiros.

## Movimento e clique
- Mover o cursor em trajetória contínua observável; não teletransportar.
- Clique só após confirmação visual de que o alvo é a ferramenta correta.
- Arrasto para formas: pressionar, mover com velocidade constante e liberar no ponto final calculado.

## Trajetórias por forma
- **Retângulo**: arrasto diagonal entre cantos opostos.
- **Elipse/círculo**: ferramenta própria com arrasto diagonal; círculo exige proporção 1:1 — verificar visualmente, não presumir.

## Tolerâncias de ambiente
- DPI, resolução e escala alteram distâncias físicas: recalcular a cada execução a partir da captura atual.
- Tema claro/escuro muda contraste dos ícones: reobservar paleta antes de selecionar cor.
- Latência do aplicativo: aguardar a interface responder antes da próxima ação; não empilhar cliques.

## Anti-padrões
- Coordenadas fixas memorizadas de sessões anteriores.
- Cliques em área incerta "para ver o que acontece".
- Velocidade acima do reconhecível pela captura de verificação.
