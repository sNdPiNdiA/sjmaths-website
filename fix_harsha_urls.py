#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create the folder structure expected by upsc/index.html syllabus tracker
for Harshvardhan-and-Southern-Dynasties-in-7th-Century-India.

Syllabus tracker expects these URLs (relative to upsc/ancient_history/):
  Harshvardhan-and-Southern-Dynasties-in-7th-Century-India/
    Military-Conquests-of-Harshvardhan/
    Administration-Harsha/
    Economy-Harsha/
    Society-and-Culture-Harsha/
    Religion-Harsha/
    Harsha-and-Buddhism/
    Art-and-Architecture-Harsha/
    Pallavas-of-Kanchi-and-Chalukyas-of-Badami/
    Administration-Pallavas-Chalukyas/
    Economy-Pallavas-Chalukyas/
    Society-and-Culture-Pallavas-Chalukyas/
    Religion-Pallavas-Chalukyas/
    Art-and-Architecture-Pallavas-Chalukyas/

Actual pages live in:
  Harshvardhan-and-Southern-Dynasties/
    Military-Conquests-of-Harshvardhan/
    Administration/
    Economy/
    Society-and-Culture/
    Religion/Harsha-and-Buddhism/   (two levels!)
    Art-and-Architecture/
    Pallavas-of-Kanchi-and-Chalukyas-of-Badami/Administration/
    Pallavas-of-Kanchi-and-Chalukyas-of-Badami/Economy/
    Pallavas-of-Kanchi-and-Chalukyas-of-Badami/Society-and-Culture/
    Pallavas-of-Kanchi-and-Chalukyas-of-Badami/Religion/
    Pallavas-of-Kanchi-and-Chalukyas-of-Badami/Art-and-Architecture/

Strategy: copy each source index.html into the expected folder.
"""

import os, shutil

ROOT = r"upsc/ancient_history"

OLD_BASE = os.path.join(ROOT, "Harshvardhan-and-Southern-Dynasties")
NEW_BASE = os.path.join(ROOT, "Harshvardhan-and-Southern-Dynasties-in-7th-Century-India")

MAPPING = [
    # (new folder name, source path relative to OLD_BASE)
    ("Military-Conquests-of-Harshvardhan",        "Military-Conquests-of-Harshvardhan"),
    ("Administration-Harsha",                      "Administration"),
    ("Economy-Harsha",                             "Economy"),
    ("Society-and-Culture-Harsha",                 "Society-and-Culture"),
    ("Religion-Harsha",                            "Religion"),
    ("Harsha-and-Buddhism",                        os.path.join("Religion", "Harsha-and-Buddhism")),
    ("Art-and-Architecture-Harsha",                "Art-and-Architecture"),
    # Pallavas-of-Kanchi-and-Chalukyas-of-Badami folder — just copy the subfolder index (no index in parent)
    ("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", os.path.join("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", "Administration")),
    ("Administration-Pallavas-Chalukyas",           os.path.join("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", "Administration")),
    ("Economy-Pallavas-Chalukyas",                  os.path.join("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", "Economy")),
    ("Society-and-Culture-Pallavas-Chalukyas",      os.path.join("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", "Society-and-Culture")),
    ("Religion-Pallavas-Chalukyas",                 os.path.join("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", "Religion")),
    ("Art-and-Architecture-Pallavas-Chalukyas",     os.path.join("Pallavas-of-Kanchi-and-Chalukyas-of-Badami", "Art-and-Architecture")),
]

def main():
    os.makedirs(NEW_BASE, exist_ok=True)
    print(f"Target base: {NEW_BASE}")

    for new_folder, src_rel in MAPPING:
        src_dir  = os.path.join(OLD_BASE, src_rel)
        dest_dir = os.path.join(NEW_BASE, new_folder)

        os.makedirs(dest_dir, exist_ok=True)

        # Copy index.html
        src_html  = os.path.join(src_dir, "index.html")
        dest_html = os.path.join(dest_dir, "index.html")
        if os.path.exists(src_html):
            shutil.copy2(src_html, dest_html)
            print(f"  Copied: {src_rel}/index.html -> {new_folder}/index.html")
        else:
            print(f"  WARNING: source not found: {src_html}")

        # Copy content.json if present
        src_json  = os.path.join(src_dir, "content.json")
        dest_json = os.path.join(dest_dir, "content.json")
        if os.path.exists(src_json):
            shutil.copy2(src_json, dest_json)

    print("\nDone!")

if __name__ == "__main__":
    main()
