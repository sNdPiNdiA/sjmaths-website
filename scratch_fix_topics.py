import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.abspath(os.path.join(os.getcwd(), 'up-upper-primary-teacher', 'mathematics'))

topics = [
    'integers-properties-and-operations',
    'bodmas-rule-simplification',
    'lcm-and-hcf-methods-applications'
]

for t in topics:
    p = os.path.join(base_dir, t, 'index.html')
    print(f"\nProcessing {t} -> {p}")
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Fix header tag squishing
    c = c.replace('<header class="topic-hero-card">', '<div class="topic-hero-card">')
    c = re.sub(r'</header>', '</div>', c, count=1)

    # 2. Fix Form Feed (0x0c) -> \frac
    c = c.replace('\x0crac', '\\frac')
    c = c.replace('\x0c', '\\f')

    # 3. Fix Tab followed by ext -> \text
    c = c.replace('\text', '\\text')
    c = c.replace('\times', '\\times')
    c = c.replace('\to', '\\to')

    # 4. Fix Carriage return followed by ightarrow -> \rightarrow
    c = c.replace('\rightarrow', '\\rightarrow')
    c = c.replace('ightarrow', '\\rightarrow')
    c = c.replace('\right', '\\right')

    # 5. Fix unescaped dots -> \dots
    c = re.sub(r'(?<=[,\s])dots(?=[,\s\$\}A-Za-z\u0900-\u097F])', r'\\dots', c)

    # 6. Check for \mathbb
    c = c.replace('mathbbN', '\\mathbb{N}')
    c = c.replace('mathbbW', '\\mathbb{W}')
    c = c.replace('mathbbZ', '\\mathbb{Z}')
    c = c.replace('mathbbQ', '\\mathbb{Q}')
    c = c.replace('mathbbR', '\\mathbb{R}')

    # 7. Check for div0 / mathbf0
    c = c.replace('7div0', '7 \\div 0')
    c = c.replace('0div7', '0 \\div 7')
    c = c.replace('mathbf0', '\\mathbf{0}')

    # Save
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Successfully updated {t}")

# Also sync alias
alias_p = os.path.join(base_dir, 'bodmas-rule-and-brackets-simplification', 'index.html')
if os.path.exists(alias_p):
    with open(os.path.join(base_dir, 'bodmas-rule-simplification', 'index.html'), 'r', encoding='utf-8') as f:
        bodmas_content = f.read()
    with open(alias_p, 'w', encoding='utf-8') as f:
        f.write(bodmas_content)
    print("Synced bodmas alias.")
