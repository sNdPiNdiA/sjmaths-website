
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

# Elements to remove
IDS_TO_REMOVE = [
    "darkToggle",
    "theme-toggle"
]

CLASSES_TO_REMOVE_REGEX = [
    r'floating-theme-btn',
    r'floating-dark-btn',
    r'theme-toggle-btn'
]

# Specific inline script patterns to remove (that often accompany these buttons)
INLINE_SCRIPTS_TO_REMOVE = [
    r'// Dark Mode Toggle Logic[\s\S]*?}\)\s*;\s*', # Common pattern observed in grep
    r'const themeIcon\s*=\s*document\.getElementById[\s\S]*?themeIcon\.classList\.add\(\'fa-moon\'\);',
    r'const darkToggle\s*=\s*document\.getElementById[\s\S]*?darkToggle\.addEventListener[\s\S]*?}\);'
]

def should_process(file_path):
    normalized_path = file_path.replace("\\", "/")
    path_parts = normalized_path.split("/")
    for part in path_parts:
        if part in EXCLUDE_DIRS:
            return False
    return file_path.endswith(".html")

def find_tag_end(content, start_index):
    """
    Finds the end index of a matched tag, handling nesting.
    Assumes start_index points to the character '<' of the opening tag.
    Returns the index *after* the closing tag.
    """
    # Simple logic similar to standardize_layout.py but customized if needed.
    # For buttons, nesting is usually shallow (<i> icon inside).
    
    tag_match = re.match(r'<([a-zA-Z0-9]+)', content[start_index:])
    if not tag_match:
        return None
    
    tag_name = tag_match.group(1).lower()
    
    # We can use a simpler approach for these specific known buttons if they are standard.
    # But a robust parser is safer.
    
    depth = 0
    i = start_index
    while i < len(content):
        next_tag_start = content.find('<', i)
        if next_tag_start == -1:
            break
            
        if content[next_tag_start:next_tag_start+2] == '</':
             close_tag_match = re.match(r'</([a-zA-Z0-9]+)>', content[next_tag_start:])
             if close_tag_match:
                 close_name = close_tag_match.group(1).lower()
                 if close_name == tag_name:
                     depth -= 1
                     if depth == 0:
                         return next_tag_start + len(close_tag_match.group(0))
                 i = next_tag_start + 1
             else:
                 i = next_tag_start + 1
        elif content[next_tag_start:next_tag_start+1] == '<':
            open_tag_match = re.match(r'<([a-zA-Z0-9]+).*?>', content[next_tag_start:], re.DOTALL)
            if open_tag_match:
                tag = open_tag_match.group(1).lower()
                full_tag = open_tag_match.group(0)
                if not full_tag.endswith('/>') and tag == tag_name: # Simple void check
                    depth += 1
                i = next_tag_start + len(full_tag)
            else:
                 i = next_tag_start + 1
        else:
             i += 1
    return None

def strip_element_by_id(content, element_id):
    # Case insensitive ID search
    pattern = re.compile(f'<(button|div|a)\\s+[^>]*id=["\']{element_id}["\']', re.IGNORECASE)
    match = pattern.search(content)
    while match:
        start_idx = match.start()
        end_idx = find_tag_end(content, start_idx)
        if end_idx:
            content = content[:start_idx] + content[end_idx:]
        else:
            # Fallback for malformed or simple tags if find_tag_end fails (e.g. strict void tag handling mismatch)
            # Try simple close
            simple_close = content.find(f'</{match.group(1)}>', start_idx)
            if simple_close != -1:
                 content = content[:start_idx] + content[simple_close + len(match.group(1)) + 3:]
            else:
                 break # Cannot safely remove
        match = pattern.search(content) # Find next occurrence
    return content

def strip_element_by_class(content, class_regex):
    pattern = re.compile(f'<(button|div|a)\\s+[^>]*class=["\'][^"\']*?{class_regex}[^"\']*?["\']', re.IGNORECASE)
    match = pattern.search(content)
    while match:
        start_idx = match.start()
        end_idx = find_tag_end(content, start_idx)
        if end_idx:
            content = content[:start_idx] + content[end_idx:]
        else:
             # Fallback
            simple_close = content.find(f'</{match.group(1)}>', start_idx)
            if simple_close != -1:
                 content = content[:start_idx] + content[simple_close + len(match.group(1)) + 3:]
            else:
                 break
        match = pattern.search(content)
    return content

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    original_content = content

    # 1. Remove by ID
    for eid in IDS_TO_REMOVE:
        content = strip_element_by_id(content, eid)

    # 2. Remove by Class
    for cls in CLASSES_TO_REMOVE_REGEX:
        content = strip_element_by_class(content, cls)

    if content != original_content:
        print(f"Removing legacy buttons from: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    print(f"Starting button removal from {ROOT_DIR}")
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
