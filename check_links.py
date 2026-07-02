import os
import re

html_path = "upsc/index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# find all href="./..."
links = re.findall(r'href="\./([^"]+)"', html)
broken = []

for link in links:
    # link should point to a folder, like ancient_history/.../
    path = os.path.join("upsc", link.strip('/'))
    if not os.path.exists(path):
        broken.append(link)

if not broken:
    print("All links are valid!")
else:
    print(f"Found {len(broken)} broken links:")
    for b in set(broken):
        print(f"- {b}")
