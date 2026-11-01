# Pipeline de publicação de PRD em Markdown/PDF

1. Produzir Markdown semântico com headings, tabelas curtas, links, versões, autor e data confirmados.
2. Escolher motor: Pandoc com template e engine PDF instalada; ou Markdown→HTML com CSS print e renderizador; ReportLab para geração programática.
3. Configurar A4 ou Letter conforme projeto, margens ~20 mm, hierarquia H1/H2/H3, numeração automática, sumário quando >8 páginas, páginas em rodapé, code blocks com quebras.
4. Resolver quebras de página antes de H1 e evitar títulos órfãos, tabelas truncadas, legibilidade baixa, links ilegíveis, diagramas sem alternativa textual.
5. Renderizar PDF como imagens de página e inspecionar pelo menos capa, sumário, tabelas longas e última página; verificar links e texto selecionável.
6. Confirmar que fontes e assets têm permissão de redistribuição; não distribuir arquivos proprietários de fontes.
7. Resultado: `PRD.md`, `PRD.pdf`, lista de diferenças e evidências; se engine ausente, manter Markdown pronto e declarar PDF pendente.

Referência: https://pandoc.org/MANUAL.html ; https://weasyprint.readthedocs.io/
