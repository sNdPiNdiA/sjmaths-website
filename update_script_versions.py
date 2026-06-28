import os
import re

ROOT_DIRS = ["ssc-cgl/general-awareness", "upsc"]

def update_versions(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Replace mindmap-engine.min.js?v=... with v=4
                    new_content = re.sub(
                        r'mindmap-engine\.min\.js\?v=\d+',
                        'mindmap-engine.min.js?v=4',
                        content
                    )
                    
                    # Replace mindmap.min.css?v=... with v=4
                    new_content = re.sub(
                        r'mindmap\.min\.css\?v=\d+',
                        'mindmap.min.css?v=4',
                        new_content
                    )
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                except Exception as e:
                    print(f"Error reading/writing {filepath}: {e}")
    print(f"Updated {count} HTML files in {directory}")

for d in ROOT_DIRS:
    if os.path.exists(d):
        update_versions(d)
