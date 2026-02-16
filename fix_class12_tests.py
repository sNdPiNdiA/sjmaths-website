"""
Script to fix Class 12 test files by adding missing navigation buttons.
Function: Adds btnPrev and btnNext after #solutionArea in all chapter-wise test files.
"""
import re
from pathlib import Path

TESTS_DIR = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-12\tests\chapter-wise")

NAV_BUTTONS_HTML = """
            <div class="nav-actions" style="margin-top: 20px; display: flex; justify-content: space-between; gap: 10px;">
                <button id="btnPrev" class="btn-nav secondary">Previous</button>
                <button id="btnNext" class="btn-nav primary">Next</button>
            </div>"""

count = 0
for html_file in TESTS_DIR.rglob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    
    # Skip if already has buttons
    if 'id="btnPrev"' in text:
        print(f"Skipping {html_file.name} (already has buttons)")
        continue
        
    # Find insertion point
    # We look for the closing div of solutionArea
    # The pattern matches <div id="solutionArea" ... > ... </div>
    # But since it might be empty or contain content, we look for the SPECIFIC closing tag structure
    # seen in the files: 
    # <div id="solutionArea" class="solution-div">
    #     <!-- Solution shown after submit -->
    # </div>
    
    if '<div id="solutionArea" class="solution-div">' in text:
        # Simple string replacement for valid HTML structure
        target = '<!-- Solution shown after submit -->\n            </div>'
        replacement = target + NAV_BUTTONS_HTML
        
        if target in text:
            new_text = text.replace(target, replacement)
            html_file.write_text(new_text, encoding="utf-8")
            count += 1
            print(f"Fixed {html_file.name}")
        else:
            # Fallback regex if indentation varies
            pattern = r'(<div id="solutionArea" class="solution-div">.*?</div>)'
            match = re.search(pattern, text, re.DOTALL)
            if match:
                new_text = text[:match.end()] + NAV_BUTTONS_HTML + text[match.end():]
                html_file.write_text(new_text, encoding="utf-8")
                count += 1
                print(f"Fixed {html_file.name} (regex)")
            else:
                print(f"Could not find insertion point in {html_file.name}")
    else:
        print(f"No solutionArea found in {html_file.name}")

print(f"\nTotal files fixed: {count}")
