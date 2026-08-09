import os
import re
import sys
import time
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

# Ensure stdout handles UTF-8 on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 1. Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(env_path):
    env_path = r'c:\Users\sande\Documents\GitHub\sjmaths-website\.env'

load_dotenv(env_path)
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file.")
    sys.exit(1)

genai.configure(api_key=api_key)

# 2. Master HTML Shell Template with Shared CSS & JS
MASTER_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">

<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{microtopic_title} - {subject_title} Mastery | SJMaths</title>
    <meta name="description" content="Master {microtopic_title} in {subject_title} with comprehensive concepts, rules, formula cards, step-by-step solved examples, and exam tricks for SSC, Railway, Banking, and State exams.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://sjmaths.com/maths-mastery/{slug}/">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Google Fonts & FontAwesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    
    <!-- KaTeX Math Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

    <!-- Global & Module Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/topic-module.css">
</head>

<body>
    <!-- Reading Progress Bar -->
    <div class="reading-progress-container">
        <div class="reading-progress-bar" id="readingProgress"></div>
    </div>

    <div id="header-container"></div>

    <main class="module-container" id="main-content">
        <!-- Hero Header -->
        <div class="module-hero">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/maths-mastery/">Quant Mastery</a>
                <i class="fas fa-chevron-right"></i>
                <span>{subject_title}</span>
            </nav>
            <h1>{microtopic_title}</h1>
            <div class="meta-grid">
                <span class="meta-badge difficulty-medium"><i class="fas fa-signal"></i> Medium Difficulty</span>
                <span class="meta-badge"><i class="far fa-clock"></i> 25-30 Mins Read</span>
                <span class="meta-badge importance"><i class="fas fa-star"></i> High Exam Weightage</span>
                <span class="meta-badge"><i class="far fa-calendar-alt"></i> Updated 2026</span>
            </div>
        </div>

        <!-- Sticky Navigation Tabs -->
        <nav class="sticky-nav-tabs">
            <div class="tabs-wrapper">
                <button class="tab-btn active" data-tab="learn"><i class="fas fa-book-open"></i> 1. Learn</button>
                <button class="tab-btn" data-tab="practice"><i class="fas fa-pen-to-square"></i> 2. Practice</button>
                <button class="tab-btn" data-tab="pyqs"><i class="fas fa-history"></i> 3. PYQs</button>
                <button class="tab-btn" data-tab="test"><i class="fas fa-vial"></i> 4. Test</button>
                <button class="tab-btn" data-tab="revision"><i class="fas fa-bolt"></i> 5. Revision</button>
            </div>
        </nav>

        <!-- TAB 1: LEARN (AI Generated Content) -->
        <div class="tab-panel active" id="tab-learn">
{learn_content}
        </div>

        <!-- TAB 2: PRACTICE PLACEHOLDER -->
        <div class="tab-panel" id="tab-practice">
            <div class="placeholder-card">
                <span class="badge-coming-soon">Under Development</span>
                <div class="placeholder-icon">🎯</div>
                <h2>Interactive Practice Questions</h2>
                <p>We are building 100+ topic-wise practice questions with instant solution toggles and speed metrics.</p>
                <button class="tab-btn active" style="margin: 0 auto;" onclick="document.querySelector('[data-tab=learn]').click()">Back to Learn Tab</button>
            </div>
        </div>

        <!-- TAB 3: PYQS PLACEHOLDER -->
        <div class="tab-panel" id="tab-pyqs">
            <div class="placeholder-card">
                <span class="badge-coming-soon">Under Development</span>
                <div class="placeholder-icon">📜</div>
                <h2>Previous Years Questions (PYQs)</h2>
                <p>Comprehensive repository of real exam questions from SSC CGL, CHSL, Railway, and Banking (2018–2025).</p>
                <button class="tab-btn active" style="margin: 0 auto;" onclick="document.querySelector('[data-tab=learn]').click()">Back to Learn Tab</button>
            </div>
        </div>

        <!-- TAB 4: TEST PLACEHOLDER -->
        <div class="tab-panel" id="tab-test">
            <div class="placeholder-card">
                <span class="badge-coming-soon">Under Development</span>
                <div class="placeholder-icon">⏱️</div>
                <h2>Timed Speed Test</h2>
                <p>Test your speed and accuracy under real exam timer pressure with detailed analytics.</p>
                <button class="tab-btn active" style="margin: 0 auto;" onclick="document.querySelector('[data-tab=learn]').click()">Back to Learn Tab</button>
            </div>
        </div>

        <!-- TAB 5: REVISION PLACEHOLDER -->
        <div class="tab-panel" id="tab-revision">
            <div class="placeholder-card">
                <span class="badge-coming-soon">Under Development</span>
                <div class="placeholder-icon">⚡</div>
                <h2>1-Page Formula & Flashcard Sheet</h2>
                <p>Instant 2-minute formula cheatsheets and key memory flashcards for quick revision.</p>
                <button class="tab-btn active" style="margin: 0 auto;" onclick="document.querySelector('[data-tab=learn]').click()">Back to Learn Tab</button>
            </div>
        </div>
    </main>

    <div id="footer-container"></div>

    <!-- Scripts -->
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
    <script src="/assets/js/topic-module.js" defer></script>
