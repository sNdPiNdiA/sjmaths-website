# -*- coding: utf-8 -*-
import os
import re

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
EXCLUDE_DIRS = {".git", ".github", "node_modules", ".venv", "scratch", "dataconnect", ".firebase"}

ANALYTICS_INJECTION = """    <script type="module">
        const load = async () => {
            try {
                await import("/assets/js/firebase-analytics-only.min.js?v=1781927005");
            } catch (e) { console.debug("Analytics deferred"); }
        };
        if ('requestIdleCallback' in window) requestIdleCallback(load); else setTimeout(load, 3000);
    </script>
"""

def clean_and_inject_analytics(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    modified = False

    # Handle settings.html auth check specifically to avoid syntax error
    if "settings.html" in file_path:
        bad_pattern = 'else logEvent(analytics, "page_view", { page_title: "Settings", page_path: "/settings.html" });'
        if bad_pattern in content:
            content = content.replace(bad_pattern, '')
            modified = True
            print(f"[{file_path}] Cleaned up settings.html custom logEvent block.")

    # Match and clean any standard or custom dynamic load block for analytics-only
    # If a script block contains "firebase-analytics-only.min.js" or "firebase-analytics-only.js"
    # and does not contain "auth" or "db", we can replace the entire block with the standard injection.
    # This matches blocks regardless of comments, variable names, or spacing.
    pattern_any_script_block = re.compile(r"<script\s+type=[\"']module[\"']>(.*?)</script>", re.DOTALL)
    
    blocks_to_replace = []
    for match in pattern_any_script_block.finditer(content):
        block_content = match.group(1)
        if "firebase-analytics-only" in block_content and "auth" not in block_content and "db" not in block_content:
            blocks_to_replace.append(match.group(0))
            
    for block in blocks_to_replace:
        content = content.replace(block, ANALYTICS_INJECTION.strip())
        modified = True
        print(f"[{file_path}] Replaced block with standardized analytics injection.")

    # Check if this page uses firebase-config.min.js and has manual page_view calls
    if "firebase-config.min.js" in content:
        # Match pattern: logEvent(analytics, "page_view", ...);
        pattern_logevent = re.compile(
            r"logEvent\(\s*analytics\s*,\s*[\"']page_view[\"']\s*,\s*\{[^}]*\}\s*\);?", 
            re.DOTALL
        )
        if pattern_logevent.search(content):
            content = pattern_logevent.sub("", content)
            modified = True
            print(f"[{file_path}] Removed manual page_view logEvent from firebase-config page.")

    # Inject Analytics if missing entirely
    has_analytics = "firebase-analytics-only" in content or "firebase-config" in content
    
    if not has_analytics:
        if "</body>" in content:
            content = content.replace("</body>", f"{ANALYTICS_INJECTION}</body>")
            modified = True
            print(f"[{file_path}] Injected missing Google Analytics script block.")
        else:
            print(f"[{file_path}] Warning: No </body> tag found; skipped injection.")

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def main():
    html_count = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                html_count += 1
                try:
                    clean_and_inject_analytics(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    
    print(f"\nDone! Scanned {html_count} HTML files.")

if __name__ == "__main__":
    main()
