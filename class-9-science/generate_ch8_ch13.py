from pathlib import Path
import re
import shutil
import sys

# ============================================================
# SJMaths CLASS 9 SCIENCE
# CHAPTER 9–13 INDEX GENERATOR
#
# MASTER TEMPLATE:
#   chapter-1-exploration-entering-world-of-secondary-science/index.html
#
# PURPOSE:
#   1. Use Chapter 1's ROOT index.html as the design/template.
#   2. Create the missing Chapter 9–13 folders.
#   3. Generate each chapter's ROOT index.html.
#   4. Remove accidental duplicate folders whose names differ
#      from the canonical folder name.
#
# Chapter 8 is NOT modified.
# ============================================================


BASE_DIR = Path(__file__).resolve().parent

MASTER_FOLDER = (
    BASE_DIR /
    "chapter-1-exploration-entering-world-of-secondary-science"
)

MASTER_FILE = MASTER_FOLDER / "index.html"


# ============================================================
# CANONICAL CHAPTER DATA
# ============================================================

CHAPTERS = {
    9: {
        "folder": "chapter-9-atomic-foundations-of-matter",
        "title": "Atomic Foundations of Matter",
        "hero": (
            "Explore the foundations of atomic matter through "
            "models, evidence, experiments, and the development "
            "of our understanding of the atom."
        ),
        "overview": (
            "In this chapter, we explore how scientists developed "
            "ideas about the structure of matter and the atom. "
            "Follow the evidence, models, experiments, and ideas "
            "that shaped modern atomic science."
        ),
        "topics": (
            "- <strong>Atomic Structure:</strong> Explore the basic ideas "
            "used to describe matter and atoms.<br>"
            "- <strong>Historical Models:</strong> Follow how atomic models "
            "changed as new evidence became available.<br>"
            "- <strong>Experimental Evidence:</strong> Understand how "
            "observations and experiments shaped atomic theory.<br>"
            "- <strong>Scientific Reasoning:</strong> Connect evidence, "
            "models, explanations, and predictions.<br>"
            "- <strong>Modern Understanding:</strong> Build a foundation "
            "for studying the structure and behaviour of matter."
        ),
    },

    10: {
        "folder": "chapter-10-sound-waves-characteristics",
        "title": "Sound Waves & Their Characteristics",
        "hero": (
            "Discover how sound is produced, transmitted, and "
            "described through vibrations, waves, frequency, "
            "amplitude, and other measurable characteristics."
        ),
        "overview": (
            "In this chapter, we investigate sound as a wave phenomenon. "
            "Learn how vibrations produce sound, how sound travels through "
            "different media, and how its measurable characteristics "
            "determine what we hear."
        ),
        "topics": (
            "- <strong>Production of Sound:</strong> Understand sound as "
            "the result of vibrations.<br>"
            "- <strong>Propagation:</strong> Explore how sound travels "
            "through a medium.<br>"
            "- <strong>Wave Characteristics:</strong> Study amplitude, "
            "frequency, wavelength, and time period.<br>"
            "- <strong>Pitch & Loudness:</strong> Relate physical quantities "
            "to characteristics of sound.<br>"
            "- <strong>Applications:</strong> Connect sound-wave ideas "
            "with everyday phenomena and technology."
        ),
    },

    11: {
        "folder": "chapter-11-reproduction-how-life-continues",
        "title": "Reproduction: How Life Continues",
        "hero": (
            "Explore how living organisms reproduce, pass genetic "
            "information, and ensure continuity of life across generations."
        ),
        "overview": (
            "In this chapter, we explore reproduction as an essential "
            "biological process. Understand how organisms produce new "
            "individuals and how reproduction contributes to the continuity "
            "and diversity of life."
        ),
        "topics": (
            "- <strong>Reproduction:</strong> Understand why reproduction "
            "is essential for continuity of life.<br>"
            "- <strong>Modes of Reproduction:</strong> Explore major "
            "patterns of reproduction in living organisms.<br>"
            "- <strong>Reproductive Processes:</strong> Study the sequence "
            "of events involved in producing new individuals.<br>"
            "- <strong>Inheritance:</strong> Connect reproduction with the "
            "transfer of biological information.<br>"
            "- <strong>Life Continuity:</strong> Understand reproduction "
            "as a foundation of biological continuity."
        ),
    },

    12: {
        "folder": "chapter-12-patterns-in-life-diversity",
        "title": "Patterns in Life & Diversity",
        "hero": (
            "Discover patterns in the living world and learn how "
            "classification helps us organise, compare, and understand "
            "the remarkable diversity of life."
        ),
        "overview": (
            "In this chapter, we examine the diversity of living organisms "
            "and the patterns scientists use to organise and understand "
            "life. Classification provides a systematic way to compare "
            "organisms and recognise relationships."
        ),
        "topics": (
            "- <strong>Diversity of Life:</strong> Explore the variety "
            "of organisms around us.<br>"
            "- <strong>Classification:</strong> Understand why organisms "
            "are grouped systematically.<br>"
            "- <strong>Patterns:</strong> Identify similarities and "
            "differences used in biological classification.<br>"
            "- <strong>Relationships:</strong> Explore how classification "
            "can reveal relationships among organisms.<br>"
            "- <strong>Scientific Organisation:</strong> Learn how "
            "systematic classification makes biological knowledge easier "
            "to study."
        ),
    },

    13: {
        "folder": "chapter-13-earth-as-a-system-energy",
        "title": "Earth as a System: Energy & Interactions",
        "hero": (
            "Understand Earth as an interconnected system in which "
            "energy flows and different natural components interact "
            "to shape our planet."
        ),
        "overview": (
            "In this chapter, we view Earth as a dynamic and interconnected "
            "system. Explore how energy and matter move through natural "
            "systems and how interactions between Earth's components "
            "produce observable changes."
        ),
        "topics": (
            "- <strong>Earth as a System:</strong> Understand the major "
            "components and interactions of Earth.<br>"
            "- <strong>Energy Flow:</strong> Explore how energy enters, "
            "moves through, and leaves Earth systems.<br>"
            "- <strong>Interactions:</strong> Connect the atmosphere, "
            "hydrosphere, geosphere, and biosphere.<br>"
            "- <strong>Natural Processes:</strong> Examine how interacting "
            "systems produce changes on Earth.<br>"
            "- <strong>Systems Thinking:</strong> Build a connected view "
            "of Earth's energy and natural processes."
        ),
    },
}


