"""
Remove per-question timer-box divs from all Class 10 exercise files
and add a single exercise-level timer in the page header.
Also clean up inline timer-box CSS and add exercise-timer CSS.
"""
import re
from pathlib import Path

EXERCISES_DIR = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice")

count = 0
for html_file in sorted(EXERCISES_DIR.rglob("exercise-*.html")):
    text = html_file.read_text(encoding="utf-8")
    original = text

    # 1. Remove all per-question timer-box divs (various patterns)
    # Pattern A: 3-line block
    pattern_a = r'\s*<div class="timer-box" id="timer-box-t\d+">\s*\n\s*<i class="fas fa-clock"></i>\s*<span id="t\d+">00:00</span>\s*\n\s*</div>\s*\n'
    text = re.sub(pattern_a, '\n', text)
    
    # Pattern B: single-line block (some files may have it on one line)
    pattern_b = r'\s*<div class="timer-box" id="timer-box-t\d+">.*?</div>\s*\n'
    text = re.sub(pattern_b, '\n', text)

    # 2. Remove inline timer-box CSS (in <style> blocks)
    # Remove the timer section comment and styles
    timer_css_pattern = r'\s*/\*\s*---\s*TIMER\s*---\s*\*/.*?\.timer-box\.running i\s*\{[^}]*\}\s*\n'
    text = re.sub(timer_css_pattern, '\n', text, flags=re.DOTALL)
    
    # Also remove .timer-box responsive line
    text = re.sub(r'\s*\.timer-box\s*\{[^}]*\}\s*\n', '\n', text)

    # 3. Add exercise timer after <h1> in page-header (if not already present)
    if 'id="exercise-timer"' not in text:
        # Try matching the page-header h1 pattern used in Class 10 files
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
        print(f"  Updated: {html_file.relative_to(EXERCISES_DIR)}")

print(f"\nDone. Updated {count} files.")
