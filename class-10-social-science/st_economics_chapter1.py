from pathlib import Path
import html

# ============================================================
# SJMaths
# CBSE CLASS 10 SOCIAL SCIENCE
# ECONOMICS — CHAPTER 1: DEVELOPMENT
#
# ARCHITECTURE
#
# class-10-social-science/
# ├── assets/
# │   ├── css/
# │   │   └── sst.css          ← SHARED
# │   └── js/
# │       └── sst.js           ← SHARED
# │
# └── economics/
#     └── chapter-1-development/
#         ├── index.html
#         ├── concepts/index.html
#         ├── ncert-exercises/index.html
#         ├── practice/index.html
#         ├── pyqs/index.html
#         ├── quiz/index.html
#         ├── revision-notes/index.html
#         └── tests/index.html
#
# NO chapter-specific CSS
# NO chapter-specific JS
# ============================================================


ROOT = Path(__file__).resolve().parent

CHAPTER = (
    ROOT
    / "economics"
    / "chapter-1-development"
)

ASSETS_CSS = ROOT / "assets" / "css"
ASSETS_JS = ROOT / "assets" / "js"

CSS_FILE = ASSETS_CSS / "sst.css"
JS_FILE = ASSETS_JS / "sst.js"


# ============================================================
# CHAPTER INFORMATION
# ============================================================

BOOK = "Economics"
CHAPTER_NO = "Chapter 1"
CHAPTER_TITLE = "Development"

PAGES = [
    (
        "concepts",
        "Learn",
        "Core concepts, definitions and explanations"
    ),
    (
        "ncert-exercises",
        "NCERT Questions",
        "NCERT exercise questions and answers"
    ),
    (
        "practice",
        "Practice",
        "Chapter-wise practice questions"
    ),
    (
        "pyqs",
        "PYQs",
        "Previous-year examination practice"
    ),
    (
        "quiz",
        "Quiz",
        "Quick objective practice"
    ),
    (
        "revision-notes",
        "Revision",
        "Fast chapter revision"
    ),
    (
        "tests",
        "Mini Test",
        "Chapter assessment"
    ),
]


# ============================================================
# SHARED CSS
#
# IMPORTANT:
# Existing sst.css is NOT overwritten.
# ============================================================