</body>

</html>
"""

# 3. AI Content Prompt (Requests ONLY the inner HTML content of Learn tab)
AI_CONTENT_PROMPT = """# ROLE

You are India's best Government Exam Mathematics educator, instructional designer, UI/UX designer, and technical writer.

Your task is to generate ONLY the inner HTML body content of the "Learn" tab for ONE mathematics microtopic.

Target Exams: SSC CGL/CHSL/MTS/CPO/GD, Railway, Banking, CDS, CAPF, State PCS, Police.
Objective: Complete self-contained mastery from basic to exam level.

--------------------------------------------------
CRITICAL WRITING STYLE RULES (CONCISE, CRISP & HIGH-YIELD)
1. NO FILLER OR FLUFF: Write in a crisp, sharp, bullet-first style. Avoid long wall-of-text paragraphs.
2. HIGH-DENSITY INFORMATION: Keep explanations short (1-2 sentences max per bullet/concept). Bold all key terms.
3. USE COMPARISON TABLES: Use `<table class="concept-table">` for comparing concepts/properties side-by-side.
4. STEP-BY-STEP EXAMPLES: Solutions should use clear numbered steps (Step 1, Step 2) with minimal wordiness.
5. COMPLETE COVERAGE: Retain 100% of all formulas, rules, shortcuts, tricks, and solved exam examples. Do NOT omit any concept!

--------------------------------------------------
INPUT

Topic:
{TOPIC}

Microtopic:
{MICROTOPIC}

--------------------------------------------------
HTML STRUCTURE TO GENERATE

Generate ONLY the following HTML sections using semantic `<section class="section-card">` elements.
Do NOT output `<html>`, `<head>`, `<body>`, `<style>`, or `<script>` tags.

1. Introduction `<section class="section-card">`
   - Crisp 2-3 sentence overview & bulleted exam relevance.

2. Learning Objectives `<section class="section-card">`
   - Bullet list of 5 concise objectives.

3. Prerequisites `<section class="section-card">`
   - Required concepts (bullet list).

4. Core Concepts `<section class="section-card">`
   - Break into logical sub-concepts using `<div class="concept-card">` or `<table class="concept-table">`.
   - For EACH concept: Definition (1-2 sentences), Intuition, Key observations, Memory tip, Mini example.

5. Rules & Properties `<section class="section-card">`
   - Explain rules concisely in `<div class="rule-card">`: Explanation, Reason, Shortcut, Exception, Example.

6. Formula Box `<section class="section-card">`
   - Formulas inside `<div class="formula-card">`: Formula in KaTeX `$$ ... $$`, Meaning, Variables, When to use/NOT to use, Memory trick.

7. Solved Examples `<section class="section-card">`
   - Step-by-step solved examples from Easy to Exam Level in `<div class="example-card">`.
   - Badges (`<span class="example-tag easy">Easy</span>`, `medium`, `hard`, `exam`).
   - Solutions inside `<details class="solution-toggle"><summary>View Step-by-Step Solution</summary><div class="solution-content">...</div></details>`.

8. Exam Tricks & Shortcuts `<section class="section-card">`
   - Calculation tricks, mental maths, elimination methods in `<div class="trick-card">`.

9. Common Mistakes & Pitfalls `<section class="section-card">`
   - Bulleted list of frequent mistakes and how to avoid them in `<div class="warning-card">`.

10. Exam Strategy & Weightage `<section class="section-card">`
    - SSC, Banking, and Railway question pattern breakdown in `<div class="strategy-grid">`.

11. Summary `<section class="section-card">`
    - Concise bullet revision notes.

12. Quick Revision Box `<div class="revision-box">`
    - High-density 1-page cheatsheet summary.

13. Key Takeaways `<section class="section-card">`
    - High-yield bullet takeaways.

14. Next Topic Recommendation `<div class="next-topic-card">`
    - Logical next microtopic to study with recommendation message.

