import os
import re

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"

def main():
    processed = 0
    modified = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        # Exclude directories
        if any(d in root for d in ['.git', 'node_modules', '.firebase']):
            continue
            
        for file in files:
            if not file.endswith(('.html', '.js', '.xml')):
                continue
                
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Case 1: href="https://sjmaths.com/classes/class-10/" -> href="https://sjmaths.com/class-10-maths/"
            # href="/classes/class-10/" -> href="/class-10-maths/"
            # We must preserve the optional domain prefix.
            content = re.sub(
                r'([\'"])((?:https://(?:www\.)?sjmaths\.com)?)/classes/class-(9|10|11|12)/(?:index\.html)?\1',
                r'\1\2/class-\3-maths/\1',
                content
            )
            
            # Case 2: >https://sjmaths.com/classes/class-10/< (sitemaps)
            content = re.sub(
                r'>((?:https://(?:www\.)?sjmaths\.com)?)/classes/class-(9|10|11|12)/(?:index\.html)?<',
                r'>\1/class-\2-maths/<',
                content
            )
            
            # Case 3: Bare strings without tags (e.g. JSON-LD items)
            # "https://sjmaths.com/classes/class-10/"
            content = re.sub(
                r'"((?:https://(?:www\.)?sjmaths\.com)?)/classes/class-(9|10|11|12)/(?:index\.html)?"',
                r'"\1/class-\2-maths/"',
                content
            )
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified += 1
            processed += 1

    print(f"Processed {processed} files, Modified {modified} files.")

if __name__ == "__main__":
    main()
