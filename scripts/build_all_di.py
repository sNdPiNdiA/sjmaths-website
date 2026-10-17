"""
build_all_di.py
Build script to generate all 5 Data Interpretation topic pages for UPSSSC Intermediate Level Mains.
"""

import os
import sys

# Ensure repo root is on sys.path
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.di_data.template import render_html_page
from scripts.di_data.topic1 import TOPIC_1
from scripts.di_data.topic2 import TOPIC_2
from scripts.di_data.topic3 import TOPIC_3
from scripts.di_data.topic4 import TOPIC_4
from scripts.di_data.topic5 import TOPIC_5

def build_all():
    topics = [TOPIC_1, TOPIC_2, TOPIC_3, TOPIC_4, TOPIC_5]
    base_out_dir = os.path.join(REPO_ROOT, "upsssc-intermediate-level", "data-interpretation")

    print(f"Building {len(topics)} Data Interpretation topic pages...")

    for idx, topic in enumerate(topics, 1):
        slug = topic["slug"]
        out_dir = os.path.join(base_out_dir, slug)
        os.makedirs(out_dir, exist_ok=True)

        html_content = render_html_page(topic)
        out_file = os.path.join(out_dir, "index.html")

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        file_size_kb = os.path.getsize(out_file) / 1024
        print(f"[{idx}/5] Successfully generated: {slug}/index.html ({file_size_kb:.1f} KB)")

    print("\nAll 5 Data Interpretation topic pages built successfully!")

if __name__ == "__main__":
    build_all()
