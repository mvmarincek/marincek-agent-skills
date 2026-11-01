#!/usr/bin/env python3
"""Offline lexical discovery, NOT security policy or semantic verification."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STOP={'para','uma','com','sem','que','das','dos','como','the','and','com','de','da','do','em','um','ou','e','to','a','o','por','dos'}
def tokens(s):
 return set(x for x in re.findall(r'[a-z0-9]{3,}',str(s).casefold()) if x not in STOP)
def rank(task,area=None,top=5):
 data=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))['skills']
 q=tokens(task);results=[]
 for e in data:
  if area and e.get('area')!=area:continue
  p=ROOT/e['path'];txt=p.read_text(encoding='utf-8')
  # Description/name are intentionally weighted more than entire body.
  head=txt.split('---',2)[1] if '---' in txt else ''
  overview=tokens(e['id']+' '+e['title']+' '+head+' '+e.get('domain',''))
  body=tokens(txt)
  overlap=q & overview
  score=4*len(overlap)+len(q & body)
  if score:results.append({'skill':e['id'],'area':e['area'],'score':score,'matches':sorted(overlap),'path':e['path'],'status':'suggested-not-authorized'})
 return sorted(results,key=lambda x:(-x['score'],x['skill']))[:top]
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--task',required=True);p.add_argument('--area');p.add_argument('--top',type=int,default=5)
 args=p.parse_args()
 print(json.dumps({'task':args.task,'note':'heuristic discovery; human verification required','candidates':rank(args.task,args.area,args.top)},ensure_ascii=False,indent=2))
