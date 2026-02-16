"""
Add exercise-level timer to remaining Class 10 exercise files 
(chapters 1-10) that have a different HTML structure.
"""
import re
from pathlib import Path

EXERCISES_DIR = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice")

count = 0
for html_file in sorted(EXERCISES_DIR.rglob("exercise-*.html")):
    text = html_file.read_text(encoding="utf-8")
    
    # Skip if already has exercise timer
    if 'id="exercise-timer"' in text:
        continue
    
    original = text
    
    # Pattern for Class 10 chapters 1-10: <h1>ChapterName – Exercise X.Y</h1>
    # Insert timer after this h1
    text = re.sub(
        r'(<h1>[^<]+</h1>)',
        r'''\1
            <div id="exercise-timer" class="exercise-timer-box">
                <i class="fas fa-clock"></i> <span id="exercise-time">00:00</span>
            </div>''',
        text,
        count=1  # Only replace the first <h1>
    )
    
    if text != original:
        html_file.write_text(text, encoding="utf-8")
        count += 1
        print(f"  Updated: {html_file.relative_to(EXERCISES_DIR)}")

print(f"\nDone. Updated {count} files.")
