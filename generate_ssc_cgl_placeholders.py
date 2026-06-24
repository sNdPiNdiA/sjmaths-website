#!/usr/bin/env python3
"""
Generate placeholder index.html files for all directories under ssc-cgl
that are missing them, to prevent 404 errors.
Sub-directories named "data" are skipped (they contain JSON data files only).
"""

import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssc-cgl")

# Template for a topic-level placeholder page
TOPIC_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SSC CGL | SJMaths</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com{canonical_path}/">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=3d4a50dc">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=9840f97f">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=075ab6f7">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c323837a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=de4b8987">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c"></noscript>
    <style>
        :root { --glass-bg: rgba(255,255,255,0.95); --glass-border: rgba(255,255,255,0.2); --shadow-lg: 0 10px 30px -5px rgba(142,68,173,0.1); }
        .topic-container { max-width: 900px; margin: 0.5rem auto; padding: 0.75rem 1.5rem 2.5rem; animation: fadeIn 0.5s ease-out; }
        .breadcrumbs { margin-bottom: 1.5rem; font-size: 0.9rem; color: var(--text-light); }
        .breadcrumbs a { color: var(--primary); text-decoration: none; font-weight: 500; }
        .topic-header { margin-bottom: 2rem; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 1.5rem; text-align: center; }
        .topic-header h1 { font-family: 'Outfit', sans-serif; font-size: clamp(1.8rem,5vw,2.5rem); font-weight: 800; background: linear-gradient(135deg,var(--primary),#e74c3c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; line-height: 1.2; }
        .topic-header p { color: var(--text-light); font-size: clamp(0.95rem,2vw,1.05rem); line-height: 1.6; max-width: 750px; margin: 0 auto; }
        .card-premium { background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 1.25rem; box-shadow: var(--shadow-lg); padding: 2rem; margin-bottom: 2rem; }
        .card-title { font-family: 'Outfit', sans-serif; font-size: 1.3rem; font-weight: 700; color: var(--text-dark); margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.5rem; border-bottom: 2px solid var(--primary); padding-bottom: 0.5rem; }
        .subject-nav { display: flex; gap: 0.5rem; margin-bottom: 2rem; overflow-x: auto; padding-bottom: 0.5rem; border-bottom: 1px solid rgba(0,0,0,0.05); }
        .sub-nav-item { padding: 0.5rem 1rem; text-decoration: none; color: var(--text-light); font-size: 0.95rem; font-weight: 600; border-radius: 20px; background: rgba(0,0,0,0.02); transition: all 0.2s ease; white-space: nowrap; }
        .sub-nav-item:hover { color: var(--primary); background: rgba(142,68,173,0.05); }
        .sub-nav-item.active { background: var(--accent-gradient); color: #ffffff; box-shadow: 0 4px 10px rgba(142,68,173,0.25); }
        .content-text { line-height: 1.7; color: var(--text-dark); }
        .coming-soon { text-align: center; padding: 3rem 1rem; }
        .coming-soon i { font-size: 3rem; color: var(--primary); margin-bottom: 1rem; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div id="header-container"></div>
    <main class="topic-container" id="main-content">
        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size:0.7rem;margin:0 0.4rem;"></i>
            <a href="/ssc-cgl/syllabus/">SSC CGL Syllabus</a> {breadcrumbs_extra}
            <span>{display_name}</span>
        </div>
        <nav class="subject-nav" aria-label="Subject quick navigation">
            <a href="/ssc-cgl/quantitative-aptitude/" class="sub-nav-item">Maths</a>
            <a href="/ssc-cgl/reasoning/" class="sub-nav-item">Reasoning</a>
            <a href="/ssc-cgl/english/" class="sub-nav-item">English</a>
            <a href="/ssc-cgl/general-awareness/" class="sub-nav-item">GK</a>
            <a href="/ssc-cgl/computer-knowledge/" class="sub-nav-item">Computer</a>
            <a href="/ssc-cgl/statistics/" class="sub-nav-item">Statistics</a>
            <a href="/ssc-cgl/finance-economics/" class="sub-nav-item">Finance</a>
        </nav>
        <div class="topic-header">
            <h1>{display_name}</h1>
            <p>Comprehensive study material, notes, and practice questions for {display_name} in SSC CGL examination.</p>
        </div>
        <div class="card-premium">
            <h2 class="card-title"><i class="fas fa-book-open"></i> Study Material</h2>
            <div class="content-text">
                <p>Welcome to the study page for <strong>{display_name}</strong>. This section covers all important concepts, formulas, and question patterns for SSC CGL Tier 1 and Tier 2 examinations.</p>
                <div class="coming-soon">
                    <i class="fas fa-clock"></i>
                    <h3>Content Coming Soon</h3>
                    <p>Detailed notes, practice questions, and video explanations for this topic are being prepared. Please check back soon or explore other topics in the meantime.</p>
                </div>
            </div>
        </div>
    </main>
    <div id="footer-container"></div>
    <script src="/assets/js/main.min.js?v=d32e47f2" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=4d1d595f" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=8667b258" defer data-cfasync="false"></script>
    <script type="module">
        const load = async () => { try { await import("/assets/js/firebase-analytics-only.min.js?v=b9396571"); } catch(e) { console.debug("Analytics deferred"); } };
        if ('requestIdleCallback' in window) requestIdleCallback(load); else setTimeout(load, 3000);
    </script>
</body>
</html>'''


def to_title(name):
    """Convert a kebab-case folder name to a human-readable title."""
    name = name.replace("-", " ").replace("_", " ")
    # fix common abbreviations
    name = re.sub(r'\bCgl\b', 'CGL', name, flags=re.IGNORECASE)
    name = re.sub(r'\bSsc\b', 'SSC', name, flags=re.IGNORECASE)
    name = re.sub(r'\bPyqs\b', 'PYQs', name, flags=re.IGNORECASE)
    name = re.sub(r'\bGk\b', 'GK', name, flags=re.IGNORECASE)
    name = re.sub(r'\bI o\b', 'I/O', name)
    name = re.sub(r'\bCpu\b', 'CPU', name)
    name = re.sub(r'\bRbi\b', 'RBI', name)
    name = re.sub(r'\bGaap\b', 'GAAP', name)
    name = re.sub(r'\bCag\b', 'CAG', name)
    name = re.sub(r'\bAc\b', 'AC', name)
    return name.title()


def generate_placeholder(dir_path, canonical_path):
    """Generate a placeholder HTML file for the given directory."""
    dir_name = os.path.basename(dir_path)
    display_name = to_title(dir_name)
    # Avoid duplicate "SSC CGL" in title - the template already adds "| SSC CGL | SJMaths"
    title = display_name
    description = f"Complete study material, notes, practice questions, and preparation guide for {display_name} in SSC CGL Tier 1 & Tier 2 examination."

    # Build breadcrumbs extra
    parts = canonical_path.strip("/").split("/")
    breadcrumbs_extra = ""
    if len(parts) > 2:
        # Add intermediate breadcrumbs (skip ssc-cgl and last part)
        for i in range(2, len(parts) - 1):
            part_name = to_title(parts[i])
            partial_path = "/" + "/".join(parts[:i+1]) + "/"
            breadcrumbs_extra += f'<a href="{partial_path}">{part_name}</a> <i class="fas fa-chevron-right" style="font-size:0.7rem;margin:0 0.4rem;"></i>\n            '

    subjects = ["Maths", "Reasoning", "English", "GK", "Computer", "Statistics", "Finance"]
    subject_paths = ["quantitative-aptitude", "reasoning", "english", "general-awareness", "computer-knowledge", "statistics", "finance-economics"]
    
    # Find which subject this belongs to
    active_idx = 0
    for i, sp in enumerate(subject_paths):
        if sp in canonical_path:
            active_idx = i
            break

    nav_items = []
    for i, (sname, spath) in enumerate(zip(subjects, subject_paths)):
        active_class = ' active' if i == active_idx else ''
        nav_items.append(f'            <a href="/ssc-cgl/{spath}/" class="sub-nav-item{active_class}">{sname}</a>')
    
    html = TOPIC_TEMPLATE.format(
        title=title,
        description=description,
        canonical_path=canonical_path,
        breadcrumbs_extra=breadcrumbs_extra,
        display_name=display_name,
    )
    return html


def main():
    generated_count = 0
    skipped_data = 0
    skipped_dup = 0

    # First, delete all existing index.html files that were generated by the previous run
    # (detect them by the "Content Coming Soon" marker in our template)
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for f in filenames:
            if f == "index.html":
                fpath = os.path.join(dirpath, f)
                try:
                    with open(fpath, "r", encoding="utf-8") as fh:
                        content = fh.read(2000)
                        if "Content Coming Soon" in content:
                            os.remove(fpath)
                            print(f"REMOVED old placeholder: {os.path.relpath(fpath, ROOT)}")
                except:
                    pass

    # Now regenerate for directories still missing index.html
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        has_html = any(f.endswith('.html') for f in filenames)
        rel_path = os.path.relpath(dirpath, ROOT)
        if rel_path == ".":
            continue

        canonical_path = "/ssc-cgl/" + rel_path.replace("\\", "/")

        # Skip data subdirectories
        if rel_path.endswith("data") or "\\data" in rel_path or "/data" in rel_path:
            if not has_html:
                skipped_data += 1
            continue

        # Check for duplicate nested folder pattern
        parts = rel_path.replace("\\", "/").split("/")
        if len(parts) >= 2 and parts[-1] == parts[-2]:
            skipped_dup += 1
            continue

        if not has_html:
            html_content = generate_placeholder(dirpath, canonical_path)
            index_path = os.path.join(dirpath, "index.html")
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            generated_count += 1
            print(f"GENERATED: {rel_path}")

    print(f"\n=== Summary ===")
    print(f"Generated: {generated_count}")
    print(f"Skipped (data dirs): {skipped_data}")
    print(f"Skipped (duplicate): {skipped_dup}")


if __name__ == "__main__":
    main()