#!/usr/bin/env python3
"""Scaffold a new original Skill under an area; no external code execution."""
from pathlib import Path
import argparse,json,re
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--area',required=True);p.add_argument('--slug',required=True);p.add_argument('--description',required=True);p.add_argument('--title');args=p.parse_args()
pattern=r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
if not re.fullmatch(pattern,args.slug) or not re.fullmatch(pattern,args.area):p.error('area and slug must be kebab-case')
area=ROOT/'areas'/args.area
if not area.is_dir():p.error('unknown area: '+args.area)
manifest=ROOT/'catalog/skills.json';data=json.loads(manifest.read_text(encoding='utf-8'))
if any(e['id']==args.slug for e in data['skills']):p.error('duplicated skill')
if '\n' in args.description or '"' in args.description:p.error('description cannot contain newline or quote')
base=area/'skills'/args.slug
if base.exists():p.error('path already exists')
base.mkdir(parents=True)
(base/'SKILL.md').write_text(f"""---
name: {args.slug}
description: "{args.description}"
license: MIT
---

# {args.title or args.slug}

## Quando ativar
TODO

## Entradas
TODO

## Procedimento
TODO

## Validação e segurança
TODO

## Entregáveis
TODO
""",encoding='utf-8')
for sub in ('references','assets'): (base/sub).mkdir()
data['skills'].append({'id':args.slug,'title':args.title or args.slug,'domain':args.area,'area':args.area,'path':f'areas/{args.area}/skills/{args.slug}/SKILL.md','status':'experimental','version':'0.1.0','depends_on':[],'supported_agents':['codex','claude-code','verdent','opencode'],'verified':'scaffold-only','installed':False})
data['count']=len(data['skills']);manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Scaffolded:',base,'- requires substantial authoring, evaluation and review')