# ============================================================
# HELPERS
# ============================================================

def chapter_folders(chapter_number):
    """Return all existing folders beginning with chapter-N-."""
    return sorted(
        p for p in BASE_DIR.glob(f"chapter-{chapter_number}-*")
        if p.is_dir()
    )


def clean_duplicate_folders():
    """
    Keep ONLY the canonical folder name for each chapter.
    Since the user has already deleted the old duplicates,
    this is mainly a safety net.

    IMPORTANT:
    - If the canonical folder does not exist, it is NOT an error;
      it will be created later.
    - Any non-canonical chapter-N-* folder is considered an
      accidental duplicate and is removed.
    """

    print()
    print("=" * 70)
    print("STEP 1 — CLEANING ACCIDENTAL DUPLICATE FOLDERS")
    print("=" * 70)
    print()

    for number, data in CHAPTERS.items():

        canonical = BASE_DIR / data["folder"]
        existing = chapter_folders(number)

        for folder in existing:

            if folder.resolve() == canonical.resolve():
                print(f"✓ Keeping: {folder.name}")
                continue

            print(f"🗑 Removing duplicate: {folder.name}")
            shutil.rmtree(folder)

        if not canonical.exists():
            print(
                f"✓ Chapter {number}: canonical folder will be created:"
            )
            print(f"  {canonical.name}")


def load_master_template():
    """Load Chapter 1 root index.html."""

    if not MASTER_FILE.exists():
        print("❌ ERROR: Chapter 1 master template not found.")
        print()
        print(MASTER_FILE)
        print()
        sys.exit(1)

    print("✓ Master template:")
    print(f"  {MASTER_FILE}")
    print()

    return MASTER_FILE.read_text(encoding="utf-8")


