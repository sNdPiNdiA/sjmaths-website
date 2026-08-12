from pathlib import Path
from html import escape
import re

# ============================================================
# SJMaths — Class 10 Social Science
# Book Chapter Hub Generator
#
# Creates:
#   class-10-social-science/
#       history/index.html
#       geography/index.html
#       political-science/index.html
#       economics/index.html
#
# Each book page contains:
#   • premium mobile-first UI
#   • dropdown/tab-style book selector
#   • clickable chapter cards
#   • chapter search
#   • chapter count
#
# Chapter names are based on the current NCERT Class X books.
# ============================================================

ROOT = Path(__file__).resolve().parent

BOOKS = {
    "history": {
        "label": "History",
        "short": "H",
        "book": "India and the Contemporary World–II",
        "accent": "#b95b4e",
        "chapters": [
            ("01", "The Rise of Nationalism in Europe", "01-rise-of-nationalism-in-europe"),
            ("02", "Nationalism in India", "02-nationalism-in-india"),
            ("03", "The Making of a Global World", "03-making-of-a-global-world"),
            ("04", "The Age of Industrialisation", "04-age-of-industrialisation"),
            ("05", "Print Culture and the Modern World", "05-print-culture-and-the-modern-world"),
        ],
    },

    "geography": {
        "label": "Geography",
        "short": "G",
        "book": "Contemporary India–II",
        "accent": "#7d9a78",
        "chapters": [
            ("01", "Resources and Development", "01-resources-and-development"),
            ("02", "Forest and Wildlife Resources", "02-forest-and-wildlife-resources"),
            ("03", "Water Resources", "03-water-resources"),
            ("04", "Agriculture", "04-agriculture"),
            ("05", "Minerals and Energy Resources", "05-minerals-and-energy-resources"),
            ("06", "Manufacturing Industries", "06-manufacturing-industries"),
            ("07", "Lifelines of National Economy", "07-lifelines-of-national-economy"),
        ],
    },

    "political-science": {
        "label": "Political Science",
        "short": "P",
        "book": "Democratic Politics–II",
        "accent": "#8d819c",
        "chapters": [
            ("01", "Power Sharing", "01-power-sharing"),
            ("02", "Federalism", "02-federalism"),
            ("03", "Gender, Religion and Caste", "03-gender-religion-and-caste"),
            ("04", "Political Parties", "04-political-parties"),
            ("05", "Outcomes of Democracy", "05-outcomes-of-democracy"),
        ],
    },

    "economics": {
        "label": "Economics",
        "short": "E",
        "book": "Understanding Economic Development",
        "accent": "#c39455",
        "chapters": [
            ("01", "Development", "01-development"),
            ("02", "Sectors of the Indian Economy", "02-sectors-of-the-indian-economy"),
            ("03", "Money and Credit", "03-money-and-credit"),
            ("04", "Globalisation and the Indian Economy", "04-globalisation-and-the-indian-economy"),
            ("05", "Consumer Rights", "05-consumer-rights"),
        ],
    },
}


def safe_text(value):
    return escape(value, quote=True)


def make_slug(text):
    text = text.lower().replace("–", "-").replace("—", "-")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def chapter_card(book_key, book, number, title, folder):
    href = f"../{folder}/index.html"

    # Useful topic labels without inventing detailed chapter content.
    tags = {
        "history": ["Concepts", "NCERT", "Practice"],
        "geography": ["Concepts", "Maps", "NCERT"],
        "political-science": ["Concepts", "Civics", "NCERT"],
        "economics": ["Concepts", "Economy", "NCERT"],
    }[book_key]

    return f"""
      <a class="chapter-card" href="{safe_text(href)}">
        <div class="chapter-top">
          <span class="chapter-number">{safe_text(number)}</span>
          <span class="chapter-book">{safe_text(book["label"])}</span>
        </div>

        <div class="chapter-title">{safe_text(title)}</div>

        <div class="chapter-bottom">
          <div class="tags">
            {"".join(f'<span>{safe_text(tag)}</span>' for tag in tags)}
          </div>
          <span class="open">Open <b>→</b></span>
        </div>
      </a>
"""


