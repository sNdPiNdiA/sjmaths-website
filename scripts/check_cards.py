import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')
topics = [
    'history-introduction-and-application-of-computer',
    'hardware-and-software',
    'input-and-output',
    'operating-system-social-networking-e-governance',
    'operation-of-printer-tablet-and-mobile',
    'artificial-intelligence',
    'machine-learning',
    'deep-learning',
    'big-data-processing',
    'internet-of-things',
    'internet',
    'world-wide-web-www',
    'internet-protocol-ip-address',
    'creation-of-e-mail-id-and-use-operation-of-e-mail',
    'it-gadgets-and-their-applications',
    'information-technology',
    'important-elements-of-word-processing-ms-word-and-excel-processing-ms-excel',
    'india-s-achievements-in-this-field'
]

pattern = re.compile(r'(<!--\s*Card 1:.*?-->.*?)(?=<!--\s*Card 2:)', re.DOTALL)

for t in topics:
    p = os.path.join('upsssc-computer', t, 'index.html')
    if not os.path.exists(p):
        print(f"MISSING: {p}")
        continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    m = pattern.search(content)
    if m:
        has_mm = '<div class="mermaid">' in m.group(1)
        print(f"OK: {t} | Match len: {len(m.group(1))} | Has mermaid: {has_mm}")
    else:
        print(f"FAILED: {t}")
