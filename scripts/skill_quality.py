#!/usr/bin/env python3
"""Static quality checker; never claim functional correctness from this output."""
from pathlib import Path
import argparse,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def audit(e):
 txt=(ROOT/e['path']).read_text(encoding='utf-8')
 checks={
 'frontmatter':txt.startswith('---\n'),
 'adequate_size':len(txt)>=850,
 'activation':bool(re.search(r'ativ[aá]|quando (?:usar|ativar)',txt,re.I)),
 'procedure':bool(re.search(r'procedimento|pipeline|etapas|fluxo|fases',txt,re.I)),
 'validation':bool(re.search(r'valid[aá]|crit[eé]rio|test[eá]',txt,re.I)),
 'safety_boundaries':bool(re.search(r'permiss[aã]o|aprova[cç][aã]o|seguran[cç]a|n[aã]o executar',txt,re.I)),
 'deliverable':bool(re.search(r'entreg[aá]|sa[ií]da|artefato|produto',txt,re.I)),
 'references_or_assets':any((ROOT/e['path']).parent.joinpath(x).is_dir() for x in ('references','assets')),
 }
 return {'id':e['id'],'checks':checks,'score':sum(checks.values()),'max_score':len(checks),'passed':all(checks.values())}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--all',action='store_true');p.add_argument('--skill');args=p.parse_args()
 entries=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))['skills']
 if args.skill:entries=[x for x in entries if x['id']==args.skill]
 if not entries:p.error('skill not found')
 results=[audit(x) for x in entries]
 print(json.dumps({'mode':'static-only','results':results},ensure_ascii=False,indent=2))
 print('WARNING: static review cannot prove safety, execution or successful model use.')
 sys.exit(0 if all(r['passed'] for r in results) else 2)
