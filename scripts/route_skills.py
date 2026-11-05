#!/usr/bin/env python3
"""Offline lexical discovery, NOT security policy or semantic verification."""
import argparse,json,re,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STOP={'para','uma','com','sem','que','das','dos','como','the','and','com','de','da','do','em','um','ou','e','to','a','o','por','dos'}
def normalize(s):
 return ''.join(c for c in unicodedata.normalize('NFKD',str(s).casefold()) if not unicodedata.combining(c))
def tokens(s):
 return set(x for x in re.findall(r'[a-z0-9]{3,}',normalize(s)) if x not in STOP)
def rank(task,area=None,top=5):
 data=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))['skills']
 q=tokens(task);results=[]
 # Explicit intent cues supplement lexical discovery; these are NOT permissions.
 web_commerce=bool(q & {'landing','site','pagina','website','commerce','vitrine','loja','configurador','checkout'})
 real_3d=bool(q & {'3d','tridimensional','game','jogavel','fotorrealista','realista','blender','glb','webgl'})
 hands=bool(q & {'ingrediente','ingredientes','mao','pegar','pegando','colocar','colocando','transportar','interacao','interagir','recheio','manipular'})
 asset_work=bool(q & {'glb','pbr','asset','assets','modelo','texturas','blender','fotorealismo','fotorrealista'})
 factory_strong=bool(q & {'carro','automovel','veiculo','automotivo','fabrica','fabricacao','montadora','manufatura','mes','erp','vin','plm','serial','industria','production','manufacturing','producao','encomenda','ordem'})
 factory_twin=factory_strong and bool(q & {'3d','real','tempo','status','montagem','fabricacao','fabrica','pedido','cliente','game','linha','sob','digital','twin','configurado','configuracao','montando','producao'})
 live_ops=bool(q & {'cozinha','chef','preparado','preparo','despachado','despachar','pedido','kds','pos','operacao','ao vivo','tempo real'.replace(' ','_')}) and bool(q & {'real','vivo','pedido','cozinha','chef','kds','pos','despachar','status','andamento'})
 for e in data:
  if area and e.get('area')!=area:continue
  p=ROOT/e['path'];txt=p.read_text(encoding='utf-8')
  # Description/name are intentionally weighted more than entire body.
  head=txt.split('---',2)[1] if '---' in txt else ''
  overview=tokens(e['id']+' '+e['title']+' '+head+' '+e.get('domain',''))
  body=tokens(txt)
  overlap=q & overview
  score=4*len(overlap)+len(q & body)
  if web_commerce and real_3d and e['id']=='immersive-commerce-3d':score+=32
  if real_3d and hands and e['id']=='tactile-3d-interactions':score+=18
  if real_3d and asset_work and e['id']=='photoreal-3d-assets':score+=16
  if real_3d and web_commerce and e['id']=='immersive-experience-quality':score+=10
  if live_ops and e['id']=='realworld-order-digital-twin':score+=35
  if factory_twin and e['id']=='made-to-order-manufacturing-twin':score+=55
  if factory_twin and web_commerce and e['id']=='immersive-commerce-3d':score+=13
  if score:results.append({'skill':e['id'],'area':e['area'],'score':score,'matches':sorted(overlap),'path':e['path'],'status':'suggested-not-authorized'})
 return sorted(results,key=lambda x:(-x['score'],x['skill']))[:top]
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--task',required=True);p.add_argument('--area');p.add_argument('--top',type=int,default=5)
 args=p.parse_args()
 print(json.dumps({'task':args.task,'note':'heuristic discovery; human verification required','candidates':rank(args.task,args.area,args.top)},ensure_ascii=False,indent=2))
