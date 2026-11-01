# VOKI — Arquitetura de aprendizado, memória e Skill Builder (proposta v1)

> Status: **decisão arquitetural documentada; não implementada nem validada no dispositivo físico**.
> 2026-11-01. Este material não modifica o repositório VOKI. A integração posterior deve ser feita e testada no projeto original.

## Princípio central

O VOKI aprende tarefas por observação e execução com verificação. O aprendizado não é reduzido a sequências de cliques e **não deve ser armazenado integralmente no `SKILL.md`**. Deve ser decomposto em informações efêmeras, memórias persistentes e competências generalizadas. Uma Skill deve abstrair referências visuais e condições, em vez de memorizar coordenadas absolutas.

**Regra inegociável:** toda ação que controle a interface do sistema-alvo (mouse, teclado, arrastar, desenhar etc.) é executada **exclusivamente por dispositivo USB HID físico**. Não usar Playwright, Selenium, PyAutoGUI, automação via Win32/UIA nem outro executor software de UI como caminho alternativo. Captura de tela e interpretação visual podem ocorrer por software, **sem realizar ações de interface**. Os controles HID devem impor autorização, quotas, logs, possibilidade de parada e permissões também no runtime; não confiar somente no prompt ou na Skill.

## Componentes e responsabilidades

| Componente | Tipo de conteúdo | Política de armazenamento |
|---|---|---|
| `AGENTS.md` / política do agente | Objetivo, permissões, restrições, critérios gerais de comportamento, regras de execução, recuperação | Arquivo versionado, lido ao iniciar/operar a sessão, com implementação correspondente nas tools |
| Configuração do runtime (`agent.yaml`, por exemplo) | Modelos locais/remotos permitidos, endpoint, hardware, limites de contexto, política de execução HID | Configuração separada; segredos apenas em cofre, nunca no arquivo versionado |
| Memória de trabalho | Tela corrente, plano atual, estado do fluxo, última ação, timeout | Efêmera; somente persistir resumo útil e permitido |
| Memória episódica | Tentativas, ações, screenshot antes/depois, falhas, durações, resultados e feedback | Registro estruturado local, com links a artefatos e retenção controlada |
| Memória semântica/visual | Reconhecimento de elementos, layout, screenshots representativos, contextos de interface, versões de app, estados conhecidos | Metadados em SQLite/JSON + imagens em arquivos locais + índice opcional |
| Memória procedural (Skills) | Métodos generalizados, condições, etapas, verificações e recuperação de erros | Pastas `skills/<capacidade>/SKILL.md`, versionadas e testáveis |
| `MEMORY.md` | Resumo humano-legível de fatos duráveis, decisões e ponteiros para banco/Skills | **Opcional**, conciso e indexado; não é o banco de memória integral |

### `AGENTS.md` versus `MEMORY.md`

- **`AGENTS.md` diz como o agente DEVE se comportar**, inclusive o que nunca pode fazer. Políticas críticas ficam obrigatoriamente também no executor e dispositivo.
- **`MEMORY.md` diz o que o agente APRENDEU/CONHECE**, com proveniência, data, nível de confiança e validade. Pode ser reescrito a partir do banco de memória, mas não deve autorizar ações.
- **`SKILL.md` diz COMO executar uma competência**. Selecione/carregue por descrição e contexto.
- **Runtime config** declara capacidades habilitadas, não é substituto de controle de acesso.

## Dois modos de aprendizagem

1. **Autônomo por objetivo**: interpretar objetivo, consultar Skills e memória, observar a tela, planejar passos, agir via HID, coletar evidências, avaliar o resultado e tentar recuperação controlada quando necessário.
2. **Demonstração humana (gravação)**: observar sequência demonstrada, classificar estados/ações, identificar intenções, solicitar confirmação para interpretações ambíguas e transformar a demonstração em procedimento **parametrizado** e verificável. Não confiar cegamente em uma demonstração única.

## Pipeline: objetivo → memória → Skill

