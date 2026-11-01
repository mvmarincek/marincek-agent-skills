# RAG jurídico de normas brasileiras — referência de arquitetura

## Duas fontes com papéis diferentes

1. **`ctresb/leis`** — base de textos normativos em Markdown, metadados YAML (tipo, número, data, situação, versão, fonte oficial) e histórico. É **candidato a fonte documental** indexável; exige checagem de cobertura e vigência.
2. **`BaruqueRodrigues/llm-legislativo`** — engenharia de dados, treinamento de Transformer causal pequeno e avaliação. É **referência de pesquisa**, não substituto de fontes oficiais nem motor recomendado de perguntas e respostas jurídicas.

## Pipeline proposto, ainda não construído

```text
Fonte oficial / ctresb/leis (escopo selecionado)
  -> aquisição incremental com checksums e validação da origem
  -> parser Markdown + YAML, versão e data da norma
  -> segmentação por artigo, parágrafo e inciso (sem perder hierarquia)
  -> índice lexical + índice semântico (RAG híbrido)
  -> recuperação filtrada por tipo/ente/data/vigência
  -> reranking + verificador de citações e do texto da fonte oficial
  -> LLM gera resposta com evidências, data e limites
  -> revisão humana para uso profissional / alto impacto
```

## Requisitos de qualidade

- Resposta deve carregar: dispositivo legal, número e ano, artigo/trecho exato, fonte oficial, data da captura e aviso de vigência.
- Diferenciar normas publicadas, consolidadas, alteradas, revogadas, pendentes, jurisprudência e propostas legislativas.
- A base tem cobertura **incompleta por esfera/tipo**, e o próprio README aponta riscos de conversão automática/OCR.
- Nunca concluir 'não existe lei' a partir de ausência no índice.
- Modo de abstenção obrigatório para evidências ausentes ou divergentes.
- Indexação incremental; evitar `git clone` de centenas de milhares de commits antes de planejar recursos de armazenamento.
- Para acompanhar mudança normativa, registrar novas edições e histórico, sem substituir silenciosamente documentos indexados.

## Relevância prática

Inspira aplicações jurídicas/Compliance e agentes de consulta normativa; não integrar automaticamente em Metadia, ISYMU ou VOKI, onde acrescentaria custo e risco sem ganho direto.

## Fontes

- https://github.com/ctresb/leis
- https://github.com/BaruqueRodrigues/llm-legislativo
- https://huggingface.co/BaruqRodrigues/llm-legislativo
