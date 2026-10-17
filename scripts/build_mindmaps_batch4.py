import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

pattern = re.compile(r'(<!--\s*Card 1:.*?-->.*?)(?=<!--\s*Card 2:)', re.DOTALL)

from mindmap_t15_gadgets import mm_t15
from mindmap_t16_it import mm_t16
from mindmap_t17_office import mm_t17
from mindmap_t18_india import mm_t18

batch4_map = {
    'it-gadgets-and-their-applications': mm_t15,
    'information-technology': mm_t16,
    'important-elements-of-word-processing-ms-word-and-excel-processing-ms-excel': mm_t17,
    'india-s-achievements-in-this-field': mm_t18
}

print("Starting Batch 4 replacements (Topics 15-18)...")
for topic, new_mm in batch4_map.items():
    file_path = os.path.join('upsssc-computer', topic, 'index.html')
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        continue
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

print("Batch 4 completed successfully!")