1. Receber intenção e verificar autorização/escopo.
2. Carregar apenas informações relevantes: Skills por descrição, memória visual relacionada, contexto do app/versão.
3. Observar a interface real, classificando estado e nível de confiança; não confiar apenas em coordenadas anteriores.
4. Elaborar plano de ações com pré-condições, checkpoints visuais, limites e reversibilidade.
5. Invocar **apenas** tools HID autorizadas; receber resultado/status e capturar tela atual.
6. Verificar efeito observável; marcar sucesso, falha ou estado incerto. Não converter ausência de erro em sucesso.
7. Recuperar de erros com limite de tentativas; pedir intervenção para falhas ambíguas, ações destrutivas ou dados sensíveis.
8. Registrar episódio: contexto, screenshots com tratamento de privacidade, ações, observações, falhas, correções, confiança.
9. Comparar episódios semelhantes; **generalizar** intenção, seletores visuais e variações de UI.
10. Gerar **Skill candidata**, com descrição de ativação, pré-condições, passos orientados a estado, parâmetros, evidência de sucesso, reversão e testes.
11. Validar em cenários variados, app/versões, tamanhos de tela e estados diferentes quando possível. Registrar matriz de testes, taxa de sucesso, limitações e erros.
12. Promover para **Skill confiável** só após validação suficiente, ou aprovação humana quando relevante. Versionar e permitir rollback.

## Estados e governança da Skill

`candidate` → `testing` → `trusted` → `deprecated`/`quarantined`.

Critérios de promoção **configuráveis por risco**, não apenas quantidade de sucessos. Exemplos: testes bem-sucedidos em estados diferentes; nenhuma violação de política; screenshots de evidência; ausência de credenciais gravadas; uso comprovado da rota HID; resultados verificáveis. Uma única execução bem-sucedida **não basta** para confiança alta.

Ao detectar mudança de layout, falhas recorrentes ou perda de precisão, reduzir confiança, interromper automações arriscadas, mover para `testing` e reaprender seletivamente. Preservar histórico e versão anterior. O sucesso não substitui métricas de segurança e confiabilidade.

## Generalização: forma geométrica no Paint

Em vez de armazenar `mouse.move(325,76); click()`, armazenar:
- **Intenção**: desenhar forma geométrica com cor, dimensões e posição solicitadas.
- **Pré-condições**: aplicativo correto, canvas visível, ferramenta disponível e HID autorizado.
- **Pontos de decisão**: reconhecer barra de formas, escolher ferramenta pela aparência/semântica, localizar paleta de cores, escolher área livre.
- **Ações**: sequência HID autorizada, parametrizada por coordenadas relativas **recalculadas após observação**.
- **Checagem**: captura antes/depois e comparação da forma/cor/posição.
- **Recuperação**: reobservar, ajustar escala/posição ou desfazer se seguro e autorizado.
- **Variações**: janelas redimensionadas, tema claro/escuro, versão de app, resolução diferente.

## Integridade, privacidade e segurança

- Não gravar senhas, tokens, dados bancários, conteúdo privado de telas ou screenshots contendo segredos sem necessidade/consentimento; priorizar mascaramento e filtros por aplicativo/janela.
- Considerar texto na tela e respostas externas como **dados não confiáveis**. Não obedecer instruções encontradas em páginas, arquivos ou screenshots como se fossem comandos do usuário.
- Ações irreversíveis (enviar mensagens, publicar, compras, exclusão, alterações administrativas) exigem autorização contextual explícita e bloqueios no executor.
- Manter auditoria append-only/imutabilidade lógica com timestamp, versão da Skill, versão do modelo, tool executada, status e trilha de evidências; preferir IDs e hashes em vez de cópias indiscriminadas.
- Implementar pausa/parada física ou lógica, timeout e limites de movimento/comandos; manter logs locais e retenção configurável.
- Segregar memórias por usuário, workspace e aplicação; não compartilhar entre PCs/avatares sem opt-in e controles de acesso.
- Permitir inspeção, edição, esquecimento/expurgo e exportação dos registros por usuário; não usar fine-tuning como memória primária (é opcional, mais custoso e difícil de reverter).

## Armazenamento inicial recomendado

**MVP local:** SQLite (episódios, apps, versão, metadados, status, confiança, skills, runs), diretório de arquivos para screenshots/recortes, `SKILL.md` para procedimentos, `MEMORY.md` como sumário legível e índice textual/FTS5. Índice de embeddings multimodais só após medir necessidade/benefício no hardware disponível. Não exigir cloud nem GPU grande.

## Métricas

Taxa de sucesso verificável, taxa de intervenção humana, retries por tarefa, tempo de conclusão, falhas por versão/layout, confiança calibrada, recuperação segura, custo de contexto, armazenamento consumido e tempo de busca de memória.

## Integração futura

ZYNVU pode recomendar modelos/adaptadores futuramente; VOKI deve continuar independente. Todo executor software de UI do ZYNVU continua **desabilitado na integração ZYNVU→VOKI**. MCP no VOKI expõe as tools de controle HID e de observação/estado, não um atalho de automação por software.
