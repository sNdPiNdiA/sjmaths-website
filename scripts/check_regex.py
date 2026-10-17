import os
import re

topics = [
    'artificial-intelligence',
    'machine-learning',
    'deep-learning',
    'big-data-processing',
    'internet-of-things',
    'india-s-achievements-in-this-field',
    'it-gadgets-and-their-applications',
    'information-technology',
    'creation-of-e-mail-id-and-use-operation-of-e-mail',
    'internet',
    'world-wide-web-www',
    'internet-protocol-ip-address',
    'important-elements-of-word-processing-ms-word-and-excel-processing-ms-excel'
]

pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)

for t in topics:
    p = os.path.join('upsssc-computer', t, 'index.html')
    html = open(p, encoding='utf-8').read()
    m = pattern.search(html)
    print(f"{t:<45} | Match: {bool(m)}")
