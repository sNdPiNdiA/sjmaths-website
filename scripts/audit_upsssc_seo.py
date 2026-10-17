import os
import sys
import re
import json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsssc-intermediate-level"
subjects = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')]

stats = {
    'total_files': 0,
    'title_length_issues': [],
    'title_tag_issues': [],
    'desc_issues': [],
    'canonical_issues': [],
    'h1_issues': [],
    'og_issues': [],
    'twitter_issues': [],
    'schema_issues': [],
    'dup_id_issues': [],
    'hindi_topics_audit': []
}

for subj in sorted(subjects):
    subj_dir = os.path.join(base_dir, subj)
    topics = [t for t in os.listdir(subj_dir) if os.path.isdir(os.path.join(subj_dir, t))]
    for t in sorted(topics):
        p = os.path.join(subj_dir, t, "index.html")
        if not os.path.exists(p):
            continue
        stats['total_files'] += 1
        with open(p, "r", encoding="utf-8") as f:
            html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        
        # 1. Title
        titles = soup.find_all("title")
        if len(titles) != 1:
            stats['title_tag_issues'].append((subj, t, f"title count = {len(titles)}"))
        else:
            t_text = titles[0].get_text(strip=True)
            if len(t_text) < 15 or len(t_text) > 120:
                stats['title_length_issues'].append((subj, t, len(t_text), t_text))
                
        # 2. Description
        descs = soup.find_all("meta", attrs={"name": "description"})
        if len(descs) != 1:
            stats['desc_issues'].append((subj, t, f"desc count = {len(descs)}"))
        else:
            d_text = descs[0].get("content", "").strip()
            if len(d_text) < 50 or len(d_text) > 320:
                stats['desc_issues'].append((subj, t, f"len={len(d_text)}: {d_text}"))
                
        # 3. Canonical
        canons = soup.find_all("link", attrs={"rel": "canonical"})
        expected_canon = f"https://sjmaths.com/upsssc-intermediate-level/{subj}/{t}/"
        if len(canons) != 1:
            stats['canonical_issues'].append((subj, t, f"canonical count = {len(canons)}"))
        elif canons[0].get("href", "") != expected_canon:
            actual = canons[0].get("href", "")
            stats['canonical_issues'].append((subj, t, f"expected {expected_canon}, got {actual}"))
            
        # 4. H1
        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            stats['h1_issues'].append((subj, t, f"h1 count = {len(h1s)}"))
            
        # 5. OG tags
        og_req = ["og:title", "og:description", "og:url", "og:type", "og:site_name", "og:image"]
        for og in og_req:
            tags = soup.find_all("meta", attrs={"property": og})
            if len(tags) != 1:
                stats['og_issues'].append((subj, t, f"{og} count = {len(tags)}"))
                
        # 6. Schema.org
        schema_scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
        if len(schema_scripts) != 1:
            stats['schema_issues'].append((subj, t, f"schema script count = {len(schema_scripts)}"))
        else:
            try:
                data = json.loads(schema_scripts[0].string)
                if "@graph" not in data:
                    stats['schema_issues'].append((subj, t, "missing @graph"))
                else:
                    types = [item.get("@type") for item in data["@graph"]]
                    if "Article" not in types or "BreadcrumbList" not in types:
                        stats['schema_issues'].append((subj, t, f"missing expected types in graph: {types}"))
            except Exception as e:
                stats['schema_issues'].append((subj, t, f"schema json error: {e}"))
                
        # 7. Duplicate IDs
        ids = {}
        for el in soup.find_all(id=True):
            el_id = el["id"]
            ids[el_id] = ids.get(el_id, 0) + 1
        dup_ids = [k for k, v in ids.items() if v > 1]
        if dup_ids:
            stats['dup_id_issues'].append((subj, t, f"duplicate ids: {dup_ids}"))

        if subj == "hindi":
            stats['hindi_topics_audit'].append({
                'topic': t,
                'title': titles[0].get_text(strip=True) if titles else '',
                'title_len': len(titles[0].get_text(strip=True)) if titles else 0,
                'desc_len': len(descs[0].get("content", "").strip()) if descs else 0,
                'canonical': canons[0].get("href", "") if canons else "",
                'h1': h1s[0].get_text(strip=True) if h1s else ""
            })

print(f"Total topic files audited: {stats['total_files']}")
print(f"Title tag count issues: {len(stats['title_tag_issues'])}")
print(f"Title length >120 chars: {len(stats['title_length_issues'])}")
print(f"Description issues: {len(stats['desc_issues'])}")
print(f"Canonical issues: {len(stats['canonical_issues'])}")
print(f"H1 issues: {len(stats['h1_issues'])}")
print(f"OG issues: {len(stats['og_issues'])}")
print(f"Schema issues: {len(stats['schema_issues'])}")
print(f"Duplicate ID issues: {len(stats['dup_id_issues'])}")

print(f"\n==================== HINDI TOPICS AUDIT (19 Topics) ====================")
for h in stats['hindi_topics_audit']:
    warn = " [>120 chars]" if h['title_len'] > 120 else ""
    print(f"• {h['topic']}: Title Len={h['title_len']}{warn}, Desc Len={h['desc_len']}, Canonical=OK")

if stats['title_length_issues']:
    print(f"\n==================== TITLES OVER 120 CHARACTERS ({len(stats['title_length_issues'])}) ====================")
    for s, t, l, txt in stats['title_length_issues'][:10]:
        print(f"[{s}/{t}] (Len: {l}) -> {txt}")
