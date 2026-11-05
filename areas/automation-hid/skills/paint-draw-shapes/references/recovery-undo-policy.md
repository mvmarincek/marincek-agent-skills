# Política de recuperação e Undo

## Limites de tentativa
- Máximo de 3 tentativas por forma; excedido, parar, registrar estado e escalar ao usuário.
- Cada tentativa deve começar por nova observação da tela — nunca repetir cegamente a ação falha.

## Quando Undo é permitido
- Somente com autorização explícita do usuário quando o undo puder afetar conteúdo anterior da sessão.
- Permitido sem autorização extra apenas quando a área de desenho está comprovadamente vazia antes/depois da própria tentativa.

## Classificação de falha comum
| Sintoma | Causa provável | Recuperação |
|---|---|---|
| Forma não aparece | Ferramenta errada não selecionada | Reobservar seletor, selecionar de novo |
| Cor errada | Paleta não confirmada visualmente | Reabrir paleta, confirmar indicador |
| Forma deformada | Trajetória ou velocidade inadequada | Redesenhar com trajetória corrigida |
| Forma em local errado | Cálculo de área baseado em tela desatualizada | Recapturar, recalcular posição relativa |
| Nada responde | Diálogo sobreposto ou app travado | Capturar tela, classificar, escalar se fora de escopo |

## Registro
Toda recuperação registra: tentativa, sintoma observado, causa provável, ação tomada e resultado. Evidências antes/depois anexadas ao episódio, sem dados privados.

## Rollback total
Se a tarefa comprometer o arquivo (ex.: desenho sobre conteúdo existente), o rollback é fechar sem salvar **somente com aprovação** — descartar trabalho do usuário nunca é automático.
