import os
import re

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
DOMAIN = "https://sjmaths.com"

# Directories and files to exclude from processing
EXCLUDE_DIRS = ['.git', '.firebase', 'node_modules', 'components', 'scripts', 'tests', 'utils', 'assets', '.vscode']
EXCLUDE_FILES = ['dashboard.html', 'profile.html', 'settings.html', 'notifications.html', 'search.html', '404.html', 'offline.html', 'login.html', 'signup.html', 'teacher-dashboard.html']

def should_process(filepath):
    """Check if the file should be processed based on exclusions."""
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    parts = rel_path.split(os.sep)
    
    # Check directory exclusions
    for part in parts[:-1]:
        if part in EXCLUDE_DIRS:
            return False
            
    # Check file exclusions
    filename = parts[-1]
    if filename in EXCLUDE_FILES:
        return False
        
    return True

def get_canonical_url(filepath):
    """Generate the canonical URL based on the file path."""
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    
    # Convert Windows paths to URL forward slashes
    url_path = rel_path.replace(os.sep, '/')
    
    # Handle index.html - it should refer to its parent directory
    if url_path.endswith('index.html'):
        if url_path == 'index.html':
            return f"{DOMAIN}/"
        else:
            # Remove 'index.html' keeping the trailing slash
            return f"{DOMAIN}/{url_path[:-10]}"
    else:
        # the html file
        return f"{DOMAIN}/{url_path}"

def process_file(filepath):
    """Inject canonical tag into the HTML file if it doesn't exist."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if canonical tag already exists
    if re.search(r'<link\s+rel=["\']canonical["\'].*?>', content, re.IGNORECASE):
        #print(f"Skipping {os.path.relpath(filepath, ROOT_DIR)} - canonical tag already exists.")
        return False

    canonical_url = get_canonical_url(filepath)
    canonical_tag = f'    <link rel="canonical" href="{canonical_url}">\n'

    # Try inserting before </head>
    head_end_match = re.search(r'</head>', content, re.IGNORECASE)
    if head_end_match:
        new_content = content[:head_end_match.start()] + canonical_tag + content[head_end_match.start():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added canonical tag to {os.path.relpath(filepath, ROOT_DIR)}")
        return True
    else:
        print(f"Warning: Could not find </head> tag in {os.path.relpath(filepath, ROOT_DIR)}")
        return False

def main():
    processed_count = 0
    modified_count = 0
    
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if should_process(filepath):
                    processed_count += 1
                    if process_file(filepath):
                        modified_count += 1

    print(f"\nProcessing complete.")
    print(f"Total HTML files processed: {processed_count}")
    print(f"Files modified: {modified_count}")

if __name__ == "__main__":
    main()
