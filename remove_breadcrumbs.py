"""Remove hardcoded breadcrumb divs from Class 9 exercise files.

These duplicate the dynamic breadcrumb injected by global-header.js.
Uses DOTALL to handle multi-line breadcrumb content.
"""
import re
from pathlib import Path

EXERCISES_DIR = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-9\ncert-exercise-practice")

count = 0
for html_file in sorted(EXERCISES_DIR.rglob("exercise-*.html")):
    text = html_file.read_text(encoding="utf-8")
    
    # Match the breadcrumb div block — content may span multiple lines
    pattern = r'\r?\n\s*<div class="breadcrumb">.*?</div>\s*\r?\n'
    new_text = re.sub(pattern, '\n', text, flags=re.DOTALL)
    
    if new_text != text:
        html_file.write_text(new_text, encoding="utf-8")
        count += 1
        print(f"  Removed breadcrumb from: {html_file.name}")

print(f"\nDone. Removed breadcrumbs from {count} files.")
