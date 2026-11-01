---
name: immersive-commerce-3d
description: "Criar ou incorporar experiências de game 3D fotorrealista e jogável em landing pages existentes ou novas, sem perder checkout, SEO, acessibilidade, analytics, nem integrar incorretamente estados reais."
license: MIT
metadata:
  version: "1.0.0"
  language: "pt-BR"
  category: "web-marketing"
---


# Immersive Commerce 3D — orquestração de landing pages jogáveis

## Quando ativar
Use quando o pedido for landing page/site/vitrine/catálogo com game 3D realista, configurador imersivo, câmera navegável, alimentos ou produtos sendo manipulados, simulação de loja, personalização automotiva, mobília sob medida, fabricação personalizada ou experiência jogável de compra. **Ativar tanto em sites existentes quanto em novas implementações**. É a skill principal; selecionar especializações só se necessárias.

## Princípio obrigatório
**O jogo é parte funcional da jornada comercial, não um vídeo, mockup, foto de fundo, cards com hover ou hero estático.** Um clique precisa alterar objetos 3D identificáveis, preservar estado, provocar animação física coerente e permitir avançar até a compra. Conteúdo gerado por IA (imagem/vídeo) é referência ou asset de apoio, não demonstra funcionalidade em tempo real.

## Etapas e roteamento
1. Descobrir repo/stack/brand/componentes existentes, fluxos de conversão, pagamentos, analytics, autenticação, política de privacidade, APIs, SEO, versão React/Next. **Não substituir landing existente, não remover checkout, não interromper analytics**. Fazer inventário/ADR de adição incremental, route guard e feature flag.
2. Definir intenção: `marketing-demo` (simulado), `product-configurator` (escolha de itens), `checkout` (real), `live-operations` (eventos verificados de backend) ou `live-video` (imagem real autorizada). Deixar explícita a diferença entre esses estados e suas fontes.
3. Entregar storyboards e mapa de câmera da **cena 3D principal**: posição real de objetos, ações, microfísica, estados, feedback e transições. Redigir eventos esperados antes de implementar shaders ou overlays.
4. Acionar `photoreal-3d-assets` para PBR/GLB otimizado e real; `tactile-3d-interactions` para Raycaster/drag/pickup/drop/IK/tweens/estado; `immersive-experience-quality` para gates. Manter `gamified-landing-page` como camada de narrativa, CTA, SEO, desempenho e conversão.
5. Em React usar Three.js + @react-three/fiber + drei, conforme versões compatíveis, Canvas client-side lazy e HTML semântico separado. Usar uma câmera definida (FOV e planos) e pixels reais do produto, não apenas painéis 2D. Adotar estados determinísticos de cena e comandos de negócio tipados.
6. Conectar seleção de componentes → preço → carrinho → checkout existente; estado validado no backend, disponibilidade de ingredientes e preço autoritativos; não aceitar total calculado no cliente como pagamento confirmado. Manter a opção convencional sem WebGL para concluir a compra.
7. Se o produto pedir acompanhar produção física depois do pagamento, **adicionar integração separada** `realworld-order-digital-twin`; para automóveis, equipamentos e fabricação sob encomenda, acionar também `made-to-order-manufacturing-twin`. Não atribuir eventos reais às animações do configurador. Usar estados emitidos pelo sistema operacional autenticado.
8. Testar uma fatia vertical antes de construir a página inteira: cenário, item escolhível, mão pega e deposita, item acumula sobre produto, desfazer, alteração de resumo/preço, checkout/fallback. Somente avançar após passar os gates de qualidade.

## Arquitetura recomendada
- `ExperienceShell`: roteamento/acessibilidade e fallback/SEO/CTA; `Scene3D`: Canvas, camera, lights, assets e picking; `InteractionController`: intenção → comando; `ProductState`: composição serializável independente da renderização; `CommerceAdapter`: catálogo/preços/carrinho/autenticação; `LiveOperationsAdapter`: apenas se contratado.
- Não colocar `fetch`/segredos/billing dentro de componentes 3D. O estado de item precisa sobreviver a recarregar ou retomar sessão conforme regras do produto.
- Revisar web-vitals e FPS de dispositivos reais; LOD e qualidade progressiva, sem assumir que uma GPU desktop é do usuário.

## Exemplo de aceitação — creperia
Na perspectiva de cliente há bancada e cubas inox reais 3D, uma chapa com massa, 3 ingredientes selecionáveis. Ao clicar em morango: selecionar cuba → animar mão/utensílio até cuba → colher peça visível → transportar por trajetória → depositar morango no espaço da massa → a peça permanece enquanto outros ingredientes entram → preço e pedido mudam. O clique de chocolate aplica molho com UV/mesh coerente; o botão de assar inicia animação distinta; dobrar, embalar, despachar encerram **uma simulação**. Após pagamento, status de cozinha vem de eventos reais, e não das cenas simuladas.

## Exemplo avançado: carro configurado, produzido e entregue
O cliente personaliza **o próprio objeto 3D** (rodas, pintura, bancos, opcionais) com materiais e geometria reais, confirma configuração e compra; o backend cria a ordem e o MES/ERP autorizado fornece marcos de produção. O mesmo carro virtual aparece em animações de carroceria, pintura, interior, inspeção e transporte quando esses marcos forem confirmados. O render é representativo; não afirma que cada movimento dos robôs é imagem da unidade real. Caso a fábrica forneça somente datas previstas, exibir previsão. Se há VIN/serial atribuído e eventos por unidade, mostrar rastreabilidade verificada; antes, mostrar status da ordem. Nunca misturar cena demonstrativa com prova industrial.

## Regras de não regressão
Reaproveitar componentes, CSS tokens, rotas, checkout, eventos e layout atuais. Criar rota/ilha imersiva por feature flag, degradar em hardware fraco e garantir que o usuário nunca perca uma compra se WebGL falhar. Evitar autoplay com áudio, timers manipulativos e elementos que escondam preço/termos.

## Contratos e referências
Ler `references/experience-contract.md`, `references/implementation-playbook.md` e `assets/vertical-slice-acceptance.json`. Escrever roteiro de interações, ARQUITETURA.md, EVIDENCIAS.md e matriz de regressão. Não inventar testes realizados, links, recursos 3D ou integração disponível.

## Critérios de aceite (gate de entrega)
- [ ] Landing nova ou existente preserva CTA, compra, SEO e mobile, com flags para a camada 3D.
- [ ] **Os objetos são geometria 3D renderizada em runtime e interativos**, não imagem/vídeo fingindo interação.
- [ ] A mão efetivamente pega e coloca item; objetos selecionados surgem sobre o produto e persistem, sem teletransporte visual.
- [ ] Mudanças de estado, preço e carrinho têm testes; operação real não depende de dados de jogo.
- [ ] Visual comparado com referência aprovada, testes de viewport/camera e fallback sem WebGL; informar resultados medidos.
- [ ] Permissões, licenças de assets e credenciais/privacidade verificadas antes de produção.

## Entregáveis
Código incremental ou novo, vídeo/gravação real de runtime, imagens antes/depois, testes executáveis, source de assets, ADR de stack, baseline de performance, instruções de deploy, limitações honestas e gate aprovado/reprovado.

**Aprovação e segurança:** não ativar ferramentas externas, gerar custos, publicar assets, alterar checkout ou implantar em produção sem autorização e verificação de licenças.
