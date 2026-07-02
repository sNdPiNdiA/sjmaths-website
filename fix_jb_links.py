import os
import re

html_path = "upsc/index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# find all href="./..."
links = re.findall(r'href="\./([^"]+)"', html)
changed_count = 0

for link in links:
    if link.startswith('ancient_history/Jainism-and-Buddhism/'):
        folder_name = link.split('/')[-2]
        
        # Check if it exists in Jainism/
        j_path = os.path.join("upsc", "ancient_history", "Jainism", folder_name)
        b_path = os.path.join("upsc", "ancient_history", "Buddhism", folder_name)
        
        new_link = None
        if os.path.exists(j_path):
            new_link = f"ancient_history/Jainism/{folder_name}/"
        elif os.path.exists(b_path):
            new_link = f"ancient_history/Buddhism/{folder_name}/"
            
        if new_link:
            html = html.replace(f'href="./{link}"', f'href="./{new_link}"')
            changed_count += 1

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Fixed {changed_count} links in upsc/index.html")