SHARED_CSS = r"""
/*
 SJMaths — Class 10 Social Science
 Shared SST stylesheet

 This file is shared by:
 History
 Geography
 Political Science
 Economics
*/

:root {
    --sst-bg: #f6f7f9;
    --sst-surface: #ffffff;
    --sst-surface-soft: #f8fafb;

    --sst-text: #18212b;
    --sst-muted: #667085;

    --sst-primary: #254b5f;
    --sst-primary-dark: #173746;

    --sst-accent: #b8894d;

    --sst-success: #2f765c;
    --sst-danger: #a54b4b;

    --sst-border: #e4e7ec;

    --sst-radius: 16px;

    --sst-shadow:
        0 8px 28px rgba(16, 24, 40, 0.07);
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background: var(--sst-bg);
    color: var(--sst-text);

    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    line-height: 1.55;
}

a {
    color: inherit;
    text-decoration: none;
}

img {
    max-width: 100%;
}

.sst-container {
    width: min(1100px, calc(100% - 24px));
    margin: auto;
}

.sst-topbar {
    position: sticky;
    top: 0;
    z-index: 100;

    background: rgba(255,255,255,.94);
    backdrop-filter: blur(12px);

    border-bottom: 1px solid var(--sst-border);
}

.sst-topbar-inner {
    min-height: 62px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 12px;
}

.sst-brand {
    font-weight: 850;
    letter-spacing: -.025em;
}

.sst-brand small {
    display: block;

    margin-top: 1px;

    color: var(--sst-muted);

    font-size: 10px;
    font-weight: 650;
}

.sst-header {
    padding: 30px 0 18px;
}

.sst-eyebrow {
    color: var(--sst-accent);

    font-size: 11px;
    font-weight: 850;

    letter-spacing: .09em;
    text-transform: uppercase;
}

.sst-header h1 {
    margin: 7px 0 7px;

    font-size: clamp(28px, 7vw, 44px);
    line-height: 1.06;

    letter-spacing: -.04em;
}

.sst-subtitle {
    margin: 0;
    color: var(--sst-muted);
}

.sst-nav {
    display: flex;
    gap: 8px;

    overflow-x: auto;

    padding: 3px 0 16px;

    scrollbar-width: none;
}

.sst-nav::-webkit-scrollbar {
    display: none;
}

.sst-nav a {
    flex: 0 0 auto;

    padding: 9px 13px;

    border: 1px solid var(--sst-border);
    border-radius: 999px;

    background: var(--sst-surface);

    color: var(--sst-muted);

    font-size: 12px;
    font-weight: 750;

    transition:
        background .18s ease,
        color .18s ease,
        border-color .18s ease,
        transform .18s ease;
}

.sst-nav a:hover {
    transform: translateY(-1px);
}

.sst-nav a.active {
    background: var(--sst-primary);
    border-color: var(--sst-primary);
    color: #fff;
}

.sst-section {
    margin: 22px 0;
}

.sst-section-label {
    display: inline-flex;

    margin-bottom: 10px;
    padding: 6px 9px;

    border-radius: 8px;

    background: #eef1f3;

    color: var(--sst-primary);

    font-size: 10px;
    font-weight: 850;

    letter-spacing: .07em;
    text-transform: uppercase;
}

.sst-grid {
    display: grid;

    grid-template-columns:
        repeat(2, minmax(0, 1fr));

    gap: 14px;
}

.sst-card {
    background: var(--sst-surface);

    border: 1px solid var(--sst-border);
    border-radius: var(--sst-radius);

    padding: 17px;

    box-shadow: var(--sst-shadow);

    transition:
        transform .18s ease,
        box-shadow .18s ease;
}

.sst-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 34px rgba(16, 24, 40, .09);
}

.sst-card h2,
.sst-card h3 {
    margin: 0 0 7px;

    line-height: 1.2;
}

.sst-card h3 {
    font-size: 17px;
}

.sst-card p {
    margin: 5px 0 0;
    color: var(--sst-muted);
}

.sst-card ul {
    margin: 9px 0 0;
    padding-left: 19px;
}

.sst-card li {
    margin: 4px 0;
}

.sst-badge {
    display: inline-flex;

    margin-bottom: 8px;
    padding: 4px 8px;

    border-radius: 999px;

    background: #f1f3f5;
    color: var(--sst-muted);

    font-size: 10px;
    font-weight: 800;
}

.sst-formula {
    margin-top: 10px;

    padding: 12px;

    border-left: 3px solid var(--sst-accent);
    border-radius: 9px;

    background: var(--sst-surface-soft);

    font-weight: 800;
}

.sst-question {
    padding: 15px;

    border: 1px solid var(--sst-border);
    border-radius: 12px;

    background: var(--sst-surface);
}

.sst-question + .sst-question {
    margin-top: 10px;
}

.sst-answer {
    margin-top: 10px;

    padding: 11px 12px;

    border-radius: 9px;

    background: var(--sst-surface-soft);
    color: #344054;
}

.sst-answer-toggle {
    margin-top: 10px;

    border: 1px solid var(--sst-border);
    border-radius: 8px;

    padding: 7px 10px;

    background: #fff;

    color: var(--sst-primary);

    cursor: pointer;

    font-weight: 750;
}

.sst-option {
    margin-top: 7px;
    padding: 9px 11px;

    border: 1px solid var(--sst-border);
    border-radius: 9px;

    background: var(--sst-surface-soft);
}

.sst-footer {
    margin: 40px 0 25px;
    padding-top: 18px;

    border-top: 1px solid var(--sst-border);

    color: var(--sst-muted);

    font-size: 12px;
}

@media (max-width: 680px) {

    .sst-container {
        width: min(100% - 18px, 1100px);
    }

    .sst-grid {
        grid-template-columns: 1fr;
    }

    .sst-header {
        padding-top: 23px;
    }

    .sst-header h1 {
        font-size: 31px;
    }

    .sst-card {
        padding: 15px;
    }
}
"""


