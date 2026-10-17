import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

upsssc_dir = 'upsssc-computer'
topics = [d for d in os.listdir(upsssc_dir) if os.path.isdir(os.path.join(upsssc_dir, d)) and not d.startswith('.')]
topics.sort()

print(f"Total topics detected: {len(topics)}")

all_passed = True

for idx, topic in enumerate(topics, 1):
    file_path = os.path.join(upsssc_dir, topic, 'index.html')
    if not os.path.exists(file_path):
        print(f"[{idx}] {topic}: FAIL - index.html missing!")
        all_passed = False
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    mermaid_divs = len(re.findall(r'<div\s+class=["\']mermaid["\']', html))
    mermaid_scripts = len(re.findall(r'mermaid(\.min)?\.js', html))
    mindmap_containers = len(re.findall(r'mindmap-container', html))
    mindmap_nodes = len(re.findall(r'mindmap-node\s+epoch-', html))
    fact_badges = len(re.findall(r'mindmap-fact-badge', html))
    has_card2 = bool(re.search(r'<!--\s*Card 2:', html))
    has_en = '<span class="lang-en">' in html
    has_hi = '<span class="lang-hi">' in html
    
    status = "OK"
    errors = []
    if mermaid_divs > 0:
        errors.append(f"Mermaid divs: {mermaid_divs}")
    if mermaid_scripts > 0:
        errors.append(f"Mermaid scripts: {mermaid_scripts}")
    if mindmap_containers != 1:
        errors.append(f"Mindmap containers: {mindmap_containers}")
    if mindmap_nodes < 5:
        errors.append(f"Mindmap nodes count low: {mindmap_nodes}")
    if not has_card2:
        errors.append("Card 2 comment missing")
    if not (has_en and has_hi):
        errors.append("Bilingual tags missing")
        
    if errors:
        all_passed = False
        print(f"[{idx:02d}] {topic}: FAIL -> {', '.join(errors)}")
    else:
        print(f"[{idx:02d}] {topic}: PASS (Nodes: {mindmap_nodes}, Badges: {fact_badges}, Card2: Intact, Mermaid: 0)")

if all_passed:
    print("\nALL 18 UPSSSC COMPUTER TOPIC FILES PASSED 100% OF CHECKS!")
else:
    print("\nSOME CHECKS FAILED - PLEASE REVIEW ABOVE.")
