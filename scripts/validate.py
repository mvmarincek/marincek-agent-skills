#!/usr/bin/env python3
"""Validate catalog and Agent Skills, including area/path integrity."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
manifest=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
entries=manifest.get('skills',[])
slug=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
if manifest.get('count')!=len(entries):errors.append('manifest count mismatch')
ids=set(); paths=set()
for e in entries:
 name=e.get('id','');rel=e.get('path','')
 if name in ids:errors.append('duplicate id '+name)
 ids.add(name)
 if not slug.fullmatch(name):errors.append('invalid id '+name)
 if rel in paths:errors.append('duplicate path '+rel)
 paths.add(rel)
 if Path(rel).is_absolute() or '..' in Path(rel).parts:errors.append('unsafe catalog path '+rel);continue
 expected=f'areas/{e.get("area")}/skills/{name}/SKILL.md'
 if rel!=expected:errors.append(f'path mismatch {name}: {rel}')
 p=ROOT/rel
 if not p.is_file():errors.append(f'missing SKILL.md: {name}');continue
 s=p.read_text(encoding='utf-8')
 m=re.match(r'^---\s*\n(.*?)\n---\s*\n',s,re.S)
 if not m:errors.append(f'no frontmatter: {name}');continue
 front=m.group(1)
 n=re.search(r'^name:\s*["\']?([^"\'\n]+)',front,re.M)
 d=re.search(r'^description:\s*["\']?(.+)',front,re.M)
 if not n or n.group(1).strip()!=name:errors.append('name mismatch '+name)
 if not d or not d.group(1).strip():errors.append('missing description '+name)
 if not s[m.end():].strip():errors.append('empty body '+name)
 for r in re.findall(r'[`(]((?:references|assets|scripts)/[^\s`)"\']+)[`)]',s):
  r=r.rstrip('.,;:')
  if '*' in r or '{' in r:continue
  if not ((p.parent/r).exists() or (r.startswith('scripts/') and (ROOT/r).exists())):
   errors.append(f'broken local reference {name}: {r}')
ext=json.loads((ROOT/'catalog/external-sources.json').read_text(encoding='utf-8'))
for i,x in enumerate(ext.get('sources',[])):
 if not str(x.get('url','')).startswith(('https://','http://')):errors.append(f'external url invalid {i}')
 if x.get('integration')!='reference-only':errors.append(f'external unexpected integration {i}')
print(f'Validated {len(entries)} skills, {len(ext.get("sources",[]))} external sources, {len(set(e.get("area") for e in entries))} populated areas.')
if errors:
 for e in errors:print('ERROR:',e)
 sys.exit(1)
print('PASS structural checks; agent runtime NOT tested.')