--------------------------------------------------
FORMATTING RULES
- Use Unicode emojis for section headers (📘 🎯 📝 💡 📏 📐 🧠 ⚡ ⚠️ 📊 📌 🚀).
- Format all math equations using KaTeX delimiters (`$$ ... $$` for block, `\\( ... \\)` or `$ ... $` for inline).
- Return ONLY clean HTML fragment. No markdown code fences (no ```html).
"""

def extract_topics():
    """Extract subject, microtopic name, and subfolder slug from maths-mastery/index.html"""
    base_dir = os.path.dirname(__file__)
    index_path = os.path.join(base_dir, "maths-mastery", "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    topics = []
    subject_matches = list(re.finditer(r'<h2 class="subject-title">\s*([^<]+)\s*<.*?(?=<h2 class="subject-title">|</main>)', content, re.DOTALL))
    
    for subject_match in subject_matches:
        subject_title = subject_match.group(1).strip()
        block = subject_match.group(0)
        
        items = re.findall(r'<a href="\./([^/]+)/" class="topic-link">([^<]+)</a>', block)
        for slug, microtopic in items:
            topics.append({
                'topic': subject_title,
                'microtopic': microtopic.strip(),
                'slug': slug.strip()
            })
    return topics

def clean_html(text):
    """Strip code fences if model output contains markdown formatting."""
    content = text.strip()
    if content.startswith("```html"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    return content.strip()

def generate_learn_content(model, topic_info):
    """Call Gemini API for the Learn tab content fragment."""
    prompt = AI_CONTENT_PROMPT.format(
        TOPIC=topic_info['topic'],
        MICROTOPIC=topic_info['microtopic']
    )
    cleaned = clean_html(response.text)
    # Replace **text** markdown bolding with HTML <strong>text</strong>
    cleaned = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', cleaned)
    return cleaned

def main():
    parser = argparse.ArgumentParser(description="Generate Learn tab content for maths-mastery microtopics using Gemini 3.6 Flash and master shared CSS/JS shell.")
    parser.add_argument("--count", type=int, default=20, help="Number of topics to generate (default: 20)")
    parser.add_argument("--start", type=int, default=0, help="Start index (default: 0)")
    parser.add_argument("--model", type=str, default="gemini-3.5-flash", help="Model name (default: gemini-3.5-flash)")
    parser.add_argument("--delay", type=float, default=20.0, help="Delay between API calls in seconds (default: 20.0)")
    parser.add_argument("--skip-existing", action="store_true", default=True, help="Skip files if already generated (>15KB)")
    args = parser.parse_args()

    all_topics = extract_topics()
    target_topics = all_topics[args.start : args.start + args.count]

    print(f"=== Starting Generation for {len(target_topics)} Topics using {args.model} ===")
    
    model = genai.GenerativeModel(args.model)
    base_dir = os.path.dirname(__file__)

    successful = 0
    skipped = 0
    failed = 0

    for idx, item in enumerate(target_topics, start=1):
        slug = item['slug']
        subject = item['topic']
        microtopic = item['microtopic']
        
        target_dir = os.path.join(base_dir, "maths-mastery", slug)
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, "index.html")

        # Check if already generated (>15KB means actual study module, not coming soon placeholder)
        if args.skip_existing and os.path.exists(target_file) and os.path.getsize(target_file) > 15360:
            size_kb = os.path.getsize(target_file) / 1024.0
            print(f"[{idx}/{len(target_topics)}] [SKIP] '{microtopic}' already generated ({size_kb:.1f} KB)")
            skipped += 1
            continue

        print(f"[{idx}/{len(target_topics)}] Generating '{microtopic}' ({subject})...")
        
        try:
            # 1. Generate inner content from Gemini
            learn_html_body = generate_learn_content(model, item)

            # 2. Wrap inside Master HTML Shell Template
            full_page_html = MASTER_HTML_TEMPLATE.format(
                subject_title=subject,
                microtopic_title=microtopic,
                slug=slug,
                learn_content=learn_html_body
            )

            # 3. Write to file
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(full_page_html)
            
            size_kb = len(full_page_html.encode('utf-8')) / 1024.0
            print(f"  [OK] Saved to {slug}/index.html ({size_kb:.1f} KB)")
            successful += 1
        except Exception as e:
            print(f"  [ERROR] generating {slug}: {e}")
            failed += 1

        if idx < len(target_topics):
            time.sleep(args.delay)

    print(f"\n=== Completed! Successful: {successful}, Failed: {failed} ===")

if __name__ == "__main__":
    main()
