import os
import re

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
CLASSES = ['9', '10', '11', '12']

def main():
    modified = 0
    
    # These are the sub-hubs that we know exist under /classes/class-X/
    SUB_HUBS = [
        'chapter-wise-notes',
        'ncert-exercise-practice',
        'previous-years-questions-chapter-wise',
        'previous-year-questions',
        'full-length-test-papers',
        'worksheets',
        'tests',
        'previous-years-papers',
        'revision-notes',
        'important-questions',
        'mcqs',
        'ncert-exemplar'
    ]
    
    for cls in CLASSES:
        filepath = os.path.join(ROOT_DIR, f'class-{cls}-maths', 'index.html')
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        for hub in SUB_HUBS:
            # Replace relative links like href="chapter-wise-notes/" 
            # with absolute links like href="/classes/class-12/chapter-wise-notes/"
            pattern = re.compile(rf'href=["\']{re.escape(hub)}/?["\']')
            content = pattern.sub(f'href="/classes/class-{cls}/{hub}/"', content)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed relative links in {filepath}")
            modified += 1

    print(f"Modified {modified} dashboard files.")

if __name__ == "__main__":
    main()