# ============================================================
# SHARED JS
#
# IMPORTANT:
# Existing sst.js is NOT overwritten.
# ============================================================

SHARED_JS = r"""
/*
 SJMaths — Shared SST JavaScript
*/

document.addEventListener("DOMContentLoaded", () => {

    // --------------------------------------------------------
    // Active navigation
    // --------------------------------------------------------

    const currentPage =
        document.body.dataset.sstPage;

    document
        .querySelectorAll("[data-sst-page]")
        .forEach(link => {

            if (
                link.dataset.sstPage ===
                currentPage
            ) {
                link.classList.add("active");
            }
        });


    // --------------------------------------------------------
    // Answer reveal
    // --------------------------------------------------------

    document
        .querySelectorAll("[data-sst-answer-toggle]")
        .forEach(button => {

            button.addEventListener("click", () => {

                const target =
                    button.parentElement
                    .querySelector(".sst-answer");

                if (!target) return;

                const hidden =
                    target.hasAttribute("hidden");

                if (hidden) {

                    target.removeAttribute("hidden");

                    button.textContent =
                        "Hide Answer";

                } else {

                    target.setAttribute(
                        "hidden",
                        ""
                    );

                    button.textContent =
                        "Show Answer";
                }
            });
        });


    // --------------------------------------------------------
    // Mobile navigation
    // --------------------------------------------------------

    const nav =
        document.querySelector(".sst-nav");

    if (nav) {

        const active =
            nav.querySelector(".active");

        if (active) {

            requestAnimationFrame(() => {

                active.scrollIntoView({
                    behavior: "instant",
                    block: "nearest",
                    inline: "center"
                });

            });
        }
    }

});
"""


# ============================================================
# WRITE SHARED ASSETS ONLY IF MISSING
# ============================================================

def ensure_shared_assets():

    ASSETS_CSS.mkdir(
        parents=True,
        exist_ok=True
    )

    ASSETS_JS.mkdir(
        parents=True,
        exist_ok=True
    )

    if not CSS_FILE.exists():

        CSS_FILE.write_text(
            SHARED_CSS,
            encoding="utf-8"
        )

        print(f"✓ Created shared CSS: {CSS_FILE}")

    else:

        print(
            f"✓ Existing shared CSS preserved: "
            f"{CSS_FILE}"
        )


    if not JS_FILE.exists():

        JS_FILE.write_text(
            SHARED_JS,
            encoding="utf-8"
        )

        print(f"✓ Created shared JS: {JS_FILE}")

    else:

        print(
            f"✓ Existing shared JS preserved: "
            f"{JS_FILE}"
        )


# ============================================================
# NAVIGATION
# ============================================================

def hub_nav():

    links = []

    for slug, title, description in PAGES:

        links.append(
            f"""
            <a
                href="./{slug}/index.html"
                data-sst-page="{slug}"
            >
                {html.escape(title)}
            </a>
            """
        )

    return "\n".join(links)


def tab_nav(current):

    links = []

    for slug, title, description in PAGES:

        active = (
            " active"
            if slug == current
            else ""
        )

        links.append(
            f"""
            <a
                class="{active.strip()}"
                href="../{slug}/index.html"
                data-sst-page="{slug}"
            >
                {html.escape(title)}
            </a>
            """
        )

    return "\n".join(links)


# ============================================================
# BASE HTML
# ============================================================

def hub_shell(content):

    return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
Development | Economics | SJMaths
</title>

<link
    rel="stylesheet"
    href="../../assets/css/sst.css"
>

</head>

<body data-sst-page="hub">

<header class="sst-topbar">

    <div class="sst-container sst-topbar-inner">

        <a class="sst-brand" href="../../index.html">

            SJMaths

            <small>
                CBSE Class 10 Social Science
            </small>

        </a>

        <span class="sst-badge">
            Economics
        </span>

    </div>

</header>


