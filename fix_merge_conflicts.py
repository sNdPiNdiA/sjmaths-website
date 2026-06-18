import os
import re

def fix_merge_conflicts(filepath):
    """Remove git merge conflict markers from a file, keeping the HEAD (current) version."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if '<<<<<<< HEAD' not in content:
        return False
    
    original = content
    
    # Pattern: remove everything between <<<<<<< HEAD and ======= (keeping HEAD lines),
    # and remove everything between ======= and >>>>>>> (discarding incoming changes)
    # Result: keep only the HEAD version lines, remove markers
    
    lines = content.split('\n')
    result = []
    in_conflict = False
    in_head = False
    in_their = False
    
    for line in lines:
        if line.startswith('<<<<<<< HEAD'):
            in_conflict = True
            in_head = True
            in_their = False
            continue
        elif line == '=======' and in_conflict:
            in_head = False
            in_their = True
            continue
        elif line.startswith('>>>>>>>') and in_conflict:
            in_conflict = False
            in_head = False
            in_their = False
            continue
        
        if in_conflict and in_head:
            result.append(line)
        elif not in_conflict:
            result.append(line)
        # Skip their version lines
    
    new_content = '\n'.join(result)
    
    # Also clean up <br> followed by merge artifacts in the service-worker
    # Clean any blank lines at the end
    new_content = new_content.strip() + '\n'
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    fixed_count = 0
    for root, dirs, files in os.walk('.'):
        # Skip hidden dirs and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules', '.venv', '__pycache__')]
        for f in files:
            if f.endswith(('.html', '.js', '.css', '.json', '.xml', '.yml', '.yaml', '.md', '.txt')):
                path = os.path.join(root, f)
                try:
                    if fix_merge_conflicts(path):
                        print(f'Fixed: {path}')
                        fixed_count += 1
                except Exception as e:
                    print(f'Error processing {path}: {e}')
    
    print(f'\nTotal files fixed: {fixed_count}')

if __name__ == '__main__':
    main()