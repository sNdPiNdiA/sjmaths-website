"""
Scan all HTML files in the project for broken internal links.
Checks href and src attributes for references to local files that don't exist.
"""
import os
import re
import sys
from urllib.parse import urlparse, unquote
from pathlib import Path

ROOT = os.path.dirname(os.path.abspath(__file__))
SKIP_DIRS = {'.git', 'node_modules', '.firebase', 'dataconnect'}
EXTERNAL_PREFIXES = ('http://', 'https://', '//', 'mailto:', 'tel:', 'javascript:', 'data:', '#', '{{', '{%')
# Patterns to extract href and src attributes
LINK_RE = re.compile(r'''(?:href|src|action)\s*=\s*["']([^"'#\s][^"']*?)["']''', re.IGNORECASE)

def collect_html_files(root):
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(('.html', '.htm')):
                html_files.append(os.path.join(dirpath, f))
    return html_files

def is_external(url):
    return any(url.startswith(p) for p in EXTERNAL_PREFIXES)

def resolve_link(html_file, link, root):
    """Resolve a link relative to the HTML file or the project root."""
    # Remove query strings and fragments
    parsed = urlparse(link)
    path = unquote(parsed.path)
    
    if not path:
        return None  # fragment-only or empty
    
    if path.startswith('/'):
        # Absolute path from root
        resolved = os.path.normpath(os.path.join(root, path.lstrip('/')))
    else:
        # Relative path from the HTML file's directory
        html_dir = os.path.dirname(html_file)
        resolved = os.path.normpath(os.path.join(html_dir, path))
    
    return resolved

def check_file(html_file, root):
    broken = []
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return [{'file': html_file, 'link': 'N/A', 'error': str(e)}]
    
    links = LINK_RE.findall(content)
    seen = set()
    
    for link in links:
        link = link.strip()
        if not link or is_external(link) or link in seen:
            continue
        seen.add(link)
        
        # Skip template variables, anchors, etc.
        if '{{' in link or '{%' in link:
            continue
        
        resolved = resolve_link(html_file, link, root)
        if resolved is None:
            continue
        
        # Check if file or directory (index.html) exists
        if not os.path.exists(resolved):
            # Also check if it's a directory with index.html
            if not os.path.exists(resolved + '.html') and not os.path.exists(os.path.join(resolved, 'index.html')):
                rel_html = os.path.relpath(html_file, root)
                broken.append({
                    'file': rel_html,
                    'link': link,
                    'resolved': os.path.relpath(resolved, root)
                })
    
    return broken

def main():
    html_files = collect_html_files(ROOT)
    
    all_broken = []
    for hf in html_files:
        broken = check_file(hf, ROOT)
        all_broken.extend(broken)
    
    # Group by source file
    by_file = {}
    for item in all_broken:
        f = item['file']
        if f not in by_file:
            by_file[f] = []
        by_file[f].append(item)
    
    report_path = os.path.join(ROOT, 'broken_links_report.txt')
    with open(report_path, 'w', encoding='utf-8') as out:
        out.write(f"Scanned {len(html_files)} HTML files\n")
        out.write(f"Found {len(all_broken)} broken links across {len(by_file)} files\n")
        out.write("=" * 80 + "\n")
        
        for src_file in sorted(by_file.keys()):
            items = by_file[src_file]
            out.write(f"\n{src_file}\n")
            for item in items:
                out.write(f"  BROKEN: {item['link']}\n")
                out.write(f"    -> resolves to: {item.get('resolved', 'N/A')}\n")
        
        out.write(f"\n{'=' * 80}\n")
        out.write(f"Total: {len(all_broken)} broken links in {len(by_file)} files\n")
    
    print(f"Report written to {report_path}")
    print(f"Found {len(all_broken)} broken links in {len(by_file)} files")

if __name__ == '__main__':
    main()
