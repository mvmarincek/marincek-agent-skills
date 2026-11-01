# Política de incorporação de repositórios terceiros

**Referenciar** uma skill não significa copiá-la. No catálogo: `name`, `url`, `license_status`, `integration`, `pin`, `source_status`. Manter links de origem e status de validação.

## Fluxo por fonte
1. Confirmar repositório e **commit SHA**; verificar se URL corresponde ao autor oficial e se fonte não é um mirror comprometido.
2. Abrir `LICENSE`, `NOTICE` e documentação (arquivos distintos podem ter exceções). Sem licença concedendo redistribuição, não publicar uma cópia.
3. Revisar scripts, hooks, CI, dependências e regras que possam conter execução, network e credenciais. Um `SKILL.md` baixado da web é conteúdo não confiável.
4. Para **incorporar conhecimento**, preferir resumo e roteiro originais com link e atribuição; evitar transcrever longos trechos ou copiar o repositório inteiro.
5. Para **vendorizar**, registrar versão, licença, atribuição, modificações, motivo e um relatório de revisão. Não alterar licença de upstream. Usar diretório separado `third_party/` com NOTICE apropriado se a redistribuição for autorizada.
6. Repositórios GPL/AGPL e licenças custom exigem análise específica; cópia indiscriminada pode criar obrigações e conflito de licenças.
7. Clonagem opcional apenas em `.cache/upstream` (ignorada pelo Git). Uma referência pode depender de API paga e ainda ser útil como conhecimento, sem instalar.

## Fontes significativas estudadas
- Scenario 3D OS: https://github.com/scenario-labs/skills — skills para Blender/3D e integrações de plataforma; separar operação local e uso do MCP pago.
- GameDev Agent Skills: consultar `catalog/external-sources.json` para origem exata e licenciamento.
- Hallmark: https://github.com/Nutlope/hallmark — design e revisão; verificar a origem e licença antes de usar.
- Matt Pocock Skills: https://github.com/mattpocock/skills — engenharia de software.
- Vercel React Best Practices: conferir catálogo e versão.
- llmfit: https://github.com/AlexsJones/llmfit — seleção de modelos compatíveis com hardware.
- Atlas: https://github.com/pacifio/atlas — coordenação e histórico; não confundir com memória LLM automática.
- Orca: https://github.com/stablyai/orca — orquestração de agentes; não é uma Skill.
- Harness²: https://github.com/google-research/harness2 — pesquisa em ambiente de agentes.
- ACP: protocolo, não Skill nem MCP Tool por si só.

## Importante
Esta biblioteca usa licenciamento MIT exclusivamente para conteúdos originais compilados aqui. Fontes e arquivos pré-existentes devem manter licenças e créditos originais. Em caso de origem incerta, manter como link de referência.
