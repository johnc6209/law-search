import re,sys
L=open(sys.argv[1]).read().replace('\f','').split('\n')
def section(a,b):
    out=[];on=False
    for l in L:
        if l.startswith(a): on=True; continue
        if on and (l.startswith(b) or l.lstrip().startswith('※')): break
        if on: out.append(l)
    return out
CIR='①②③④⑤⑥⑦⑧⑨'
def parse(lines):
    recs=[];art=None;cur=None;hang=''
    for raw in lines:
        if not raw.strip(): continue
        s=raw.strip()
        if re.match(r'^제\d+장',s): continue
        m=re.match(r'^제(\d+)조(?:의?(\d+))?\s*(.*)$',s) if not raw.startswith(' ') else None
        if m:
            art=m.group(1)+('의'+m.group(2) if m.group(2) else ''); hang=''; s=m.group(3).strip()
            cur=None
            if not s: continue
        # sub markers
        mh=re.match(r'^([%s](?:\s*,?\s*[%s])*)\s*(.*)$'%(CIR,CIR),s)
        if mh:
            hang=','.join(str(CIR.index(c)+1) for c in mh.group(1) if c in CIR); s=mh.group(2).strip()
            cur=None
            if not s: continue
        mo=re.match(r'^(\d+)\.\s*(.*)$',s)
        if mo:
            cur=[art,hang,mo.group(1),mo.group(2).strip()]; recs.append(cur); continue
        if cur is not None and (raw.startswith(' ') ) and not mh:
            cur[3]+=s; continue
        cur=[art,hang,'',s]; recs.append(cur)
    return recs
for name,a,b in [('형법','<별표 1>','<별표 2>'),('군형법','<별표 2>','<별표 3>')]:
    with open(name+'.txt','w') as f:
        for r in parse(section(a,b)):
            f.write('|'.join(r)+'\n')
