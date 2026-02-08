
import os
import re

# Configuration
ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
EXCLUDE_DIRS = {
    "node_modules",
    "_legacy_site",
    "_nextjs_migration_backup",
    ".git",
    ".firebase",
    "dataconnect"
}

# CSS Files to Ensure (Absolute Paths)
REQUIRED_CSS = [
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" crossorigin="anonymous">',
    '<link rel="stylesheet" href="/assets/css/main.min.css">',
    '<link rel="stylesheet" href="/assets/css/layout.min.css">',
    '<link rel="stylesheet" href="/assets/css/component.min.css">',
    '<link rel="stylesheet" href="/assets/css/improved-ui.min.css">'
]

def should_process(file_path):
    normalized_path = file_path.replace("\\", "/")
    path_parts = normalized_path.split("/")
    for part in path_parts:
        if part in EXCLUDE_DIRS:
            return False
    return file_path.endswith(".html")

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    original_content = content
    
    # Check for <head>
    head_match = re.search(r'<head.*?>', content, re.IGNORECASE)
    if not head_match:
        if "chapter-1-number-systems" in file_path:
             print(f"DEBUG: No <head> found in {file_path}")
        return

    insertions = []
    
    # 1. FontAwesome
    if 'font-awesome' not in content and 'all.min.css' not in content:
        insertions.append(REQUIRED_CSS[0])
        
    # 2. Main CSS
    if 'main.min.css' not in content:
        insertions.append(REQUIRED_CSS[1])
        
    # 3. Layout CSS
    if 'layout.min.css' not in content:
        insertions.append(REQUIRED_CSS[2])
        
    # 4. Component CSS
    if 'component.min.css' not in content:
        insertions.append(REQUIRED_CSS[3])
        
    # 5. Improved UI CSS
    if 'improved-ui.min.css' not in content:
        insertions.append(REQUIRED_CSS[4])
        
    if not insertions:
        if "chapter-1-number-systems" in file_path:
             print(f"DEBUG: No insertions needed for {file_path}")
        return

    # Insert before </head>
    closing_head = re.search(r'</head>', content, re.IGNORECASE)
    if closing_head:
        insert_text = "\n    " + "\n    ".join(insertions)
        content = content[:closing_head.start()] + insert_text + "\n" + content[closing_head.start():]
    else:
        if "chapter-1-number-systems" in file_path:
             print(f"DEBUG: No </head> closing tag found in {file_path}")
        return
    
    if content != original_content:
        print(f"Updating CSS in: {file_path}")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"ERROR writing to {file_path}: {e}")

def main():
    print(f"Starting CSS standardization from {ROOT_DIR}")
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            file_path = os.path.join(root, file)
            if should_process(file_path):
                process_file(file_path)
                count += 1
    print(f"Processed {count} HTML files.")

if __name__ == "__main__":
    main()
