# Curadoria interna de referências gráficas

Estas são **referências**, não dependências nem instalações garantidas. Antes de usar, verificar URL, licença e compatibilidade na biblioteca v10.

| Fonte existente | Papel | Usar quando | Cuidado |
|---|---|---|---|
| Hallmark — https://github.com/Nutlope/hallmark | direção estética/auditoria | refinamento premium | verificar documentação atual |
| frontend-design — https://skills.sh/anthropics/skills/frontend-design | composição e UX | construção de UI única | não copiar marcas |
| Vercel React Best Practices — https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices | renderização/performance | React/Next.js | aplicar conforme stack |
| Matt Pocock Skills — https://github.com/mattpocock/skills | TS/engenharia | TypeScript e qualidade | usar skills específicas |
| GameDev Agent Skills — https://github.com/gamedev-skills/awesome-gamedev-agent-skills | estética de game, lógica | UI de jogo e 3D | revisar licença e pacote real |
| Platform Design Skills | sistemas de design | padronização | conferir origem no catálogo |
| awwwards-motion — https://skills.sh/adamperlis/awwwards-motion/awwwards-motion | motion premium | narrativa e transições | não gerar jitter |
| 60fps.design — https://60fps.design/ | inspiração motion/MCP | microinterações | MCP opcional, verificar custo |
| Scenario 3D OS — https://github.com/scenario-labs/skills | pipeline Blender e 3D | assets reais personalizados | geração cloud pode ter custo |

## Padrão de decisão
1. Design premium sem 3D? frontend-design + motion + React best practices.
2. Dashboard 3D em tempo real? R3F/Three.js + otimização + game skills.
3. Assets modelados em Blender? Scenario Blender skills + Python local; não instalar serviço Scenario por padrão.
4. Conteúdo e marketing? priorizar copy, narrativa, CTA, hipótese e instrumentação.

## Orçamento visual
- Mobile: evitar render 3D full-screen persistente; considerar poster fallback e entrada sob interação.
- Garantir texto SEO legível mesmo sem JavaScript/WebGL.
- Definir preferência `prefers-reduced-motion`; desabilitar parallax/agitação.
- Animações com `transform/opacity` preferencialmente, sem layout thrashing.
- Verificar contrastes e foco visível; ensaiar performance em equipamento de entrada.
