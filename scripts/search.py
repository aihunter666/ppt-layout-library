#!/usr/bin/env python3
"""Search 3,207 verified original PPT layout images without network access."""
import argparse,json
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--query',default='')
    p.add_argument('--category')
    p.add_argument('--aspect',choices=['16:9','9:16'])
    p.add_argument('--group',choices=['basic','professional','cover','agenda','section','ending'])
    p.add_argument('--ids',nargs='+')
    p.add_argument('--limit',type=int,default=12)
    a=p.parse_args();base=Path(__file__).resolve().parents[1]/'library'
    rows=json.loads((base/'catalog.json').read_text());found=[]
    for r in rows:
        if a.group and a.group not in r.get('groups',[r['group']]):continue
        if a.category and a.category not in r['categories']:continue
        if a.aspect and r['aspect']!=a.aspect:continue
        if a.ids and not set([r['code'],*r.get('aliases',[])]).intersection(a.ids):continue
        hay=json.dumps(r,ensure_ascii=False).lower()
        if not all(t in hay for t in a.query.lower().split()):continue
        found.append(r)
    out=[dict(r,image=str((base/r['image']).resolve())) for r in found[:max(0,a.limit)]]
    print(json.dumps(dict(matched=len(found),shown=len(out),results=out),ensure_ascii=False,indent=2))

if __name__=='__main__':main()
