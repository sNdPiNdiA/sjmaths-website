import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

pattern = re.compile(r'(<!--\s*Card 1:.*?-->.*?)(?=<!--\s*Card 2:)', re.DOTALL)

from mindmap_t11_internet import mm_t11
from mindmap_t12_www import mm_t12
from mindmap_t13_ip import mm_t13
from mindmap_t14_email import mm_t14

batch3_map = {
    'internet': mm_t11,
    'world-wide-web-www': mm_t12,
    'internet-protocol-ip-address': mm_t13,
    'creation-of-e-mail-id-and-use-operation-of-e-mail': mm_t14
}

print("Starting Batch 3 replacements (Topics 11-14)...")
for topic, new_mm in batch3_map.items():
    file_path = os.path.join('upsssc-computer', topic, 'index.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = pattern.search(content)
    if not m:
        print(f"ERROR: Could not find Card 1 pattern in {topic}")
        continue
    
    updated_content = content[:m.start()] + new_mm + "\n\n" + content[m.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"SUCCESS: Replaced Card 1 in {topic}")

print("Batch 3 completed successfully!")
