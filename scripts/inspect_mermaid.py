import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
from check_cards import topics, pattern

for t in topics:
    p = os.path.join('upsssc-computer', t, 'index.html')
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m = pattern.search(c)
    if m:
        mermaid_match = re.search(r'<div class="mermaid">(.*?)</div>', m.group(1), re.DOTALL)
        if mermaid_match:
            lines = [l.strip() for l in mermaid_match.group(1).splitlines() if l.strip() and not l.strip().startswith('%%') and not l.strip().startswith('graph') and not l.strip().startswith('flowchart') and not l.strip().startswith('classDef') and not l.strip().startswith('class ')]
            print(f"=== {t} ({len(lines)} lines) ===")
            for l in lines[:6]:
                print("  ", l[:120])
