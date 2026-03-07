import re
import os

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"

def main():
    classes_dir = os.path.join(ROOT_DIR, 'classes')
    modified = 0
    pattern = re.compile(r'(<section class="seo-pillar-content".*?</section>)\s*(</main>)', re.DOTALL)
    
    for root, dirs, files in os.walk(classes_dir):
        if 'index.html' in files:
            path = os.path.join(root, 'index.html')
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find and swap the section and </main> if the section is before </main>
            if pattern.search(content):
                new_content = pattern.sub(r'\2\n\n    \1', content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {path}")
                modified += 1
                
    print(f"Total fixed: {modified}")

if __name__ == "__main__":
    main()
