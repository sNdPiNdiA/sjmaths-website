import os
import re
import subprocess
import glob

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the UPSC Exam Focus dict block in lists
    # It starts with an open brace, has "label": "UPSC Exam Focus" (or single quotes), and matching nested braces.
    # We can write a regex or a simple brace-matcher. Let's do a robust brace-matching parser.
    
    modified = False
    
    # We can find where "UPSC Exam Focus" starts
    index = 0
    while True:
        pos = content.find('"UPSC Exam Focus"', index)
        if pos == -1:
            pos = content.find("'UPSC Exam Focus'", index)
        if pos == -1:
            break
            
        # Find the opening brace of this dict block before pos
        brace_open_idx = content.rfind('{', 0, pos)
        if brace_open_idx == -1:
            index = pos + 17
            continue
            
        # Match braces forward to find the closing brace
        brace_count = 1
        i = brace_open_idx + 1
        while i < len(content) and brace_count > 0:
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
            i += 1
            
        if brace_count == 0:
            # We found the block content[brace_open_idx:i]
            # Now let's remove it and any trailing or leading commas
            block = content[brace_open_idx:i]
            
            # Check if there is a comma before or after
            # Let's look at the surrounding characters
            left = content[:brace_open_idx].rstrip()
            right = content[i:].lstrip()
            
            if left.endswith(','):
                # Remove trailing comma from left
                left = left[:-1].rstrip()
            elif right.startswith(','):
                # Remove leading comma from right
                right = right[1:].lstrip()
                
            content = left + '\n' + right
            modified = True
            # Since we modified the content, we restart search from 0 (simple and safe)
            index = 0
        else:
            index = pos + 17

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully cleaned: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    py_files = glob.glob("add_*_mindmaps.py")
    print(f"Found {len(py_files)} python files.")
    for py_file in py_files:
        clean_file(py_file)
        
    print("\nRe-running all cleaned scripts...")
    for py_file in py_files:
        print(f"Running {py_file}...")
        subprocess.run(["python", py_file], check=True)
        print(f"Finished {py_file}\n")

if __name__ == '__main__':
    main()
