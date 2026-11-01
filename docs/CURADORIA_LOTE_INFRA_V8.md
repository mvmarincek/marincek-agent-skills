# Lote de monitoramento, inteligência e audiovisual — curadoria v8

| Recurso | Tipo real | Classe | Aplicação recomendada | Link |
|---|---|---|---|---|
| HyperFrames | Framework + skills de agentes | **NÚCLEO** (perfil audiovisual) | Demos SaaS, clips You8, marketing codificado | https://github.com/heygen-com/hyperframes |
| Shodan | Serviço de busca e monitoramento de ativos expostos | **POR_PROJETO** | Inspecionar apenas ativos próprios/autorizados | https://www.shodan.io/ |
| Zabbix | Plataforma open-source de monitoramento | **POR_PROJETO** | Monitoramento de servidores e IoT | https://www.zabbix.com/ |
| BuiltWith | Inteligência comercial de tecnologias web | **POR_PROJETO** | Prospeção B2B / stack visível | https://builtwith.com/ |
| CloudSEK XVigil | Plataforma comercial de proteção de risco digital | **POR_PROJETO** | Proteção corporativa de marcas, vazamentos, phishing | https://www.cloudsek.com/platform/xvigil |
| SpyCloud | Plataforma comercial de identidade/ameaças | **ARQUIVAR** | Alternativa enterprise | https://spycloud.com/ |
| Nagios Core | Ferramenta open source de monitoramento | **ARQUIVAR** | Alternativa ao Zabbix | https://www.nagios.org/projects/nagios-core/ |
| SolarWinds NPM | Plataforma comercial de monitoramento de redes | **ARQUIVAR** | Redes enterprise, não micro-SaaS | https://www.solarwinds.com/network-performance-monitor |
| TorBot | Coletor OSINT de conteúdos e links Tor | **ARQUIVAR** | Pesquisa de segurança com acesso autorizado | https://github.com/DedSecInside/TorBot |
| Russian Market | Referência a marketplace criminoso | **REMOVER_DO_CATALOGO_ATIVO** | Nenhuma integração/operação; apenas conceito de threat intelligence | Não incluir link operacional |
| Firecrawl | Skills e API de extração web | **DUPLICATA** | Já existente na v7 | https://github.com/firecrawl/skills |

## Correções das peças promocionais
- **Firecrawl:** extrai conteúdos públicos e autorizados em formatos como Markdown/JSON. A frase sobre passar por “backdoors” e não disparar alarmes é enganosa e não deve aparecer na documentação técnica.
- **SpyCloud:** trabalha com inteligência de credenciais expostas e inteligência de ameaças; nenhuma promessa generalizada de “recuperar arquivos de servidores criminosos” foi confirmada.
- **TorBot:** não equivale a exploração nem identifica automaticamente “portas escondidas” que podem ser acessadas; é crawler OSINT.
- **Shodan:** indexação de banners públicos não autoriza exploração de hosts descobertos.
- **Zabbix / Nagios / SolarWinds:** produtos parcialmente sobrepostos: **não instalar os três** por suposta complementaridade.
- **HyperFrames:** framework Apache-2.0, mas licenças de vídeos, imagens, músicas e marcas usados nas composições devem ser tratadas separadamente. Documentação oficial indica Node.js 22+ e FFmpeg para render local.

## Fontes oficiais consultadas em 2026-11-01
- HyperFrames Help Center: https://help.heygen.com/en/articles/15001510-hyperframes-x-heygen
- HyperFrames repositório: https://github.com/heygen-com/hyperframes
- Shodan explicação: https://help.shodan.io/the-basics/what-is-shodan
- Zabbix: https://www.zabbix.com/
- BuiltWith: https://builtwith.com/
- CloudSEK XVigil: https://www.cloudsek.com/platform/xvigil
- SpyCloud: https://spycloud.com/
- Nagios Core: https://www.nagios.org/projects/nagios-core/
- SolarWinds: https://www.solarwinds.com/network-performance-monitor
- TorBot: https://github.com/DedSecInside/TorBot
- Firecrawl: https://firecrawl.dev/

**Observação:** dados de screenshots (stars, claims, datas) não foram tratados como fatos verificados. Nenhuma das ferramentas foi instalada ou executada.
