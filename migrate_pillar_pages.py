import os
import re
import shutil

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
CLASSES = ['9', '10', '11', '12']

def main():
    for cls in CLASSES:
        old_dir = os.path.join(ROOT_DIR, 'classes', f'class-{cls}')
        old_file = os.path.join(old_dir, 'index.html')
        
        new_dir = os.path.join(ROOT_DIR, f'class-{cls}-maths')
        new_file = os.path.join(new_dir, 'index.html')
        
        if not os.path.exists(old_file):
            print(f"File not found: {old_file}")
            continue
            
        # Create new directory if it doesn't exist
        os.makedirs(new_dir, exist_ok=True)
        
        # Read the content
        with open(old_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix relative assets (CSS, JS) from ../../assets to /assets
        # The old file was 2 levels deep (classes/class-X/). 
        # The new file is 1 level deep (class-X-maths/).
        # It's safest to convert all ../../assets to /assets
        content = re.sub(r'(href|src)=["\']\.\./\.\./assets/', r'\1="/assets/', content)
        
        # Fix Canonical tag
        old_canonical = f"https://sjmaths.com/classes/class-{cls}/"
        new_canonical = f"https://sjmaths.com/class-{cls}-maths/"
        content = content.replace(old_canonical, new_canonical)
        
        # Also fix any OG url
        content = content.replace(f'property="og:url" content="{old_canonical}"', f'property="og:url" content="{new_canonical}"')
        
        # Fix JSON-LD Breadcrumbs
        # Change the Breadcrumb item for Class X to point to new URL
        content = content.replace(f'"item": "{old_canonical}"', f'"item": "{new_canonical}"')
        
        # Also inside Schema "CollectionPage" URL
        content = content.replace(f'"url": "{old_canonical}"', f'"url": "{new_canonical}"')
        
        # Home Breadcrumb internal link
        content = content.replace(f'<a href="/classes/class-{cls}/">Class {cls}</a>', f'<a href="/class-{cls}-maths/">Class {cls}</a>')
        
        # Write the new file
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Created {new_file}")

if __name__ == "__main__":
    main()