<main class="sst-container">

    <section class="sst-header">

        <div class="sst-eyebrow">
            Economics · Chapter 1
        </div>

        <h1>
            Development
        </h1>

        <p class="sst-subtitle">
            Chapter learning hub
        </p>

    </section>


    <nav class="sst-nav">

        {hub_nav()}

    </nav>


    {content}


    <footer class="sst-footer">

        SJMaths · CBSE Class 10 Social Science ·
        Economics · Development

    </footer>

</main>


<script src="../../assets/js/sst.js"></script>

</body>

</html>
"""


def tab_shell(title, current, content):

    return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
{html.escape(title)} | Development | SJMaths
</title>

<link
    rel="stylesheet"
    href="../../../assets/css/sst.css"
>

</head>


<body data-sst-page="{current}">

<header class="sst-topbar">

    <div class="sst-container sst-topbar-inner">

        <a
            class="sst-brand"
            href="../index.html"
        >

            SJMaths

            <small>
                CBSE Class 10 Social Science
            </small>

        </a>

        <span class="sst-badge">
            Economics
        </span>

    </div>

</header>


<main class="sst-container">

    <section class="sst-header">

        <div class="sst-eyebrow">
            Economics · Chapter 1
        </div>

        <h1>
            Development
        </h1>

        <p class="sst-subtitle">
            {html.escape(title)}
        </p>

    </section>


    <nav class="sst-nav">

        {tab_nav(current)}

    </nav>


    {content}


    <footer class="sst-footer">

        SJMaths · CBSE Class 10 Social Science ·
        Economics · Chapter 1

    </footer>

</main>


<script src="../../../assets/js/sst.js"></script>

</body>

</html>
"""


# ============================================================
# CHAPTER HUB
# ============================================================

def create_hub():

    cards = []

    for slug, title, description in PAGES:

        cards.append(
            f"""
            <a
                class="sst-card"
                href="./{slug}/index.html"
            >

                <span class="sst-badge">
                    {html.escape(title)}
                </span>

                <h3>
                    {html.escape(title)}
                </h3>

                <p>
                    {html.escape(description)}
                </p>

            </a>
            """
        )

    content = f"""
    <section class="sst-section">

        <div class="sst-section-label">
            Chapter Sections
        </div>

        <div class="sst-grid">

            {''.join(cards)}

        </div>

    </section>
    """

    return hub_shell(content)


# ============================================================
# LEARN / CONCEPTS
# ============================================================

def create_concepts():

    content = """

<section class="sst-section">

<div class="sst-section-label">
Core Concepts
</div>


<div class="sst-grid">


<article class="sst-card">

<h3>Development</h3>

<p>
Development refers to progress towards goals
that improve people's lives.
</p>

</article>


<article class="sst-card">

<h3>Different People, Different Goals</h3>

<p>
Different people may have different
developmental goals because their
situations and priorities differ.
</p>

</article>


<article class="sst-card">

<h3>Income and Other Goals</h3>

<ul>

<li>Higher income</li>
<li>Equal treatment</li>
<li>Freedom</li>
<li>Security</li>
<li>Respect</li>

</ul>

</article>


<article class="sst-card">

<h3>Conflicting Goals</h3>

<p>
Development for one group may sometimes
conflict with the goals of another group.
</p>

</article>


<article class="sst-card">

<h3>National Development</h3>

<p>
National development requires consideration
of goals that benefit society broadly and fairly.
</p>

</article>


<article class="sst-card">

<h3>Per Capita Income</h3>

<div class="sst-formula">

Per Capita Income =
Total Income ÷ Total Population

</div>

</article>


<article class="sst-card">

<h3>Average Income</h3>

<p>
Average income is useful for comparison,
but it does not show how income is distributed.
</p>

</article>


<article class="sst-card">

<h3>Other Indicators</h3>

<ul>

<li>Infant Mortality Rate</li>
<li>Literacy Rate</li>
<li>Net Attendance Ratio</li>
<li>Life Expectancy</li>

</ul>

</article>


<article class="sst-card">

<h3>Public Facilities</h3>

<p>
Health, education and other public facilities
can improve people's quality of life.
</p>

</article>


<article class="sst-card">

<h3>Human Development</h3>

<p>
Human development considers important
dimensions of people's well-being.
</p>

</article>


<article class="sst-card">

<h3>Human Development Index</h3>

<p>
HDI considers major dimensions of human
development rather than income alone.
</p>

</article>


<article class="sst-card">

<h3>Sustainability</h3>

<p>
Development should consider the needs
of future generations.
</p>

</article>


</div>

</section>
"""

    return tab_shell(
        "Learn & Concepts",
        "concepts",
        content
    )


