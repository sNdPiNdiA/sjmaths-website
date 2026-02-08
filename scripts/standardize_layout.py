
import os
import re

# Configuration
ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
ASSETS_PATH_PREFIX = "/assets"
EXCLUDE_DIRS = {
    "node_modules",
    "_legacy_site",
    "_nextjs_migration_backup",
    ".git",
    ".firebase",
    "dataconnect"
}

# Scripts to remove
SCRIPTS_TO_REMOVE = [
    r'<script\s+src=[\'"].*?/exercise-header\.js[\'"].*?></script>',
    r'<script\s+src=[\'"].*?/exercise-footer\.js[\'"].*?></script>',
    r'<script\s+src=[\'"].*?/checkBrokenLinks\.js[\'"].*?></script>',
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
    # Identify the tag name
    tag_match = re.match(r'<([a-zA-Z0-9]+)', content[start_index:])
    if not tag_match:
        return None
    
    tag_name = tag_match.group(1).lower()
    
    # Simple stack-based parser
    depth = 0
    i = start_index
    
    # Iterate through the string looking for tags
    while i < len(content):
        # Find next tag start
        next_tag_start = content.find('<', i)
        if next_tag_start == -1:
            break
            
        # Check if it's a closing tag
        if content[next_tag_start:next_tag_start+2] == '</':
            close_tag_match = re.match(r'</([a-zA-Z0-9]+)>', content[next_tag_start:])
            if close_tag_match:
                close_tag_name = close_tag_match.group(1).lower()
                if close_tag_name == tag_name:
                    depth -= 1
                    if depth == 0:
                        # Found the matching closing tag
                        return next_tag_start + len(close_tag_match.group(0))
                i = next_tag_start + 1
            else:
                 i = next_tag_start + 1
        
        # Check if it's an opening tag
        elif content[next_tag_start:next_tag_start+1] == '<':
            # Check if self-closing or regular
            # Note: This is a simplified check. HTML5 void elements don't strictly need /> but generic logic often requires mismatched tag awareness.
            # For header/footer/div, they are normal tags.
            
            open_tag_match = re.match(r'<([a-zA-Z0-9]+).*?>', content[next_tag_start:], re.DOTALL)
            if open_tag_match:
                found_tag = open_tag_match.group(1).lower()
                full_tag = open_tag_match.group(0)
                
                # Check for self-closing slash at end of tag content
                if not full_tag.endswith('/>') and found_tag == tag_name:
                     depth += 1
                
                i = next_tag_start + len(full_tag)
            else:
                 i = next_tag_start + 1
        else:
            i += 1
            
    return None

def strip_element_by_id(content, element_id):
    """Removes element with specific ID, handling nested tags."""
    # Find start
    pattern = re.compile(f'<div\\s+id=["\']{element_id}["\'].*?>', re.IGNORECASE)
    match = pattern.search(content)
    if match:
        start_idx = match.start()
        end_idx = find_tag_end(content, start_idx)
        if end_idx:
            # Replace with empty container
            return content[:start_idx] + f'<div id="{element_id}"></div>' + content[end_idx:]
    return content

def strip_tag(content, tag_name):
    """Removes a tag (like <header> or <footer>), handling nesting."""
    pattern = re.compile(f'<{tag_name}.*?>', re.IGNORECASE)
    match = pattern.search(content)
    if match:
        start_idx = match.start()
        end_idx = find_tag_end(content, start_idx)
        if end_idx:
            # Replace with appropriate container
            container_id = "header-container" if tag_name == "header" else "footer-container"
            return content[:start_idx] + f'<div id="{container_id}"></div>' + content[end_idx:]
    return content

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    original_content = content
    
    # 1. Strip Header
    if '<div id="header-container"' in content:
        content = strip_element_by_id(content, "header-container")
    elif '<header' in content:
        content = strip_tag(content, "header")
    else:
        if '<body' in content:
            content = re.sub(r'(<body.*?>)', r'\1\n    <div id="header-container"></div>', content, count=1, flags=re.IGNORECASE)

    # 2. Strip Footer
    if '<div id="footer-container"' in content:
        content = strip_element_by_id(content, "footer-container")
    elif '<footer' in content:
        content = strip_tag(content, "footer")
    else:
         content = re.sub(r'(</body>)', r'    <div id="footer-container"></div>\n\1', content, count=1, flags=re.IGNORECASE)

    # 3. Remove Legacy Scripts
    for script_pattern in SCRIPTS_TO_REMOVE:
        content = re.sub(script_pattern, '', content, flags=re.IGNORECASE)

    # 4. Inject Global Scripts
    global_header_script = '<script src="/assets/js/global-header.js" defer></script>'
    global_footer_script = '<script src="/assets/js/global-footer.js" defer></script>'
    
    has_header_script = 'src="/assets/js/global-header.js"' in content
    has_footer_script = 'src="/assets/js/global-footer.js"' in content

    scripts_to_add = []
    if not has_header_script:
        scripts_to_add.append(global_header_script)
    if not has_footer_script:
        scripts_to_add.append(global_footer_script)

    if scripts_to_add:
        injection_block = "\n    " + "\n    ".join(scripts_to_add)
        if 'src="/assets/js/main.min.js"' in content:
             content = content.replace('<script src="/assets/js/main.min.js"', injection_block + '\n    <script src="/assets/js/main.min.js"')
        elif 'src="assets/js/main.min.js"' in content:
             content = content.replace('<script src="assets/js/main.min.js"', injection_block + '\n    <script src="assets/js/main.min.js"')         
        else:
             content = content.replace('</body>', injection_block + '\n</body>')

    if content != original_content:
        # Check against catastrophic deletion
        if len(content) < len(original_content) * 0.5:
             print(f"WARNING: Skipping {file_path} due to suspicious content size reduction.")
             return

        print(f"Updating: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    print(f"Starting standardization from {ROOT_DIR}")
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
