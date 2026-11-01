#!/usr/bin/env python3
"""Read or locally clone selected GitHub repos in ignored cache for manual audit.
Never installs, executes, publishes, or vendors external code."""
import argparse,json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--list',action='store_true')
p.add_argument('--name',help='Exact/partial source name (one match required for cloning)')
p.add_argument('--clone',action='store_true',help='clone source into ignored cache; no installation')
p.add_argument('--limit',type=int,default=100)
args=p.parse_args()
items=json.loads((ROOT/'catalog'/'external-sources.json').read_text(encoding='utf-8'))['sources']
filtered=[x for x in items if not args.name or args.name.casefold() in x['name'].casefold()]
if args.list or not args.clone:
 for x in filtered[:args.limit]:print(x['name'], x['url'], '[ref only; license not audited]')
 if not args.clone:sys.exit(0)
if len(filtered)!=1:p.error('provide a --name that resolves to exactly one catalog source')
x=filtered[0]
u=urlparse(x['url'])
if u.scheme!='https' or u.hostname!='github.com' or not re.fullmatch(r'/[\w.\-]+/[\w.\-]+/?',u.path):
 p.error('cloning is available only for exact github.com repository URLs, without paths')
owner,repo=[z for z in u.path.split('/') if z]
cache=ROOT/'.cache'/'upstream'/f'{owner}__{repo}'
if cache.exists():p.error('cache exists; remove or inspect manually instead of overwriting')
cache.parent.mkdir(parents=True,exist_ok=True)
cmd=['git','-c','core.hooksPath=/dev/null','-c','filter.lfs.smudge=','-c','filter.lfs.required=false','clone','--depth=1','--single-branch','--',x['url'],str(cache)]
print('Cloning for inspection only:',x['name'])
r=subprocess.run(cmd,check=False)
if r.returncode:sys.exit(r.returncode)
commit=subprocess.check_output(['git','-C',str(cache),'rev-parse','HEAD'],text=True).strip()
licenses=[str(z.relative_to(cache)) for z in cache.iterdir() if z.is_file() and z.name.upper().startswith(('LICENSE','LICENCE','NOTICE','COPYING'))]
print('COMMIT:',commit)
print('POSSIBLE LICENSE/NOTICE:',licenses if licenses else '[none found at root]')
print('Cached locally. NOT installed, executed, copied into skills/, or published to GitHub.')
