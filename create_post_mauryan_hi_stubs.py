#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates hi/index.html stubs for each Post-Mauryan subtopic by copying
the English page and setting lang="hi", then the mindmap script patches it
with Hindi content since is_hindi=True when 'hi' is in path.
"""

import os, shutil, re

BASE = r"upsc/ancient_history/History-of-Post-Mauryan-Period"

HINDI_TITLES = {
    "Shungas":                "शुंग वंश",
    "Kanvas":                 "कण्व वंश",
    "Chedis":                 "चेदि वंश (खारवेल)",
    "Indo-Greeks":            "इंडो-ग्रीक",
    "Parthians":              "पार्थियन (पह्लव)",
    "Sakas":                  "शक",
    "Satavahanas":            "सातवाहन वंश",
    "Kushans":                "कुषाण वंश",
    "Kushans-Kanishkas-Rule": "कनिष्क का शासन",
}

def create_hi_page(src_html, dest_html, folder_name):
    with open(src_html, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')

    # Set language
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)

    # Update canonical URL to point to /hi/ version
    html = re.sub(
        r'<link rel="canonical" href="([^"]+)"',
        lambda m: f'<link rel="canonical" href="{m.group(1).rstrip("/")}/hi/"',
        html, count=1
    )

    hn = HINDI_TITLES.get(folder_name, folder_name)

    # Update title and description
    html = re.sub(r'<title>[^<]+</title>',
                  f'<title>{hn} - UPSC सिविल सेवा अध्ययन गाइड | SJMaths</title>', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{hn} पर विस्तृत UPSC अध्ययन गाइड। अध्ययन नोट्स, माइंडमैप, मनेमोनिक्स और प्रश्नोत्तर।"',
                  html, count=1)

    os.makedirs(os.path.dirname(dest_html), exist_ok=True)
    with open(dest_html, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created: {dest_html}")

def main():
    total = 0
    for folder_name in os.listdir(BASE):
        folder_path = os.path.join(BASE, folder_name)
        if not os.path.isdir(folder_path):
            continue
        src = os.path.join(folder_path, "index.html")
        if not os.path.exists(src):
            continue
        dest = os.path.join(folder_path, "hi", "index.html")
        create_hi_page(src, dest, folder_name)
        total += 1
    print(f"\nCreated {total} Hindi stubs. Now run add_post_mauryan_mindmaps.py to patch them.")

if __name__ == "__main__":
    main()
