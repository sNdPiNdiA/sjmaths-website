import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

p = 'upsssc-up-gk/geographical-landscape-and-environment/index.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

titles = re.findall(r'<div class="card-title">(.*?)</div>', c, re.DOTALL)
print('Titles count:', len(titles))
for t in titles[:10]:
    clean = re.sub(r'<[^>]+>', ' ', t).strip()
    print(' -', clean)