def replace_first(pattern, replacement, html, flags=re.DOTALL):
    return re.sub(
        pattern,
        replacement,
        html,
        count=1,
        flags=flags
    )


def update_page(template, number, data):
    """Create a chapter-specific root index from the Chapter 1 template."""

    html = template

    title = data["title"]
    folder = data["folder"]

    url = (
        f"https://sjmaths.com/class-9-science/"
        f"{folder}/"
    )

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    html = replace_first(
        r"<title>.*?</title>",
        f"<title>{title} - Class 9 Science Ch {number} | SJMaths</title>",
        html
    )

    # --------------------------------------------------------
    # META DESCRIPTION
    # --------------------------------------------------------

    html = replace_first(
        r'<meta name="description"\s*content=".*?">',
        (
            f'<meta name="description"\n'
            f'        content="Complete Class 9 Science Chapter '
            f'{number} - {title}. Access concepts, NCERT exercise '
            f'solutions, quizzes, tests, and revision notes.">'
        ),
        html
    )

    # --------------------------------------------------------
    # CANONICAL
    # --------------------------------------------------------

    html = replace_first(
        r'<link rel="canonical" href=".*?">',
        f'<link rel="canonical" href="{url}">',
        html,
        flags=0
    )

    # --------------------------------------------------------
    # OG TITLE
    # --------------------------------------------------------

    html = replace_first(
        r'<meta property="og:title" content=".*?">',
        (
            f'<meta property="og:title" '
            f'content="{title} - Class 9 Science Chapter '
            f'{number} | SJMaths">'
        ),
        html,
        flags=0
    )

    # --------------------------------------------------------
    # OG DESCRIPTION
    # --------------------------------------------------------

    html = replace_first(
        r'<meta property="og:description"\s*content=".*?">',
        (
            f'<meta property="og:description"\n'
            f'        content="Complete Class 9 Science Chapter '
            f'{number} with concepts, NCERT solutions, quizzes, '
            f'tests, and revision notes.">'
        ),
        html
    )

    # --------------------------------------------------------
    # OG URL
    # --------------------------------------------------------

    html = replace_first(
        r'<meta property="og:url" content=".*?">',
        f'<meta property="og:url" content="{url}">',
        html,
        flags=0
    )

    # --------------------------------------------------------
    # JSON-LD HEADLINE
    # --------------------------------------------------------

    html = replace_first(
        r'"headline":\s*".*?"',
        (
            f'"headline": "{title} | '
            f'Class 9 Science Chapter {number}"'
        ),
        html,
        flags=0
    )

    # --------------------------------------------------------
    # JSON-LD DESCRIPTION
    # --------------------------------------------------------

    html = replace_first(
        r'"description":\s*".*?"',
        (
            f'"description": "Complete chapter with '
            f'concepts, NCERT exercise solutions, quizzes, '
            f'tests, and revision notes."'
        ),
        html,
        flags=0
    )

    # --------------------------------------------------------
    # JSON-LD URL
    # --------------------------------------------------------

    html = replace_first(
        r'"url":\s*"https://sjmaths\.com/class-9-science/.*?"',
        f'"url": "{url}"',
        html,
        flags=0
    )

    # --------------------------------------------------------
    # BREADCRUMB
    # --------------------------------------------------------

    html = replace_first(
        r'<span style="color: #0f9d8a;">.*?</span>',
        (
            f'<span style="color: #0f9d8a;">'
            f'{title}'
            f'</span>'
        ),
        html
    )

    # --------------------------------------------------------
    # HERO NUMBER
    # --------------------------------------------------------

    html = html.replace(
        "Chapter\n                01 • Class 9 Science",
        f"Chapter\n                {number:02d} • Class 9 Science"
    )

    html = html.replace(
        "Chapter 01 • Class 9 Science",
        f"Chapter {number:02d} • Class 9 Science"
    )

    # --------------------------------------------------------
    # HERO H1
    # --------------------------------------------------------

    html = replace_first(
        r"<h1>.*?</h1>",
        f"<h1>{title}</h1>",
        html
    )

    # --------------------------------------------------------
    # HERO DESCRIPTION
    # --------------------------------------------------------

    html = replace_first(
        r'(<header class="sj-hero-v6".*?<h1>.*?</h1>)\s*<p>.*?</p>',
        (
            r'\1\n'
            f'            <p>{data["hero"]}</p>'
        ),
        html
    )

    # --------------------------------------------------------
    # CHAPTER OVERVIEW
    # --------------------------------------------------------

    html = replace_first(
        r'(<small[^>]*>Chapter Overview</small>\s*'
        r'<h2>What You\'ll Learn in This Chapter</h2>.*?'
        r'</div>\s*</div>\s*)'
        r'<p>.*?</p>',
        (
            r'\1'
            f'<p>{data["overview"]}</p>'
        ),
        html
    )

    # --------------------------------------------------------
    # KEY TOPICS
    # --------------------------------------------------------

    html = replace_first(
        r'(<strong[^>]*>Key Topics Covered</strong>\s*'
        r'</div>\s*<p[^>]*>).*?(</p>)',
        (
            r'\1'
            f'{data["topics"]}'
            r'\2'
        ),
        html
    )

    # --------------------------------------------------------
    # NEXT CHAPTER LINK
    # --------------------------------------------------------

    next_number = number + 1

    if next_number in CHAPTERS:

        next_folder = CHAPTERS[next_number]["folder"]

        # Replace Chapter 1's hard-coded Chapter 2 URL
        html = html.replace(
            "../chapter-2-cell-building-block-of-life/",
            f"../{next_folder}/"
        )

    else:
        # Chapter 13 has no next chapter.
        html = re.sub(
            r'<a href="\.\./chapter-2-cell-building-block-of-life/" class="sj-btn next">.*?</a>',
            "",
            html,
            flags=re.DOTALL
        )

    # --------------------------------------------------------
    # ADD GENERATED MARKER
    # --------------------------------------------------------

    marker = (
        f"<!-- ==================================================\n"
        f" SJMaths Class 9 Science\n"
        f" Chapter {number}: {title}\n"
        f" Generated from Chapter 1 root index template\n"
        f" ================================================== -->\n"
    )

    html = html.replace(
        "<body>",
        "<body>\n" + marker,
        1
    )

    return html


