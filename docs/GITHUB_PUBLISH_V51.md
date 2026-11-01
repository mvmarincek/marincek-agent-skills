# Como publicar v5.1 no repositório já existente

Repositório: `https://github.com/mvmarincek/marincek-agent-skills` (público, branch `main`, última versão confirmada v4.0 em 2026-11-01). A versão v5.1 com 28 Skills está no ZIP entregue e **ainda não foi enviada**.

## Passos PowerShell no Windows

```powershell
git clone https://github.com/mvmarincek/marincek-agent-skills.git
cd marincek-agent-skills
git checkout -b feat/immersive-3d-realtime-commerce-v5-1
# Copie todo o conteúdo do ZIP v5.1 sobre a raiz deste repositório,
# substituindo os arquivos em conflito, sem apagar outros arquivos remotos.
python .\scripts\validate.py
python -m unittest discover -s tests -v
python .\scripts\route_skills.py --task "carro configurado 3D montando na fábrica MES ERP" --top 5
git status
git add -A
git commit -m "feat(skills): immersive 3D commerce and manufacturing digital twins v5.1"
git push --set-upstream origin feat/immersive-3d-realtime-commerce-v5-1
```

Após `git push`, abra PR para `main`, inspecione diff, testes, fontes e licenças. Não fazer `git push --force` nem modificar segredos. O conector GitHub desta sessão retornou 403 ao tentar criar a branch; isso não prova falta de permissão do usuário no Git local, apenas da integração nesta sessão.
