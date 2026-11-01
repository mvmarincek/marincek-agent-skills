# Publicação no GitHub `mvmarincek`

A conexão GitHub desta conversa foi confirmada como `mvmarincek`. O repositório público `mvmarincek/Prompts` já existe, mas não é recomendado publicar automaticamente o material do VOKI e de segurança em um repositório público. **Não foi criado um repositório remoto automaticamente**.

## Opção recomendada: novo repositório privado

1. Extraia o ZIP, entre na pasta `mvmarincek-agent-skills` e revise o conteúdo. Não publique segredos ou informações internas do VOKI sem sua própria aprovação.
2. Instale Git e GitHub CLI (`gh`) e faça `gh auth login`, se necessário.
3. Execute no terminal do Windows, **dentro da pasta**, após revisar:

```powershell
git init -b main
git add .
git commit -m "feat: bootstrap private agent skills knowledge base"
gh repo create mvmarincek/agent-skills --private --source . --remote origin --push
```

Se seu GitHub já tiver o repositório `agent-skills`, substitua o último comando por um fluxo de branch/PR de atualização; não faça `git push --force`.

## Opção alternativa: pasta no repositório `Prompts`

Escolha esta opção **somente se quiser publicar todo o conteúdo como público**. Crie a pasta `agent-skills/` naquele repositório e envie os arquivos por PR para revisão, sem alterar os prompts existentes. Recomenda-se copiar apenas as Skills genéricas e manter as específicas do VOKI no repo privado.

## Ciclo de manutenção
- `feature/skill-<nome>` para nova Skill, com PR e validador automático.
- Cadastro de novos links em `catalog/external-sources.json`, revisão de licença e mudanças via PR.
- Releases semânticos e changelog; testes com Codex, Verdent e Claude antes de marcar status `tested`.
- Instalação seletiva em cada projeto, preferencialmente com version/commit pin.

## Status neste pacote
O ZIP está pronto para Git. Ele não concede acesso ao GitHub local do usuário e não garante que `gh` esteja autenticado no computador do usuário.
