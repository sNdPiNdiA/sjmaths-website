from pathlib import Path
import re
import shutil
import sys

# ============================================================
# SJMaths Class 9 Science
# COPY CHAPTER 1 CONCEPTS TEMPLATE -> CHAPTERS 8–13
#
# Source:
#   chapter-1-exploration-entering-world-of-secondary-science/
#       concepts/index.html
#
# Creates:
#   chapter-8-.../concepts/index.html
#   chapter-9-.../concepts/index.html
#   ...
#   chapter-13-.../concepts/index.html
#
# Also copies Chapter 1's chapter-animations.js into each
# chapter's concepts folder if it exists.
#
# IMPORTANT:
# This copies the Chapter 1 CONTENT as a TEMPLATE.
# It does NOT invent chapter-specific scientific content.
# Replace the concept text later when the actual chapter
# content is ready.
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

SOURCE_CHAPTER = BASE_DIR / (
    "chapter-1-exploration-entering-world-of-secondary-science"
)

SOURCE_CONCEPTS = SOURCE_CHAPTER / "concepts"
SOURCE_INDEX = SOURCE_CONCEPTS / "index.html"
SOURCE_ANIMATIONS = SOURCE_CONCEPTS / "chapter-animations.js"


CHAPTERS = {
    8: {
        "folder": "chapter-8-journey-inside-atom",
        "title": "Journey Inside the Atom",
    },
    9: {
        "folder": "chapter-9-atomic-foundations-of-matter",
        "title": "Atomic Foundations of Matter",
    },
    10: {
        "folder": "chapter-10-sound-waves-characteristics-and-applications",
        "title": "Sound Waves: Characteristics & Applications",
    },
    11: {
        "folder": "chapter-11-reproduction-how-life-continues",
        "title": "Reproduction: How Life Continues",
    },
    12: {
        "folder": "chapter-12-patterns-in-life-diversity-and-classification",
        "title": "Patterns in Life, Diversity & Classification",
    },
    13: {
        "folder": "chapter-13-earth-as-a-system-energy-matter-and-life",
        "title": "Earth as a System: Energy, Matter & Life",
    },
}


def check_source():
    if not SOURCE_INDEX.exists():
        print("ERROR: Chapter 1 Concepts template not found:")
        print(SOURCE_INDEX)
        sys.exit(1)

    print("✓ Source template found:")
    print(f"  {SOURCE_INDEX}")

    if SOURCE_ANIMATIONS.exists():
        print("✓ Chapter animations found:")
        print(f"  {SOURCE_ANIMATIONS}")
    else:
        print("⚠ chapter-animations.js not found.")
        print("  Only index.html will be copied.")

    print()


def replace_metadata(html, chapter_number, title, folder_name):
    chapter_url = (
        f"https://sjmaths.com/class-9-science/"
        f"{folder_name}/concepts/"
    )

    # --------------------------------------------------------
    # <title>
    # --------------------------------------------------------
    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{title} | Class 9 Science Ch {chapter_number} | SJMaths</title>",
        html,
        count=1,
        flags=re.DOTALL,
    )

    # --------------------------------------------------------
    # Meta description
    # --------------------------------------------------------
    html = re.sub(
        r'<meta name="description" content=".*?">',
        (
            f'<meta name="description" content="Explore {title}, '
            f'Class 9 Science Chapter {chapter_number}, through detailed '
            f'concepts, examples, interactive learning and explanations.">'
        ),
        html,
        count=1,
    )

    # --------------------------------------------------------
    # Canonical
    # --------------------------------------------------------
    html = re.sub(
        r'<link rel="canonical" href=".*?">',
        f'<link rel="canonical" href="{chapter_url}">',
        html,
        count=1,
    )

    # --------------------------------------------------------
    # Breadcrumb:
    # ../index.html currently points to Chapter 1 overview.
    # Keep the same relative structure, but change its text.
    # --------------------------------------------------------
    html = re.sub(
        r'<a href="../index\.html">.*?</a>',
        f'<a href="../index.html">{title}</a>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    # --------------------------------------------------------
    # Chapter-specific links
    # --------------------------------------------------------
    # The source template already uses ../index.html and
    # ../ncert-exercises/, which are correct from:
    # chapter-X/concepts/index.html
    #
    # Therefore no ../ path change is required.

    # --------------------------------------------------------
    # Replace Chapter 1's visible "Exploration" text in the
    # breadcrumb only if it survived the replacement.
    # --------------------------------------------------------
    html = html.replace(
        ">Exploration<",
        f">{title}<",
    )

    return html


def add_generated_comment(html, chapter_number, title):
    marker = (
        "<!-- ==================================================\n"
        "     SJMaths Class 9 Science\n"
        f"     Chapter {chapter_number}: {title}\n"
        "     Concepts page generated from Chapter 1 template.\n"
        "     ================================================== -->\n"
    )

    if "<body>" in html:
        html = html.replace(
            "<body>",
            "<body>\n" + marker,
            1,
        )

    return html


def generate_chapter(chapter_number, data, source_html):
    folder = BASE_DIR / data["folder"]

    if not folder.exists():
        print(
            f"❌ Chapter {chapter_number} folder does not exist:"
        )
        print(f"   {folder}")
        print(
            "   This script will NOT create chapter folders."
        )
        return False

    concepts_folder = folder / "concepts"
    concepts_folder.mkdir(exist_ok=True)

    output_index = concepts_folder / "index.html"

    html = replace_metadata(
        source_html,
        chapter_number,
        data["title"],
        folder.name,
    )

    html = add_generated_comment(
        html,
        chapter_number,
        data["title"],
    )

    output_index.write_text(
        html,
        encoding="utf-8",
    )

    print(
        f"✓ Chapter {chapter_number} concepts/index.html"
    )

    # Copy animation JS if it exists
    if SOURCE_ANIMATIONS.exists():
        output_animation = concepts_folder / "chapter-animations.js"
        shutil.copy2(
            SOURCE_ANIMATIONS,
            output_animation,
        )
        print(
            f"  ✓ chapter-animations.js"
        )

    return True


def main():
    print()
    print("=" * 70)
    print(" SJMaths — Concepts Template Generator")
    print(" Chapter 1 Concepts → Chapters 8–13")
    print("=" * 70)
    print()

    check_source()

    source_html = SOURCE_INDEX.read_text(
        encoding="utf-8"
    )

    success = 0

    for chapter_number, data in CHAPTERS.items():
        print(
            f"Processing Chapter {chapter_number}: "
            f"{data['title']}"
        )

        if generate_chapter(
            chapter_number,
            data,
            source_html,
        ):
            success += 1

        print()

    print("=" * 70)
    print(
        f"✓ COMPLETE — {success}/{len(CHAPTERS)} chapters processed"
    )
    print("=" * 70)
    print()
    print(
        "Chapter 1 was not modified."
    )
    print(
        "No chapter folders were created."
    )
    print(
        "Only concepts/index.html and chapter-animations.js "
        "were generated inside existing Chapters 8–13."
    )
    print()


if __name__ == "__main__":
    main()