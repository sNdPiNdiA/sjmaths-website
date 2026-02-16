"""
Final fix for Class 10 exercise files (Chapters 11-14).
1. Appends exercise timer CSS to exercise.min.css and exercise-shared.min.css.
2. Cleans up Ch 11-14 HTML files:
   - Removes inline JS timer logic.
   - Removes hardcoded breadcrumbs.
   - Injects link to exercise.min.css.
"""
import re
from pathlib import Path

# CSS to append
TIMER_CSS = """.exercise-timer-box{display:inline-flex;align-items:center;gap:8px;background:#f0f0f0;padding:8px 20px;border-radius:50px;font-family:'Poppins',sans-serif;font-weight:600;font-size:1rem;color:#555;transition:.3s;margin-top:10px}.exercise-timer-box.running{background:#e8f5e9;color:#27ae60;border:1px solid #27ae60}@keyframes pulse-timer{0%{transform:scale(1)}50%{transform:scale(1.05)}100%{transform:scale(1)}}.exercise-timer-box.running i{animation:pulse-timer 1s infinite}"""

ROOT = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website")
CSS_DIR = ROOT / "assets" / "css"
CLASS10_DIR = ROOT / "classes" / "class-10" / "ncert-exercise-practice"

def update_css_file(filename):
    file_path = CSS_DIR / filename
    if file_path.exists():
        text = file_path.read_text(encoding="utf-8")
        if ".exercise-timer-box" not in text:
            file_path.write_text(text + "\n" + TIMER_CSS, encoding="utf-8")
            print(f"Updated {filename}")
        else:
            print(f"{filename} already has timer styles.")
    else:
        print(f"Warning: {filename} not found.")

# 1. Update CSS files
update_css_file("exercise.min.css")
update_css_file("exercise-shared.min.css")

# 2. Process HTML files (Ch 11-14)
# Identify folders for Ch 11-14
target_chapters = ["chapter-11", "chapter-12", "chapter-13", "chapter-14"]
count = 0

for chapter_dir in CLASS10_DIR.iterdir():
    if not chapter_dir.is_dir(): continue
    # Check if directory name starts with one of the targets
    if any(chapter_dir.name.startswith(prefix) for prefix in target_chapters):
        for html_file in chapter_dir.glob("exercise-*.html"):
            text = html_file.read_text(encoding="utf-8")
            original = text
            
            # A. Remove inline JS timer logic
            # Pattern: <script>\s*// --- AUTO-TIMER LOGIC ---.*?</script>
            # We use a broad pattern to catch the script block containing 'let timers = {};'
            # Be careful not to remove other scripts.
            # Look for strict start of the timer block
            if "// --- AUTO-TIMER LOGIC ---" in text:
                text = re.sub(
                    r'<script>\s*// --- AUTO-TIMER LOGIC ---.*?</script>', 
                    '', 
                    text, 
                    flags=re.DOTALL
                )
            
            # B. Remove hardcoded breadcrumb
            # <div class="breadcrumb">...</div>
            # Using a safer regex that ensures we match the div class breadcrumb
            text = re.sub(
                r'\s*<div class="breadcrumb">\s*<a href="#">Home</a>.*?</div>\s*',
                '\n',
                text,
                flags=re.DOTALL
            )
            
            # C. Inject CSS link if missing
            if 'href="/assets/css/exercise.min.css"' not in text:
                # Inject before </head>
                css_link = '    <link rel="stylesheet" href="/assets/css/exercise.min.css">\n'
                text = text.replace('</head>', css_link + '</head>')
            
            if text != original:
                html_file.write_text(text, encoding="utf-8")
                count += 1
                print(f"Updated {html_file.name}")

print(f"\nProcessed Ch 11-14 files. Updated {count} files.")
