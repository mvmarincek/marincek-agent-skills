# Gates visuais e funcionais — observáveis

| Gate | Prova mínima | Falha típica |
| --- | --- | --- |
| G0 | Diff da landing original e fluxos antes/depois | Alterar ou remover checkout existente |
| G1 | Vídeo real de pickup, carry, drop e duas peças persistindo | Mockup/PNG, nova peça só no card |
| G2 | Render final com material PBR, 3 câmeras e asset manifest | 'realista' declarado sem modelo ou review |
| G3 | E2E do funil com gateway em sandbox e DOM fallback | Só animação sem pedido válido |
| G4 | Events replay/dedup/orderAuth e status sem eventos | Contador automático simula cozinha real |
| G5 | Benchmark móvel e desktop com métricas | FPS inventado, WebGL obrigatório |
| G6 | Licenças, sem PII, consentimento para stream | vídeo de clientes sem autorização |

Os gates G0-G3 são requisitos do game comercial; G4 apenas se integração com operação real; G5/G6 continuam aplicáveis em todo produto. `NOT_TESTED` não pode ser convertido em PASS por revisão de texto.
