#!/usr/bin/env python3
"""Copy selected skill directories to agent discovery roots. No network access."""
import argparse,datetime,json,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CLIENTS={'codex':('.agents/skills','.agents/skills'),
 'claude':('.claude/skills','.claude/skills'),
 'verdent':('.verdent/skills','.verdent/skills'),
 'opencode':('.opencode/skills','.config/opencode/skills')}
p=argparse.ArgumentParser()
p.add_argument('--targets',nargs='+',choices=CLIENTS,default=['codex','claude','verdent'])
p.add_argument('--scope',choices=['global','project'],default='global')
p.add_argument('--project-path',type=Path,default=Path.cwd())
p.add_argument('--skills',nargs='*')
p.add_argument('--replace',action='store_true')
p.add_argument('--dry-run',action='store_true')
args=p.parse_args()
manifest=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
available={e['id']:e for e in manifest['skills']}
selected=args.skills if args.skills is not None else sorted(available)
if len(set(selected))!=len(selected) or any(n not in available for n in selected):p.error('unknown or duplicated slug')
for agent in dict.fromkeys(args.targets):
 sub=CLIENTS[agent][0 if args.scope=='project' else 1]
 base=args.project_path.resolve() if args.scope=='project' else Path.home()
 dest_root=base/sub
 for slug in selected:
  source=ROOT/available[slug]['path'];source=source.parent
  if not source.is_dir() or not (source/'SKILL.md').is_file():raise FileNotFoundError(source)
  dest=dest_root/slug
  if dest.exists():
   if not args.replace:print('SKIP already exists',dest);continue
   stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
   backup=dest_root/(slug+'.backup-'+stamp)
   print('BACKUP',dest,'->',backup)
   if not args.dry_run:dest.rename(backup)
  print('INSTALL',source,'->',dest)
  if not args.dry_run:
   dest_root.mkdir(parents=True,exist_ok=True)
   shutil.copytree(source,dest)
print('Done: no tools, cloud resources or models were installed. Verify client discovery.')
