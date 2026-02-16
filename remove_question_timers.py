"""
Remove per-question timer-box divs from all Class 9 exercise files
and add a single exercise-level timer in the exercise header.
"""
import re
from pathlib import Path

EXERCISES_DIR = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-9\ncert-exercise-practice")

count = 0
for html_file in sorted(EXERCISES_DIR.rglob("exercise-*.html")):
    text = html_file.read_text(encoding="utf-8")
    original = text

    # 1. Remove all per-question timer-box divs (3 lines each)
    # Pattern: <div class="timer-box" id="timer-box-tN">
    #              <i class="fas fa-clock"></i> <span id="tN">00:00</span>
    #          </div>
    pattern = r'\s*<div class="timer-box" id="timer-box-t\d+">\s*\n\s*<i class="fas fa-clock"></i>\s*<span id="t\d+">00:00</span>\s*\n\s*</div>\s*\n'
    text = re.sub(pattern, '\n', text)

    # 2. Add exercise timer after <h1> in exercise-header (if not already present)
    if 'id="exercise-timer"' not in text:
        # Insert timer after the <h1>...</h1> line inside exercise-header
        text = re.sub(
            r'(<h1>Exercise [\d.]+ Practice</h1>)',
            r'''\1
            <div id="exercise-timer" class="exercise-timer-box">
                <i class="fas fa-clock"></i> <span id="exercise-time">00:00</span>
            </div>''',
            text
        )

    if text != original:
        html_file.write_text(text, encoding="utf-8")
        count += 1
        # Count how many timer-boxes were removed
        removed = len(re.findall(r'timer-box-t\d+', original)) - len(re.findall(r'timer-box-t\d+', text))
        print(f"  {html_file.name}: removed {removed} question timers, added exercise timer")

print(f"\nDone. Updated {count} files.")