# ============================================================
# NCERT EXERCISES
# ============================================================

def create_ncert():

    questions = [

        (
            "Why do different persons have different notions of development?",
            "Different people have different life situations, needs and aspirations."
        ),

        (
            "Do different developmental goals always conflict?",
            "No. Different goals may coexist, although some developmental goals can conflict."
        ),

        (
            "Why is average income used for comparing countries?",
            "Average income provides a common basis for comparison between countries with different populations."
        ),

        (
            "What is a limitation of average income?",
            "It does not show how income is distributed among people."
        ),

        (
            "Why is income not a complete measure of development?",
            "Development also involves health, education, equality, security and other aspects of life."
        ),

        (
            "Why are public facilities important?",
            "Public facilities can provide essential services to people collectively and improve access."
        ),

        (
            "Why is sustainability important?",
            "Development should not damage the resource base required by future generations."
        ),

    ]

    blocks = []

    for number, (question, answer) in enumerate(
        questions,
        start=1
    ):

        blocks.append(
            f"""
            <article class="sst-question">

                <strong>
                    {number}. {html.escape(question)}
                </strong>

                <button
                    class="sst-answer-toggle"
                    type="button"
                    data-sst-answer-toggle
                >
                    Show Answer
                </button>

                <div
                    class="sst-answer"
                    hidden
                >

                    <strong>Answer:</strong>

                    {html.escape(answer)}

                </div>

            </article>
            """
        )

    content = f"""
    <section class="sst-section">

        <div class="sst-section-label">
            NCERT Questions
        </div>

        {''.join(blocks)}

    </section>
    """

    return tab_shell(
        "NCERT Questions",
        "ncert-exercises",
        content
    )


# ============================================================
# PRACTICE
# ============================================================

def create_practice():

    items = [

        (
            "Concept",
            "Explain why two people can have different developmental goals."
        ),

        (
            "Application",
            "Give two examples where income is not the only factor affecting quality of life."
        ),

        (
            "Calculation",
            "A country's total income is ₹5,00,000 and its population is 100. Find its per capita income."
        ),

        (
            "Comparison",
            "Why can two countries with similar average income have different levels of development?"
        ),

        (
            "Data Interpretation",
            "A state has high per capita income but poor health indicators. Can it automatically be called more developed?"
        ),

        (
            "Higher Order",
            "Explain why public facilities can contribute to development."
        ),

    ]

    cards = []

    for tag, question in items:

        cards.append(
            f"""
            <article class="sst-card">

                <span class="sst-badge">
                    {html.escape(tag)}
                </span>

                <h3>
                    Practice Question
                </h3>

                <p>
                    {html.escape(question)}
                </p>

            </article>
            """
        )

    content = f"""
    <section class="sst-section">

        <div class="sst-section-label">
            Practice
        </div>

        <div class="sst-grid">

            {''.join(cards)}

        </div>

    </section>
    """

    return tab_shell(
        "Practice",
        "practice",
        content
    )


# ============================================================
# PYQs
# ============================================================

