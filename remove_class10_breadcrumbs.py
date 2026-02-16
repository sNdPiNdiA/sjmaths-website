"""Remove hardcoded breadcrumb divs from Class 10 exercise files."""
import re
from pathlib import Path

EXERCISES_DIR = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice")
count = 0
for html_file in sorted(EXERCISES_DIR.rglob("exercise-*.html")):
    text = html_file.read_text(encoding="utf-8")
    original = text
    # Remove hardcoded breadcrumb div (multi-line)
    text = re.sub(
        r'\s*<div class="breadcrumb">\s*\n.*?</div>\s*\n',
        '\n',
        text,
        flags=re.DOTALL,
        count=1
    )
    if text != original:
        html_file.write_text(text, encoding="utf-8")
        count += 1
        print(f"  Removed breadcrumb from: {html_file.name}")
print(f"\nDone. Fixed {count} files.")
