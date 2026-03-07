import os
import re

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"

def main():
    processed = 0
    modified = 0
    
    # We want to find cases where it says href="/class-12-maths/chapter-wise-notes/"
    # or href="https://sjmaths.com/class-12-maths/chapter-wise-notes/"
    # and change the root back to /classes/class-12/...
    
    # List of known sub-hubs we did NOT move:
    SUB_HUBS = [
        'chapter-wise-notes',
        'ncert-exercise-practice',
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
    
    # Build regex: (href="|href='|src="|src='|url:\s*'|url:\s*")((?:https://(?:www\.)?sjmaths\.com)?)/class-(9|10|11|12)-maths/([a-zA-Z0-9-]+)
    
    pattern = re.compile(r'([\'">])((?:https://(?:www\.)?sjmaths\.com)?)/class-(9|10|11|12)-maths/([a-zA-Z0-9-]+)/')
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if any(d in root for d in ['.git', 'node_modules', '.firebase']):
            continue
            
        for file in files:
            if not file.endswith(('.html', '.js', '.xml')):
                continue
                
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            def replacer(match):
                prefix = match.group(1) # ' or " or >
                domain = match.group(2) # https://... or empty
                cls = match.group(3)    # 9, 10, 11, 12
                sub_dir = match.group(4)# chapter-wise-notes
                
                # Check if it's one of the deep subdirectories we didn't migrate
                # If it's just index.html, it's fine. If it's a sub-hub, we must revert it.
                # Actually, any subdirectory under /class-X-maths/ MUST be reverted
                # because we ONLY moved the root index.html to /class-X-maths/
                
                # So if there's a sub_dir here, it's 100% wrong.
                
                return f"{prefix}{domain}/classes/class-{cls}/{sub_dir}/"
                
            content = pattern.sub(replacer, content)
            
            # Also need to fix JSON-LD bare strings: "https://sjmaths.com/class-12-maths/chapter-wise-notes/"
            # The regex above catches them if they start with open quote -> match.group(1) == '"'
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified += 1
            processed += 1

    print(f"Processed {processed} files, Modified {modified} files.")

if __name__ == "__main__":
    main()
