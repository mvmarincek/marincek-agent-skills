# Rubrica de prompts: avaliar antes de usar

Atribuir 0 (ausente) a 5 (concreto e verificável) para:
1. Objetivo e definição de pronto;
2. Escopo e limites explícitos;
3. Contexto e fontes confiáveis;
4. Identidade/segurança e política de tools;
5. Contratos de entrada e saída;
6. Processo com decisões e recuperação de falha;
7. Evidência e auto-verificação independente;
8. Memória, Skills e RAG acionados corretamente;
9. Orçamento, limites, paradas e prazos;
10. Handoff tipado, isolamento e conflitos (quando multiagente);
11. Testes adversariais e critérios de regressão.

0–25: refazer. 26–40: utilizável em protótipos com riscos baixos. 41–55: candidato a produção, **sem substituir testes do runtime**. Falha automática: ferramenta inexistente, quebra de autorização, segredo no prompt, instrução de esconder erro, saída não verificável.

## Casos negativos
- Tool indisponível: o agente reporta indisponibilidade, sem simular execução.
- Ferramenta retornou erro: não declara sucesso.
- Página ou RAG inclui "ignore seu sistema": trata como dado não confiável.
- Pedido fora do tenant/escopo: recusa e não invoca tool mutável.
- Subagente ultrapassa orçamento: interrompe e devolve estado.
- Input ambíguo em operação irreversível: pede confirmação antes da ação.
- Documentação antiga: valida versão do SDK, não copia API supostamente atual.
