import os
import re
from pathlib import Path

ROOT = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website")
NOTES_DIR = ROOT / "classes" / "class-9" / "chapter-wise-notes"

def get_chapter_files():
    """Collect all chapter index.html files."""
    chapters = []
    if not NOTES_DIR.exists():
        print(f"Directory not found: {NOTES_DIR}")
        return []

    for chapter_dir in sorted(NOTES_DIR.iterdir()):
        if not chapter_dir.is_dir():
            continue
        
        index_file = chapter_dir / "index.html"
        if index_file.exists():
            # Extract chapter number for sorting
            m = re.match(r'chapter-(\d+)', chapter_dir.name)
            chap_num = int(m.group(1)) if m else 999
            
            chapters.append({
                'path': index_file,
                'dir_name': chapter_dir.name,
                'chap_num': chap_num
            })
    
    # Sort by chapter number
    chapters.sort(key=lambda x: x['chap_num'])
    return chapters

def check_navigation(chapters):
    issues = []
    print(f"Checking {len(chapters)} chapters for navigation integrity...\n")

    for i, chap in enumerate(chapters):
        content = chap['path'].read_text(encoding='utf-8', errors='ignore')
        
        # Extract body tag attributes
        body_match = re.search(r'<body([^>]*)>', content, re.IGNORECASE)
        if not body_match:
            issues.append(f"[{chap['dir_name']}] No <body> tag found.")
            continue
            
        attrs = body_match.group(1)
        
        # Extract data-prev and data-next
        prev_match = re.search(r'data-prev="([^"]*)"', attrs)
        next_match = re.search(r'data-next="([^"]*)"', attrs)
        
        prev_link = prev_match.group(1) if prev_match else None
        next_link = next_match.group(1) if next_match else None
        
        # Validate PREV
        if i == 0:
            if prev_link:
                 issues.append(f"[{chap['dir_name']}] First chapter should not have data-prev (found: {prev_link})")
        else:
            if not prev_link:
                issues.append(f"[{chap['dir_name']}] Missing data-prev attrib.")
            else:
                # Check file existence
                target = (chap['path'].parent / prev_link).resolve()
                if not target.exists():
                     issues.append(f"[{chap['dir_name']}] Broken data-prev data: {prev_link} -> {target}")
                
                 # Check logic (should point to previous chapter)
                expected_prev_dir = chapters[i-1]['dir_name']
                if expected_prev_dir not in str(target):
                    issues.append(f"[{chap['dir_name']}] Logical error in data-prev. Expected to point to {expected_prev_dir}, but points to {prev_link}")

        # Validate NEXT
        if i == len(chapters) - 1:
            if next_link:
                 issues.append(f"[{chap['dir_name']}] Last chapter should not have data-next (found: {next_link})")
        else:
            if not next_link:
                issues.append(f"[{chap['dir_name']}] Missing data-next attrib.")
            else:
                # Check file existence
                target = (chap['path'].parent / next_link).resolve()
                if not target.exists():
                     issues.append(f"[{chap['dir_name']}] Broken data-next data: {next_link} -> {target}")
                
                # Check logic (should point to next chapter)
                expected_next_dir = chapters[i+1]['dir_name']
                if expected_next_dir not in str(target):
                     issues.append(f"[{chap['dir_name']}] Logical error in data-next. Expected to point to {expected_next_dir}, but points to {next_link}")

        # Validate Hardcoded Nav Buttons
        nav_btns = re.findall(r'<a[^>]+href="([^"]*)"[^>]*class="[^"]*nav-btn[^"]*"[^>]*>(.*?)</a>', content, re.IGNORECASE | re.DOTALL)
        for href, text in nav_btns:
            # Resolve href
            if href.startswith('/'):
                # Absolute path from root
                target = (ROOT / href.lstrip('/')).resolve()
            else:
                # Relative path
                target = (chap['path'].parent / href).resolve()
            
            if not target.exists():
                issues.append(f"[{chap['dir_name']}] Broken Nav Button Link: {href} -> {target}")
            
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            # print(f"  Checked btn '{clean_text}' -> {target.name}") # Debug

    return issues

def main():
    chapters = get_chapter_files()
    issues = check_navigation(chapters)
    
    with open("nav_audit.txt", "w", encoding="utf-8") as f:
        if issues:
            f.write("FOUND ISSUES:\n")
            for issue in issues:
                f.write(f" - {issue}\n")
        else:
            f.write("SUCCESS: All chapter navigation links are valid and logically correct.\n")
    
    print("Audit complete. Check nav_audit.txt")

if __name__ == "__main__":
    main()
