# Playbook: landing existente e landing nova

## EXISTENTE
1. `git status`, mapear rotas, componentes, design system, testes, CRM/checkout, scripts e URLs principais; registrar baseline.
2. Criar branch `feat/immersive-3d-<feature>` e feature flag off por padrão; usar carregamento dinâmico client-only para WebGL quando SSR/Next exigir.
3. Criar `ExperienceShell` e encapsular a cena em rota `/experiencia` ou seção opcional, sem substituir hero/proposta/CTA existentes. Sem classes globais colidindo.
4. Injetar `CommerceAdapter` em vez de alterar diretamente gateway. API server valida precificação e disponibilidade.
5. E2E com flag on/off: CTA, formas de pagamento, navegação, SEO/canonical, LGPD/cookies, Googlebot sem WebGL.

## NOVA
1. Brief, identidade e conversão; wireframe com caminho tradicional sem 3D.
2. Criar storyboard da cena e o protótipo técnico da interação crítica antes de criar o hero.
3. Reutilizar stack e design tokens do cliente quando existirem; criar desde o início contrato de estados, schema de produto e API.
4. Só integrar gráficos avançados depois de provar gameplay.

## Dual-mode
- `demo`: toda a sequência é simulação, com texto explícito.
- `live`: evento assinado/verificado pelo servidor atualiza status do pedido no app; sem falsificar presença de chef ou execução ao vivo.
- `video`: stream real opcional e autorizado, com privacidade, consentimento, retenção definida e acesso restrito.

## Escopo e orçamento técnico
WebGPU apenas após compatibilidade; WebGL como baseline, fallback acessível em HTML. Nenhum pacote 3D de terceiros é presumido instalado. Licenças de assets/skills e custos de serviços MCP aprovados antes de download/geração.