def page_html(book_key):
    book = BOOKS[book_key]

    selector_items = []
    for key, item in BOOKS.items():
        active = " active" if key == book_key else ""
        selector_items.append(
            f'<a class="book-tab{active}" href="../{key}/index.html">'
            f'<span>{safe_text(item["short"])}</span>{safe_text(item["label"])}</a>'
        )

    cards = "\n".join(
        chapter_card(book_key, book, number, title, folder)
        for number, title, folder in book["chapters"]
    )

    total = len(book["chapters"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="CBSE Class 10 {safe_text(book['label'])} — chapter-wise concepts, NCERT, practice, revision and tests.">
<meta name="theme-color" content="#110f0e">
<title>Class 10 {safe_text(book['label'])} | SJMaths</title>

<style>
:root {{
  --bg:#110f0e;
  --bg2:#181412;
  --panel:rgba(31,25,22,.86);
  --panel2:rgba(39,31,27,.96);
  --text:#f8f2e9;
  --muted:#b5a89a;
  --line:rgba(236,220,201,.12);
  --accent:{book["accent"]};
  --gold:#dfb276;
  --shadow:0 20px 48px rgba(0,0,0,.34);
}}

*{{box-sizing:border-box}}

html{{scroll-behavior:smooth}}

body {{
  margin:0;
  min-height:100vh;
  color:var(--text);
  font-family:Inter,"Segoe UI",Roboto,Arial,sans-serif;
  background:
    radial-gradient(circle at 5% 0%,rgba(197,139,85,.12),transparent 27%),
    radial-gradient(circle at 95% 5%,rgba(169,75,63,.10),transparent 25%),
    linear-gradient(135deg,var(--bg),#171311 55%,#0e0c0b);
}}

a{{color:inherit;text-decoration:none}}

.shell {{
  max-width:1180px;
  margin:auto;
  padding:18px 14px 55px;
}}

.hero {{
  position:relative;
  overflow:hidden;
  padding:22px;
  border:1px solid var(--line);
  border-radius:24px;
  background:linear-gradient(145deg,rgba(47,37,31,.96),rgba(22,18,16,.96));
  box-shadow:var(--shadow);
}}

.hero::after {{
  content:"";
  position:absolute;
  width:190px;
  height:190px;
  right:-75px;
  top:-80px;
  border-radius:50%;
  background:var(--accent);
  opacity:.16;
  filter:blur(14px);
}}

.hero-inner{{position:relative;z-index:1}}

.breadcrumb {{
  display:flex;
  gap:7px;
  color:#887d72;
  font-size:.72rem;
  font-weight:750;
}}

.breadcrumb span:last-child{{color:#d8cabe}}

.eyebrow {{
  display:inline-flex;
  margin-top:25px;
  padding:7px 11px;
  border:1px solid rgba(224,178,122,.18);
  border-radius:999px;
  color:#e5d5c5;
  background:rgba(255,255,255,.045);
  font-size:.72rem;
  font-weight:850;
  text-transform:uppercase;
  letter-spacing:.08em;
}}

.hero h1 {{
  margin:13px 0 7px;
  font-size:clamp(2rem,7vw,3.35rem);
  line-height:1.02;
  letter-spacing:-.05em;
}}

.book-name {{
  margin:0;
  color:#b8aa9b;
  font-family:Georgia,"Times New Roman",serif;
  font-size:.94rem;
}}

.hero-stats {{
  display:flex;
  gap:20px;
  margin-top:20px;
}}

.stat strong {{
  display:block;
  font-size:1rem;
}}

.stat span {{
  display:block;
  margin-top:2px;
  color:#897e73;
  font-size:.68rem;
  text-transform:uppercase;
  letter-spacing:.07em;
}}

.book-tabs {{
  display:flex;
  gap:7px;
  margin-top:18px;
  padding:6px;
  overflow-x:auto;
  border:1px solid var(--line);
  border-radius:15px;
  background:rgba(255,255,255,.035);
  scrollbar-width:none;
}}

.book-tabs::-webkit-scrollbar{{display:none}}

.book-tab {{
  flex:0 0 auto;
  display:inline-flex;
  align-items:center;
  gap:7px;
  padding:9px 11px;
  border:1px solid transparent;
  border-radius:10px;
  color:#968a7e;
  font-size:.72rem;
  font-weight:800;
  white-space:nowrap;
}}

.book-tab span {{
  display:grid;
  place-items:center;
  width:22px;
  height:22px;
  border-radius:7px;
  background:rgba(255,255,255,.06);
  font-size:.65rem;
}}

.book-tab.active {{
  color:#f3e9de;
  background:rgba(255,255,255,.075);
  border-color:var(--line);
}}

.book-tab.active span {{
  color:#1b130e;
  background:var(--gold);
}}

.section-head {{
  display:flex;
  justify-content:space-between;
  align-items:end;
  gap:12px;
  margin:27px 4px 12px;
}}

.section-head h2 {{
  margin:0;
  font-size:1rem;
  letter-spacing:-.02em;
}}

.section-head p {{
  margin:3px 0 0;
  color:#81766b;
  font-size:.73rem;
}}

.search {{
  display:flex;
  align-items:center;
  gap:9px;
  margin-bottom:13px;
  padding:11px 13px;
  border:1px solid var(--line);
  border-radius:14px;
  background:rgba(255,255,255,.035);
}}

.search span{{color:#8d8175}}

.search input {{
  width:100%;
  border:0;
  outline:0;
  color:var(--text);
  background:transparent;
  font-size:.86rem;
}}

.search input::placeholder{{color:#766c63}}

.chapter-grid {{
  display:grid;
  grid-template-columns:1fr;
  gap:12px;
}}

.chapter-card {{
  display:flex;
  flex-direction:column;
  min-height:190px;
  padding:17px;
  border:1px solid var(--line);
  border-radius:19px;
  background:linear-gradient(145deg,rgba(34,28,25,.88),rgba(21,18,16,.94));
  box-shadow:var(--shadow);
  transition:transform .18s ease,border-color .18s ease;
}}

.chapter-card:hover {{
  transform:translateY(-2px);
  border-color:rgba(255,255,255,.22);
}}

.chapter-top {{
  display:flex;
  justify-content:space-between;
  gap:10px;
  color:#8f8377;
  font-size:.69rem;
  font-weight:800;
  text-transform:uppercase;
  letter-spacing:.06em;
}}

.chapter-number{{color:var(--accent)}}

.chapter-title {{
  margin-top:26px;
  max-width:580px;
  font-size:1.22rem;
  line-height:1.25;
  font-weight:850;
  letter-spacing:-.025em;
}}

.chapter-bottom {{
  display:flex;
  align-items:end;
  justify-content:space-between;
  gap:10px;
  margin-top:auto;
  padding-top:22px;
}}

.tags {{
  display:flex;
  flex-wrap:wrap;
  gap:5px;
}}

.tags span {{
  padding:4px 7px;
  border:1px solid rgba(255,255,255,.075);
  border-radius:999px;
  color:#8d8277;
  background:rgba(255,255,255,.03);
  font-size:.64rem;
}}

.open {{
  display:inline-flex;
  align-items:center;
  gap:7px;
  color:var(--accent);
  font-size:.73rem;
  font-weight:900;
  white-space:nowrap;
}}

.open b {{
  display:grid;
  place-items:center;
  width:27px;
  height:27px;
  border-radius:50%;
  background:var(--accent);
  color:#18110e;
}}

.empty {{
  padding:30px;
  border:1px solid var(--line);
  border-radius:18px;
  color:#94887c;
  text-align:center;
  background:rgba(255,255,255,.03);
}}

.footer {{
  margin-top:30px;
  padding-top:17px;
  border-top:1px solid var(--line);
  color:#6f665e;
  font-size:.68rem;
  text-align:center;
}}

@media(min-width:700px){{
  .shell{{padding:28px 24px 60px}}
  .hero{{padding:34px}}
  .chapter-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}
}}

@media(min-width:1050px){{
  .chapter-grid{{grid-template-columns:repeat(3,minmax(0,1fr))}}
}}

@media(max-width:430px){{
  .hero{{padding:19px}}
  .hero h1{{font-size:2.15rem}}
  .chapter-card{{min-height:180px}}
}}
</style>
</head>

<body>
<div class="shell">

  <header class="hero">
    <div class="hero-inner">

      <nav class="breadcrumb" aria-label="Breadcrumb">
        <span>SJMaths</span>
        <span>›</span>
        <span>Class 10</span>
        <span>›</span>
        <span>Social Science</span>
        <span>›</span>
        <span>{safe_text(book["label"])}</span>
      </nav>

      <div class="eyebrow">CBSE · {safe_text(book["label"])}</div>

      <h1>{safe_text(book["label"])}</h1>
      <p class="book-name">{safe_text(book["book"])}</p>

      <div class="hero-stats">
        <div class="stat">
          <strong>{total:02d}</strong>
          <span>Chapters</span>
        </div>
        <div class="stat">
          <strong>NCERT</strong>
          <span>Based</span>
        </div>
        <div class="stat">
          <strong>01</strong>
          <span>Book</span>
        </div>
      </div>

    </div>
  </header>

  <nav class="book-tabs" aria-label="Social Science books">
    {"".join(selector_items)}
  </nav>

  <section>
    <div class="section-head">
      <div>
        <h2>All chapters</h2>
        <p>Select a chapter to open its dedicated learning page.</p>
      </div>
    </div>

    <label class="search">
      <span>⌕</span>
      <input id="search" type="search" placeholder="Search chapters..." autocomplete="off">
    </label>

    <div class="chapter-grid" id="chapters">
      {cards}
    </div>
  </section>

  <footer class="footer">
    SJMaths · Class 10 Social Science · {safe_text(book["label"])}
  </footer>

</div>

<script>
const input = document.getElementById("search");
const cards = [...document.querySelectorAll(".chapter-card")];

input.addEventListener("input", () => {{
  const query = input.value.trim().toLowerCase();
  let visible = 0;

  cards.forEach(card => {{
    const match = card.textContent.toLowerCase().includes(query);
    card.style.display = match ? "" : "none";
    if(match) visible++;
  }});

  let empty = document.getElementById("emptyState");

  if(!visible) {{
    if(!empty) {{
      empty = document.createElement("div");
      empty.id = "emptyState";
      empty.className = "empty";
      empty.textContent = "No chapter matched your search.";
      document.getElementById("chapters").appendChild(empty);
    }}
  }} else if(empty) {{
    empty.remove();
  }}
}});
</script>

</body>
</html>
"""


def create_chapter_folders():
    for book_key, book in BOOKS.items():
        book_dir = ROOT / book_key
        book_dir.mkdir(parents=True, exist_ok=True)

        for _, _, folder in book["chapters"]:
            chapter_dir = book_dir / folder
            chapter_dir.mkdir(parents=True, exist_ok=True)


def main():
    print("=" * 76)
    print("SJMaths — Class 10 Social Science Chapter Hub Generator")
    print("=" * 76)
    print(f"Root: {ROOT}")
    print()

    create_chapter_folders()

    for book_key, book in BOOKS.items():
        book_dir = ROOT / book_key
        output = book_dir / "index.html"
        output.write_text(page_html(book_key), encoding="utf-8")

        print(f"✓ {book['label']}: {len(book['chapters'])} chapters")
        print(f"  {output}")

    print()
    print("TOTAL CHAPTERS:", sum(len(book["chapters"]) for book in BOOKS.values()))
    print()
    print("Created/verified:")
    print("  history/index.html")
    print("  geography/index.html")
    print("  political-science/index.html")
    print("  economics/index.html")
    print()
    print("Each book page includes:")
    print("  ✓ Book dropdown/tab navigation")
    print("  ✓ Searchable chapter list")
    print("  ✓ Clickable chapter cards")
    print("  ✓ Mobile-first responsive UI")
    print("  ✓ Premium dark academic styling")
    print()
    print("IMPORTANT:")
    print("Chapter cards point to <chapter-folder>/index.html.")
    print("Your chapter generators can later populate those pages.")


if __name__ == "__main__":
    main()