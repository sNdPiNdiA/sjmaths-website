import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

gk_dir = 'upsssc-up-gk'
topics = sorted([d for d in os.listdir(gk_dir) if os.path.isdir(os.path.join(gk_dir, d)) and d != 'history-of-uttar-pradesh'])

for t in topics:
    p = os.path.join(gk_dir, t, 'index.html')
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # check Card 1 match
    m1 = re.search(r'(<!--\s*Card 1:\s*Mind Map\s*-->.*?)(<!--\s*Card 2:)', c, re.DOTALL)
    m2 = re.search(r'(<div class="card-premium">.*?Mindmap.*?)(<div class="card-premium")', c, re.DOTALL | re.IGNORECASE)

    if m1:
        print(f"{t}: matched by Card 1 comment (length={len(m1.group(1))})")
    elif m2:
        print(f"{t}: matched by card-premium Mindmap (length={len(m2.group(1))})")
    else:
        print(f"{t}: NO MATCH FOUND!")