def create_chapter(number, template):
    """Create folder and root index.html."""

    data = CHAPTERS[number]

    folder = BASE_DIR / data["folder"]

    # Create the chapter folder NOW because user deleted 9–13.
    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    output = folder / "index.html"

    html = update_page(
        template,
        number,
        data
    )

    output.write_text(
        html,
        encoding="utf-8"
    )

    print(f"✓ Chapter {number}")
    print(f"  Folder : {folder.name}")
    print(f"  Index  : {output}")
    print()


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 70)
    print(" SJMaths — Class 9 Science")
    print(" Generate Chapter 9–13 Overview Pages")
    print("=" * 70)

    # --------------------------------------------------------
    # Load Chapter 1 master
    # --------------------------------------------------------

    template = load_master_template()

    # --------------------------------------------------------
    # Clean accidental duplicates
    # --------------------------------------------------------

    clean_duplicate_folders()

    # --------------------------------------------------------
    # Generate Chapters 9–13
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("STEP 2 — CREATING CHAPTER 9–13 INDEX FILES")
    print("=" * 70)
    print()

    for number in range(9, 14):

        create_chapter(
            number,
            template
        )

    print("=" * 70)
    print("✓ COMPLETE")
    print("=" * 70)
    print()
    print("Chapter 1 was used as the master design.")
    print("Chapter 8 was NOT modified.")
    print("Chapters 9–13 were created.")
    print("No chapter-specific Concepts/NCERT/etc. files were touched.")
    print()


if __name__ == "__main__":
    main()