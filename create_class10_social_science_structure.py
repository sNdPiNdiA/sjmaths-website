from pathlib import Path

# ================================================================
# SJMaths — CBSE Class 10 Social Science
# COMPLETE FOLDER STRUCTURE GENERATOR
#
# Creates the four NCERT books:
#   1. History
#   2. Geography
#   3. Political Science
#   4. Economics
#
# For every chapter:
#   concepts/
#   ncert-exercises/
#   practice/
#   pyqs/
#   quiz/
#   revision-notes/
#   tests/
#
# This script creates FOLDERS ONLY.
# It does not create HTML/content files.
# ================================================================

# Run this script from anywhere inside the project.
# The script finds the Git repository root by looking for .git.
# If no .git is found, it uses the current working directory.

def find_project_root():
    current = Path.cwd().resolve()

    for path in [current, *current.parents]:
        if (path / ".git").exists():
            return path

    return current


ROOT = find_project_root()
SST_ROOT = ROOT / "class-10-social-science"

# Current NCERT Class X book/chapter structure checked against
# NCERT's currently available Class X textbook listings/reprints.
BOOKS = {
    "history": {
        "title": "India and the Contemporary World-II",
        "chapters": [
            ("01-rise-of-nationalism-in-europe",
             "The Rise of Nationalism in Europe"),
            ("02-nationalism-in-india",
             "Nationalism in India"),
            ("03-making-of-a-global-world",
             "The Making of a Global World"),
            ("04-age-of-industrialisation",
             "The Age of Industrialisation"),
            ("05-print-culture-and-the-modern-world",
             "Print Culture and the Modern World"),
        ],
    },

    "geography": {
        "title": "Contemporary India-II",
        "chapters": [
            ("01-resources-and-development",
             "Resources and Development"),
            ("02-forest-and-wildlife-resources",
             "Forest and Wildlife Resources"),
            ("03-water-resources",
             "Water Resources"),
            ("04-agriculture",
             "Agriculture"),
            ("05-minerals-and-energy-resources",
             "Minerals and Energy Resources"),
            ("06-manufacturing-industries",
             "Manufacturing Industries"),
            ("07-lifelines-of-national-economy",
             "Lifelines of National Economy"),
        ],
    },

    "political-science": {
        "title": "Democratic Politics-II",
        "chapters": [
            ("01-power-sharing",
             "Power Sharing"),
            ("02-federalism",
             "Federalism"),
            ("03-gender-religion-and-caste",
             "Gender, Religion and Caste"),
            ("04-political-parties",
             "Political Parties"),
            ("05-outcomes-of-democracy",
             "Outcomes of Democracy"),
        ],
    },

    "economics": {
        "title": "Understanding Economic Development",
        "chapters": [
            ("01-development",
             "Development"),
            ("02-sectors-of-the-indian-economy",
             "Sectors of the Indian Economy"),
            ("03-money-and-credit",
             "Money and Credit"),
            ("04-globalisation-and-the-indian-economy",
             "Globalisation and the Indian Economy"),
            ("05-consumer-rights",
             "Consumer Rights"),
        ],
    },
}


CHAPTER_SECTIONS = [
    "concepts",
    "ncert-exercises",
    "practice",
    "pyqs",
    "quiz",
    "revision-notes",
    "tests",
]


def main():
    print("=" * 78)
    print(" SJMaths — CBSE Class 10 Social Science")
    print(" COMPLETE FOUR-BOOK FOLDER STRUCTURE")
    print("=" * 78)
    print()
    print(f"Project root : {ROOT}")
    print(f"SST root     : {SST_ROOT}")
    print()

    SST_ROOT.mkdir(parents=True, exist_ok=True)

    total_books = 0
    total_chapters = 0
    total_sections = 0

    for book_slug, book in BOOKS.items():
        book_dir = SST_ROOT / book_slug
        book_dir.mkdir(parents=True, exist_ok=True)
        total_books += 1

        print(f"BOOK: {book['title']}")
        print(f"  {book_dir}")

        for chapter_slug, chapter_title in book["chapters"]:
            chapter_dir = book_dir / chapter_slug
            chapter_dir.mkdir(parents=True, exist_ok=True)
            total_chapters += 1

            print(f"  ├── {chapter_slug}/")

            for section in CHAPTER_SECTIONS:
                section_dir = chapter_dir / section
                section_dir.mkdir(parents=True, exist_ok=True)
                total_sections += 1
                print(f"  │   ├── {section}/")

            print()

        print()

    print("=" * 78)
    print("COMPLETE")
    print("=" * 78)
    print(f"Books created/verified    : {total_books}")
    print(f"Chapters created/verified : {total_chapters}")
    print(f"Section folders            : {total_sections}")
    print()
    print("Structure:")
    print("  class-10-social-science/")
    print("    ├── history/")
    print("    ├── geography/")
    print("    ├── political-science/")
    print("    └── economics/")
    print()
    print("Each chapter contains:")
    print("  concepts/")
    print("  ncert-exercises/")
    print("  practice/")
    print("  pyqs/")
    print("  quiz/")
    print("  revision-notes/")
    print("  tests/")
    print()
    print("No HTML or content files were created.")
    print("=" * 78)


if __name__ == "__main__":
    main()