def create_pyqs():

    content = """

<section class="sst-section">

<div class="sst-section-label">
PYQ Practice
</div>


<article class="sst-card">

<h3>
Examination Practice
</h3>

<p>
Use this section for verified previous-year questions
when the PYQ dataset is added. The questions below are
PYQ-style practice and are not labelled as actual
previous-year questions.
</p>

</article>


<div class="sst-section">

<div class="sst-grid">


<article class="sst-card">

<span class="sst-badge">
1 Mark
</span>

<h3>
Objective
</h3>

<p>
Define per capita income.
</p>

</article>


<article class="sst-card">

<span class="sst-badge">
2 Marks
</span>

<h3>
Short Answer
</h3>

<p>
State two limitations of average income.
</p>

</article>


<article class="sst-card">

<span class="sst-badge">
3 Marks
</span>

<h3>
Explain
</h3>

<p>
Explain why income is important but not sufficient
for measuring development.
</p>

</article>


<article class="sst-card">

<span class="sst-badge">
5 Marks
</span>

<h3>
Long Answer
</h3>

<p>
Explain the important factors that should be
considered while comparing development.
</p>

</article>


</div>

</div>

</section>
"""

    return tab_shell(
        "PYQs",
        "pyqs",
        content
    )


# ============================================================
# QUIZ
# ============================================================

def create_quiz():

    questions = [

        (
            "Per capita income is calculated as:",
            [
                "Population ÷ Total Income",
                "Total Income ÷ Total Population",
                "Total Income × Population",
                "Population − Income"
            ],
            1
        ),

        (
            "Which indicator measures deaths of children before the age of one year?",
            [
                "Literacy Rate",
                "Life Expectancy",
                "Infant Mortality Rate",
                "Attendance Ratio"
            ],
            2
        ),

        (
            "Average income does not show:",
            [
                "Total population",
                "Income distribution",
                "Average income",
                "Total income"
            ],
            1
        ),

        (
            "Sustainable development considers:",
            [
                "Only present needs",
                "Only income",
                "Present and future needs",
                "Only industrial growth"
            ],
            2
        ),

    ]

    blocks = []

    for number, (
        question,
        options,
        correct
    ) in enumerate(
        questions,
        start=1
    ):

        options_html = []

        for index, option in enumerate(options):

            options_html.append(
                f"""
                <div class="sst-option">

                    <strong>
                        {"ABCD"[index]}.
                    </strong>

                    {html.escape(option)}

                </div>
                """
            )

        blocks.append(
            f"""
            <article class="sst-question">

                <strong>
                    {number}. {html.escape(question)}
                </strong>

                {''.join(options_html)}

                <button
                    class="sst-answer-toggle"
                    type="button"
                    data-sst-answer-toggle
                >
                    Show Answer
                </button>

                <div
                    class="sst-answer"
                    hidden
                >

                    Correct answer:
                    <strong>
                        {"ABCD"[correct]}
                    </strong>

                </div>

            </article>
            """
        )

    content = f"""
    <section class="sst-section">

        <div class="sst-section-label">
            Quick Quiz
        </div>

        {''.join(blocks)}

    </section>
    """

    return tab_shell(
        "Quiz",
        "quiz",
        content
    )


# ============================================================
# REVISION
# ============================================================

def create_revision():

    content = """

<section class="sst-section">

<div class="sst-section-label">
Quick Revision
</div>


<div class="sst-grid">


<article class="sst-card">

<h3>
Development
</h3>

<ul>

<li>Different people may have different goals.</li>

<li>Developmental goals can sometimes conflict.</li>

<li>Income is important but not sufficient.</li>

</ul>

</article>


<article class="sst-card">

<h3>
Per Capita Income
</h3>

<div class="sst-formula">

Per Capita Income =
Total Income ÷ Total Population

</div>

</article>


<article class="sst-card">

<h3>
Limitations of Average Income
</h3>

<ul>

<li>It is an average.</li>

<li>It does not show distribution.</li>

<li>It cannot capture every aspect of development.</li>

</ul>

</article>


<article class="sst-card">

<h3>
Important Indicators
</h3>

<ul>

<li>Infant Mortality Rate</li>

<li>Literacy Rate</li>

<li>Net Attendance Ratio</li>

<li>Life Expectancy</li>

</ul>

</article>


<article class="sst-card">

<h3>
Public Facilities
</h3>

<ul>

<li>Health</li>

<li>Education</li>

<li>Essential services</li>

</ul>

</article>


<article class="sst-card">

<h3>
Human Development
</h3>

<ul>

<li>Health</li>

<li>Education</li>

<li>Income</li>

<li>Overall well-being</li>

</ul>

</article>


<article class="sst-card">

<h3>
Sustainability
</h3>

<ul>

<li>Resources are limited.</li>

<li>Environmental damage matters.</li>

<li>Future generations must be considered.</li>

</ul>

</article>


<article class="sst-card">

<h3>
Exam Reminder
</h3>

<div class="sst-formula">

Development ≠ Income Alone

</div>

</article>


</div>

</section>
"""

    return tab_shell(
        "Revision",
        "revision-notes",
        content
    )


