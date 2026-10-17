import os
import re

base_dir = "upsssc-computer"
folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)

print(f"Total topic folders: {len(folders)}")
for f in sorted(folders):
    p = os.path.join(base_dir, f, "index.html")
    if os.path.exists(p):
        size = os.path.getsize(p)
        with open(p, "r", encoding="utf-8") as fl:
            content = fl.read()
        m = pattern.search(content)
        has_mermaid_script = "mermaid.initialize" in content
        print(f"{f:<65} | Size: {size:>7} | Match: {bool(m)} | MermaidScript: {has_mermaid_script}")
    else:
        print(f"{f:<65} | Missing index.html")

