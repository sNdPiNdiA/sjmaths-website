import os
import re

topics = [
    "indus-valley-civilization",
    "vedic-culture-and-mahajanapadas",
    "buddhism-and-jainism",
    "maurya-gupta-and-harshavardhana",
    "delhi-sultanate",
    "mughal-empire",
    "maratha-vijayanagara-bhakti-sufi"
]

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsssc-intermediate-level\history"

for topic in topics:
    file_path = os.path.join(base_dir, topic, "index.html")
    if not os.path.exists(file_path):
        print(f"Skipping {topic}, not found.")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Ensure upsssc-intermediate.min.css is linked
    if "/assets/css/upsssc-intermediate.min.css" not in content:
        # replace upsssc-lower or insert before </head>
        if "upsssc-lower.min.css" in content:
            content = re.sub(r'<link [^>]*href="/assets/css/upsssc-lower\.min\.css[^"]*"[^>]*>\s*', '<link href="/assets/css/upsssc-intermediate.min.css" rel="stylesheet"/>\n', content)
        else:
            content = content.replace("</head>", '<link href="/assets/css/upsssc-intermediate.min.css" rel="stylesheet"/>\n</head>')

    # Remove obsolete css links if present
    content = re.sub(r'<link [^>]*href="/assets/css/upsssc-lower\.min\.css[^"]*"[^>]*>\s*', '', content)
    content = re.sub(r'<link [^>]*href="/assets/css/topic-details\.min\.css[^"]*"[^>]*>\s*', '', content)

    # 2. Remove redundant inline <style> block
    content = re.sub(r'<style>\s*/\* =========================================================\s*STRICT BILINGUAL ISOLATION[\s\S]*?</style>\s*', '', content)

    # 3. Standardize main container to topic-page-container
    content = re.sub(r'<main class="container"[^>]*>', '<main class="topic-page-container" id="main-content">', content)

    # 4. Remove redundant inline toggleLanguageMode script block
    content = re.sub(r'// Robust Synchronous Language Toggle Function[\s\S]*?window\.toggleLanguageMode[\s\S]*?};\s*', '', content)

    # 5. Link upsssc-intermediate.min.js
    if "/assets/js/upsssc-intermediate.min.js" not in content:
        if "upsssc-lower.min.js" in content:
            content = re.sub(r'<script [^>]*src="/assets/js/upsssc-lower\.min\.js[^"]*"[^>]*></script>', '<script defer src="/assets/js/upsssc-intermediate.min.js"></script>', content)
        else:
            content = content.replace("</body>", '<script defer src="/assets/js/upsssc-intermediate.min.js"></script>\n</body>')
    content = re.sub(r'<script [^>]*src="/assets/js/upsssc-lower\.min\.js[^"]*"[^>]*></script>\s*', '', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Standardized {topic} successfully.")
