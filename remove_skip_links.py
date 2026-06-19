import os
import re
import subprocess

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    if 'class="skip-link"' not in content and "class='skip-link'" not in content:
        return False

    # Regex to match: optional spaces/tabs, followed by <a class="skip-link">...</a>, followed by optional spaces/newlines
    pattern = re.compile(r'[ \t]*<a\s+[^>]*class=["\']skip-link["\'][^>]*>.*?</a>\s*\n?', re.DOTALL | re.IGNORECASE)

    new_content, count = pattern.subn('', content)

    if count > 0:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False
    return False

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Run git grep to find all files containing "skip-link"
    print("Finding files with 'skip-link' using git grep...")
    try:
        output = subprocess.check_output(['git', 'grep', '-l', 'skip-link'], cwd=root_dir, text=True)
        files = [line.strip() for line in output.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        print("Error running git grep or no matches found:", e)
        return

    print(f"Found {len(files)} files. Starting removal...")
    
    modified_count = 0
    for file_path_rel in files:
        file_path = os.path.join(root_dir, file_path_rel)
        # Skip CSS files from tag removal
        if file_path.endswith('.css'):
            continue
            
        if process_file(file_path):
            modified_count += 1
            if modified_count % 100 == 0:
                print(f"Modified {modified_count} files...")

    print(f"Done! Modified {modified_count} files.")

if __name__ == '__main__':
    main()