# ============================================================
# MINI TEST
# ============================================================

def create_test():

    questions = [

        "Define development in your own words.",

        "Write the formula for per capita income.",

        "Why can average income hide inequality?",

        "Explain two non-income goals of development.",

        "Explain the importance of public facilities.",

        "What is meant by human development?",

        "Why is sustainability important?",

    ]

    blocks = []

    for number, question in enumerate(
        questions,
        start=1
    ):

        blocks.append(
            f"""
            <div class="sst-question">

                <strong>
                    {number}. {html.escape(question)}
                </strong>

            </div>
            """
        )

    content = f"""
    <section class="sst-section">

        <div class="sst-section-label">
            Mini Test
        </div>

        <article class="sst-card">

            <h3>
                Chapter 1 Assessment
            </h3>

            <p>
                Attempt all questions without referring
                to your notes.
            </p>

        </article>

        <div class="sst-section">

            {''.join(blocks)}

        </div>

    </section>
    """

    return tab_shell(
        "Mini Test",
        "tests",
        content
    )


# ============================================================
# WRITE HELPER
# ============================================================

def write_file(path, content):

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content,
        encoding="utf-8"
    )

    print(f"✓ {path}")


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 76)
    print("SJMaths — Class 10 Social Science")
    print("Economics — Chapter 1: Development")
    print("FULL TAB GENERATOR")
    print("=" * 76)
    print()

    # --------------------------------------------------------
    # Shared assets
    # --------------------------------------------------------

    print("STEP 1 — Shared SST assets")
    print("-" * 76)

    ensure_shared_assets()

    print()

    # --------------------------------------------------------
    # Chapter hub
    # --------------------------------------------------------

    print("STEP 2 — Chapter hub")
    print("-" * 76)

    write_file(
        CHAPTER / "index.html",
        create_hub()
    )

    print()

    # --------------------------------------------------------
    # Seven actual pages
    # --------------------------------------------------------

    print("STEP 3 — Creating all tab pages")
    print("-" * 76)

    pages = {

        "concepts":
            create_concepts(),

        "ncert-exercises":
            create_ncert(),

        "practice":
            create_practice(),

        "pyqs":
            create_pyqs(),

        "quiz":
            create_quiz(),

        "revision-notes":
            create_revision(),

        "tests":
            create_test(),
    }


    for slug, document in pages.items():

        write_file(
            CHAPTER
            / slug
            / "index.html",
            document
        )


    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print()
    print("=" * 76)
    print("✓ CHAPTER 1 GENERATION COMPLETE")
    print("=" * 76)

    print()
    print("Shared CSS:")
    print(f"  {CSS_FILE}")

    print()
    print("Shared JS:")
    print(f"  {JS_FILE}")

    print()
    print("Chapter hub:")
    print(f"  {CHAPTER / 'index.html'}")

    print()
    print("Created tabs:")

    for slug, title, description in PAGES:

        print(
            f"  ✓ {title:<20} "
            f"{CHAPTER / slug / 'index.html'}"
        )

    print()
    print("Architecture:")
    print("  ✓ ONE shared sst.css")
    print("  ✓ ONE shared sst.js")
    print("  ✓ NO page-specific CSS")
    print("  ✓ NO page-specific JS")
    print("  ✓ All seven tabs have real index.html files")
    print("  ✓ Correct relative asset paths")
    print("  ✓ Existing shared CSS/JS were preserved")

    print()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()