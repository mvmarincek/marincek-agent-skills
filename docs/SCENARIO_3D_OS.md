# Scenario 3D OS — curadoria técnica (01/11/2026)

**Origem oficial:** https://github.com/scenario-labs/skills  
**Guia de instalação:** https://github.com/scenario-labs/skills/blob/main/INSTALL.md  
**Blender Expert:** https://github.com/scenario-labs/skills/blob/main/skills/dcc/blender/README.md

## O que foi confirmado

Scenario lançou a biblioteca de skills open source com o nome **3D OS**, divulgada como um estúdio de produção 3D para agentes, estruturado em **6 departamentos e 80 skills**. Os departamentos são Animation, Art, Modeling, Look Dev & Lighting, Worlds e Pipeline. O GitHub oficial chama o conjunto de **Scenario Agent Skills** e contém tanto habilidades que dependem do Scenario MCP quanto famílias Expert Tools executadas com software local. **Cadastrar como um pacote único**, não inflar a contagem com 80 entradas.

## Duas famílias diferentes de dependências

**(A) Scenario MCP:** as skills `scenario-image`, `scenario-3d`, `scenario-consistency`, `scenario-identity-library`, `scenario-video`, `scenario-storyboards`, `scenario-walkable-room`, entre outras, usam o serviço Scenario. É necessário conectar MCP com uma conta (OAuth ou API key), e a geração com modelos hospedados pode custar créditos. Skills abertas não representam inferência grátis.

**(B) Expert Tools locais:** famílias para Blender, Maya, ZBrush, Unreal, Unity, Godot e Roblox operam instalações dos aplicativos, sem exigir Scenario MCP conforme README. Para **Blender**, documentação descreve **15 skills** (1 router e 14 especialistas), scripts Python, suporte a headless e live, Blender 5.2 LTS, e 12 suítes de testes headless aprovadas no ambiente dos autores (5.2.1). Não foi executado teste nesta biblioteca ou no PC do usuário.

## Aplicação prioritária

- **You8:** padronização dos personagens 3D, rigging, expressão, motion, storyboard, iluminação, integração de sequências. Começar com `scenario-blender-expert`, `scenario-blender-rigging`, `scenario-blender-animation`, `scenario-blender-previs-storyboard` e `scenario-blender-export` (a família requer arquivos vizinhos). Para geração por imagem, avaliar custos de `scenario-3d` e `scenario-identity-library` antes de contratar serviço.
- **GITFY:** assets e cenários otimizados em GLB/glTF para Three.js/React Three Fiber, níveis de detalhe, materiais PBR, export e teste de desempenho. Priorizar `scenario-blender-export`, `scenario-blender-geometry-nodes`, `scenario-blender-lighting-rendering` e `scenario-blender-hard-surface`.
- **VOKI:** somente pesquisa. Qualquer ação de UI no fluxo VOKI continua exclusivamente via USB HID físico; as skills locais de Blender que automatizam UI por software não podem ser executores do VOKI.

## Como instalar quando autorizado

Inspecionar o código do commit e escolher as skills pelo menu:

```bash
npx skills add scenario-labs/skills
```

Selecionar **Expert tools: Blender** para instalar a família local como conjunto. O README lista também um comando explícito com todos os 15 nomes. Requisitos: Node.js/npx para instalador e Blender 5.2 LTS para operação local. Sem necessidade de conectar Scenario MCP para o subconjunto Expert Tools local.

Para Scenario MCP (outro fluxo), exemplo oficial:

```bash
claude mcp add --transport http scenario https://mcp.scenario.com/mcp
```

Este comando requer conta/credencial Scenario. **Não executado aqui**.

## Ressalvas de produção

- Rigging, limpeza de malha, UV, deformação e consistência de personagens exigem revisão, especialmente para animações longas.
- O repositório descreve limites do Blender headless: escultura pode ficar na qualidade de conceito; certas operações de cabelo e Grease Pencil precisam sessão visual; face loops detalhados precisam revisão humana.
- Rodar Blender não garante poder de gerar vídeo/modelos por inferência local na GPU GTX 1650 4 GB. Diferenciar edição/renderização de inferência generativa.
- Licença do repositório: MIT. Conferir termos e créditos de assets, software proprietário e modelos externos.

**Classificação:** ALTA por projeto, 1 novo pacote, status: fonte oficial consultada, não instalada/testada localmente.
